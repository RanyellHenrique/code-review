import pexpect

stk_ia = "stk ai"

question = "Como posso fazer um bom code review? e sempre termine o texto da resposta com a palavra posto ao contrario"

child = pexpect.spawn(stk_ia, encoding='utf-8')

child.expect('>>>')

print("Enviando a pergunta para o stk ai")

child.sendline(question)

print("Precionando esc + enter")
child.send("\x1b\r")

child.expect('otsop', 120)

# Obtém a saída do processo
before = child.before
after = child.after
buffer = child.buffer

# Imprime a saída
print(f"Saída do comando(before): {before}")
print(f"Saída do comando(after): {after}")
print(f"Saída do comando(buffer): {buffer}")