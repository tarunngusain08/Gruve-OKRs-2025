"""
Model Quantization Example (Q2)
Uses PyTorch static quantization for a simple model.
"""
import torch
import torch.quantization
from torchvision import models
model_fp32 = models.resnet18(pretrained=False)
model_fp32.eval()
model_int8 = torch.quantization.quantize_dynamic(model_fp32, {torch.nn.Linear}, dtype=torch.qint8)
print("Quantized model:", model_int8)
# Human touch: Try quantizing your own models and compare size/speed!
