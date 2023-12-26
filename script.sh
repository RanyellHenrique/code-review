#!/usr/bin/expect -f
set timeout 30
spawn stk ai
expect ">>>   (Send the request with 'Alt+Enter' or 'Esc then Enter'.)"
sleep 1
send "Como posso fazer um bom code review? comece a resposta com INICIO ao contrario e encerre a resposta com a palavra FINAL ao Contrario \n"
sleep 1
send "\x1b\x0d"
expect "LANIF"
interact