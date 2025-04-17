# $$Honor~Calculus~Notes$$

## $$UCUG1105$$

### $Inequation:$

#### $Normal~Inequation:$

##### $$\frac{2(x-1)}{x+1}\leqslant\ln{x}\leqslant\frac{1}{2}\left(x-\frac{1}{x}\right)$$

##### $$\frac{2}{\frac{1}{a}+\frac{1}{b}}\leqslant\sqrt{ab}<\frac{a-b}{\ln{a}-\ln{b}}<\frac{a+b}{2}\leqslant\sqrt{\frac{a^2+b^2}{2}}$$

##### $$0<sin(x)<x<tan(x)$$

##### $$cosx<\frac{sinx}{x}<1$$

### $Some~Function:$

#### $Trigonometric~Function:$

##### $$sin^2x+cos^2x=1$$

##### $$sin2x=2sinxcosx$$

##### $$cos2x=cos^2x-sin^2x=2cos^2x-1=1-2sin^2x$$

##### $$sin\alpha+sin\beta=2sin\frac{\alpha+\beta}{2}cos\frac{\alpha-\beta}{2}$$

##### $$sin\alpha cos\beta=\frac{1}{2}\left(sin(\alpha+\beta)+sin({\alpha-\beta})\right)$$

#### $Riemann~Zeta~Function:$

##### $$\zeta(s)=\sum_{k=1}^{\infty}\frac{1}{k^s}$$

##### $Harmonic~Series:$

##### $$\zeta(1)=\sum_{k=1}^{\infty}(1+\frac{1}{2}+\dotsb)=+\infty$$

### $Limit~Conclution:$

#### $Converge:$

##### $$Monotone+Bounded\rightarrow{Converge}$$

##### $$Converge\rightarrow{Bounded}$$

##### $$Monotone+Unbounded\rightarrow{Diverge~to~ \pm\infty}$$

#### $Arithmetic~Rules:$

##### $$\lim_{n\rightarrow{+\infty}}c=c$$

##### $$\lim_{x\rightarrow a}{\left(f(x)+g(x)\right)}=\lim_{x\rightarrow a}{f(x)}+\lim_{x\rightarrow a}{g(x)}$$

##### $$\lim_{x\rightarrow a}{\left(f(x)g(x)\right)}=\lim_{x\rightarrow a}{f(x)}\lim_{x\rightarrow a}{g(x)}$$

##### $$\lim_{x\rightarrow a}{\frac{f(x)}{g(x)}}=\frac{\lim_{x\rightarrow a}{f(x)}}{\lim_{x\rightarrow a}{g(x)}}~(\lim_{x\rightarrow a}{g(x)}\not ={0})$$

##### $$\lim_{x\rightarrow{a}}f(x)=\pm\infty \rightarrow{\lim_{x\rightarrow{a}}\frac{1}{f(x)}}=0$$

##### $$\lim_{x\rightarrow{a}}f(x)=0~\&~f(x)>0\rightarrow{\lim_{x\rightarrow{a}}\frac{1}{f(x)}}=+\infty$$

##### $$\lim_{x\rightarrow{a}}f(x)=0~\&~f(x)<0\rightarrow{\lim_{x\rightarrow{a}}\frac{1}{f(x)}}=-\infty$$

#### $Sandwich~Roles:$

##### $$\left\{\begin{array}{lr}{f(x)\leqslant{g(x)}\leqslant{h(x)}} \\ {\lim_{x\rightarrow{a}}f(x)}={\lim_{x\rightarrow{a}}h(x)}=L\end{array}\right. \rightarrow\lim_{x\rightarrow{a}}g(x)=L$$

#### $Continuous~Funcions:$

##### $$\lim_{n\rightarrow \infty}f(x_n)=f\left(\lim_{n\rightarrow \infty}x_n\right)$$

##### $$\lim_{x\rightarrow a}f(g(x))=f\left(\lim_{x\rightarrow a}g(x)\right)$$

### $Intergration$


以下是一些常用的积分公式，涵盖了三角函数、分子分母次数不等、反三角函数和双曲三角函数等常见情况：

### 1. 基本积分公式

- 常数积分：
  \[
  \int a \, dx = ax + C
  \]

- 幂函数积分：
  \[
  \int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)
  \]

### 2. 三角函数积分

- 正弦函数：
  \[
  \int \sin x \, dx = -\cos x + C
  \]

- 余弦函数：
  \[
  \int \cos x \, dx = \sin x + C
  \]

- 正切函数：
  \[
  \int \tan x \, dx = -\ln |\cos x| + C
  \]

- 余切函数：
  \[
  \int \cot x \, dx = \ln |\sin x| + C
  \]

- 正割函数：
  \[
  \int \sec x \, dx = \ln |\sec x + \tan x| + C
  \]

- 余割函数：
  \[
  \int \csc x \, dx = \ln |\csc x - \cot x| + C
  \]
  \[
  \int \sec^2 x \, dx = \tan x + C
  \]
  \[
  \int \csc^2 x \, dx = -\cot x + C
  \]
  \[
  \int \sec x \tan x \, dx = \sec x + C
  \]
  \[
  \int \csc x \cot x \, dx = -\csc x + C
  \]

