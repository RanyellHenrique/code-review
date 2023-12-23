import subprocess
import pexpect

stk_ia = "stk ai"

question = "Como posso fazer um bom code review?"

child = pexpect.spawn(stk_ia)

child.expect('(Envie a requisição com ')

# Envia a pergunta para o processo
child.sendline(question)
child.sendcontrol('alt+enter')

# Espera a resposta
child.expect('(Envie a requisição com ')

# Obtém a saída do processo
stdout = child.before

# Imprime a saída
print(f"Saída do comando: {stdout}")