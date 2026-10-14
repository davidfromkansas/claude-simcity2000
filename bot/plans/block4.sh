cd /home/user/claude-simcity2000/bot
T(){ python3 -I tile.py $1 $2; }
RD(){ ./vis.sh $1 $2 $3 $4 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T $1 $2) $(T $3 $4); sleep 0.4; ./sc nodlg 2>/dev/null; }
D(){ ./vis.sh $2 $3 $4 $5 >/dev/null; ./sc tool $1; sleep 0.4; ./sc drag $(T $2 $3) $(T $4 $5); sleep 0.4; ./sc nodlg 2>/dev/null; }
for y in 97 104 110 117 124; do RD 78 $y 108 $y; done
for x in 84 92; do RD $x 91 $x 110; RD $x 114 $x 123; done; for x in 100 108; do RD $x 91 $x 108; RD $x 108 $x 123; done
L="22 82 55 90"; for x in 85 93; do D "$L" $x 91 $x 110; D "$L" $x 114 $x 125; done; D "$L" 101 91 101 108; D "$L" 101 108 101 125; D "$L" 78 90 78 110; D "$L" 78 114 78 125; D "$L" 78 125 101 125
R="22 128 75 135"; C="47 128 100 135"; I="68 128 120 135"; P="47 82 85 90"
for s in "79 83" "86 91" "94 99" "102 107"; do set -- $s; D "$I" $1 91 $2 96; D "$R" $1 98 $2 103; D "$C" $1 105 $2 109; D "$I" $1 114 $2 116; D "$R" $1 118 $2 123; done; D "$I" 102 111 107 113
D "$P" 99 86 99 104; D "$P" 99 104 99 121; for y in 94 101 107 115 121; do D "$P" 79 $y 107 $y; done
./vis.sh 87 99 95 99 >/dev/null; ./sc tool 47 155 88 179; sleep 0.5; ./sc click $(T 87 106); sleep 0.8; ./sc nodlg 2>/dev/null; ./sc tool 47 155 88 163; sleep 0.5; ./sc click $(T 95 106); sleep 0.8; ./sc nodlg 2>/dev/null
./sc tool 22 105 55 113; ./sc pause; ./sc save; echo BLOCKDONE
