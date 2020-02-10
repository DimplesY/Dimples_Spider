import pymysql

db = pymysql.connect("127.0.0.1", "root", "yanjie", "bookdb",cursor=pymysql.cursors.DictCursor)

cursor = db.cursor()

sql = '''
    select * from book
'''
try:
    cursor.execute(sql)
    data = cursor.fetchall()
    for more in data:
        print(more)
except:
    print("错误！")
    # 当DML(数据库操纵语言)语句时
    # db.rollback()

db.close()