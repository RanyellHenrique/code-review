import subprocess


stk_ia = "stk ai"

question = "Como posso fazer um bom code review?"

# Use 'pexpect' para simular interação com terminal se necessário
# Você precisará instalar o módulo pexpect com 'pip install pexpect'
import pexpect

# Inicia o processo
child = pexpect.spawn(stk_ia)

# Espera que o processo esteja pronto para receber a entrada
child.expect('>>>')

# Envia a pergunta para o processo
child.sendline(question)

# Espera a resposta
child.expect(pexpect.EOF)

# Obtém a saída do processo
stdout = child.before

# Imprime a saída
print(f"Saída do comando: {stdout}")