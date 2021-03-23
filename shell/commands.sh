#!/bin/bash
# curl  -I > get back header only
curl -I www.google.com | grep Set-Cookie
# size with summary and total
du -sch --max-depth=1
tree  $1 --du -h
# check doc fast
man grep | grep -e "-e" -B 1 -A 2 -m 5
#q python-q-text-as-data
ps -ef | q -H "select uid, count(*) cnt from - group by uid"
ls -l | tail -n +2 | q "select distinct c6 from -" # no header

