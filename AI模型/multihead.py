import torch

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads, d_model, dropout=0.1):
        super(MultiHeadAttention, self).__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.dropout = torch.nn.Dropout(dropout)
        self.query_linear = torch.nn.Linear(d_model, d_model)
        self.key_linear = torch.nn.Linear(d_model, d_model)
        self.value_linear = torch.nn.Linear(d_model, d_model)

    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        # 分割输入到多个头
        query_heads = self.query_linear(query).view(batch_size, -1, self.num_heads, self.d_k)
        key_heads = self.key_linear(key).view(batch_size, -1, self.num_heads, self.d_k)
        value_heads = self.value_linear(value).view(batch_size, -1, self.num_heads, self.d_k)
        # 计算注意力得分
        attention_scores = torch.matmul(query_heads, key_heads.transpose(1, 2)) / torch.sqrt(self.d_k)
        if mask is not None:
            attention_scores = attention_scores.masked_fill(mask == 0, -1e9)
        # 应用 Softmax 函数
        attention_scores = torch.nn.Softmax(dim=-1)(attention_scores)
        # 进行 dropout 操作
        attention_scores = self.dropout(attention_scores)
        # 计算注意力加权的 value
        context = torch.matmul(attention_scores, value_heads)
        # 合并多头的结果
        context = context.view(batch_size, -1, self.d_model)
        return context