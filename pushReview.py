from pushTestdemo.pushRedis import RedisMethod
from pushTestdemo.push import Push
from pushTestdemo.Sql import Sql
import time


class PushUnittest(object):

    def __init__(self, push_limit, expect_limit, testcase_id, is_succeed):

        ''' content: 限制expect_result: 预期限制 '''
        self.push_limit = push_limit
        self.expect_limit = expect_limit
        self.case_id = testcase_id
        self.redis = RedisMethod(self.push_limit)
        self.sql = Sql()
        self.push_test = Push()
        self.is_succeed = is_succeed

    def push(self):
        '''
        1，清空限制/设置限制 --content
        2，清空推送日志
        3，进行推送
        4，等待2分钟
        5，拿到推送日志，断言
        6，拿到推送限制日志，断言 --expect_result
        '''
        self.redis.flush_redis()
        self.sql.del_date()
        if self.is_succeed is True:
            print("走未被限制的逻辑")
            self.redis.set_redis()
            if self.push_test.push_plan() == 200:
                time.sleep(70)
                if self.sql.pushlog():
                    # r = self.redis.get_result()
                    # print(r)   打印 实际redis
                    # print(self.expect_limit)  打印预期redis
                    if self.redis.get_result() == self.expect_limit:
                        print("redis符合预期")
                        print(self.case_id + "-----测试通过\n")
                        print("==============================================================")
                    else:
                        print("比较失败")
            else:
                print(self.case_id + "-----测试失败")
                quit()
        elif self.is_succeed is False:
            print("走被限制的逻辑")
            self.redis.set_redis()
            if self.push_test.push_plan() == 200:
                time.sleep(70)
                if self.sql.errorlog():
                    # print(self.redis.get_result()) 打印 实际redis
                    # print(self.expect_limit)   打印预期redis
                    if self.redis.get_result() == self.expect_limit:
                        print("redis符合预期")
                        print(self.case_id + "-----测试通过\n")
                        print("==============================================================")
                    else:
                        print("redis不符合预期，比较失败")
            else:
                print(self.case_id + "-----测试失败")
                quit()
        else:
            print("你传了什么东西")
            quit()


if __name__ == '__main__':

    pass
