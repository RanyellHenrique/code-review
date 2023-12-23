import subprocess
import pexpect


print("Iniciando consulta ao StackSpot AI")

stk_ia = "stk ai"

question = "Como posso fazer um bom code review? e sempre termine o texto da resposta com a palavra posto ao contrario"

child = pexpect.spawn(stk_ia)

child.expect('>>>')

# Envia a pergunta para o processo
child.send(question)

# Pressione Enter
child.send('\x1B\x0D') 

child.expect('otsop', 60)

# Obtém a saída do processo
before = child.before
after = child.after
buffer = child.buffer

# Imprime a saída
print(f"Saída do comando(before): {before}")
print(f"Saída do comando(after): {after}")
print(f"Saída do comando(buffer): {buffer}")