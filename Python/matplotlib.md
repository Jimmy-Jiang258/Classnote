
## 1. **绘图核心函数**

### **`pyplot` 模块**

`matplotlib.pyplot` 提供了类似 MATLAB 的绘图功能，以下是常用的绘图函数：

#### **基本绘图**

##### **折线图`plt.plot(x, y, format, **kwargs)`**

- **`x`**: x 轴数据，列表、数组或 pandas 序列。
- **`y`**: y 轴数据，列表、数组或 pandas 序列。
- **`format`**: 可选，指定线条颜色、样式和标记符号（例如：`'r--'` 表示红色虚线）。
- **`kwargs`**: 其他可选参数，如 `label`（图例标签）、`linewidth`（线宽）。

##### **散点图`plt.scatter(x, y, s, c, **kwargs)`**

- **`x`**: x 轴数据。
- **`y`**: y 轴数据。
- **`s`**: 可选，点的大小。
- **`c`**: 可选，点的颜色（单一颜色或颜色数组）。
- **`kwargs`**: 其他参数如透明度 `alpha`、颜色映射 `cmap`。

##### **柱状图`plt.bar(x, height, width, **kwargs)(plt.barh())`**

- **`x`**: 柱子位置，通常为整数或分类变量。
- **`height`**: 柱子的高度。
- **`width`**: 可选，柱子的宽度，默认为 0.8。
- **`kwargs`**: 可选参数，如颜色 `color`，边框宽度 `edgecolor`。

##### **直方图`plt.hist(data, bins, **kwargs)`**

- **`data`**: 数据数组或列表。
- **`bins`**: 可选，分组的区间数或区间边界。
- **`kwargs`**: 可选参数如直方图类型 `histtype`（如 `bar` 或 `step`）。

##### **饼图`plt.pie(data, labels, autopct, **kwargs)`**

- **`data`**: 每部分的数值。
- **`labels`**: 可选，每部分的标签。
- **`autopct`**: 可选，显示百分比格式（如 `'%1.1f%%'`）。
- **`kwargs`**: 其他参数如起始角度 `startangle`。

#### **高级图表**

##### **箱线图`plt.boxplot(data, vert=True, patch_artist=False, **kwargs)`**

- **`data`**: 数据数组或列表，通常是多组数据。
- **`vert`**: 可选，布尔值，表示是否垂直显示，默认 `True`。如果为 `False`，将以水平方式显示箱线图。
- **`patch_artist`**: 可选，布尔值，是否填充箱体的颜色，默认为 `False`。若为 `True`，箱体将使用指定的颜色填充。
- **`kwargs`**: 其他可选参数，如：
  - `whiskerprops`: 控制胡须线的样式。
  - `boxprops`: 控制箱体的样式。
  - `flierprops`: 控制异常值的样式。

##### **小提琴图`plt.violinplot(data, showmeans=False, showmedians=True, **kwargs)`**

- **`data`**: 数据数组或列表。
- **`showmeans`**: 可选，布尔值，是否显示均值，默认为 `False`。
- **`showmedians`**: 可选，布尔值，是否显示中位数，默认为 `True`。
- **`kwargs`**: 其他参数如颜色映射、宽度等。

##### **茎叶图`plt.stem(x, y, basefmt=" ", **kwargs)`**

- **`x`**: x 轴数据。
- **`y`**: y 轴数据。
- **`basefmt`**: 可选，指定基线的格式，通常使用空格 `basefmt=" "` 来移除基线。
- **`kwargs`**: 可选参数，如线条颜色、标记大小等。

##### **带误差线的图`plt.errorbar(x, y, yerr, xerr=None, fmt='o', **kwargs)`**

- **`x`**: x 轴数据。
- **`y`**: y 轴数据。
- **`yerr`**: y 轴方向的误差，通常为数组或列表，表示每个数据点的误差。
- **`xerr`**: 可选，x 轴方向的误差。
- **`fmt`**: 可选，数据点的样式（如 `'o'` 表示圆点）。
- **`kwargs`**: 其他参数，如线条样式 `linestyle`，颜色 `color`。



##### **等高线图`plt.contour(X, Y, Z, levels, **kwargs)`**

- **`X`, `Y`**: 生成网格的坐标数组。
- **`Z`**: 等高线数据，是一个二维数组，表示在每个 `(x, y)` 坐标下的值。
- **`levels`**: 可选，指定等高线的层次。如果没有指定，`matplotlib` 将自动选择。
- **`kwargs`**: 可选，其他参数如颜色、线型等。


