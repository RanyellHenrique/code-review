#!/usr/bin/expect -f
spawn stk ai
expect ">>>"
send "Como posso fazer um bom code review? encerre a resposta com a palavra FINAL ao Contrario\r"
send "\033\r"
expect "LANIF"
interact