import json
import requests
from pushTest.mySql import MysqlToken


class Push(object):
    def __init__(self):
        self.push_url = "接口地址"
        self.push_json = {"PKID": "planid",
                           "JobId": "jobid",
                           "PushTemplateID": "templateID",
                           "PushSmsTemplateID": "SmsTemplateID",
                           "ActionType": "ActionType"}
        self.token = MysqlToken()
        self.token.update_finalresult()
        self.headers = {"Content-type": "application/json",
                        "Authorization": self.token.get_token()}

    def push_plan(self):
        r = requests.post(self.push_url, data=json.dumps(self.push_json), headers=self.headers)
        if r.status_code == 200:
            # print(self.token.get_token())
            print("推送ok")
        elif r.status_code == 404:
            # print(self.token.get_token())
            print("cookie过期")
        return r.status_code


if __name__ == '__main__':
    pass

