import subprocess
import pexpect

stk_ia = "stk ai"

question = "Como posso fazer um bom code review? e sempre termine o texto da resposta com |=+"

child = pexpect.spawn(stk_ia)

child.expect('>>>')

# Envia a pergunta para o processo
child.sendline(question)
# Pressione Esc
child.sendcontrol('[')

# Pressione Enter
child.sendline('')

# Espera a resposta
child.expect('|=+', 60)

# Obtém a saída do processo
stdout = child.before
after = child.after

# Imprime a saída
print(f"Saída do comando: {stdout}")
print(f"Saída do comando: {after}")