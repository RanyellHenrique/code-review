import subprocess
import pexpect

stk_ia = "stk ai"

question = "Como posso fazer um bom code review?"

child = pexpect.spawn(stk_ia)

child.expect('> Bem-vindo ao StackSpot Ai. Por favor, insira seu prompt abaixo:', 60)

# Envia a pergunta para o processo
child.sendline(question)

# Espera a resposta
child.expect(pexpect.EOF)

# Obtém a saída do processo
stdout = child.before

# Imprime a saída
print(f"Saída do comando: {stdout}")