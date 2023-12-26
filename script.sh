#!/usr/bin/expect -f
set timeout 30
spawn stk ai
expect ">>>   (Send the request with 'Alt+Enter' or 'Esc then Enter'.)"
sleep 2
send "Como posso fazer um bom code review? encerre a resposta com a palavra FINAL ao Contrario"
send "\x1b\x0d"
expect "LANIF"
interact