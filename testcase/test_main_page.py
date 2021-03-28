from testcase.public import LoginPageOp
import time as t


class MainPageTest(LoginPageOp):

    def test_transferService(self):
        '''
        要素检查
        :return:
        '''
        self.login()
        self.enterPage2(2)
        self.driver.switch_to.frame('mainTarget')            #第一个iframe
        self.assertEqual('转账服务首页', self.etransferwelpage.etransfer_item.text)
        # js1 = "document.getElementById('etrsferremittance').click()"
        # self.driver.execute_script(js1)
        # self.driver.execute_script("document.querySelectorAll(p#etrsferremittance).click()")
        t.sleep(3)
        self.driver.switch_to.frame('rightMainIframeTransfer_wel')
        self.assertEqual('待办交易', self.etransferwelpage.daibanjiaoyi.text)
        self.assertEqual('最近转账', self.etransferwelpage.zuijinzhuanzhang.text)
        self.assertEqual('快捷操作', self.etransferwelpage.kuaijiecaozuo.text)
        self.driver.switch_to.parent_frame()       #切到上一层
        # self.etransferwelpage.etrsferremittance.click()  # 点击转账
        js1 = "document.getElementById('etrsferremittance').click()"
        self.driver.execute_script(js1)
        t.sleep(5)
