### $String ~ library:$

- str[`a`,`b`]:返回`str`中的第`a` 和第`b`个字符之间的所有字符
- str.capitalize:将`str`的首字母变为大写
- str.ljust(width,[fillchar]):左对齐
- str.rjust(width,[fillchar]):右对齐
- str.center(width[,fillchar]):中间对齐
- str.fine(`sub`[,`start`[,`end`]])：在`str`中寻找字符`ch`的位置并返回数值
- str.replace(`old`,`new`[,`count`]):在`str`中寻找`count`个`old`字符串并替换成`new`字符串
- str.lower():将`str`字符串转换为小写字符
- str.startwith(`prefix`[,`start`[,`end`]]):是否以`prefix`开头
- str.endwith(`suffix`[,`start`[,`end`]]):是否以`suffix`结尾
- str.swapcase():将`str`中的字符大小写互换
- str.strip([`chars`]):去除两边的`chars`，默认是空格
- str.lstrip([`chars`]):去除左边的`chars`，默认是空格
- str.rstrip([`chars`]):去除右边的`chars`，默认是空格
- str.split([`sep`, [maxsplit]]):以`sep`为分隔符，把`str`分成一个list，maxsplit表示分割的次数，默认的分割符为空白字符。
- str.isalnum():`str`是否全是字母和数字，并至少有一个字符
- str.isalpha():`str`是否全是字母，并至少有一个字符
- str.isdigit():`str`是否全是数字，并至少有一个字符
- str.isspace():`str`是否全是空白字符，并至少有一个字符
- str.islower():`str`中的字母是否全是小写
- str.isupper():`str`中的字母是否便是大写
- str.istitle():`str`是否是首字母大写的
- len(`str`):输出`str`的长度

### $List ~ library:$

- x.append(`char`):加入元素`char`
- x.extend(`char`):加入元素`char`
- x.insert(`position`,`char`):在`x.[position]`位置插入`char`元素
- x.remove(`char`):从前往后删除第一个`char`元素
- x.sort():将list中的元素排序
- len(`x`):寻找`x`的长度
- max(`x`):寻找`x`中最大元素
- min(`x`):寻找`x`中最小元素
- sum(`x`):对`x`中元素求和

### $ Dictionary ~ library:$

- dic.keys()：返回一个包含字典所有键的集合
- dic.values()：返回一个包含字典所有值的集合
- dic.items()：返回一个包含字典所有键值对元组的集合
- dic.get(`word`,`num`)：获取字典中`word`的值，如果不存在，则返回`num`。
- pop(`word`)：删除字典中`word`的键值对，并返回该键的值
- popitem()：删除字典中的最后一个键值对，并返回该键的值

### $ File ~ library:$

#### $Open ~ \& ~ close:$

- `file`=open(`'test.txt'`(,'r')):打开`"test.txt"`文件（只读）
- `file`=open(`'test2.bin'`(,'rb')):打开`"test2.bin"`的二进制文件（只读）
- `file`=open(`'test.txt'`(,'w')):打开`"test.txt"`文件（写入）
- `file`=open(`'test2.bin'`(,'wb')):打开`'test2.bin'`的二进制文件（写入）
- `file`=open(`'test.txt'`(,'a')):打开`"test.txt"`文件（追加）
- `file`=open(`'test2.bin'`(,'ab')):打开`'test2.bin'`的二进制文件（追加）
- `file`=open(`'test.txt'`(,'r+')):打开`"test.txt"`文件（读写）
- `file`=open(`'test2.bin'`(,'rb+')):打开`'test2.bin'`的二进制文件（读写）
- close(`file`):关闭`file`

<br>

- with open(`'test.txt'`(,'opr')) as `file`:自动管理文件打开与关闭，更安全

##### $PS：$

- 写入模式打开文本时，若文本不存在则创建新文件；若已存在，则清空文件内容
- 追加模式打开文本时，若文本不存在则创建新文件

#### $Read:$

- a=`file`.read(`size`):返回一整个字符串，读取结束返回空字符串
- line = file.readline():读取一行内容
- lines = file.readlines():读取所有行并返回一个列表

#### $Write:$

- file.write('`text`'):向文件中立即写入`text`
- file.tell():获取当前读写位置
- file.seek(`offset`(,`whence`)):读写位置移动到第`offset`个字节处，`whence`为参考位置，默认为`0`：从头开始，`1`：从当前开始，`2`从末尾开始
  
#### $Others:$

##### $Os:$

- os.mkdir(`'directory'`):创建目录
- os.remove(`'text.txt'`):删除`text.txt`文件

##### $Shutil:$

- shutil.move(`'sourse`,`'destination/'`):移动文件
- shutil.copy(`'sourse`,`'destination/'`):复制文件

##### $Os.path:$

- filename = os.path.basename():获取文件名
- extension = os.path.splitext()[1]:获取文件拓展名

### $Tuple ~ library:$

#### $Read:$

- eg:`a`,`b`,`c`=`tuple`
- 左侧变量数应等于`tuple`值的数量

#### $Connect:$

- `tuple3`=`tuple1`+`tuple2`
- `tuple2`的元素加在`tuple1`后

#### $Function:$