##### 3D 折线图`ax.plot3D(x, y, z, **kwargs)`

- **`x`, `y`, `z`**: 3D 数据坐标。
- **`kwargs`**: 其他参数，如颜色 `color`，线型 `linestyle`。


##### 3D 散点图`ax.scatter3D(x, y, z, **kwargs)`

- **`x`, `y`, `z`**: 3D 数据坐标。
- **`kwargs`**: 其他可选参数，如颜色 `color`，大小 `s`。


##### 3D 曲面图`ax.plot_surface(X, Y, Z, **kwargs)`

- **`X`, `Y`**: 生成网格的坐标数组。
- **`Z`**: 曲面的高度值。
- **`kwargs`**: 其他可选参数，如颜色映射 `cmap`，光照效果 `lighting`。

##### 3D 等高线图`ax.contour3D(X, Y, Z, levels, **kwargs)`

- **`X`, `Y`**: 网格坐标。
- **`Z`**: 高度值。
- **`levels`**: 等高线的级别。

##### **热力图`plt.imshow(data, cmap, interpolation, **kwargs)`**

- **`data`**: 要显示的二维数据（如矩阵）。
- **`cmap`**: 可选，颜色映射（如 `'hot'`, `'coolwarm'`）。
- **`interpolation`**: 可选，插值方法（如 `'nearest'`, `'bilinear'`）。

##### - `plt.imshow()`

- 显示图像或矩阵数据。

##### `plt.quiver()`

- 绘制矢量场。

---

## 2. **布局与样式**

##### **`plt.figure(figsize, dpi)`**

- **`figsize`**: 可选，图形尺寸（宽，高），单位为英寸。
- **`dpi`**: 可选，每英寸点数（分辨率）。

##### **`plt.subplots(nrows, ncols, **kwargs)`**

- **`nrows`**: 行数。
- **`ncols`**: 列数。
- **`kwargs`**: 其他参数如共享轴 `sharex`, `sharey`。

##### - `plt.subplot()`

- 在单个绘图窗口中绘制子图。

##### - `plt.tight_layout()`

- 自动调整子图间距，避免重叠。

##### - `plt.grid()`

- 添加或控制网格线。

##### - `plt.style.use()`

- 使用预定义的绘图样式。

---

## 3. **坐标轴与标签**

##### **`plt.xlabel(label, **kwargs)`**

- **`label`**: 字符串类型，x 轴标签。
- **`kwargs`**: 可选字体参数（如字体大小 `fontsize`，字体类型 `fontname`）。

##### **`plt.ylabel(label, **kwargs)`**

- 与 `xlabel` 类似，但作用于 y 轴。

##### **`plt.title(title, **kwargs)`**

- **`title`**: 图表标题，字符串类型。
- **`kwargs`**: 可选字体参数。

##### **`plt.legend(loc, **kwargs)`**

- **`loc`**: 可选，图例位置（如 `'upper left'` 或数字索引）。
- **`kwargs`**: 其他选项如边框 `frameon`。

##### **`plt.xticks(ticks, labels, **kwargs)`**

- **`ticks`**: 可选，刻度位置列表。
- **`labels`**: 可选，刻度标签列表。
- **`kwargs`**: 其他字体参数。

##### **`plt.yticks(ticks, labels, **kwargs)`**

- 与 `xticks` 类似，但作用于 y 轴。
  
##### **`plt.axis()`**

- 控制坐标轴范围和显示样式。
- 
---

## 4. **颜色与标记**

- `plt.colormaps()`: 查看可用的颜色映射。
- `plt.set_cmap()`: 设置当前颜色映射。
- `plt.colorbar()`: 添加颜色条，适用于映射数据（如热图）。
- `plt.scatter()` 和 `plt.plot()` 中可用 `c`, `marker`, `linestyle` 等参数自定义颜色和样式。

---

## 5. **保存与显示**

##### **`plt.show(block)`**

- **`block`**: 是否阻塞运行，默认 `True`。

##### **`plt.savefig(fname, dpi, **kwargs)`**

- **`fname`**: 文件名（如 `'output.png'`）。
- **`dpi`**: 分辨率，默认为当前图形的 DPI 设置。
- **`kwargs`**: 可选参数，如透明背景 `transparent=True`。

---

## 6. **交互与动画**

- `plt.pause()`: 暂停以显示更新的图表（用于动态绘图）。
- `FuncAnimation`: 创建动画。
