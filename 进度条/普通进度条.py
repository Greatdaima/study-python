import sys
import time

for i in range(0, 101, 10):
    print("\r", "进度: {}%: ".format(i), "▓" * (i // 2), end='')
    sys.stdout.flush()
    time.sleep(0.1)
    print(i,end='')
