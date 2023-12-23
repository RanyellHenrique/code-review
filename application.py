import subprocess
import pexpect

stk_ia = "stk ai"

question = "Como posso fazer um bom code review? e sempre termine o texto da resposta com |=+"

child = pexpect.spawn(stk_ia)

child.expect('>>>')

# Envia a pergunta para o processo
child.sendline(question)

# Pressione Enter
child.send('\x1b\x0d') 

# Obtém a saída do processo
before = child.before
after = child.after
buffer = child.buffer

# Imprime a saída
print(f"Saída do comando(before): {before}")
print(f"Saída do comando(after): {after}")
print(f"Saída do comando(buffer): {buffer}")