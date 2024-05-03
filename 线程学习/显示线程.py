import multiprocessing
import time

def worker(n):
    print(f"开始执行任务 {n}")
    time.sleep(5)
    print(f"任务 {n} 完成")

p1 = multiprocessing.Process(target=worker, args=(1,))
p2 = multiprocessing.Process(target=worker, args=(2,))

p1.start()
p2.start()

p1.join()
p2.join()