- index():查找元组并返回给定值的索引
- count():返回指定值的出现频率
- all()如果所有元素为真或元组为空，则返回True
- any():如果元组的任何一个元素为真，则返回True；如果元组为空，则返回False
- len():返回元组的长度或大小
- enumerate():返回元组的枚举对象
- max():返回给定元组的最大元素
- min():返回给定元组的最小元素
- sum():将元组中的数字相加
- sorted():输入元组元素并返回一个新的排序列表
- tuple():将可迭代对象转换为元组

### $Numpy~library:$

#### $Functions:$

- import numpy as np
- np.zeros()
- np.ones()
- np.eye()
- np.arange()
- np.random
- np.random.random():输出一个\(0,1\]的数
- np.random.normal()
- np.random.randint()

#### $Array:$

- x1=np.array([`x`,`y`,`z`],[`a`,`b`,`c`]):创建二维数组
- x1.sum():逐个求和
- x1.sum(axis=0):逐列求和
- x1.sum(axis=1):逐行求和
- np.concayenate([`x`,`y`]):将`x`和`y`两个数组拼接
- np.concayenate([`x`,`y`],axis=0):将`x`和`y`两个数组垂直拼接
- np.concayenate([`x`,`y`],axis=1):将`x`和`y`两个数组水平拼接
- np.split(`x`,[`pos1`,`pos2`]):在`pos1`和`pos2`分割数组`x`

#### $Sort:$

- np.sort(`x`):将`x`升序
- np.argsort(`x`):返回将`x`升序排列的数字位置
- np.partition(`x`)
- np.count_nonzero(`x`<`value`):输出`x`数组中小于`value`的数的数量
- `x`<`value`:返回一个`bool`类型数组

### $Pandas~library:$

#### $Create~DataFrame:$

- df=pd.DataFrame(pd.read_csv('name.csv'),header=1):读取CSV文件
- df=pd.DataFrame(pd.read_excel('name.xlsx')):读取XLSX文件
- df=pd.DataFrame({"id"=[x,y,z],"date"=[a,b,c]······}):创建数据表
- df.to_csv('name.csv'):导出CSV文件
- df.to_excel('name.xlsx'):导出XLSX文件

#### $Read~DataFrame:$

- df.shape:维度查看
- df.info():数据表基本信息（维度、列名称、数据格式、所占空间等）
- df.index:得到所有行的行索引名的一个对象
- df.index.values:得到所有行的行索引名的一个列表list
- df.columns:得到所有列的列索引名的一个对象
- df.columns.values:得到所有列的列索引名的一个列表list
- df.dtypes:每一列数据的格式
- df['B'].dtype:某一列格式
- df["姓名"].values:获取某一列的所有数值
- row_i = df.iloc[3].values:获取第3行数据
- df.isnull():查看空值
- df['A'].isnull():查看某一列的空值
- df['A'].unique():查看某一列的唯一值
- df.values:查看数据表的值
- df.head()：默认查看前5行数据
- df.tail()：默认查看后5行数据

**定位表格中的指定元素**:

- df.at['行标签名', '列标签名']
- df.iat['行索引号', '列索引号']
- df.loc['行标签名', '列标签名']
- df.iloc[行索引数字, 列索引数字]
- df.loc['行标签名1':'行标签名2', '列标签名1': '列标签名2']
- df.iloc[行索引数字1:行索引数字2, 列索引数字1:列索引数字2]

#### $https://blog.csdn.net/Strive_For_Future/article/details/126710810$

matplotlib.pyplot

### $Sklearn~library:$

#### $Decision~Tree:$

- from sklearn.tree import DecisionClassifier
- clf = DecisionClassifier(max_depth=3)
- clf.fit(X,y)$~ ~ ~ ~ ~ ~ ~$# Create a Decision Tree classifier
- clf.predict(X_test) # Predict on X_test

#### $Random~Forest:$

- From sklearn.ensemble import RandomForestClassifier
- $~~~~~$# Creat a random forest classifier
- clf = RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2)
- $~~~~~$# Evaluate with cross validation
- scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
- mean_score = scores.mean()
- print("Cross-validation accuracy={mean_score:.4f}")

#### $Implementation:XGBoost$

- from xgboost import XGBClassifier
- $~~~~~$# read data
- from sklearn.datasets import load_iris
- from sklearn.model_selection import train_test_split
- data = load_iris()
- X_train, X_test, y_train, y_test = train_test_split(data['data'], data['target'], test_size=.2)
- $~~~~~$# create model instance
- bst = XGBClassifier(n_estimators=2, max_depth=2, learning_rate=1,objective='binary:logistic')
- $~~~~~$# fit model
- bst.fit(X_train, y_train)
- $~~~~~$# make predictions
- preds = bst.predict(X_test)

### $Torch~Library:$

#### $Neural~Networks:$

**Load the dataset:**

- import torch
- from torch import nn
- from torch.utils.data import DataLoader
- from torchvision import datasets, transforms
- transform = transforms.Compose([transforms.ToTensor(),\
- transforms.Normalize((0.5,), (0.5,))])
- $~~~~~$# Download training data from open datasets.
- training_data = datasets.MNIST(root=“./data”,train=True,\
- download=True,transform=transform)
- $~~~~~$# Download test data from open datasets.
- test_data = datasets.FashionMNIST(root=”./data",train=False,\
- download=True,transform=transform)
- train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
- test_loader = DataLoader(dataset=test_dataset, batch_size=1000, shuffle=False)

