import pyautogui
import keyboard
import threading
import time

def click_mouse(): #aqui ele inicia o click com o mouse com um sleep de 1 seg
    while not should_exit.is_set():
        pyautogui.click()
        time.sleep(1)

def detect_key(): #aqui ele verifica se a tecla de quebrar o codigo foi feita, para parar o autoclick
    keyboard.wait('q')
    should_exit.set()

should_exit = threading.Event()

mouse_thread = threading.Thread(target=click_mouse) #inicia as threads para clicar o mouse e detectar a tecla pressionada
key_thread = threading.Thread(target=detect_key)

mouse_thread.start()
key_thread.start()

mouse_thread.join() #espera até que as threads finalizem
key_thread.join()