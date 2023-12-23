import subprocess

# Executar um programa que requer interação
process = subprocess.Popen(['stk', 'ai'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


process.stdin.write("Como fazer um code review?")
process.stdin.flush()
# Enviar diretamente os caracteres para simular 'Alt + Enter'
process.stdin.write("\x1b\n")
process.stdin.flush()

# Agora você pode interagir com o programa através do processo.stdin


# Leia a saída do programa, se necessário
output, error = process.communicate()

print("Saída do programa:", output)
print("Erro do programa:", error)