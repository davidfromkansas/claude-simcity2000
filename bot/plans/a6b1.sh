cd /home/user/claude-simcity2000/bot
T(){ python3 -I tile.py $1 $2; }
RD(){ ./vis.sh $1 $2 $3 $4 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T $1 $2) $(T $3 $4); sleep 0.4; ./sc nodlg 2>/dev/null; }
D(){ ./vis.sh $2 $3 $4 $5 >/dev/null; ./sc tool $1; sleep 0.4; ./sc drag $(T $2 $3) $(T $4 $5); sleep 0.4; ./sc nodlg 2>/dev/null; }
# attempt 6 block 1 = attempt 4 block 1 + avenue + verified neighbor link
RD 76 30 76 1; RD 76 30 76 57
./vis.sh 76 0 76 2 >/dev/null; ./sc tool 22 105 55 113; sleep 0.3; ./sc drag $(T 76 1) $(T 76 0); sleep 1.2; ./sc click 265 261; sleep 0.8; ./sc nodlg 2>/dev/null
for y in 20 27 34 41 48 55; do RD 77 $y 108 $y; done; for x in 84 92 100 108; do RD $x 21 $x 54; done
L="22 82 55 90"; for x in 77 85 93 101; do D "$L" $x 21 $x 37; D "$L" $x 37 $x 55; done; D "$L" 77 56 101 56
R="22 128 75 135"; C="47 128 100 135"; I="68 128 120 135"
for s in "78 83" "86 91" "94 99" "102 107"; do set -- $s; D "$R" $1 21 $2 26; D "$R" $1 49 $2 54; done
for s in "78 83" "86 91" "94 99"; do set -- $s; D "$C" $1 28 $2 33; D "$I" $1 35 $2 40; done
D "$I" 102 39 107 40; D "$I" 106 35 107 38; D "$C" 78 42 83 47; D "$I" 102 28 107 33
./vis.sh 103 36 101 36 >/dev/null; ./sc tool 22 82 60 105; sleep 1; ./sc click 199 145; sleep 0.6; ./sc click $(T 103 36); sleep 0.8; ./sc nodlg 2>/dev/null
./vis.sh 72 22 74 33 >/dev/null; ./sc tool 47 82 85 105; sleep 0.5; for y in $(seq 22 33); do ./sc click $(T 72 $y); sleep 0.2; done
D "$L" 73 34 73 21; ./vis.sh 73 21 77 21 >/dev/null; ./sc tool 22 82 55 90; sleep 0.4; for x in 73 74 75 76; do ./sc click $(T $x 21); sleep 0.2; done
P="47 82 85 90"; D "$P" 74 23 74 51; for y in 23 30 37 44 51; do D "$P" 73 $y 91 $y; D "$P" 91 $y 107 $y; done
./vis.sh 87 43 87 43 >/dev/null; ./sc tool 47 155 88 179; sleep 0.5; ./sc click $(T 87 43); sleep 0.8; ./sc nodlg 2>/dev/null
./sc tool 22 105 55 113; ./sc save
echo A6B1DONE
