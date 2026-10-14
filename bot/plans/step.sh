# one check-in step: run ~3-4 game months, pause, close any budget window, print health
cd /home/user/claude-simcity2000/bot
./sc run cheetah ${1:-4}; ./sc pause
import -window "$(xdotool search --name DOSBox | head -1)" /tmp/sc/chk.png 2>/dev/null
./sc save | cut -c1-150
python3 -I -c "
import sys;sys.path.insert(0,'.');import sc2parse as p;m=p.parse(p.SAVE);g=m['graphs'];c=p.chunks(p.SAVE);b=c['XBLD'];bt=c['XBIT']
print('spare water/power',g['water_pct'][:1],g['power_pct'][:1],'unpowered',sum(1 for i in range(16384) if 0x70<=b[i]<0xC0 and not bt[i]&64),'dry',sum(1 for i in range(16384) if 0x70<=b[i]<0xC0 and not bt[i]&16),'rubble',sum(1 for v in b if 1<=v<=4))"
./sc paused
