import torch
import sys


print(f'Python Version: \n> {sys.version}')
print(f'Is Cuda Available? \n> {torch.cuda.is_available()}')
print(f'CUDNN Version: \n> {torch.backends.cudnn.version()}')
print(f'Device Count: \n> {torch.cuda.device_count()}')
CURRENT_DEVICE = torch.cuda.current_device()
print(f'Current Device: \n> {CURRENT_DEVICE}')
print(f'Device Name: \n> {torch.cuda.get_device_name(CURRENT_DEVICE)}')
