#!/usr/bin/expect -f
set timeout 100
spawn stk ai
expect ">>>"
sleep 0.5
send "Como posso fazer um bom code review? comece a resposta com INICIO ao contrario e encerre a resposta com a palavra FINAL ao Contrario \r"
sleep 0.5
send "\x1b\x0d"
expect "LANIF"
interact