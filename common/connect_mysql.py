import pymysql
dbinfo = {
    "host": "49.235.92.12",
    "port": 3309,
    "user": "root",
    "password": "123456"
}

class ConnectDb():
    def __init__(self, dbinfo, database="apps"):
        # 连接数据库
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **dbinfo)
        # 创建游标
        self.cursor = self.db.cursor()

    def select_sql(self,sql):
        # 查询语句
        # sql1 = 'select * from auth_user where username =  "test";'
        self.cursor.execute(sql)
        # 得到查询结果
        res = self.cursor.fetchall()
        # print(res)
        return res

    def execute_sql(self,sql):
        # sql2 = 'UPDATE auth_user set email="223@qq.com" WHERE username="test";'
        try:
            self.cursor.execute(sql)
            self.db.commit() # 提交才生效
        except:
            # 执行报错回滚
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    db = ConnectDb(dbinfo=dbinfo, database="apps")
    sql = 'SELECT * from auth_user WHERE username="test";'
    res = db.select_sql(sql)
    print(res)



