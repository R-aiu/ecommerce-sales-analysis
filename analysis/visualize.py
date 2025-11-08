import matplotlib.pyplot as plt
from analysis.sales_analysis import get_monthly_sales

def plot_monthly_sales():
    """绘制月度销售额趋势图"""
    # 1. 获取数据
    df = get_monthly_sales()
    if df is None or df.empty:
        print("无数据可绘制")
        return

    # 2. 解决中文乱码
    # 替换为系统已有的中文字体（以微软雅黑为例）
    plt.rcParams["font.family"] = ["Microsoft YaHei", "SimSun", "sans-serif"]

    # 3. 绘图
    plt.figure(figsize=(10, 6))  # 图表大小
    plt.plot(df['month'], df['total_sales'], marker='o', color='b')  # 折线+数据点
    plt.title('月度销售额趋势分析', fontsize=15)  # 标题
    plt.xlabel('月份', fontsize=12)  # x轴标签
    plt.ylabel('销售额（元）', fontsize=12)  # y轴标签
    plt.grid(linestyle='--', alpha=0.7)  # 网格线
    plt.xticks(rotation=45)  # 月份标签旋转45度，避免重叠
    plt.tight_layout()  # 自动调整布局
    plt.show()  # 显示图表

# 测试绘图
if __name__ == "__main__":
    plot_monthly_sales()