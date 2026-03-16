# House Price Prediction Project

## 项目简介
本项目旨在通过数据分析与机器学习技术预测加州房价。  
目标是探索影响房价的关键因素，并构建可用的预测模型，为房产决策提供参考。

---

## 项目功能
- **数据预处理与探索性分析 (EDA)**：清洗缺失值，处理异常值，分析特征分布。
- **房价预测模型构建**：基于随机森林回归 (Random Forest Regressor) 算法实现。
- **可视化分析结果**：自动生成特征重要性排序、房价分布图及相关性热度图。
- **项目结构规范化**：采用标准工程化目录，支持 GitHub 部署与版本控制。

---

## 项目结构
```text
house-price-prediction/
├── data/               # 原始数据和处理后的数据集
├── notebooks/          # Jupyter Notebook 分析文件
│   └── house_price_analysis.ipynb
├── outputs/            # 模型输出、图表、分析结果
├── src/                # Python 脚本、函数模块
├── README.md           # 项目说明文档
├── requirements.txt    # Python 依赖列表
└── project_log.md      # 项目每日日志记录
```

---

## 使用说明

1. **克隆项目到本地**：
   ```bash
   git clone [https://github.com/XINXIAO-project/house-price-prediction.git](https://github.com/XINXIAO-project/house-price-prediction.git)
   cd house-price-prediction
   ```

2. **安装依赖环境**：
   ```bash
   pip install -r requirements.txt
   ```

3. **运行分析流程**：
   在 Jupyter Notebook 中打开并运行 `notebooks/house_price_analysis.ipynb` 进行分析。

4. **查看输出结果**：
   所有的可视化图表和模型评估结果会自动保存到 `outputs/` 文件夹中。

---


## 更新与日志
- **日常开发记录**：请查阅 `project_log.md` 获取每日进度。
- **文档维护**：`README.md` 仅在项目架构变更、功能迭代或重大修改时更新。

---

## 注意事项
- **项目性质**：本项目仅供个人学习与研究使用。
- **数据来源**：California Housing Dataset。
- **推荐环境**：Python 3.x，建议使用虚拟环境进行管理。


## Dataset

- 因数据集过大无法上传，以下是数据集链接：https://www.kaggle.com/datasets/juhibhojani/house-price