# coding= utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# bs=webdriver.Chrome()
bs=webdriver.Firefox()
goal_url='http://www.uestcedu.com/ifree/console/'
bs.get(goal_url)
print 'before login=================================='
print bs.title

account=bs.find_element_by_id('txtLoginName')
password=bs.find_element_by_id('txtPassword')
login_btn=bs.find_element_by_id('login_button')

def sendkeys(ele,value):
    ele.clear()
    ele.send_keys(value)

sendkeys(account,'20160210447670')
sendkeys(password,'2192168')
login_btn.click()
# 在线课程
bs.find_element_by_css_selector("[menu_name='M00370003']").click()
time.sleep(2)
bs.switch_to.alert.accept()
try:
    WebDriverWait(bs,10,2).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,'learning_course_progress'))
    )

except Exception as e:
    print ('进入异常了',e)
finally:
    pass

bs.switch_to.frame('f_M00370003')
# 获取当前窗口
window_one=bs.current_window_handle
# 点击课程

bs.find_element_by_xpath('//*[@id="tr_tblDataList_18"]/td[8]/a[1]').click()
#隐式等待，最长等待5秒
bs.implicitly_wait(5)
# 获取新窗口
window_all=bs.window_handles
for x in window_all:
    if x != window_one:
        bs.switch_to.window(x)
        bs.switch_to.default_content()
        bs.switch_to.frame('w_main')
        print '进入新窗口了,切换frame，然后点击进入课程'
        # 进入课程首页
        bs.find_element_by_id('spanLearnContent_84053').click()
        time.sleep(5)

# 获取到所有需要点击挂课程的项目，并遍历执行方法
bs.switch_to.frame('w_code')
btnNext = bs.find_element_by_id('btnNext')
# bs.execute_script('window.search=function(){var itemAll=document.getElementsByClassName("h_scorm_content");for (var i=0;i<itemAll.length;i++){itemAll[i]=itemAll[i].parentNode.parentNode.firstChild}return itemAll;}')
# itemAll_js=bs.execute_script('search()')
# print itemAll_js
itemAll = bs.find_elements_by_class_name('h_scorm_content')
print len(itemAll)
try:
    for x in range(len(itemAll)):
        # y = len(itemAll)-x-2
        item = itemAll[x]
        state = bs.execute_script('return arguments[0].parentNode.parentNode.firstChild.getAttribute("class")=="scorm completed"', item)
        times = 0
        # 轮巡取状态
        while state == False:
            time.sleep(10)
            state = bs.execute_script('return arguments[0].parentNode.parentNode.firstChild.getAttribute("class")=="scorm completed"',item)
            if state == True:
                break
            times = times+1
            # 超时处理
            if times >= 33:
                btnNext.click()
                break

        if state == True:
            btnNext.click()

        print '第 %d 个课程完成状态为 %s' % (x+1, state)

except Exception as e:
    print ('挂课程异常',e)
finally:
    print'浏览器关闭'
    bs.quit()
