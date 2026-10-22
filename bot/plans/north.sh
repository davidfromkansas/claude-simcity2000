cd /home/user/claude-simcity2000/bot
T(){ python3 -I tile.py $1 $2; }
RD(){ ./vis.sh $1 $2 $3 $4 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T $1 $2) $(T $3 $4); sleep 0.4; ./sc nodlg 2>/dev/null; }
D(){ ./vis.sh $2 $3 $4 $5 >/dev/null; ./sc tool $1; sleep 0.4; ./sc drag $(T $2 $3) $(T $4 $5); sleep 0.4; ./sc nodlg 2>/dev/null; }
RD 77 6 101 6; RD 101 6 126 6; RD 77 13 92 13; RD 101 13 106 13
for x in 84 92 100; do RD $x 1 $x 19; done; for x in 116 124; do RD $x 1 $x 11; done; RD 108 7 108 11
L="22 82 55 90"; for x in 77 85 101 117 125; do D "$L" $x 1 $x 20; done; D "$L" 93 1 93 12
R="22 128 75 151"; C="47 128 100 151"; P="47 82 85 90"
for s in "78 83" "86 91" "94 99" "102 107"; do set -- $s; D "$R" $1 1 $2 5; D "$C" $1 7 $2 12; done
D "$C" 109 7 115 11; D "$C" 118 7 123 11; D "$R" 118 1 123 5; D "$R" 78 14 83 19; D "$R" 86 14 91 19; D "$R" 102 14 106 19
D "$P" 74 4 74 23; for y in 3 9 16; do D "$P" 75 $y 100 $y; done; D "$P" 100 9 123 9; D "$P" 100 3 107 3
./vis.sh 88 10 88 10 >/dev/null; ./sc tool 47 155 88 179; sleep 0.5; ./sc click $(T 111 9); sleep 0.8; ./sc nodlg 2>/dev/null
./sc tool 22 105 55 113; ./sc pause; ./sc save; echo BLOCKDONE
