import pandas as pd
from db.db_connect import get_connection  # 正确引用db目录下的db_connect.py模块

def import_order_details_from_excel(file_path):
    """从Excel导入订单明细到order_details表"""
    # 1. 读取Excel数据
    try:
        df = pd.read_excel(file_path)
        print(f"成功读取Excel，共{len(df)}条数据")
    except Exception as e:
        print(f"读取Excel失败：{e}")
        return

    # 2. 连接数据库并插入
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    # 3. 逐行插入（实际项目可批量插入优化效率）
    success = 0
    for _, row in df.iterrows():
        try:
            sql = """
            INSERT INTO order_details (order_id, product_id, quantity, unit_price)
            VALUES (%s, %s, %s, %s)
            """
            # 将numpy类型转换为Python原生类型（int/float）
            values = (
                int(row['order_id']),  # 转换为Python int
                int(row['product_id']),  # 转换为Python int
                int(row['quantity']),  # 转换为Python int
                float(row['unit_price'])  # 转换为Python float（处理价格）
            )
            cursor.execute(sql, values)
            success += 1
        except Exception as e:
            print(f"插入失败（行{_}）：{e}")

    # 4. 提交并关闭连接
    conn.commit()
    cursor.close()
    conn.close()
    print(f"导入完成，成功{success}条，失败{len(df)-success}条")

# 测试导入（运行此文件）
if __name__ == "__main__":
    import_order_details_from_excel("../data/orders_sample.xlsx")  # 用../回到项目根目录，再进入data目录