import sys

import os
os.chdir('D:/dev/project/EWebTest')
sys.path.append('D:/dev/project/EWebTest')

from testcase.init_driver import InitDriver
from utils.helper import Helper
from utils.winControl import WinControl
from base.page_objects import PageObject

import time as t


class LoginPageOp(InitDriver, PageObject, Helper):
    '''
    公共组件：登录
    '''
    mrfkzh = Helper().getXmlData('jbckzh1')  #默认付款账号
    fkzh2 = Helper().getXmlData('ybckzh1')    #付款账号2
    zhmc = Helper().getXmlData('fkrmc2')  #账户名称
    bizhong = Helper().getXmlData('bz')   #币种
    khhmc = Helper().getXmlData('khhmc2')
    zhmc1 = Helper().getXmlData('fkrmc1')  #付款人账号名称，切换的
    skrzh = Helper().getXmlData('jbckzh2')  #收款人账号
    skrmc = Helper().getXmlData('skrmc2')  #收款人名称
    skrsjh = Helper().getXmlData('phoneNo')  #收款人手机号
    skrkhh = Helper().getXmlData('khh2')  #收款人开户行
    #跨行信息
    skrzh1 = Helper().getXmlData('jbckzh4')  # 收款人账号
    skrmc1 = Helper().getXmlData('skrmc4')  # 收款人名称
    skrsjh1 = Helper().getXmlData('phoneNo4')  # 收款人手机号
    skrkhh1 = Helper().getXmlData('khh4')  # 收款人开户行

    key = Helper().getXmlData('key')
    lhh = Helper().getXmlData('lhh')

    fukuanjine = Helper().getXmlData('fkje2')   #本行付款金额
    dbxe = Helper().getXmlData('dbxe')  #单笔限额
    jedx = Helper().getXmlData('jedx')  #金额大写
    fee1 = Helper().getXmlData('fee1')  #手续费0
    yingshoufee1 = Helper().getXmlData('yingshoufee1')  # 本行应收手续费
    youhuifee1 = Helper().getXmlData('youhuifee1')  # 优惠本行手续费

    khzzjine = Helper().getXmlData('khzzjine')  #跨行转账金额
    khzzjine1 = Helper().getXmlData('khzzjine1')
    jedx1 = Helper().getXmlData('jedx1')  #跨行付款金额大写
    fee2 = Helper().getXmlData('fee2')  #跨行手续费
    yingshoufee = Helper().getXmlData('yingshoufee')  #跨行应收手续费
    youhuifee = Helper().getXmlData('youhuifee')   #优惠手续费

    wenxintishi =  Helper().getXmlData('wxtishi')   #温馨提示
    date = Helper().getXmlData('date')  #传进去预约日期
    manualyongtu = Helper().getXmlData('yongtu')

    #设置一个变量
    arg_yongtu = 'yongtu'
    arg_liushuihao = 'liushuihao'


    def login(self):
        self.driver.get(Helper().getXmlData('url'))
        t.sleep(2)
        self.loginpage.CifNo.send_keys(Helper().getXmlData('CifNo'))
        self.loginpage.UserId.send_keys(Helper().getXmlData('UserId'))
        self.loginpage.input_VerifyCode.send_keys(Helper().getXmlData('verifyCode'))
        js = "document.getElementById('loginbtn').click();"
        self.driver.execute_script(js)
        t.sleep(3)

    def logout(self):
        self.mainpage.logout_btn.click()

    def public_transfer(self, menu: int, item, frame):
        '''
        切换到内容页面通用方法
        :return:
        '''
        self.login()
        self.enterPage2(menu)
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.etransferwelpage.lable_qr.send_keys(item)
        searchbtn = self.driver.find_element_by_xpath("//label[text()='请输入功能名称']/../div/ul/li[text()='"+item+"']")
        searchbtn.click()
        t.sleep(2)
        self.driver.switch_to.frame(frame)             #传入二级页面的frame

    def ocr(self, img_path):
        image = Image.open(img_path)
        print(pytesseract.image_to_string(image))

        file_name = 'a.jpeg'
        res = requests.get(img_path)
        with open(file_name, 'wb') as f:
            f.write(res.content)

    def pass_control(self, title):
        if autoit.win_exists(title) == 1:
            autoit.control_focus("[Class:IEFrame]", "Edit3")
            t.sleep(2)
            autoit.mouse_click()
            pyautogui.press('1')
            pyautogui.press('1')
            pyautogui.press('1')
            pyautogui.press('1')
            # autoit.control_send("[Class:IEFrame]", "Edit3", "q123456")
            print(222)

    def enterPage2(self, seq: int):
        js = "document.getElementsByTagName('a')[" + str(seq) + "].click()"
        self.driver.execute_script(js)
        t.sleep(3)

    def enterPage(self):
        for i in range(1, 13):                  #循环把所有的页头标签点击一遍,一共12个标签
            print(i)
            js = "document.getElementsByTagName('a')["+str(i)+"].click()"
            self.driver.execute_script(js)
            t.sleep(3)
        self.driver.execute_script("document.getElementsByTagName('a')[0].click()")        #点首页

    def isElementExist(self, ele):
        flag = True
        if len(ele) == 0:
            flag = False
            return flag
        if len(ele) == 1:
            return flag
        else:
            flag = False
            return flag

    def isElementExists(self, ele):
        flag = True
        try:
            ele
        except:
            flag = False
        return flag

    def chooseGroup(self):             #在转账的frame2下面时调用
        account = Helper().getXmlData('jbckzh2')
        skrmc = Helper().getXmlData('skrmc2')
        khh = Helper().getXmlData('khh2')
        for i in range(2, 6):
            print(i)
            ele = self.driver.find_element_by_xpath("//div[@id='GroupId']/a["+str(i)+"]")
            ele.click()
            self.etransferpage.chax.click()
            t.sleep(1)
            try:
                self.etransferpage.xuanze.click()
                self.assertEqual(account, self.etransferpage.shoukuanzhangh.text)
                self.assertEqual(skrmc, self.etransferpage.shoukuanrenmc.text)
                self.assertEqual(khh, self.etransferpage.kaihuh.text)
                break           #找到可以选择的就退出循环
            except:
                print('该分组内无收款人信息！')

    def test(self):
        date = self.driver.execute_script("var d = new Date(); d.getTime();")
        print(date)



