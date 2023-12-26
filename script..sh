spawn stk ai
expect ">>>"
send -- "Como posso fazer um bom code review? encerre a resposta com a palavra FINAL ao Contrario\r"
expect "LANIF"
send -- "\033\r" # This is the ESC key followed by Enter
interact