import mysql.connector
from mysql.connector import Error

def get_connection():
    """获取数据库连接，失败时返回None并打印错误"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='ecommerce_db',  # 之前创建的数据库名
            user='root',              # 你的MySQL用户名
            password='670186'        # 替换为你的MySQL密码
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"数据库连接失败：{e}")
        return None

# 测试连接（运行此文件验证）
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("数据库连接成功！")
        conn.close()  # 记得关闭连接