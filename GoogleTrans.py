import time

import xlwt
from selenium import webdriver

workbook = xlwt.Workbook()
workshell = workbook.add_sheet('sheet1')

print("翻译文本：")
trans=input()
print("翻译次数：")
n=input()
#n = 15
#print(trans+"翻译"+n+"次")
T = 0.8
browserEn = webdriver.Chrome("D:\\chromedriver")#翻译成英文
browserCn = webdriver.Chrome("D:\\chromedriver")#翻译成中文
workshell.write(0, 0, trans)
#提供中文——>英文 循环(英文——>中文 中文——>英文)
#初次翻译英文
browserEn.get("https://translate.google.cn/?sl=auto&tl=en&text="+trans+"&op=translate")
i = 0
global Eng
global Cn
for span in browserEn.find_elements_by_tag_name("span"):

    i = (i + 1)
    if i == 87:

        browserCn.get("https://translate.google.cn/?sl=en&tl=zh-CN&text=" + span.text + "&op=translate")
        Eng = span.text
        workshell.write(0, 1, Eng)

for a in range(1, int(n)):
    txt = browserCn.find_element_by_class_name("er8xn")  # 改文本
    txt.clear()
    txt.send_keys(Eng)
    time.sleep(T)
    # En->Cn
    i = 0
    for span in browserCn.find_elements_by_tag_name("span"):
        i = (i + 1)
        if i == 88:
            print(span.text)
            Cn = span.text
        # print(i)

    # Cn->En
    txt = browserEn.find_element_by_class_name("er8xn")  # 改文本
    txt.clear()
    txt.send_keys(Cn)
    time.sleep(T)
    i = 0
    for span in browserEn.find_elements_by_tag_name("span"):#找英文
        i = (i + 1)
        if i == 87:
            print(span.text)
            Eng = span.text
    workshell.write(a, 0, Cn)
    workshell.write(a, 1, Eng)

browserCn.close()
browserEn.close()
workbook.save('D:\\翻译.xls')