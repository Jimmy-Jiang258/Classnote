### $Iostream ~ library:$

- cin:输入
- cout:输出
- cerr:输出报错，不带缓冲
- clog:输出报错，带缓冲

<br>

- ifstream:输入文件
- ofstream:输出文件
- fstream:输入输出文件，文件流
  
<br>

- stringstream:将字符串与其他数据类型转换
- istringstream:只读字符串
- ostringstream:只写字符串

### $Iomanip ~ library:$

- setbase(n)设置整数为n进制(n=8,10,16)
- setfill(n):设置字符填充，c可以是字符常或字符变量
- setprecision(n):设置浮点数的有效数字为n位
- setw(n):设置字段宽度为n位
- setiosflags(ios::fixed):设置浮点数以固定的小数位数显示
- setiosflags(ios::scientific):设置浮点数以科学计数法表示
- setiosflags(ios::left):输出左对齐
- setiosflags(ios::right):输出右对齐
- setiosflags(ios::skipws):忽略前导空格
- setiosflags(ios::uppercase):在以科学计数法输出E与十六进制输出X以大写输出，否则小写。
- setiosflags(ios::showpos):输出正数时显示"+"号
- setiosflags(ios::showpoint):强制显示小数点
- resetiosflags() :终止已经设置的输出格式状态，在括号中应指定内容

<br>

- dec:设置整数为十进制
- hex:设置整数为十六进制
- oct:设置整数为八进制

### $Char ~ library:$

- isupper(`ch`): 判断字符 `ch` 是否是大写字母。
- islower(`ch`): 判断字符 `ch` 是否是小写字母。
- toupper(`ch`): 将小写字母 `ch` 转为大写字母。
- tolower(`ch`): 将大写字母 `ch` 转为小写字母。
- salpha(`ch`): 判断字符 `ch` 是否是字母（包括大写和小写字母）。
- isdigit(`ch`): 判断字符 `ch` 是否是数字。
- isspace(`ch`): 判断字符 `ch` 是否是空白字符（如空格、制表符、换行符等）。
- ispunct(`ch`): 判断字符 `ch` 是否是标点符号。
- isxdigit(`ch`): 判断字符 `ch` 是否是十六进制数字。
- strlen(`str`)获取`str`的长度。
- strcmp(`str1`, `str2`)比较`str1`和`str2`的大小。
- strcpy(`dest`, `src`)将`src`复制到`dest`中。
- strcat(`dest`, `src`)将`src`拼接到`dest`的末尾。
- strstr(`str`, `substr`)查找`substr`在`str`中的位置。

$PS:$
- 以上函数中 `ch` 也可以用字符串 `a` 的 `a[i]` 来使用

### $String ~ library:$

- size()：返回字符串的长度
- empty()：判断字符串是否为空
- clear()：清空字符串
- append()：在字符串末尾添加字符或字符串
- insert()：在指定位置插入字符或字符串
- erase()：删除指定位置的字符或一段字符
- replace()：替换指定位置的字符或一段字符
- substr()：截取子字符串
- find()：查找子字符串的位置
- rfind()：从后往前查找子字符串的位置
- compare()：比较两个字符串
- c_str()：将字符串转换为C风格字符串
- stoi()：将字符串转换为整数
- stod()：将字符串转换为双精度浮点数
- to_string()：将数字转换为字符串
- str.erase(unique(alls.begin(),alls.end()),str.end()):去重

### $Char ~\& ~ String:$

#### char*转string:

- str=p

#### string 转char*:

- const char *p = str.c_str()

### $Culculate~library:$

- abs(`value`):获取`value`的绝对值。
- ceil(`value`):获取大于等于`value`的最小整数。
- floor(`value`):获取小于等于`value`的最大整数。
- round(`value`):获取最近的整数
- sqrt(`value`):获取`value`的平方根。
- pow(`base`, `exponent`):获取`base`的`exponent`次幂。
- log(`value`):获取以`e`为底的`value`的对数。
- exp(`value`):获取`e`的`value`次幂。
- sin(`value`):获取`value`的正弦值。
- cos(`value`):获取`value`的余弦值。
- tan(`value`):获取`value`的正切值。

### $Algorithm~library:$

- min(`a`,`b`):`a`和`b`中的较小值
- max(`a`,`b`):`a`和`b`中的较大值
- sort(array.begin(),array.end()):将`array`升序
- binary_search(array.begin(), array.end(), `a`)：在`array`中二分查找`a`，找到返回 True
- replace(array.begin(), array.end(), `a`, `b`):在`array`中将所有的`a`换成`b`

### $Vector ~ library:$

#### $Kinds ~ of ~ vector:$

- 顺序容器: `vector` `string` `deque` `list`
- 关联容器: `set` `multlist` `map` `multimap`
- 适配器容器: `stack` `queue` `priority_queue`

#### $Initialize:$

- `容器类型()`：默认构造函数，创建空的容器。
- `容器类型(size)`：创建具有`size`个元素的容器，元素使用默认值初始化。
- `容器类型(begin, end)`：用另一个容器或迭代器范围`(begin, end)`进行初始化。

