#!/usr/bin/expect -f
set timeout 30
spawn stk ai
expect ">>>   (Send the request with 'Alt+Enter' or 'Esc then Enter'.)"
sleep 4
send "Como posso fazer um bom code review? comece a resposta com INICIO ao contrario e encerre a resposta com a palavra FINAL ao Contrario"
send "\x1b\x0d"
expect -re  `r"OICINI(.*?)LANIF"`
echo $expect_out(1,string)
interact