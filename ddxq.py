# -*- coding: utf-8 -*-
from aip import AipOcr
import os
import time

def screenshot():
    filePath = "/sdcard/snapshot.png"
    runAdb("shell screencap -p "+filePath)
    runAdb("pull "+filePath+" android.png")
    return "android.png"

#adb
def runAdb(cmd):
    adb_path = "/usr/bin/adb"
    print(adb_path+" "+cmd)
    process = os.popen(adb_path+" "+cmd)
    output = process.read()
    return

""" 你的 APPID AK SK """
APP_ID = 'XXXXXX'
API_KEY = 'XXXXXX'
SECRET_KEY = 'XXXXXX'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#答案列表
strlist = ["逾期","基金经理","该做法不对","正确","说法错误","份额赎回","打客服电话挂失","相关方平台核实","优先保障钱卡安全","坏账风险","资金不急用的闲钱","系统学习投资知识","错的","不会","错误","说法正确","不可以","这种说法是正确的","置之不理","不买，可能被骗","社会保险","提醒父亲小心陷阱","与银行咨询","不一样","可以","流动性风险","银行柜台","正规渠道购买","不对，股市有风险","高利率或资费标准","不妥，存在风险","这个说法不对","谨慎对待","300","都是骗钱的","仔细阅读后决定","正确","可以","无法开机","提高警惕不透露","说法正确","喝腊八粥","年利率","不相信不咨询","建议其找工作人员","不予理会","不可能的","仔细阅读安装条款","与保险公司核实","定期进行手机杀毒","自主选择权","份额赎回","保险行业协会","保持警惕谢绝传单","以便网站调取记录","这个说法是错误","说法正确。","说法正确","向电视销售者求偿","不予理睬","谨慎核实信息真伪","与运营商核实","这种说法正确","引诱大学生贷款","警惕拒绝","妥善保管驾照","不予理睬","应退回全部货款","应退回全部货款","保持警惕谨慎识别","置之不理","提示父母有风险","说法错误","不可以","不要轻易同意","注意保护个人隐私","补足差额发放","不可信","身份证号码","短期价格大涨","做法错误，且不安全","硬币","置之不理","无痕浏览窗口","关掉网页查杀病毒","不安全","正确的","坚持官方付款流程","谨慎勾选授权协议","货币基金","进行风险评测","影响个人征信","向交管部门核实","不予理会","不予理会","相等","流动性风险","知情权","CVV/CVC码","做法正确","手机天猫"]

#主程序
def startup():
    screenshot()
    image = get_file_content('android.png')

    """ 可选参数 """
    options = {}
    options["vertexes_location"] = "true"
    client.general(image, options)
    a1 = client.general(image, options)

    for text in a1['words_result']:
        #print(text['words'])
        for str1 in strlist:
            if str1 in text['words']:
                print(text['location'])
                runAdb("shell input tap " + str(text['location']['left']) + " " + str(text['location']['top']))

#启动
while True:
    startup()
