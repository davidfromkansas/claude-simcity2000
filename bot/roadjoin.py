"""roadjoin.py OUT.plan : join every road piece the audit calls cut off to the main network by the shortest path
(<= 8 tiles) over empty land or rubble. Claudeville 4 attempt 9 (after the 2028 great fire)."""
import sys,re,subprocess;sys.path.insert(0,'/home/user/claude-simcity2000/bot')
from collections import deque
from citymap import City,is_road,is_rubble
import sc2parse as p
c=City();bit=p.chunks(p.SAVE)['XBIT'];N=128
out=subprocess.run(['python3','-I','audit.py'],capture_output=True,text=True,cwd='/home/user/claude-simcity2000/bot').stdout
pieces=[]
for m in re.finditer(r'road piece of \d+ tiles at x(\d+)-(\d+) y(\d+)-(\d+)|stray road tile at x(\d+)-\d+ y(\d+)-',out):
  if m.group(1): pieces.append((int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4))))
  else: x,y=int(m.group(5)),int(m.group(6)); pieces.append((x,x,y,y))
roads={(x,y) for x,y in c.tiles() if is_road(c.t(x,y))}
free=lambda x,y:(c.t(x,y)==0 or is_rubble(c.t(x,y))) and not bit[y*N+x]&4
steps=[]
for x0,x1,y0,y1 in pieces:
  piece=c.flood([q for q in roads if x0<=q[0]<=x1 and y0<=q[1]<=y1][:1], lambda x,y:(x,y) in roads)
  other=roads-piece
  prev={q:None for q in piece};dq=deque(piece);end=None
  while dq and not end:
    x,y=dq.popleft()
    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      n=(x+dx,y+dy)
      if n in prev or not(0<=n[0]<N and 0<=n[1]<N): continue
      if n in other: end=(x,y);break
      if free(*n): prev[n]=(x,y);dq.append(n)
  if end is None or end in piece: print('no free path for piece',x0,y0) if end is None else None; continue
  path=[];q=end
  while q not in piece: path.append(q);q=prev[q]
  if len(path)<=8: steps+=['road %d %d %d %d'%(a,b,a,b) for a,b in path]
  else: print('long path',len(path),x0,y0)
open(sys.argv[1],'w').write('# road joins for cut-off road pieces (attempt 9 after the 2028 fire)\n'+'\n'.join(steps)+'\n');print(len(steps),'tiles')
