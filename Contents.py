import datetime

'''单日设备限制1-1，
全局3-2，
全局标签3-1，
标签3-2，
模版3-1
'''

# 限制的头部
limit_head = "---头部内容"



# 限制的类型
limit_type_day = "--每日设备推送限制"
limit_type_global = "全局限制"
limit_type_global_tag = "全局标签限制"
limit_type_tag = "标签限制"
limit_type_errortag = "无关联的标签限制"
limit_type_template = "模版限制"
limit_type_errortemplate = "无关联的模版限制"
# 限制的日期
limit_date = datetime.datetime.now().strftime('%#Y/%#m/%#d')  # 当日
limit_yes_date = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%#Y/%#m/%#d')  # 前天
limit_bef_yes_date = (datetime.datetime.now()+datetime.timedelta(days=-2)).strftime('%#Y/%#m/%#d')  # 大前天
limit_bef_bef_yes_date = (datetime.datetime.now()+datetime.timedelta(days=-3)).strftime('%#Y/%#m/%#d')  # 大大前天

# 限制的设备号
openid = "用于测试的openid"

# 单日设备推送限制
testcase_id_1 = "推送服务用例-01/单日设备推送受限"
result_1 = False
limit_case1 = limit_head + limit_type_day + limit_date + openid
push_limit_day_pre_1 = {limit_case1: '1'}

push_limit_day_ect_1 = {limit_case1: '1'}

testcase_id_2 = "推送服务用例-02/单日设备未推送受限"
result_2 = True
limit_case2_1 = limit_head + limit_type_day + limit_date + openid
limit_case2_2 = limit_head + limit_type_template + limit_date +openid
limit_case2_3 = limit_head + limit_type_global + limit_date +openid
limit_case2_4 = limit_head + limit_type_global_tag + limit_date +openid
limit_case2_5 = limit_head + limit_type_tag + limit_date +openid

push_limit_day_pre_2 = {limit_case2_1: '0'}

push_limit_day_ect_2 = {limit_case2_1: '1',
                         limit_case2_2: '1',
                         limit_case2_3: '1',
                         limit_case2_4: '1',
                         limit_case2_5: '1'}

testcase_id_3 = "推送服务用例-03/单日设备推送跨天未受限"
result_3 = True
limit_case3_1 = limit_head + limit_type_template + limit_date + openid
limit_case3_2 = limit_head + limit_type_day + limit_date + openid
limit_case3_3 = limit_head + limit_type_global + limit_date + openid
limit_case3_4 = limit_head + limit_type_day + limit_yes_date + openid
limit_case3_5 = limit_head + limit_type_global_tag + limit_date + openid
limit_case3_6 = limit_head + limit_type_tag + limit_date + openid

push_limit_day_pre_3 = {limit_case3_4: '1'}

push_limit_day_ect_3 = {limit_case3_1: '1',
                         limit_case3_2: '1',
                         limit_case3_3: '1',
                         limit_case3_4: '1',
                         limit_case3_5: '1',
                         limit_case3_6: '1'}


# 全局限制
testcase_id_4 = "推送服务-04/全局设备推送受限"
result_4 = False
limit_case4_1 = limit_head + limit_type_global + limit_date + openid
limit_case4_2 = limit_head + limit_type_day + limit_date + openid
push_limit_day_pre_4 = {limit_case4_1: '2'}
push_limit_day_ect_4 = {limit_case4_2: '0',
                         limit_case4_1: '2'}

testcase_id_5 = "推送服务用例-05/全局设备推送不受限"
result_5 = True
limit_case5_1 = limit_head + limit_type_global + limit_bef_bef_yes_date + openid
limit_case5_2 = limit_head + limit_type_global + limit_date + openid
limit_case5_3 = limit_head + limit_type_template + limit_date + openid
limit_case5_4 = limit_head + limit_type_global_tag + limit_date + openid
limit_case5_5 = limit_head + limit_type_tag + limit_date + openid
limit_case5_6 = limit_head + limit_type_day + limit_date + openid
push_limit_day_pre_5 = {limit_case5_1: '2'}

push_limit_day_ect_5 = {limit_case5_1: '2',
                         limit_case5_2: '1',
                         limit_case5_3: '1',
                         limit_case5_4: '1',
                         limit_case5_5: '1',
                         limit_case5_6: '1'}


testcase_id_6 = "推送服务用例-06/全局推送跨天受限"
result_6 = False
limit_case6_1 = limit_head + limit_type_global + limit_bef_yes_date + openid
limit_case6_2 = limit_head + limit_type_global + limit_yes_date + openid
limit_case6_3 = limit_head + limit_type_day + limit_date + openid
push_limit_day_pre_6 = {limit_case6_1: '1',
                         limit_case6_2: '1'}

