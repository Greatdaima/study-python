from transformers import PretrainedConfig

class LlamaConfig(PretrainedConfig):
    def __init__(self):
        super(LlamaConfig).__init__(self)
        self.attention_bias = False
        self.attention_dropout = 0.0
        self.bos_token_id = 1
        self.eos_token_id = 2
        self.hidden_act = "silu"
        self.hidden_size = 1024
        self.initializer_range = 0.02
        self.intermediate_size = 11008
        self.max_position_embeddings = 2048
        self.model_type = "llama"
        self.num_attention_heads = 32
        self.num_hidden_layers = 32
        self.num_key_value_heads = 32
        self.pretraining_tp = 1
        self.rms_norm_eps = 1e-06
        self.rope_scaling = None
        self.rope_theta = 10000.0
        self.tie_word_embeddings = False
        self.use_cache = True
        self.vocab_size = 32000
