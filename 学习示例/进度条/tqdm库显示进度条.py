from tqdm import tqdm
import time

# 基本进度条
for i in tqdm(range(100)):
    time.sleep(0.01)

# 设置进度条的前缀，使用desc参数
for i in tqdm(range(100), desc="Processing"):
    time.sleep(0.01)

# 设置进度条的长度，使用total参数
for i in tqdm(range(100), total=200):
    time.sleep(0.01)

# 在进度条后面显示一些信息，使用postfix参数
for i in tqdm(range(100), postfix={"processed": i}):
    time.sleep(0.01)

# 设置进度条的填充字符，使用bar_format参数
for i in tqdm(range(100), bar_format="{l_bar}{bar:30}{r_bar}"):
    time.sleep(0.01)