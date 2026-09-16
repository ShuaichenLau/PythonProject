import pymysql
import pymysql.cursors

# 数据库查询
def execute_select_query():
    # 1. 数据库连接配置
    connection_config = {
        'host': 'localhost',  # 数据库地址
        'port': 3306,  # 端口，默认3306
        'user': 'root',  # 用户名
        'password': 'admin',  # 密码
        'database': 'mall',  # 数据库名
        'charset': 'utf8mb4',  # 字符集，推荐 utf8mb4 兼容表情和特殊字符
        # 🌟 核心优化：让返回结果自动组装成【字典格式】(Key-Value)，类似于 Java 的 Map，而不是枯燥的元组
        'cursorclass': pymysql.cursors.DictCursor
    }

    # 2. 建立连接（使用 with 自动管理连接关闭）
    try:
        with pymysql.connect(**connection_config) as connection:
            # 3. 创建游标（使用 with 自动管理游标关闭）
            with connection.cursor() as cursor:
                # 4. 编写 SQL 语句（推荐使用 %s 作为占位符，绝对不要用字符串拼接，防止 SQL 注入）
                sql = "SELECT id, member_id, coupon_id FROM oms_order WHERE pay_type = %s AND member_username = %s"
                params = (1, 'test')  # 对应 SQL 中的两个 %s

                # 5. 执行查询
                cursor.execute(sql, params)

                # 6. 获取查询结果
                # fetchall() 获取所有行。如果只想取一条，可以使用 fetchone()
                result_list = cursor.fetchall()

                # 7. 遍历处理结果
                print(f"成功查询到 {len(result_list)} 条数据：")
                for row in result_list:
                    # 因为设置了 DictCursor，可以直接通过字段名作为 Key 取值
                    id = row['id']
                    member_id = row['member_id']
                    coupon_id = row['coupon_id']
                    print("商品ID: {}, 会员ID: {}, 优惠券ID: {}".format(id, member_id, coupon_id))

    except pymysql.MySQLError as e:
        print(f"数据库连接或查询发生异常: {e}")


if __name__ == '__main__':
    execute_select_query()