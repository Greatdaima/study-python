from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
def on_move(x,y):
    print(f'鼠标位置：{x,y}')


def on_click(x, y, button, pressed):
    if pressed:
        print(f"鼠标点击事件：({x}, {y}, {button})")

def on_press(key):
    if hasattr(key, 'char'):
        # 如果按键有对应的字符表示（例如字母、数字、符号等）
        print(f'按键 {key.char} 被{"按下" if key else "释放"}')
    else:
        # 如果按键没有对应的字符表示（例如功能键、控制键等）
        print(f'特殊按键 {key} 被{"按下" if key else "释放"}')


# 监听键盘事件
keyboard_listener = KeyboardListener(on_press=on_press)
keyboard_listener.start()

# 监听鼠标事件
mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()

# 阻塞主线程，保持监听
keyboard_listener.join()
mouse_listener.join()
