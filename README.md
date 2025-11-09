# 电商销售分析系统

一个基于Python+MySQL的电商数据可视化分析工具，支持数据导入、销售统计和图表展示。

## 功能说明
1. 数据导入：从Excel导入订单明细到数据库
2. 销售分析：统计月度销售额、商品销量排名、用户复购率
3. 可视化：生成月度销售额趋势图

## 安装步骤
1. 克隆仓库：`git clone https://github.com/你的用户名/ecommerce-sales-analysis.git`
2. 安装依赖：`pip install pandas matplotlib mysql-connector-python openpyxl`
3. 配置数据库：修改`db/connect.py`中的MySQL用户名和密码
4. 初始化数据库：执行`database_init.sql`（包含表结构和测试数据）

## 使用方法
1. 运行`main.py`启动图形界面
2. 在“数据导入”区域选择Excel文件并导入
3. 在“数据分析”区域点击按钮查看统计结果或生成图表

## 项目结构
- `main.py`：图形界面入口
- `db/`：数据库连接和操作
- `analysis/`：数据分析和可视化
- `utils/`：数据导入工具
- `data/`：存放Excel数据（本地使用，不上传GitHub）
