from selenium import webdriver
import time
import unittest

from page.login.login_page import *
from page.main.main_page import *
from page.main.etransfer_page import *
from page.main.eauth_page import *
from page.main.eacquery import *


class InitDriver(unittest.TestCase):
    def startBrowser(self, name):
        '''
        打开浏览器函数，传入浏览器名称
        :param name:
        :return:
        '''
        try:
            if name == "firefox" or name == "Firefox" or name == "ff":
                print("start browser name: Firefox")
                # options = webdriver.FirefoxOptions()
                # options.add_argument('--no-sandbox')
                # options.add_argument('-headless')      #这里firefox跟chrome设置不同差一个横线
                # driver = webdriver.Firefox(options=options)
                # print("Test in firefox headless...")
                # fp = webdriver.FirefoxProfile(r'C:/Users/chenxy/AppData/Roaming/Mozilla/Firefox/Profiles/zxlxaetk.default')
                driver = webdriver.Firefox()
                # driver.maximize_window()
                return driver
            elif name == "chrome" or name == "Chrome":
                print("start browser name: Chrome")
                # options = webdriver.ChromeOptions()
                # options.add_argument('--no-sandbox')    #支持chrom在root环境下跑
                # options.add_argument('headless')  # 无头模式后台运行
                # driver = webdriver.Chrome(options=options)
                # print("Test in chrome headless...")
                driver = webdriver.Chrome()
                driver.maximize_window()
                return driver
            elif name == "ie" or name == "Ie":
                print("start browser name :Ie")
                driver = webdriver.Ie()
                driver.maximize_window()
                return driver
            elif name == "phantomjs" or name == "Phantomjs":
                print("start browser name :phantomjs")
                driver = webdriver.PhantomJS()
                driver.maximize_window()
                return driver
            elif name == "edge" or name == "Edge":
                print("start browser name :Edge")
                driver = webdriver.Edge()
                driver.maximize_window()
                return driver
            elif name == "opera" or name == "Opera":
                print("start browser name :Opera")
                driver = webdriver.Opera()
                driver.maximize_window()
                return driver
            else:
                print("Not found this browser,You can use 'firefox', 'chrome', 'ie', 'edge', 'opera' or 'phantomjs'")
        except Exception as msg:
            print("启动浏览器出现异常：%s" % str(msg))

    @classmethod
    def setUpClass(cls):

        cls.driver = cls.startBrowser(cls, name='ie')
        cls.driver.implicitly_wait(20)

        cls.loginpage = LoginPage(cls.driver)
        cls.mainpage = MainPage(cls.driver)

        cls.etransferwelpage = EtransferWelPage(cls.driver)
        cls.etransferpage = EtransferPage(cls.driver)
        cls.agentpayeesalpage = AgentPayeeSalaryPage(cls.driver)
        cls.agentqrypayeesalpage = AgentQryPayeeSalaryPage(cls.driver)
        cls.etrsagentsalarypage = ETrsAgentSalaryPage(cls.driver)
        cls.etrsagentsalaryqrypage = ETrsAgentSalaryQryPage(cls.driver)
        cls.batchbucklepage = BatchBucklePage(cls.driver)
        cls.batchbuckleqrypage = BatchBuckleQryPage(cls.driver)
        cls.pairaccountquerypage = PairAccountQueryPage(cls.driver)
        cls.bankcodeqrypage = BankCodeQryPage(cls.driver)
        cls.etransfernotrealtimepage = ETransferNotRealTimePage(cls.driver)
        cls.etrspurposemgmtpage = EtrspurposemgmtPage(cls.driver)
        cls.payeebookmanagemgrpage = PayeeBookManageMgrPage(cls.driver)

        cls.eauthpage = EauthPage(cls.driver)

        cls.eacquerypage = EacqueryPage(cls.driver)

        time.sleep(2)

        if not cls.driver:
            cls.skipTest('Web browser not available.')

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

        #去转账管理-收款人账户管理中，删除保存的最近转账人
        #去转账管理-转账用途维护中删除全部新增的用途信息，每次跑每次删
