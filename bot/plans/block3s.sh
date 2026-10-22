cd /home/user/claude-simcity2000/bot
T(){ python3 -I tile.py $1 $2; }
RD(){ ./vis.sh $1 $2 $3 $4 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T $1 $2) $(T $3 $4); sleep 0.4; ./sc nodlg 2>/dev/null; }
D(){ ./vis.sh $2 $3 $4 $5 >/dev/null; ./sc tool $1; sleep 0.4; ./sc drag $(T $2 $3) $(T $4 $5); sleep 0.4; ./sc nodlg 2>/dev/null; }
for y in 62 69 76 83 90; do RD 109 $y 126 $y; done; for x in 116 124; do RD $x 57 $x 89; done
./vis.sh 116 56 124 56 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; for x in 116 124; do ./sc click $(T $x 56); sleep 0.3; done
L="22 82 55 90"; for x in 109 117 125; do D "$L" $x 57 $x 90; done
R="22 128 75 135"; I="68 128 120 135"; C="47 128 100 135"; P="47 82 85 90"
for s in "110 115" "118 123"; do set -- $s; D "$R" $1 57 $2 61; D "$I" $1 70 $2 75; D "$R" $1 84 $2 89; D "$I" $1 77 $2 82; done; D "$C" 118 63 123 68
for y in 59 72 79 86; do D "$P" 108 $y 123 $y; done
./vis.sh 111 65 111 65 >/dev/null; ./sc tool 47 155 88 179; sleep 0.5; ./sc click $(T 111 67); sleep 0.8; ./sc nodlg 2>/dev/null
./sc tool 22 105 55 113; ./sc save; echo BLOCKDONE
