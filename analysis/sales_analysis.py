import pandas as pd
from db.db_connect import get_connection

def get_monthly_sales(start_date=None, end_date=None):
    """获取指定日期范围内的月度销售额"""
    conn = get_connection()
    if not conn:
        return None

    # 构建SQL（支持日期筛选）
    sql = """
    SELECT 
        DATE_FORMAT(o.order_date, '%Y-%m') AS month,
        SUM(od.quantity * od.unit_price) AS total_sales
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    """
    params = []
    if start_date and end_date:
        sql += " WHERE o.order_date BETWEEN %s AND %s"
        params = [start_date, end_date]
    sql += " GROUP BY month ORDER BY month"

    # 执行查询并转为DataFrame
    df = pd.read_sql(sql, conn, params=params)
    conn.close()
    return df

# 测试统计功能
if __name__ == "__main__":
    sales_df = get_monthly_sales()  # 不填日期则查全部
    if sales_df is not None:
        print("月度销售额统计：")
        print(sales_df)