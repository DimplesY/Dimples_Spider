from pymysql import connect
from pymysql import cursors

class DB():
    def __init__(self, host="localhost", port="3306", db="", user="root", passwd="root", chartset="utf-8"):
        # 建立连接
        self.conn = connect(host=host, port=port, db=db, user=user, passwd=passwd, chartset=chartset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with DB(host='192.168.68.129',user='root',passwd='zhumoran',db='text3') as db:
        db.execute('select * from course')
        print(db)
        for i in db:
            print(i)