push_limit_day_ect_6 = {limit_case6_1: '1',
                         limit_case6_2: '1',
                         limit_case6_3: '0'}

testcase_id_7 = "推送服务用例-07/全局推送跨天不受限"
result_07 = True
limit_case7_1 = limit_head + limit_type_global + limit_bef_bef_yes_date + openid
limit_case7_2 = limit_head + limit_type_global + limit_bef_yes_date + openid
limit_case7_3 = limit_head + limit_type_global + limit_date + openid
limit_case7_4 = limit_head + limit_type_template + limit_date + openid
limit_case7_5 = limit_head + limit_type_global_tag + limit_date + openid
limit_case7_6 = limit_head + limit_type_tag + limit_date + openid
limit_case7_7 = limit_head + limit_type_day + limit_date + openid
push_limit_day_pre_7 = {limit_case7_1: '1',
                         limit_case7_2: '1'}

push_limit_day_ect_7 = {limit_case7_1: '1',
                         limit_case7_2: '1',
                         limit_case7_3: '1',
                         limit_case7_4: '1',
                         limit_case7_5: '1',
                         limit_case7_6: '1',
                         limit_case7_7: '1'}

# 标签-全局
testcase_id_8 = "推送服务用例-08/标签全局推送受限"
result_8 = False
limit_case8_1 = limit_head + limit_type_global_tag + limit_date + openid
limit_case8_2 = limit_head + limit_type_day + limit_date + openid
limit_case8_3 = limit_head + limit_type_global + limit_date + openid
push_limit_day_pre_8 = {limit_case8_1: '1'}

push_limit_day_ect_8 = {limit_case8_1: '1',
                         limit_case8_2: '0',
                         limit_case8_3: '0'}


testcase_id_9 = "推送服务用例-09/标签全局推送跨天受限"
result_9 = False
limit_case9_1 = limit_head + limit_type_global_tag + limit_bef_yes_date + openid
limit_case9_2 = limit_head + limit_type_day + limit_date + openid
limit_case9_3 = limit_head + limit_type_global + limit_date + openid
push_limit_day_pre_9 = {limit_case8_1: '1'}

push_limit_day_ect_9 = {limit_case8_1: '1',
                         limit_case8_2: '0',
                         limit_case8_3: '0'}

testcase_id_10 = "推送服务用例-10/标签全局推送跨天不受限"
result_10 = True
limit_case10_1 = limit_head + limit_type_global_tag + limit_bef_bef_yes_date + openid
limit_case10_2 = limit_head + limit_type_global + limit_date + openid
limit_case10_3 = limit_head + limit_type_template + limit_date + openid
limit_case10_4 = limit_head + limit_type_global_tag + limit_date + openid
limit_case10_5 = limit_head + limit_type_tag + limit_date + openid
limit_case10_6 = limit_head + limit_type_day + limit_date + openid
push_limit_day_pre_10 = {limit_case10_1: '1'}

push_limit_day_ect_10 = {limit_case10_1: '1',
                         limit_case10_2: '1',
                         limit_case10_3: '1',
                         limit_case10_4: '1',
                         limit_case10_5: '1',
                         limit_case10_6: '1'}


testcase_id_11 = "推送服务用例-11/标签全局推送不受限"
result_11 = True
limit_case11_1 = limit_head + limit_type_global_tag + limit_date + openid
limit_case11_2 = limit_head + limit_type_day + limit_date + openid
limit_case11_3 = limit_head + limit_type_global + limit_date + openid
limit_case11_4 = limit_head + limit_type_tag + limit_date + openid
limit_case11_5 = limit_head + limit_type_template + limit_date + openid
push_limit_day_pre_11 = {limit_case11_1: '0'}

push_limit_day_ect_11 = {limit_case11_1: '1',
                         limit_case11_2: '1',
                         limit_case11_3: '1',
                         limit_case11_4: '1',
                         limit_case11_5: '1'}


# 标签
testcase_id_12 = "推送服务用例-12/标签推送受限"
result_12 = False
limit_case12_1 = limit_head + limit_type_tag + limit_date + openid
limit_case12_2 = limit_head + limit_type_day + limit_date + openid
limit_case12_3 = limit_head + limit_type_global + limit_date + openid
limit_case12_4 = limit_head + limit_type_global_tag + limit_date + openid
push_limit_day_pre_12 = {limit_case12_1: '2'}

push_limit_day_ect_12 = {limit_case12_1: '2',
                         limit_case12_2: '0',
                         limit_case12_3: '0',
                         limit_case12_4: '0'}

