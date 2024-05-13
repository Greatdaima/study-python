import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # TODO: set the GPU device

import torch
from torch.nn import functional as F
from transformers import AutoTokenizer, pipeline
from infini_gemma import GemmaForCausalLM
from infini_gemma import GemmaConfig

print("Torch Version:", torch.__version__)
print("CUDA:", torch.cuda.is_available())

if torch.cuda.is_available():
    device = "cuda:0"  # set GPU device using CUDA_VISIBLE_DEVICES
else:
    device = "cpu"

config = GemmaConfig.from_pretrained(
    "google/gemma-2b",
)

print(config)

# Create the Gemma model with Infini-attention
model = GemmaForCausalLM(config)
# model = model.from_pretrained("google/gemma-2b")
pretrained_model = GemmaForCausalLM.from_pretrained("google/gemma-2b")
# Step 4: Transfer weights
# Note: This is a simplified example; you need to ensure that each parameter's dimensions match.
for param in model.named_parameters():
    name = param[0]
    if name in pretrained_model.state_dict():
        # Check if dimensions match, and only then assign the weights
        if param[1].size() == pretrained_model.state_dict()[name].size():
            param[1].data = pretrained_model.state_dict()[name].data.clone()
        else:
            print(f"Skipping {name} due to size mismatch.")
print(model)