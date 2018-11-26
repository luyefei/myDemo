import pymysql


class MysqlToken(object):

    def __init__(self, host="服务器地址", user="用户名", password="密码", db="数据库实例", charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    def get_token(self):
        db = pymysql.connect(self.host, self.user, self.password, db=self.db, charset=self.charset)
        cursor = db.cursor()
        cursor.execute("取最新的Token")
        db.commit()
        token = 'Bearer '+cursor.fetchone()[0]
        db.close()
        return token

    def update_finalresult(self):
        db = pymysql.connect(self.host, self.user, self.password, db="数据库实例", charset="utf8")
        cursor = db.cursor()
        cursor.execute("更新结果集最新时间为当天（可推）")
        db.commit()
        db.close()


if __name__ == '__main__':

    r = MysqlToken()
    r.get_token()




