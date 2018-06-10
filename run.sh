SPAWN='/usr/bin/spawn-fcgi'
PYTHON_APP='/tmp/myapp/main.py'
ADDRESS='127.0.0.1'
PORT='9001'
THREADS='4'
PID='/tmp/spawn-fcgi-1.pid'

killall main.py
sleep 2
#/usr/bin/spawn-fcgi -f /tmp/myapp/main.py -a 127.0.0.1 -p 9001 -F 4
eval '$SPAWN -f $PYTHON_APP -a $ADDRESS -p $PORT -F $THREADS -P $PID'