#### $Operate:$

- `operator=`：赋值运算符，将一个容器赋值给另一个容器。
- `assign(begin, end)`：用迭代器范围`[begin, end)`的内容替换容器内容。
- `assign(size, value)`：用`size`个`value`替换容器内容。

#### $Read:$

- `at(index)`：返回指定位置的元素，带边界检查。
- `operator[]`：返回指定位置的元素，不带边界检查。
- `front()`：返回第一个元素。
- `back()`：返回最后一个元素。
- `data()`：返回指向容器内存的指针（适用于`vector`等连续存储的容器）。

#### $Capacity:$

- `size()`：返回容器中元素的数量。
- `empty()`：检查容器是否为空。
- `max_size()`：返回容器可能容纳的最大元素数量。
- `capacity()`：返回当前分配的存储空间（仅适用于`vector`等）。
- `reserve(n)`：将容器的容量增加到至少`n`（仅适用于`vector`）。

#### $Write:$

- `clear()`：清空容器。
- `insert(pos, value)`：在`pos`位置插入元素`value`。
- `insert(pos, count, value)`：在`pos`位置插入`count`个`value`。
- `insert(pos, begin, end)`：在`pos`位置插入迭代器范围`[begin, end)`的元素。
- `erase(pos)`：删除`pos`位置的元素。
- `erase(begin, end)`：删除`[begin, end)`范围的元素。
- `push_back(value)`：在容器末尾添加`value`（适用于`vector`、`deque`等）。
- `pop_back()`：移除最后一个元素。
- `push_front(value)`：在容器开头添加`value`（适用于`list`、`deque`等）。
- `pop_front()`：移除第一个元素（适用于`list`、`deque`等）。
- `emplace(pos, args)`：在`pos`位置原地构造一个元素。
- `emplace_back(args)`：在末尾原地构造一个元素。
- `swap(other)`：交换两个容器的内容。

#### $Iterator:$

- `begin()`：返回指向第一个元素的迭代器。
- `end()`：返回指向容器末尾之后位置的迭代器。
- `rbegin()`：返回指向最后一个元素的反向迭代器。
- `rend()`：返回指向第一个元素之前位置的反向迭代器。
- `cbegin()`：返回常量迭代器，指向第一个元素。
- `cend()`：返回常量迭代器，指向末尾之后的位置。

#### $Find:$

- `find(value)`：查找元素`value`（适用于关联容器，如`set`、`map`）。
- `count(value)`：返回元素`value`的出现次数（适用于关联容器）。
- `lower_bound(value)`：返回第一个不小于`value`的迭代器（适用于有序容器）。
- `upper_bound(value)`：返回第一个大于`value`的迭代器（适用于有序容器）。
- `equal_range(value)`：返回`value`所在范围的迭代器对（适用于有序容器）。

### $Map ~ library:$

- map<`type`,`type`> ID_Name = {{`key1`,`value1`},{`key2`,`value2`},$\cdots$}:初始化并赋值
- ID_Name[`key`] = `"value"`:单个插入
- ID_Name.insert(pair<int,string>(`key`,`value`)):单个插入

### $Set ~ library:$

- set<`type`>s:定义
- insert(`a`):插入元素`a`
- count(`a`):判断容器中是否存在某个元素`a`
- size():返回容器的尺寸，也可以元素的个数
- erase(`a`):删除集合中某个元素`a`
- clear():清空集合
- empty():判断是否为空
- begin():返回第一个节点的迭代器
- end():返回最后一个节点加1的迭代器
- rbegin():反向迭代器
- rend():反向迭代器
- find():查找某个指定元素的迭代器
- lower_bound():二分查找第一个不小于某个值的元素的迭代器
- get_allocator():返回集合的分配器
- swap():交换两个集合的变量
- max_size():返回集合能容纳元素的最大限值

### $Regex ~ Library:$

- regex_search(`text`,`pattern`):在`text`中寻找一个或者多个数字
- regex_hatch(`text`,`pattern`):在`text`中寻找字符串

### $Radom ~ library:$

- srand((unsigned)time(NULL))+rand():生成时基随机数

### $Eigen ~ library:$

- `Matrix`:矩阵
- `Vector`:向量
- `Eigenvalues`:计算特征值和特征向量
- `Inverse`:求逆矩阵
- `Transpose`:求转置矩阵
- `Determinant`:计算行列式
- `Solve`:解线性方程组

### $OpenCV ~ library:$

- imread():读取图像。
- imshow():显示图像。
- waitKey():等待按键。
- resize():调整图像大小。
- cvtColor():颜色空间转换。
- GaussianBlur():高斯模糊。
- Canny():边缘检测。
- findContours():查找轮廓。


getline(istream& is, string& str): 从输入流 `is` 中读取一行，并存入 `str`。可以使用 `str.length()` 或 `str.size()来查看字符串的长度（sizeof()查看数组长度）。

setprecision()
transform(,,,)
static_cast<int>(a)
const
