import subprocess

mesage = 'Como posso fazer um bom code review? comece a resposta com INICIO ao contrario e encerre a resposta com a palavra FINAL ao Contrario'
# Executar um programa que requer interação
process = subprocess.Popen(["expect", 'script.sh', mesage], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output, error = process.communicate()

print("Saída do programa:", output)
print("Erro do programa:", error)