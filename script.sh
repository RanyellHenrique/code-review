#!/usr/bin/expect -f
spawn stk ai
expect ">>>   (Send the request with 'Alt+Enter' or 'Esc then Enter'.)"
send -- "Como posso fazer um bom code review? encerre a resposta com a palavra FINAL ao Contrario\r"
send -- "\033\r" # This is the ESC key followed by Enter
expect "LANIF"
interact