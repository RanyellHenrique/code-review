import subprocess

stk_ia = "stk ai"

question = "Como posso fazer um bom code review?"

process = subprocess.Popen(stk_ia.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout, stderr = process.communicate(question)

# Verifica se houve algum erro
if process.returncode != 0:
    print(f"Ocorreu um erro: {stderr}")
else:
    print(f"Saída do comando: {stdout}")