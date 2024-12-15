### `sklearn`（Scikit-learn）函数库文档详细总结

`sklearn`（Scikit-learn）是一个广泛使用的机器学习库，提供了各种数据预处理、模型训练、评估和选择的工具。它支持监督学习、无监督学习、模型选择和评估等任务，并且接口简单易用，适用于各种机器学习任务。

以下是对 `sklearn` 库中常用函数和模块的详细总结，包括其主要功能、使用方法和示例。

---

## 1. **安装 `sklearn`**

首先，你需要安装 `sklearn` 库，可以通过 `pip` 安装：

```bash
pip install scikit-learn
```

---

## 2. **数据预处理（Preprocessing）**

### 2.1 **StandardScaler**
`StandardScaler` 是标准化数据的常用方法，能将数据的均值变为 0，标准差变为 1。

- **功能**：标准化数据，将每一列减去均值并除以标准差。
- **用法**：
    ```python
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)  # X 是输入数据
    ```

### 2.2 **MinMaxScaler**
`MinMaxScaler` 用于将特征缩放到指定的最小值和最大值之间（默认是 0 到 1）。

- **功能**：将每个特征缩放到给定的最小值和最大值。
- **用法**：
    ```python
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    ```

### 2.3 **OneHotEncoder**
`OneHotEncoder` 用于将分类变量转换为独热编码（One-Hot Encoding）形式。

- **功能**：将分类特征转化为独热编码。
- **用法**：
    ```python
    from sklearn.preprocessing import OneHotEncoder

    encoder = OneHotEncoder(sparse=False)  # sparse=False 返回的是数组而非稀疏矩阵
    X_encoded = encoder.fit_transform(X)
    ```

### 2.4 **LabelEncoder**
`LabelEncoder` 用于将分类标签转化为数值型标签。

- **功能**：将类别标签转换为数字编码。
- **用法**：
    ```python
    from sklearn.preprocessing import LabelEncoder

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)  # y 是目标标签
    ```

---

## 3. **监督学习（Supervised Learning）**

### 3.1 **线性回归（Linear Regression）**
`LinearRegression` 是最常用的回归模型之一，用于拟合线性模型。

- **功能**：拟合一个线性回归模型，求解自变量与因变量之间的关系。
- **用法**：
    ```python
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    model.fit(X_train, y_train)  # X_train 是特征，y_train 是目标变量
    y_pred = model.predict(X_test)  # 预测
    ```

### 3.2 **逻辑回归（Logistic Regression）**
`LogisticRegression` 用于分类任务，特别是二分类问题。

- **功能**：基于逻辑函数进行分类预测，常用于二分类问题。
- **用法**：
    ```python
    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    ```

### 3.3 **决策树（Decision Tree）**
`DecisionTreeClassifier` 和 `DecisionTreeRegressor` 用于分类和回归任务。

- **功能**：基于决策树算法进行分类或回归。
- **用法**：
    ```python
    from sklearn.tree import DecisionTreeClassifier

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    ```

### 3.4 **支持向量机（SVM）**
`SVC`（支持向量分类）是用于分类任务的支持向量机实现，`SVR` 是用于回归的实现。

- **功能**：基于支持向量机算法进行分类或回归。
- **用法**：
    ```python
    from sklearn.svm import SVC

    model = SVC()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    ```

---

## 4. **无监督学习（Unsupervised Learning）**

### 4.1 **K-means 聚类**
`KMeans` 用于将数据分为 K 个簇，是常见的聚类算法。

- **功能**：将数据分成指定数量的簇。
- **用法**：
    ```python
    from sklearn.cluster import KMeans

    model = KMeans(n_clusters=3)  # 设置为3个簇
    model.fit(X)  # X 是输入数据
    labels = model.predict(X)  # 预测每个数据点的簇标签
    ```

### 4.2 **主成分分析（PCA）**
`PCA` 用于数据降维，常用于减少特征维度。

- **功能**：通过主成分分析（PCA）对数据进行降维。
- **用法**：
    ```python
    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)  # 降到2维
    X_pca = pca.fit_transform(X)
    ```

### 4.3 **聚类评估：轮廓系数（Silhouette Coefficient）**
用于评估聚类的效果，值越高表示聚类效果越好。

- **功能**：计算聚类的轮廓系数。
- **用法**：
    ```python
    from sklearn.metrics import silhouette_score

    score = silhouette_score(X, labels)
    print("Silhouette Score:", score)
    ```

---

## 5. **模型评估（Model Evaluation）**

### 5.1 **交叉验证（Cross-Validation）**
`cross_val_score` 用于交叉验证模型的表现。

- **功能**：对模型进行交叉验证，评估模型的泛化能力。
- **用法**：
    ```python
    from sklearn.model_selection import cross_val_score

    model = LogisticRegression()
    scores = cross_val_score(model, X, y, cv=5)  # 5折交叉验证
    print("Cross-validation scores:", scores)
    ```

### 5.2 **混淆矩阵（Confusion Matrix）**
`confusion_matrix` 用于评估分类模型的性能。

- **功能**：生成混淆矩阵，评估分类模型的准确性。
- **用法**：
    ```python
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y_true, y_pred)  # y_true 和 y_pred 是真实标签和预测标签
    print("Confusion Matrix:\n", cm)
    ```

### 5.3 **精度（Accuracy）**
`accuracy_score` 用于评估分类任务的准确率。

- **功能**：计算分类模型的准确率。
- **用法**：
    ```python
    from sklearn.metrics import accuracy_score

    accuracy = accuracy_score(y_true, y_pred)
    print("Accuracy:", accuracy)
    ```

---

## 6. **模型选择（Model Selection）**

### 6.1 **网格搜索（GridSearchCV）**
`GridSearchCV` 用于调优模型的超参数，找到最佳参数组合。

- **功能**：通过穷举搜索超参数空间，找到最优的超参数组合。
- **用法**：
    ```python
    from sklearn.model_selection import GridSearchCV

    param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
    grid_search = GridSearchCV(SVC(), param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    print("Best parameters:", grid_search.best_params_)
    ```

### 6.2 **交叉验证的随机搜索（RandomizedSearchCV）**
`RandomizedSearchCV` 进行超参数搜索时，随机选择超参数组合。

- **功能**：通过随机搜索超参数空间，找到最佳超参数组合。
- **用法**：
    ```python
    from sklearn.model_selection import RandomizedSearchCV

    param_dist = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
    random_search = RandomizedSearchCV(SVC(), param_dist, n_iter=10, cv=5)
    random_search.fit(X_train, y_train)
    print("Best parameters:", random_search.best_params_)
    ```

---

## 7. **总结**

- **`sklearn.preprocessing`**：提供了标准化、归一化、独热编码等常用数据预处理方法。
- **`sklearn.linear_model`**、**`sklearn.svm`** 等：提供了多种监督学习算法，如线性回归、逻辑回归、支持向量机

等。
- **`sklearn.cluster`**、**`sklearn.decomposition`** 等：提供了无监督学习算法，如 K-means 聚类、PCA 降维等。
- **`sklearn.model_selection`**：提供了交叉验证、超参数调优、训练集和测试集划分等工具。
- **`sklearn.metrics`**：提供了多种评估模型性能的方法，如精度、混淆矩阵、F1 分数等。

通过使用 `sklearn`，你可以轻松进行数据预处理、模型训练、评估和选择，广泛应用于分类、回归、聚类、降维等机器学习任务。
```

这个 Markdown 文档涵盖了 `sklearn` 中常见的函数和方法，适合用于机器学习项目中的数据预处理、模型训练、评估和选择等任务。