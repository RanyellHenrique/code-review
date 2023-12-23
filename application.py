import subprocess
import pexpect

stk_ia = "stk ai"

question = "Como posso fazer um bom code review?"

child = pexpect.spawn(stk_ia)

child.expect('>>>')

# Envia a pergunta para o processo
child.sendline(question)
# Pressione Esc
child.sendcontrol('[')

# Pressione Enter
child.sendline('')

# Espera a resposta
child.expect('>>>')

# Obtém a saída do processo
stdout = child.before

# Imprime a saída
print(f"Saída do comando: {stdout}")