testcase_id_13 = "推送服务用例-13/标签推送未受限"
result_13 = True
limit_case13_1 = limit_head + limit_type_tag + limit_date + openid
limit_case13_2 = limit_head + limit_type_day + limit_date + openid
limit_case13_3 = limit_head + limit_type_global + limit_date + openid
limit_case13_4 = limit_head + limit_type_global_tag + limit_date + openid
limit_case13_5 = limit_head + limit_type_template + limit_date + openid
push_limit_day_pre_13 = {limit_case13_1: '0'}

push_limit_day_ect_13 = {limit_case13_1: '1',
                         limit_case13_2: '1',
                         limit_case13_3: '1',
                         limit_case13_4: '1',
                         limit_case13_5: '1'}

testcase_id_14 = "推送服务用例-14/标签推送未受限"
result_14 = True
limit_case14_1 = limit_head + limit_type_tag + limit_date + openid
limit_case14_2 = limit_head + limit_type_day + limit_date + openid
limit_case14_3 = limit_head + limit_type_global + limit_date + openid
limit_case14_4 = limit_head + limit_type_global_tag + limit_date + openid
limit_case14_5 = limit_head + limit_type_template + limit_date + openid
push_limit_day_pre_14 = {limit_case14_1: '1'}

push_limit_day_ect_14 = {limit_case14_1: '2',
                         limit_case14_2: '1',
                         limit_case14_3: '1',
                         limit_case14_4: '1',
                         limit_case14_5: '1'}

testcase_id_15 = "推送服务用例-15/标签推送跨天受限"
result_15 = False
limit_case15_1 = limit_head + limit_type_tag + limit_bef_yes_date + openid
limit_case15_2 = limit_head + limit_type_tag + limit_yes_date + openid
limit_case15_3 = limit_head + limit_type_tag + limit_date + openid
limit_case15_4 = limit_head + limit_type_day + limit_date + openid
limit_case15_5 = limit_head + limit_type_global + limit_date + openid
limit_case15_6 = limit_head + limit_type_global_tag + limit_date + openid
push_limit_day_pre_15 = {limit_case15_1: '1',
                         limit_case15_2: '1',
                         limit_case15_3: '0'}

push_limit_day_ect_15 = {limit_case15_1: '1',
                         limit_case15_2: '1',
                         limit_case15_3: '0',
                         limit_case15_4: '0',
                         limit_case15_5: '0',
                         limit_case15_6: '0'}


testcase_id_16 = "推送服务用例-16/标签推送跨天不受限"
result_16 = True
limit_case16_1 = limit_head + limit_type_tag + limit_bef_bef_yes_date + openid
limit_case16_2 = limit_head + limit_type_tag + limit_bef_yes_date + openid
limit_case16_3 = limit_head + limit_type_tag + limit_yes_date + openid
limit_case16_4 = limit_head + limit_type_tag + limit_date + openid
limit_case16_5 = limit_head + limit_type_day + limit_date + openid
limit_case16_6 = limit_head + limit_type_global + limit_date + openid
limit_case16_7 = limit_head + limit_type_global_tag + limit_date + openid
limit_case16_8 = limit_head + limit_type_template + limit_date + openid
push_limit_day_pre_16 = {limit_case16_1: '1',
                         limit_case16_2: '1',
                         limit_case16_3: '0',
                         limit_case16_4: '0'}

push_limit_day_ect_16 = {limit_case16_1: '1',
                         limit_case16_2: '1',
                         limit_case16_3: '0',
                         limit_case16_4: '1',
                         limit_case16_5: '1',
                         limit_case16_6: '1',
                         limit_case16_7: '1',
                         limit_case16_8: '1'}

testcase_id_17 = "推送服务用例-17/标签推送不受限"
result_17 = True
limit_case17_1 = limit_head + limit_type_errortag + limit_date + openid
limit_case17_2 = limit_head + limit_type_tag + limit_date + openid
limit_case17_3 = limit_head + limit_type_day + limit_date + openid
limit_case17_4 = limit_head + limit_type_global + limit_date + openid
limit_case17_5 = limit_head + limit_type_global_tag + limit_date + openid
limit_case17_6 = limit_head + limit_type_template + limit_date + openid
push_limit_day_pre_17 = {limit_case17_1: '3'}

push_limit_day_ect_17 = {limit_case17_1: '3',
                         limit_case17_2: '1',
                         limit_case17_3: '1',
                         limit_case17_4: '1',
                         limit_case17_5: '1',
                         limit_case17_6: '1'}

