import torch
import torch.onnx

class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = torch.nn.Linear(10, 5)
        self.fc1.name = '全连接层1'  # 设置中文名称
        self.fc2 = torch.nn.Linear(5, 1)
        self.fc2.name = '全连接层2'  # 设置中文名称

    def forward(self, x):
        x = self.fc1(x)
        x = torch.nn.functional.relu(x)
        x = self.fc2(x)
        return x

# 创建模型实例
model = SimpleNet()

# 设置模型为评估模式
model.eval()

# 创建一个随机的输入张量
dummy_input = torch.randn(1, 10)

# 导出模型
torch.onnx.export(model,               # 模型
                  dummy_input,         # 模型输入（用于追踪）
                  "E:\python-test\study-python\模型查看\model.onnx",        # 导出的ONNX文件名
                  export_params=True,  # 存储训练好的参数
                  opset_version=10,    # ONNX版本
                  do_constant_folding=True, # 执行常量折叠优化
                  input_names = ['input'],   # 输入名
                  output_names = ['output'], # 输出名
                  dynamic_axes={'input' : {0 : 'batch_size'},    # 批处理变量
                                'output' : {0 : 'batch_size'}})