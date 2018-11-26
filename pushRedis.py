import redis


class RedisMethod(object):

    def __init__(self, push_limit, host='redis集群服务器', port='端口', db="实例库", key="要查找的关键字"):
        '''@:parameter
           push_limit:推送限制
           key:设备id
        '''
        self.push_limit = push_limit
        self.host = host
        self.port = port
        self.db = db
        self.key = key
        self.cursor = redis.Redis(host=self.host, port=self.port, db=self.db)

    def get_result(self):
        me = self.cursor
        result = me.keys(self.key)
        reality = {}
        for n in result:
            get_result = me.get(n)
            reality["%s" % n.decode()] = get_result.decode()
        return reality  # 返回字典

    def set_redis(self):
        me = self.cursor
        for n in self.push_limit:
            me.set(n, self.push_limit[n])
        print("redis插入ok")

    def del_redis(self):
        me = self.cursor
        result = me.keys(self.key)
        for i in result:
            me.delete(i)

    def flush_redis(self):
        me = self.cursor
        me.flushall()
        print("redis清理完毕")


if __name__ == '__main__':
    pass
