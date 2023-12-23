import subprocess
from pynput import keyboard
from pynput.keyboard import Key

# Função para pressionar e soltar teclas
def press_and_release_keys(keys):
    with keyboard.Controller() as controller:
        for key in keys:
            controller.press(key)
        for key in reversed(keys):
            controller.release(key)

# Executar um programa que requer interação
process = subprocess.Popen(['stk ai'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Agora, você pode automatizar a entrada de teclado conforme necessário
# Por exemplo, pressionando Enter e Alt simultaneamente
process.stdin.write("Como posso fazer um bom code review?")
press_and_release_keys([Key.alt_gr, Key.enter])

# Agora você pode interagir com o programa através do processo.stdin
process.stdin.flush()

# Leia a saída do programa, se necessário
output, error = process.communicate()

print("Saída do programa:", output)
print("Erro do programa:", error)