class WinOp:
    '''
    操作一些web以外的窗口
    '''
    # w1 = WinControl('Windows 安全中心')
    # w2 = WinControl('验证密码')
    # m = MouseControl()
    # hwnd_title = dict()

    def cer_confirm(self, title):
        w = WinControl(title)
        if w.exists() == 1:
            print(222)              #前端显示
            w.controlFocus('Edit3')
            w.controlSend('Edit3', 'q123456', mode=0)
            # w.controlSetText(control='Edit', control_text='q123456')
            print(1234)
            # if title == 'Windows 安全中心':
            #     self.m.click(title, text='', x=100, y=170, button="main", clicks=1)  #根据窗口的pos做x/y的移动并点击

    # def get_all_hwnd(self, hwnd, mouse):                         #遍历窗口句柄
    #     if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
    #         self.hwnd_title.update({hwnd: GetWindowText(hwnd)})
    #
    # def abc(self):
    #     # win = FindWindow(None, u'验证密码')             #找不到这个窗口，可能是被限制了安全
    #     EnumWindows(self.get_all_hwnd, 0)
    #     for h, t in self.hwnd_title.items():
    #        if t is not "":
    #           print(h, t)              #打印窗口句柄和窗口名字
    #
    # def get_child_windows(self, parent):
    #     if not parent:
    #         return
    #     hwndChildList = []
    #     EnumChildWindows(parent, lambda hwnd, param:param.append(hwnd), hwndChildList)
    #     for hwnd in hwndChildList:
    #         # if GetClassName(hwnd) == 'Edit':
    #         #     print(hwnd)
    #         if GetDlgCtrlID(hwnd) == 102:
    #             print(hwnd)
    #     print(hwndChildList)
    #     return hwndChildList



if __name__ == '__main__':
    win = WinOp()
    # win.get_child_windows(parent=FindWindow(u'IEFrame', None))
    win.cer_confirm('苏州农村商业银行企业网上银行(证书版) - Internet Explorer')







