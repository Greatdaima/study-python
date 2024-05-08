import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        # 创建位置编码矩阵
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        # 添加一个维度以匹配输入形状 (batch_size, seq_len, d_model)
        self.pe = pe.unsqueeze(0)

    def forward(self, x):
        # 扩展位置编码以匹配批次大小和序列长度
        pe = self.pe[:, :x.size(1), :]
        x = x + pe
        return self.dropout(x)


class TransformerModel(nn.Module):
    def __init__(self, d_model, nhead, num_layers, dim_feedforward, dropout=0.1, vocab_size=10000):
        super(TransformerModel, self).__init__()

        # Transformer的编码器部分
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        # 位置编码
        self.pos_encoder = PositionalEncoding(d_model, dropout)

        # 输入嵌入层
        self.embedding = nn.Embedding(vocab_size, d_model)

    def forward(self, src):
        # 通过嵌入层
        src = self.embedding(src)
        # 计算位置编码
        src = self.pos_encoder(src)
        # 通过Transformer编码器
        output = self.transformer_encoder(src)
        return output
# 参数示例
d_model = 512  # 模型维度
nhead = 8     # 注意力头数
num_layers = 6  # 编码器层数
dim_feedforward = 2048  # 前馈网络的维度
dropout = 0.1  # 丢弃率
vocab_size = 10000  # 词汇表大小

# 创建模型实例
model = TransformerModel(d_model, nhead, num_layers, dim_feedforward, dropout, vocab_size)
# 示例输入
src = torch.randint(0, vocab_size, (10, 20))  # 10个长度为20的序列
# 前向传播
output = model(src)
print(output.shape)  # 输出形状应为 (10, 20, 512)