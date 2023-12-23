import pexpect

stk_ia = "stk ai"

question = "Como posso fazer um bom code review? e sempre termine o texto da resposta com a palavra posto ao contrario"

child = pexpect.spawn(stk_ia)

child.expect('>>>')

print("Enviando a pergunta para o stk ai")

child.sendline(question)

print("Precionando esc + enter")
child.send('\x1b\x0d')

child.expect('>>>')

# Obtém a saída do processo
before = child.before.decode('utf-8')
after = child.after.decode('utf-8')
buffer = child.buffer.decode('utf-8')

# Imprime a saída
print(f"Saída do comando(before): {before}")
print(f"Saída do comando(after): {after}")
print(f"Saída do comando(buffer): {buffer}")