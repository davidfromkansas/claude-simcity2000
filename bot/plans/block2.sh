cd /home/user/claude-simcity2000/bot
T(){ python3 -I tile.py $1 $2; }
RD(){ ./vis.sh $1 $2 $3 $4 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T $1 $2) $(T $3 $4); sleep 0.4; ./sc nodlg 2>/dev/null; }
D(){ ./vis.sh $2 $3 $4 $5 >/dev/null; ./sc tool $1; sleep 0.4; ./sc drag $(T $2 $3) $(T $4 $5); sleep 0.4; ./sc nodlg 2>/dev/null; }
RD 76 56 76 90; for y in 62 69 76 83 90; do RD 77 $y 108 $y; done; for x in 84 92 100 108; do RD $x 57 $x 89; done
./vis.sh 84 56 108 56 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; for x in 84 92 100 108; do ./sc click $(T $x 56); sleep 0.3; done
L="22 82 55 90"; for x in 77 85 93 101; do D "$L" $x 57 $x 73; D "$L" $x 73 $x 90; done
R="22 128 75 135"; C="47 128 100 135"; I="68 128 120 135"
for s in "78 83" "86 91" "94 99" "102 107"; do set -- $s; D "$R" $1 57 $2 61; D "$R" $1 84 $2 89; done
for s in "78 83" "86 91" "94 99"; do set -- $s; D "$I" $1 70 $2 75; done; D "$I" 106 70 107 73; D "$I" 102 74 107 75
D "$C" 78 63 83 68; D "$C" 86 63 91 68; D "$I" 94 63 99 68; D "$I" 102 63 107 68; D "$C" 78 77 83 82; D "$I" 86 77 91 82; D "$I" 102 77 107 82
./vis.sh 103 71 101 71 >/dev/null; ./sc tool 22 82 60 105; sleep 1; ./sc click 199 145; sleep 0.6; ./sc click $(T 103 71); sleep 0.8; ./sc nodlg 2>/dev/null
P="47 82 85 90"; D "$P" 74 51 74 70; D "$P" 74 70 74 87; for y in 59 65 72 86; do D "$P" 75 $y 91 $y; D "$P" 91 $y 107 $y; done; D "$P" 75 82 107 82
./vis.sh 72 34 73 45 >/dev/null; ./sc tool 47 82 85 105; sleep 0.5; for y in $(seq 34 44); do ./sc click $(T 72 $y); sleep 0.2; done; D "$L" 73 34 73 45
./vis.sh 95 79 95 79 >/dev/null; ./sc tool 47 155 88 163; sleep 0.5; ./sc click $(T 95 59); sleep 0.8; ./sc nodlg 2>/dev/null
./sc tool 22 105 55 113; ./sc save; echo BLOCK2DONE
