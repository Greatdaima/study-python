from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

def on_press(key):
    print(f'按键 {key} 被按下')

def on_move(x, y):
    print(f'鼠标移动到 ({x}, {y})')

# 监听键盘事件
keyboard_listener = KeyboardListener(on_press=on_press)
keyboard_listener.start()

# 监听鼠标事件
mouse_listener = MouseListener(on_move=on_move)
mouse_listener.start()

# 阻塞主线程，保持监听
keyboard_listener.join()
mouse_listener.join()
