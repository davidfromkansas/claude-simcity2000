#!/bin/bash
# seq.sh STEP... : run build steps in order, then audit. A step is "loan" (loan.sh), "LOAN" (LOAN_OK=1 loan.sh),
# or "plan[:args]" (build.py plans/plan.plan args, commas -> spaces). Stops at the first refused loan.
# Written for Claudeville 4 attempt 3 so a whole replayed sequence runs in one background call.
cd "$(dirname "$0")"
for s in "$@"; do
  case $s in
    loan) bash loan.sh | tail -1 | grep -q "refused" && { echo "SEQ: loan refused"; break; } ;;
    LOAN) LOAN_OK=1 bash loan.sh | tail -1 ;;
    *) p=${s%%:*}; a=""; [ "$p" != "$s" ] && a=${s#*:}; a=${a//,/ }
       echo "== $p $a"; r=$(timeout 4000 python3 -I -u build.py plans/$p.plan $a 2>&1 | grep -v "outside the plan" | grep -E "PROBLEM|BUILD|money|ERROR")
       echo "$r" | tail -4
       echo "$r" | grep -q "BUILD: checked" || bad="$bad $p" ;;
  esac
done
[ -n "$bad" ] && echo "SEQ NOT CLEAN (read their output):$bad"   # attempt 6: a refused plan went unnoticed for 5 years
python3 -I audit.py | grep "FAIL\|AUDIT"
./sc save | tail -1 | cut -c1-90
echo SEQDONE