# 模版
testcase_id_18 = "推送服务用例-18/模版推送受限"
result_18 = False
limit_case18_1 = limit_head + limit_type_template + limit_date + openid
limit_case18_2 = limit_head + limit_type_day + limit_date + openid
limit_case18_3 = limit_head + limit_type_global + limit_date + openid
limit_case18_4 = limit_head + limit_type_global_tag + limit_date + openid
limit_case18_5 = limit_head + limit_type_tag + limit_date + openid
push_limit_day_pre_18 = {limit_case18_1: '1'}

push_limit_day_ect_18 = {limit_case18_1: '1',
                         limit_case18_2: '0',
                         limit_case18_3: '0',
                         limit_case18_4: '0',
                         limit_case18_5: '0'}

testcase_id_19 = "推送服务用例-19/模版推送未受限"
result_19 = True
limit_case19_1 = limit_head + limit_type_template + limit_date + openid
limit_case19_2 = limit_head + limit_type_day + limit_date + openid
limit_case19_3 = limit_head + limit_type_global + limit_date + openid
limit_case19_4 = limit_head + limit_type_global_tag + limit_date + openid
limit_case19_5 = limit_head + limit_type_tag + limit_date + openid
push_limit_day_pre_19 = {limit_case19_1: '0'}

push_limit_day_ect_19 = {limit_case19_1: '1',
                         limit_case19_2: '1',
                         limit_case19_3: '1',
                         limit_case19_4: '1',
                         limit_case19_5: '1'}

testcase_id_20 = "推送服务用例-20/模版推送跨天受限"
result_20 = False
limit_case20_1 = limit_head + limit_type_template + limit_bef_yes_date + openid
limit_case20_2 = limit_head + limit_type_template + limit_yes_date + openid
limit_case20_3 = limit_head + limit_type_template + limit_date + openid
limit_case20_4 = limit_head + limit_type_day + limit_date + openid
limit_case20_5 = limit_head + limit_type_global + limit_date + openid
limit_case20_6 = limit_head + limit_type_global_tag + limit_date + openid
limit_case20_7 = limit_head + limit_type_tag + limit_date + openid
push_limit_day_pre_20 = {limit_case20_1: '1',
                         limit_case20_2: '0',
                         limit_case20_3: '0'}

push_limit_day_ect_20 = {limit_case20_1: '1',
                         limit_case20_2: '0',
                         limit_case20_3: '0',
                         limit_case20_4: '0',
                         limit_case20_5: '0',
                         limit_case20_6: '0',
                         limit_case20_7: '0'}

testcase_id_21 = "推送服务用例-21/模版推送跨天未受限"
result_21 = True
limit_case21_1 = limit_head + limit_type_template + limit_bef_bef_yes_date + openid
limit_case21_2 = limit_head + limit_type_template + limit_bef_yes_date + openid
limit_case21_3 = limit_head + limit_type_template + limit_yes_date + openid
limit_case21_4 = limit_head + limit_type_template + limit_date + openid
limit_case21_5 = limit_head + limit_type_day + limit_date + openid
limit_case21_6 = limit_head + limit_type_global + limit_date + openid
limit_case21_7 = limit_head + limit_type_global_tag + limit_date + openid
limit_case21_8 = limit_head + limit_type_tag + limit_date + openid
push_limit_day_pre_21 = {limit_case21_1: '1',
                         limit_case21_2: '0',
                         limit_case21_3: '0',
                         limit_case21_4: '0'}

push_limit_day_ect_21 = {limit_case21_1: '1',
                         limit_case21_2: '0',
                         limit_case21_3: '0',
                         limit_case21_4: '1',
                         limit_case21_5: '1',
                         limit_case21_6: '1',
                         limit_case21_7: '1',
                         limit_case21_8: '1'}


testcase_id_22 = "推送服务用例-22/模版推送跨天未受限"
result_22 = True
limit_case22_1 = limit_head + limit_type_errortemplate + limit_date + openid
limit_case22_2 = limit_head + limit_type_template + limit_date + openid
limit_case22_3 = limit_head + limit_type_day + limit_date + openid
limit_case22_4 = limit_head + limit_type_global + limit_date + openid
limit_case22_5 = limit_head + limit_type_global_tag + limit_date + openid
limit_case22_6 = limit_head + limit_type_tag + limit_date + openid
push_limit_day_pre_22 = {limit_case22_1: '1'}

push_limit_day_ect_22 = {limit_case22_1: '1',
                         limit_case22_2: '1',
                         limit_case22_3: '1',
                         limit_case22_4: '1',
                         limit_case22_5: '1',
                         limit_case22_6: '1'}



