cd /home/user/claude-simcity2000/bot
T(){ python3 -I tile.py $1 $2; }
RD(){ ./vis.sh $1 $2 $3 $4 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T $1 $2) $(T $3 $4); sleep 0.4; ./sc nodlg 2>/dev/null; }
D(){ ./vis.sh $2 $3 $4 $5 >/dev/null; ./sc tool $1; sleep 0.4; ./sc drag $(T $2 $3) $(T $4 $5); sleep 0.4; ./sc nodlg 2>/dev/null; }
for y in 97 104 110 117 124; do RD 109 $y 126 $y; done; for x in 116 124; do RD $x 91 $x 107; RD $x 107 $x 123; done
L="22 82 55 90"; for x in 109 117 125; do D "$L" $x 90 $x 107; D "$L" $x 107 $x 125; done; D "$L" 102 125 125 125
R="22 128 75 135"; C="47 128 100 135"; I="68 128 120 135"; P="47 82 85 90"
for s in "110 115" "118 123"; do set -- $s; D "$I" $1 91 $2 96; D "$R" $1 98 $2 103; D "$C" $1 105 $2 109; D "$I" $1 111 $2 116; D "$R" $1 118 $2 123; done
for y in 94 101 107 115 121; do D "$P" 108 $y 123 $y; done
./vis.sh 119 106 119 106 >/dev/null; ./sc tool 47 155 88 179; sleep 0.5; ./sc click $(T 119 106); sleep 0.8; ./sc nodlg 2>/dev/null
./sc tool 22 105 55 113; ./sc pause; ./sc save; echo BLOCKDONE
