import pymssql
import time

create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class Sql(object):

    def __init__(self):
        self.db = pymssql.connect("服务器ip", "用户名", "密码",
                                  database="实例库名", charset="utf8")
        self.cursor = self.db.cursor()

    def errorlog(self):
        '''
        {'Target': 'opneid', 'Code': '推送结果'}
        :return:
        '''
        self.cursor.execute("取openid，推送结果".format(i=create_date))
        row = self.cursor.fetchone()
        row_dict = {"Target": "openid".format(target=row[0]),
                    "Code": "推送结果".format(code=row[1])}
        if row_dict["Target"] == "openid" and (row_dict["Code"] == "推送结果"
                                                                     or row_dict["Code"] == "推送结果"):
            print("errorlog--sql比较ok")
            return True
        else:
            print("errorlog--sql比较出错")
            return False

    def pushlog(self):
        '''
        {'Target': 'openid', 'SendResult': '推送结果'}
        :return:
        '''
        self.cursor.execute("取openid和推送结果".format(i=create_date))
        row = self.cursor.fetchone()
        row_dict = {"Target": "openid".format(target=row[0].strip()),
                    "SendResult": "openid".format(code=row[1])}
        if row_dict["Target"] == "openid" and row_dict["SendResult"] == "推送结果":
            print("pushlog---sql比较ok")
            return True
        else:
            print("pushlog---sql比较错了")
            return False

    def del_date(self):
        self.cursor.execute("清空推送日志")
        self.db.commit()
        self.cursor.execute("清空推送日志")
        self.db.commit()
        print("sql---清理执行完毕")


if __name__ == '__main__':
    s = Sql()
    s.errorlog()
