cd /home/user/claude-simcity2000/bot
T(){ python3 -I tile.py $1 $2; }
RD(){ ./vis.sh $1 $2 $3 $4 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T $1 $2) $(T $3 $4); sleep 0.4; ./sc nodlg 2>/dev/null; }
D(){ ./vis.sh $2 $3 $4 $5 >/dev/null; ./sc tool $1; sleep 0.4; ./sc drag $(T $2 $3) $(T $4 $5); sleep 0.4; ./sc nodlg 2>/dev/null; }
for y in 20 27 34 41 48 55; do RD 109 $y 126 $y; done; for x in 116 124; do RD $x 21 $x 54; done
L="22 82 55 90"; for x in 109 117 125; do D "$L" $x 21 $x 56; done; D "$L" 102 56 125 56
R="22 128 75 135"; C="47 128 100 135"; I="68 128 120 135"; P="47 82 85 90"
for s in "110 115" "118 123"; do set -- $s; D "$R" $1 21 $2 26; D "$I" $1 28 $2 33; D "$I" $1 35 $2 40; D "$R" $1 49 $2 54; done; D "$C" 110 42 115 47; D "$I" 118 42 123 47
for y in 23 30 37 44 51; do D "$P" 108 $y 123 $y; done
./sc tool 22 105 55 113; ./sc save; echo BLOCK3DONE
