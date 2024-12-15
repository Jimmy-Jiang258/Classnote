
# PyTorch 使用指南

## 1. 安装 PyTorch 和扩展库

### 1.1 安装 PyTorch
安装 PyTorch 和常用的扩展库，可以通过以下命令进行安装：

```bash
pip install torch torchvision torchaudio
```

- `torch` 是 PyTorch 的核心库，支持深度学习和张量计算。
- `torchvision` 提供计算机视觉相关的功能，如数据集加载、图像预处理和模型训练。
- `torchaudio` 提供音频处理的功能，适用于音频数据的加载、转换和特征提取。

---

## 2. **PyTorch 基础：张量操作**

### 2.1 张量（Tensor）
张量是 PyTorch 的核心数据结构，类似于 NumPy 数组，但可以在 GPU 上加速计算。以下是创建和操作张量的一些常见方法：

- **创建张量**：
    ```python
    import torch
    tensor = torch.tensor([1, 2, 3])  # 从列表创建张量
    zeros = torch.zeros(2, 3)  # 创建全零张量
    ones = torch.ones(3, 3)  # 创建全一张量
    rand_tensor = torch.rand(2, 2)  # 创建随机张量
    ```

- **张量操作**：
    ```python
    a = torch.tensor([1, 2, 3])
    b = torch.tensor([4, 5, 6])
    c = a + b  # 张量加法
    d = a * b  # 张量乘法
    print(c, d)
    ```

- **矩阵运算**：
    ```python
    mat1 = torch.rand(2, 3)
    mat2 = torch.rand(3, 2)
    result = torch.mm(mat1, mat2)  # 矩阵乘法
    print(result)
    ```

- **广播（Broadcasting）**：
    ```python
    a = torch.tensor([1, 2, 3])
    b = torch.tensor([1])
    c = a + b  # 广播机制：b 会被自动扩展为与 a 相同形状
    ```

---

## 3. **PyTorch 神经网络：`torch.nn`**

### 3.1 定义神经网络
使用 `torch.nn` 模块构建神经网络模型，通过继承 `nn.Module` 类来定义。

```python
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 2)  # 定义全连接层

    def forward(self, x):
        return self.fc1(x)  # 前向传播

# 实例化模型
model = SimpleNN()
```

### 3.2 损失函数与优化器
- **定义损失函数**：
    ```python
    criterion = nn.CrossEntropyLoss()  # 适用于分类任务
    ```

- **定义优化器**：
    ```python
    import torch.optim as optim
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)  # 随机梯度下降优化器
    ```

### 3.3 训练模型
```python
inputs = torch.tensor([[1.0, 2.0]])
targets = torch.tensor([[0.0, 1.0]])

# 前向传播
outputs = model(inputs)

# 计算损失
loss = criterion(outputs, targets)

# 反向传播
optimizer.zero_grad()  # 清除之前的梯度
loss.backward()  # 计算梯度
optimizer.step()  # 更新权重
```

---

## 4. **CUDA 支持：使用 GPU 加速**

### 4.1 检查 GPU 可用性
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

### 4.2 将模型和数据移动到 GPU
```python
model = model.to(device)  # 将模型移到 GPU
inputs = inputs.to(device)  # 将数据移到 GPU
```

---

## 5. **音频处理：`torchaudio`**

`torchaudio` 是 PyTorch 的一个扩展库，专门用于音频数据的处理和分析。

### 5.1 安装 `torchaudio`
```bash
pip install torchaudio
```

### 5.2 加载和保存音频文件
```python
import torchaudio

# 加载音频文件
waveform, sample_rate = torchaudio.load("audio.wav")

# 保存音频文件
torchaudio.save("output.wav", waveform, sample_rate)
```

### 5.3 音频特征提取
- **提取梅尔频率倒谱系数（MFCC）**：
    ```python
    transform = torchaudio.transforms.MFCC(
        sample_rate=16000, melkwargs={"n_fft": 400, "hop_length": 160, "n_mels": 23, "center": False}
    )
    mfcc = transform(waveform)
    ```

- **提取短时傅里叶变换（STFT）**：
    ```python
    stft = torchaudio.transforms.Spectrogram(n_fft=400, win_length=None, hop_length=160, power=None)(waveform)
    ```

### 5.4 数据增强
```python
# 添加噪声
noise = torch.randn_like(waveform) * 0.1
waveform_with_noise = waveform + noise
```

---

## 6. **计算机视觉：`torchvision`**

`torchvision` 是 PyTorch 用于计算机视觉任务的扩展库，提供了图像数据集、常用的图像预处理、数据增强、预训练模型等功能。

### 6.1 安装 `torchvision`
```bash
pip install torchvision
```

### 6.2 图像数据集
`torchvision.datasets` 提供了许多常见的数据集接口，方便加载和处理图像数据集。

- **加载 MNIST 数据集**：
    ```python
    import torchvision.transforms as transforms
    from torchvision.datasets import MNIST
    from torch.utils.data import DataLoader

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    trainset = MNIST(root='./data', train=True, download=True, transform=transform)
    trainloader = DataLoader(trainset, batch_size=32, shuffle=True)
    ```

- **加载 CIFAR-10 数据集**：
    ```python
    from torchvision.datasets import CIFAR10
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    trainset = CIFAR10(root='./data', train=True, download=True, transform=transform)
    trainloader = DataLoader(trainset, batch_size=32, shuffle=True)
    ```

### 6.3 图像预处理与增强
`torchvision.transforms` 提供了许多常用的图像预处理与数据增强方法：

- **图像预处理**：
    ```python
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    ```

- **数据增强**：
    ```python
    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(30),
        transforms.RandomResizedCrop(224),
        transforms.ToTensor()
    ])
    ```

### 6.4 预训练模型
`torchvision.models` 提供了多个预训练的深度学习模型，适用于图像分类等任务。

- **加载预训练的 ResNet-18**：
    ```python
    from torchvision import models
    model = models.resnet18(pretrained=True)
    ```

- **冻结模型的卷积层**：
    ```python
    for param in model.parameters():
        param.requires_grad = False
    model.fc = nn.Linear(model.fc.in_features, 10)  # 修改输出层
    ```

### 6.5 模型训练与评估
- **训练模型**：
    ```python
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    for epoch in range(10):
        for data in trainloader:
            inputs, labels = data
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
    ```

- **评估模型**：
    ```python
    model.eval()  # 设置为评估模式
    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            inputs, labels = data
            outputs = model(inputs)


            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Accuracy: {100 * correct / total}%")
    ```

---

## 7. **总结**

- **PyTorch** 是一个强大的深度学习框架，支持张量操作、自动微分、神经网络构建和训练，并能够在 GPU 上加速计算。
- **`torchaudio`** 提供了音频数据处理的功能，适合音频分析、特征提取和数据增强等任务。
- **`torchvision`** 提供了丰富的计算机视觉工具，支持数据集加载、图像预处理与增强、预训练模型等，帮助快速实现视觉任务。

结合使用 `torch`、`torchaudio` 和 `torchvision`，你可以高效地进行机器学习、深度学习以及音频与图像处理任务。