### 3. 反三角函数积分

- 反正弦函数：
  \[
  \int \frac{dx}{\sqrt{1 - x^2}} = \arcsin x + C
  \]

- 反余弦函数：
  \[
  \int \frac{dx}{\sqrt{1 - x^2}} = \arccos x + C
  \]

- 反正切函数：
  \[
  \int \frac{dx}{1 + x^2} = \arctan x + C
  \]

- 反余切函数：
  \[
  \int \frac{dx}{x^2 + 1} = \text{arccot}\,x + C
  \]

### 4. 双曲三角函数积分

- 双曲正弦函数：
  \[
  \int \sinh x \, dx = \cosh x + C
  \]

- 双曲余弦函数：
  \[
  \int \cosh x \, dx = \sinh x + C
  \]

- 双曲正切函数：
  \[
  \int \tanh x \, dx = \ln |\cosh x| + C
  \]

- 双曲余切函数：
  \[
  \int \coth x \, dx = \ln |\sinh x| + C
  \]

- 双曲正割函数：
  \[
  \int \text{sech} x \, dx = 2 \arctan(\tanh \frac{x}{2}) + C
  \]

- 双曲余割函数：
  \[
  \int \text{csch} x \, dx = \ln |\coth x - \text{csch} x| + C
  \]

### 5. 分子分母次数不等的积分

对于分子分母次数不等的积分，通常需要进行部分分式分解、代换或使用特定的技巧。例如：

- 分式 \( \int \frac{1}{x^2 + 1} dx \) 可以使用反正切函数：
  \[
  \int \frac{dx}{x^2 + 1} = \arctan x + C
  \]

- 分式 \( \int \frac{1}{x} dx \) 结果是对数函数：
  \[
  \int \frac{dx}{x} = \ln |x| + C
  \]

### 6. 其他常见积分

- 指数函数：
  \[
  \int e^x \, dx = e^x + C
  \]

- 复合函数的积分：利用代换法。
- 换元法
换元法是将复杂的积分转化为更简单的形式。设 \( u = g(x) \)，则有：
\[
\int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du
\]
常见的应用：
    - \( \int e^{x^2} \cdot 2x \, dx \) 通过令 \( u = x^2 \) 来简化。

- 分部积分法
分部积分法基于公式：
\[
\int u \, dv = uv - \int v \, du
\]
常用于处理积的积分，例如：
\[
\int x e^x \, dx
\]
可以选择 \( u = x \) 和 \( dv = e^x \, dx \)。

### 7. 特殊积分

- **高斯积分**：
- 
  \[
  \int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
  \]
- **贝塔函数与伽马函数**：有时积分可以通过与贝塔函数或伽马函数的关系来计算。

### 牛顿-莱布尼兹公式&莱布尼兹法则

#### 1. 第一部分：定积分的求值

如果函数 \( f(x) \) 在区间 \( [a, b] \) 上连续，则定积分可以通过原函数来表示：

\[
\int_a^b f(x) \, dx = F(b) - F(a)
\]

其中 \( F(x) \) 是 \( f(x) \) 的一个原函数，也就是说，\( F'(x) = f(x) \)。

#### 2. 第二部分：导数与定积分的关系

如果我们有一个函数 \( F(x) \)，它是一个依赖于变量 \( x \) 的定积分，且积分的上下限与 \( x \) 有关，即：

\[
F(x) = \int_a^{g(x)} f(t) \, dt
\]

这里，\( g(x) \) 是 \( x \) 的一个函数，且 \( f(t) \) 是关于 \( t \) 的函数。牛顿-莱布尼兹公式的第二部分告诉我们，\( F(x) \) 对 \( x \) 的导数是：

\[
\frac{d}{dx} \left( \int_a^{g(x)} f(t) \, dt \right) = f(g(x)) \cdot g'(x)
\]

#### 3.莱布尼兹法则

假设我们有一个定积分：

\[
F(x) = \int_{g_1(x)}^{g_2(x)} f(t) \, dt
\]

其中，\(g_1(x)\) 和 \(g_2(x)\) 都是关于 \(x\) 的函数，\(f(t)\) 是被积函数，且我们需要求 \(F(x)\) 对 \(x\) 的导数。

根据 **莱布尼兹法则**，我们可以求出导数：

\[
\frac{d}{dx} \left( \int_{g_1(x)}^{g_2(x)} f(t) \, dt \right) = f(g_2(x)) \cdot \frac{d}{dx} g_2(x) - f(g_1(x)) \cdot \frac{d}{dx} g_1(x)
\]

### $Words:$

#### $Indeterminate~Form~不定式\\Monotone~单调\\Bounded~有界\\Euclidean~space~欧几里得空间\\Injectivity~单射\\ Surjective~满射\\Bijective~双射\\Inverse~Function~反函数\\Union~并集~A\bigcup B\\Intersection~交集~A\bigcap B\\Complement~补集\\Disjoint~互斥\\$
