import datetime
import unittest

from testcase.public import LoginPageOp
import time as t


class EtransferPageTest(LoginPageOp):

    # 二级菜单-转账服务首页
    def public_transfer_veriry_logout(self, deal, **kwargs):
        '''
        公共验证点1：进入转账-转账汇款
        :return:
        '''
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        if kwargs:
            items = kwargs['item']
            if deal == 'dbjy':  # 待办交易
                self.public_transfer_verify_dbjy(item=items)  # 待处理交易or已处理交易
        else:
            if deal == 'zjzz':
                self.public_transfer_veriry_zjzz
            elif deal == 'zzhk':  # 转账汇款
                self.public_transfer_veriry_zzhk
            elif deal == 'dfgz':  # 代发工资
                self.public_transfer_verify_dfgz
            elif deal == 'ghdf':  # 工会代发
                self.public_transfer_veriry_ghdf
            elif deal == 'pldk':  # 批量代扣
                self.public_transfer_veriry_pldk
            elif deal == 'jymxcx':  # 交易明细查询
                # self.driver.switch_to.default_content
                # self.assertTrue(self.isElementExists(self.eacquerypage.zhanghuguanli_bigtab))
                # self.driver.switch_to.frame(self.etransferwelpage.mainframe)
                self.public_transfer_veriry_jymxcx
            elif deal == 'dfgzcx':  # 代发工资查询
                self.public_transfer_veriry_dfgzcx
            elif deal == 'ghdfcx':  # 工会代发查询
                self.public_transfer_veriry_ghdfcx
            elif deal == 'pldkcx':  # 批量代扣查询
                self.public_transfer_veriry_pldkcx
            elif deal == 'pdzhcx':  # 配对账户查询
                self.public_transfer_veriry_pdzhcx
            elif deal == 'hhcx':  # 行号查询
                self.public_transfer_veriry_hhcx
            elif deal == 'yyzzcx':  # 预约转账撤销
                self.public_transfer_veriry_yyzzcx
            elif deal == 'zzytwh':  # 转账用途维护
                self.public_transfer_veriry_zzytwh
            elif deal == 'skrzhgl':  # 收款人账户管理
                self.public_transfer_veriry_skrzhgl

        self.driver.switch_to.default_content()
        self.logout()
        t.sleep(2)

    def public_transfer_verify_dbjy(self, item):
        '''
        功能验证点：进入到交易授权页面
        :param item:
        :return:
        '''
        self.driver.switch_to.frame(self.eauthpage.frame2)
        if item == 'waitDeal':
            self.assertEqual('交易授权', self.eauthpage.jiaoyishouquan.text)  # 校验跳转到“交易授权”页面
            self.assertIn('起止日期', self.driver.page_source)  # 校验跳转到“未授权”tab
            self.assertNotIn('审核起止日期：', self.driver.page_source)  # 而不是跳转到“已授权”tab
        elif item == 'hasDeal':
            self.assertEqual('交易授权', self.eauthpage.jiaoyishouquan.text)  # 校验跳转到“交易授权”页面
            self.assertIn('交易状态：', self.driver.page_source)  # 校验不是跳转到“未授权”tab
            self.assertIn('审核起止日期：', self.driver.page_source)  # 而是跳转到“已授权”tab

    @property
    def public_transfer_verify_dfgz(self):
        '''
        公共验证点1：进入代发服务-代发工资
        :return:
        '''
        self.assertTrue(self.isElementExists(self.agentpayeesalpage.daifagongzi_sidebar))
        self.assertTrue(self.isElementExists(self.agentpayeesalpage.daifagongzi_tab))
        self.driver.switch_to.frame(self.agentpayeesalpage.frame2)
        self.assertTrue(self.isElementExists(self.agentpayeesalpage.daifagongzi))

    @property
    def public_transfer_veriry_zzhk(self):
        '''
        公共验证点1：进入转账-转账汇款
        :return:
        '''
        self.assertTrue(self.isElementExists(self.etransferpage.etrsferremittance))  # 侧边栏
        self.assertTrue(self.isElementExists(self.etransferpage.singleTransfer_tab))  # 红色标签
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.assertTrue(self.isElementExists(self.etransferpage.danbizhuanzhang_tab))  # 标签2
        self.assertTrue(self.isElementExists(self.etransferpage.fukuanren))
        self.assertTrue(self.isElementExists(self.etransferpage.shoukuanren))
        self.assertTrue(self.isElementExists(self.etransferpage.jiaoyixinxi))

    @property
    def public_transfer_veriry_ghdf(self):
        '''
        公共验证点1：进入代发服务-工会代发
        :return:
        '''
        self.assertTrue(self.isElementExists(self.etrsagentsalarypage.gonghuidaif_sidebar))
        self.assertTrue(self.isElementExists(self.etrsagentsalarypage.gonghuidaif_tab))
        self.driver.switch_to.frame(self.etrsagentsalarypage.frame2)
        self.assertTrue(self.isElementExists(self.etrsagentsalarypage.gonghuidaifa))

    @property
    def public_transfer_veriry_pldk(self):
        '''
        公共验证点1：进入批量代扣-批量代扣
        :return:
        '''
        self.assertTrue(self.isElementExists(self.batchbucklepage.piliangdaik_sidebar))
        self.assertTrue(self.isElementExists(self.batchbucklepage.piliangdaik_tab))
        self.driver.switch_to.frame(self.batchbucklepage.frame2)
        self.assertTrue(self.isElementExists(self.batchbucklepage.shougongluru))
        self.assertTrue(self.isElementExists(self.batchbucklepage.wenjianshangc))
        self.assertTrue(self.isElementExists(self.batchbucklepage.daikouxinxi))

    @property
    def public_transfer_veriry_jymxcx(self):
        '''
        公共验证点1：进入账户管理-账户查询-交易明细查询
        :return:
        '''
        self.assertTrue(self.isElementExists(self.eacquerypage.jiaoyimingxichax_sidebar))
        self.assertTrue(self.isElementExists(self.eacquerypage.duozhanghmingxchax_sidebar))
        self.assertTrue(self.isElementExists(self.eacquerypage.tongyishitchax_sidebar))
        self.assertTrue(self.isElementExists(self.eacquerypage.zhuanzmingxichax_sidebar))
        self.assertTrue(self.isElementExists(self.eacquerypage.jiaoyimingxcx_tab))
        self.driver.switch_to.frame(self.eacquerypage.frame2)
        self.assertTrue(self.isElementExists(self.eacquerypage.jiaoyimingxchax_title))

    @property
    def public_transfer_veriry_dfgzcx(self):
        '''
        公共验证点1：进入转账服务-代发服务-代发工资查询
        :return:
        '''
        self.assertTrue(self.isElementExists(self.agentqrypayeesalpage.daifagongzichax_sidebar))
        self.assertTrue(self.isElementExists(self.agentqrypayeesalpage.daifagongzichx_tab))
        self.driver.switch_to.frame(self.agentqrypayeesalpage.frame2)
        self.assertTrue(self.isElementExists(self.agentqrypayeesalpage.daifagongzichax))

    @property
    def public_transfer_veriry_ghdfcx(self):
        '''
        公共验证点1：进入转账服务-代发服务-工会代发查询
        :return:
        '''
        self.assertTrue(self.isElementExists(self.etrsagentsalaryqrypage.gonghuidaifchax_sidebar))
        self.assertTrue(self.isElementExists(self.etrsagentsalaryqrypage.gonghuidaifchax_tab))
        self.driver.switch_to.frame(self.etrsagentsalaryqrypage.frame2)
        self.assertTrue(self.isElementExists(self.etrsagentsalaryqrypage.gonghuidaifchax))

    @property
    def public_transfer_veriry_pldkcx(self):
        '''
        公共验证点1：进入转账服务-批量代扣-批量代扣结果查询
        :return:
        '''
        self.assertTrue(self.isElementExists(self.batchbuckleqrypage.piliangdaikjgchax_sidebar))
        self.assertTrue(self.isElementExists(self.batchbuckleqrypage.piliangdaikjgchax_tab))
        self.driver.switch_to.frame(self.batchbuckleqrypage.frame2)
        self.assertTrue(self.isElementExists(self.batchbuckleqrypage.piliangdaikchax))

    @property
    def public_transfer_veriry_pdzhcx(self):
        '''
        公共验证点1：进入转账服务-我要查询-配对账户查询
        :return:
        '''
        self.assertTrue(self.isElementExists(self.pairaccountquerypage.peiduizhanghchax_sidebar))
        self.assertTrue(self.isElementExists(self.pairaccountquerypage.peiduizhanghchax_tab))
        self.driver.switch_to.frame(self.pairaccountquerypage.frame2)
        self.assertTrue(self.isElementExists(self.pairaccountquerypage.peiduizhanghchax))

    @property
    def public_transfer_veriry_hhcx(self):
        '''
        公共验证点1：进入转账服务-转账管理-行号查询
        :return:
        '''
        self.assertTrue(self.isElementExists(self.bankcodeqrypage.hanghaochax_sidebar))
        self.assertTrue(self.isElementExists(self.bankcodeqrypage.hanghaochax_tab))
        self.driver.switch_to.frame(self.bankcodeqrypage.frame2)
        self.assertTrue(self.isElementExists(self.bankcodeqrypage.hanghaochax))

    @property
    def public_transfer_veriry_yyzzcx(self):
        '''
        公共验证点1：预约转账撤销
        :return:
        '''
        self.assertTrue(self.isElementExists(self.etransfernotrealtimepage.yuyuezzchex_sidebar))
        self.assertTrue(self.isElementExists(self.etransfernotrealtimepage.yuyuezzchex_tab))
        self.driver.switch_to.frame(self.etransfernotrealtimepage.frame2)
        self.assertTrue(self.isElementExists(self.etransfernotrealtimepage.yuyuezzchex))

    @property
    def public_transfer_veriry_zzytwh(self):
        '''
        公共验证点1：转账用途维护
        :return:
        '''
        self.assertTrue(self.isElementExists(self.etrspurposemgmtpage.zhuanzytweih_sidebar))
        self.assertTrue(self.isElementExists(self.etrspurposemgmtpage.zhuanzytweih_tab))
        self.driver.switch_to.frame(self.etrspurposemgmtpage.frame2)
        self.assertTrue(self.isElementExists(self.etrspurposemgmtpage.zhuanzytweih))

    @property
    def public_transfer_veriry_skrzhgl(self):
        '''
        公共验证点1：收款人账户管理
        :return:
        '''
        self.assertTrue(self.isElementExists(self.payeebookmanagemgrpage.shoukrzhguanl_sidebar))
        self.assertTrue(self.isElementExists(self.payeebookmanagemgrpage.shoukrzhguanl_tab))
        self.driver.switch_to.frame(self.payeebookmanagemgrpage.frame2)
        self.assertTrue(self.isElementExists(self.payeebookmanagemgrpage.shoukuanrzhguanli_tab2))
        self.assertTrue(self.isElementExists(self.payeebookmanagemgrpage.fenzuguanli_tab))
        self.assertTrue(self.isElementExists(self.payeebookmanagemgrpage.chaxunjieguo))

    def test_transfer_wel_000(self):
        '''
        校验所有不能点击的要素
        :return:
        '''
        pass

    def test_transfer_wel_001(self):
        '''
        点击'待处理交易'，进入交易授权-未授权页面;
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.assertEqual('待处理交易', self.etransferwelpage.daichulijiaoyi.text)
        self.etransferwelpage.daichulijiaoyi.click()
        t.sleep(2)
        self.driver.switch_to.default_content()  # 切出frame
        # self.public_transfer_verify_dbjy(item='waitDeal')
        self.public_transfer_veriry_logout('dbjy', item='waitDeal')  # 校验点

    def test_transfer_wel_002(self):
        '''
        点击‘笔数’，进入交易授权-未授权页面
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.bishu.click()
        t.sleep(2)
        self.driver.switch_to.default_content()  # 切出frame
        self.public_transfer_veriry_logout('dbjy', item='waitDeal')  # 校验点

    def test_transfer_wel_003(self):
        '''
        点击‘已处理交易’，进入交易授权-已授权页面；
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        # self.driver.execute_script("document.getElementsByTagName('img')[2].click()")
        self.etransferwelpage.yichulijiaoyi.click()
        t.sleep(5)
        self.driver.switch_to.default_content()  # 切出frame
        self.public_transfer_veriry_logout('dbjy', item='hastDeal')  # 校验点

    def test_transfer_wel_004(self):
        '''
        点击‘笔数’，进入交易授权-已授权页面
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.bishu2.click()
        t.sleep(2)
        self.driver.switch_to.default_content()  # 切出frame
        self.public_transfer_veriry_logout('dbjy', item='hastDeal')  # 校验点


    def test_transfer_wel_006(self):
        '''
        快捷操作-我要转账-点击转账汇款
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.zhuanzhanghuik.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('zzhk')  # 校验点

    def test_transfer_wel_007(self):
        '''
        快捷操作-我要代发-点击代发工资
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.daifagongzi.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('dfgz')

    def test_transfer_wel_008(self):
        '''
        快捷操作-我要代发-工会代发
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)  # 组件
        self.etransferwelpage.gonghuidaifa.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('ghdf')

    def test_transfer_wel_009(self):
        '''
        快捷操作-我要代发-批量代扣
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.piliangdaikou.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('pldk')

    def test_transfer_wel_010(self):
        '''
        快捷操作-我要查询-交易明细查询
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.jiaoyimingxichax.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('jymxcx')

    def test_transfer_wel_011(self):
        '''
        快捷操作-我要查询-代发工资查询
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.daifagongzichax.click()
        t.sleep(3)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('dfgzcx')

    def test_transfer_wel_012(self):
        '''
        快捷操作-我要查询-工会代发查询
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.gonghuidaifachax.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('ghdfcx')

    def test_transfer_wel_013(self):
        '''
        快捷操作-我要查询-批量代扣查询
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.piliangdaikouchax.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('pldkcx')

    def test_transfer_wel_014(self):
        '''
        快捷操作-我要查询-配对账户查询
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.peiduizhanghuchax.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('pdzhcx')

    def test_transfer_wel_015(self):
        '''
        快捷操作-我要查询-行号查询
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.hanghaochax.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('hhcx')

    def test_transfer_wel_016(self):
        '''
        预约转账撤销
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.yuyuezzchexiao.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('yyzzcx')

    def test_transfer_wel_017(self):
        '''
        转账用途维护
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.zzyongtuweihu.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('zzytwh')

    def test_transfer_wel_018(self):
        '''
        收款人账户管理
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        self.etransferwelpage.shoukuanrenzhguanli.click()
        t.sleep(2)
        self.driver.switch_to.default_content()
        self.public_transfer_veriry_logout('skrzhgl')

    def test_transfer_wel_019(self):
        '''
        点开左侧菜单，进入三级菜单
        :return:
        '''
        self.login()
        self.enterPage2(2)  # 进入转账服务菜单
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)

        self.etransferwelpage.etransfer.click()
        self.etransferpage.etrsferremittance1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.etransferpage.singleTransfer_tab))

        self.etransferwelpage.einterbmanage.click()
        self.etransfernotrealtimepage.yuyuezzchex_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.etransfernotrealtimepage.yuyuezzchex_tab))
        self.etrspurposemgmtpage.zhuanzytweih_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.etrspurposemgmtpage.zhuanzytweih_tab))
        self.payeebookmanagemgrpage.shoukrzhguanl_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.payeebookmanagemgrpage.shoukrzhguanl_tab))
        self.bankcodeqrypage.hanghaochax_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.bankcodeqrypage.hanghaochax_tab))
        self.pairaccountquerypage.peiduizhanghchax_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.pairaccountquerypage.peiduizhanghchax_tab))

        self.etransferwelpage.eagentpayeesalary.click()
        self.agentpayeesalpage.daifagongzi_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.agentpayeesalpage.daifagongzi_tab))
        self.etrsagentsalarypage.gonghuidaif_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.etrsagentsalarypage.gonghuidaif_tab))
        self.agentqrypayeesalpage.daifagongzichax_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.agentqrypayeesalpage.daifagongzichx_tab))
        self.etrsagentsalaryqrypage.gonghuidaifchax_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.etrsagentsalaryqrypage.gonghuidaifchax_tab))

        self.etransferwelpage.ebatchbucklemgmt.click()
        self.batchbucklepage.piliangdaik_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.batchbucklepage.piliangdaik_tab))
        self.batchbuckleqrypage.piliangdaikjgchax_sidebar1.click()
        t.sleep(2)
        self.assertTrue(self.isElementExists(self.batchbuckleqrypage.piliangdaikjgchax_tab))

        self.driver.switch_to.default_content()
        self.logout()

    # 二级菜单-转账
    def test_etrsferremittance_001(self):
        '''
        本行转账，不保存最近转账人；
        付款用途：选择录入默认用途
        :return:
        '''
        # 数据准备：去转账管理中删除本客户保存的转账记录；
        self.public_transfer(2, u'单笔转账', self.etransferpage.frame2)
        t.sleep(3)
        self.public_fukuanren_case(flag='case1')  # 默认付款账号
        self.public_shoukuanren_case(flag='case0', bank='self')
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.public_jiaoyixinxi_and_confirm(flag='case0', paymethod='choose1', bank='self')

    def test_transfer_wel_005(self):  # 转账完一笔后，查询最近转账记录
        '''
        最近转账：可能有数据，可能无数据
        :return:
        '''
        self.public_transfer(2, u'转账服务首页', self.etransferwelpage.frame2)
        t.sleep(1)
        try:
            print('有数据')
            self.isElementExists(self.etransferwelpage.shoukuanzhangh)
            self.isElementExists(self.etransferwelpage.zhanghumingc)
            self.isElementExists(self.etransferwelpage.jiaoyijine)
            self.isElementExists(self.etransferwelpage.caozuo)
            self.etransferwelpage.yijianzhuanz.click()  # 点击一键转账
            t.sleep(5)
            self.driver.switch_to.parent_frame()
            self.isElementExists(self.etransferpage.singleTransfer_tab)
            self.isElementExists(self.etransferpage.etrsferremittance)
            self.driver.switch_to.frame(self.etransferpage.frame2)
            self.public_shoukuanren_verify             #收款人回显
            self.assertEqual('请输入付款金额', self.etransferpage.fukuanjine.get_attribute('placeholder'))   #付款金额无
        except:
            print('暂无数据')
            self.assertIn('暂无相关转账记录', self.driver.page_source)
        self.driver.switch_to.default_content()
        self.logout()

    def test_etrsferremittance_002(self):
        '''
        本行转账，保存最近转账人；
        付款用途：新建用途
        :return:
        '''
        self.public_transfer(2, u'单笔转账', self.etransferpage.frame2)
        t.sleep(3)
        self.public_fukuanren_case(flag='case1')  # 默认账号
        self.public_shoukuanren_case(flag='case1', bank='self')
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.public_jiaoyixinxi_and_confirm(flag='case0', paymethod='choose2', bank='self')

    def test_etrsferremittance_003(self):
        '''
        本行转账，快捷选择收款人
        预约：周期预约，单次
        :return:
        '''
        self.public_transfer(2, u'单笔转账', self.etransferpage.frame2)
        t.sleep(3)
        self.public_fukuanren_case(flag='case2')  # 切换账号
        self.public_shoukuanren_case(flag='case1', bank='other')  # 本行转账
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.public_jiaoyixinxi_and_confirm(flag='case1', freq='once', bank='other')

    def test_etrsferremittance_004(self):
        '''
        本行转账，快捷选择收款人,选择最近转账人
        周期预约：按日
        :return:
        '''
        self.public_transfer(2, u'单笔转账', self.etransferpage.frame2)
        t.sleep(3)
        self.public_fukuanren_case(flag='case2')  # 切换账号
        self.public_shoukuanren_case(flag='case3', bank='self')  # 最近转账
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.public_jiaoyixinxi_and_confirm(flag='case1', freq='period', every='daily', bank='self')

    def test_etrsferremittance_005(self):
        '''
        跨行转账
        周期预约，按周
        :return:
        '''
        self.public_transfer(2, u'单笔转账', self.etransferpage.frame2)
        t.sleep(3)
        self.public_fukuanren_case(flag='case2')  # 切换账号
        self.public_shoukuanren_case(flag='case1', bank='other')  # 跨行转账
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.public_jiaoyixinxi_and_confirm(flag='case1', freq='period', every='weekly', bank='other')

    def test_etrsferremittance_006(self):
        '''
        快捷选择收款人；
        周期预约，按月
        :return:
        '''
        self.public_transfer(2, u'单笔转账', self.etransferpage.frame2)
        t.sleep(3)
        self.public_fukuanren_case(flag='case2')  # 切换账号
        self.public_shoukuanren_case(flag='case1', bank='other')  # 跨行转账
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.public_jiaoyixinxi_and_confirm(flag='case1', freq='period', every='monthly', bank='other')


    @property
    def public_transfer_monthly(self):
        self.public_shoukuanren_case(flag='case3', bank='self')  # 最近转账
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.frame2)
        self.public_jiaoyixinxi_and_confirm(flag='case1', freq='period', every='monthly')

    def public_fukuanren_case(self, flag):
        '''
        填写付款人信息，切换默认账号
        :return:
        '''
        self.isElementExists(self.etransferpage.xinxiluru)
        self.assertEqual(self.mrfkzh, self.etransferpage.fukuanzhanghao.text)  # 校验默认付款账号
        balance1 = self.etransferpage.keyongyue.text
        self.assertEqual(self.zhmc, self.etransferpage.zhanghumingc.text)  # 比对账户名称
        self.assertEqual(self.bizhong, self.etransferpage.bizhong.text)
        if flag == 'case1':                    #搭配实时转账
            print(u'使用默认付款账号转账！')
            self.etransferpage.zhguishudchax.click()  # 归属地查询，弹窗
            self.assertEqual(self.mrfkzh, self.etransferpage.tanchuangzhangh.text)
            self.assertEqual(self.khhmc, self.etransferpage.tanchuangkaihuhmc.text)
            self.etransferpage.quxiaobtn.click()
        elif flag == 'case2':            #搭配预约转账
            self.etransferpage.fukuanzhanghao.click()
            self.etransferpage.switchzhangh.click()  # 切换账号
            balance2 = self.etransferpage.keyongyue.text
            self.assertNotEqual(balance1, balance2)  # 校验余额有变动
            self.assertEqual(self.zhmc1, self.etransferpage.zhanghumingc.text)  # 切换后比对账户名称

    def public_shoukuanren_case(self, flag, bank):
        '''
        填写收款人信息
        :return:
        '''
        if flag == 'case0':  # 不保存为常用收款人
            self.public_input_shoukuanren(bank)
            self.etransferpage.label.click()  # 取消保存
        elif flag == 'case1':
            self.public_input_shoukuanren(bank)
            self.etransferpage.shoukrshoujih.send_keys(self.skrsjh)  # 输入手机号
        elif flag == 'case2' and bank == 'self':  # 选择收款人
            self.etransferpage.xuanzeshoukrbtn.click()
            t.sleep(2)
            self.etransferpage.xuanze.click()
            self.public_shoukuanren_verify
        elif flag == 'case3' and bank == 'self':  # 点击最近转账
            self.etransferpage.recentTrans.click()
            self.public_shoukuanren_verify

    def public_jiaoyixinxi_and_confirm(self, flag, bank, **kwargs):
        '''
        填写交易信息
        :return:
        '''
        self.public_input_payee(bank)
        self.etransferpage.move_to_element(self.etransferpage.tixing2)
        self.etransferpage.move_to_element(self.etransferpage.tixing1)
        if flag == 'case0':  # 全部默认，实时转账
            paymethod = kwargs['paymethod']
            if paymethod == 'choose1':
                self.etransferpage.shouxufbz.click()
                t.sleep(1)
                # 手续费窗口的取消按钮，webdriver点击不到
                self.driver.execute_script(
                    "document.querySelector('#statisticsCodeBox > div.singleBtnBox.clearfix > p').click()")
            elif paymethod == 'choose2':   #新建新的用途并使用
                self.etransferpage.yongtuweihubtn.click()  # 跳转到另一个页面
                t.sleep(3)
                #此处新建一个用途维护
                # self.driver.switch_to.default_content()
                # self.driver.switch_to.frame(self.etransferwelpage.mainframe)
                # self.driver.execute_script("document.querySelector('#SingleTransfer').click()")   #点击单笔转账标签切回来
                # t.sleep(2)
                # self.driver.switch_to.frame(self.etransferpage.frame2)  # 切回来
                # t.sleep(15)
                self.driver.switch_to_default_content()
                self.driver.switch_to.frame(self.etransferwelpage.mainframe)
                self.etransferpage.singleTransfer_tab_notactive.click()
                t.sleep(3)
                self.driver.switch_to.frame(self.etransferpage.frame2)
                self.etransferpage.bigresetbtn.click()    #重置一下
                t.sleep(2)
                self.public_shoukuanren_case(flag='case1', bank='self')
                self.public_input_payee(bank='self')
                self.etransferpage.fukuanyongt.click()  #查找更新的用途
                t.sleep(3)
                self.etransferpage.yongtu2.click()  # 修改用途，最后一个标签
                t.sleep(2)

            self.isElementExists(self.etransferpage.zhuanzhangsm)
            self.public_click_confirm(nflag=1, bank='self')  # 在提交页面点击确认
            self.assertEqual(self.etransferpage.czhuanzhangfangshi.text, '实时到账')
            self.assertEqual(self.etransferpage.cfukzhangh.text, self.mrfkzh)   #付款账号校验，确认结果页面的其他校验，在最后面
            self.assertEqual(self.etransferpage.cyongtu.text, self.arg_yongtu)
            self.public_transfer_confirm_and_click(bank)  # 确认页面的公共的元素的值，校验完后点击下一步

            self.public_transfer_submit_verify(bank)     #arg_yongtu#在提交结果页面检查
            self.isElementExists(self.etransferpage.tjjiaoyiyishoul)  # 实时转账结果
            self.assertEqual(self.etransferpage.tjfukzhangh, self.mrfkzh)
            self.assertEqual(self.etransferpage.tjfkfangshi.text, '实时到账')
            self.assertEqual(self.etransferpage.tjyongtu.text, self.arg_yongtu)    #全局变量与该页面的用途比对

            self.etransferpage.tjjixuzhuanz.click()
            #返回转账页面

        elif flag == 'case1':  # 预约
            freq = kwargs['freq']
            date = self.date

            self.etransferpage.shoudongluru.click()          #修改用途
            t.sleep(1)
            self.etransferpage.fukuanyongtinput.send_keys(self.manualyongtu)
            self.etransferpage.yuyuezhuanz.click()  # 预约转账
            t.sleep(2)
            self.isElementExists(self.etransferpage.zhuanzhangsm1)
            if freq == 'once':  # 单次预约
                self.public_yuqijieshuriqi(date, yuyue='once')  # 设置预约必须是当天往后一天，这里传了一个固定值
                t.sleep(1)
                self.public_click_confirm(nflag=1, bank=bank)  # 检查一些fee
                self.assertEqual(self.etransferpage.czhuanzhangfangshi.text, '预约转账')
                self.assertEqual(self.etransferpage.cyuyuefangs.text, '单次预约')
                self.assertEqual(self.etransferpage.cyuyuezhuanzriqi.text, date)
            elif freq == 'period':  # 周期预约
                every = kwargs['every']
                self.etransferpage.zhouqiyuyue.click()
                t.sleep(2)
                if every == 'daily':
                    #这里传了一个date固定值
                    self.public_yuqijieshuriqi(date, yuyue='period')  # 设置预约是当天往后2天,周期预约比单次预约更多1天
                    t.sleep(2)
                    self.etransferpage.gouxuank.click()   #开启预约提醒
                    t.sleep(2)
                    self.etransferpage.tongzhisjh.send_keys(self.skrsjh1)  # 随便写一个手机号
                    self.public_click_confirm(nflag=1, bank=bank)  # 检查一些fee
                    self.assertEqual(self.etransferpage.czhouqiyypinl.text.replace(' ', ''), '每日')
                    self.assertEqual(self.etransferpage.cfaqiri.text, '每日')
                    self.assertEqual(self.etransferpage.cyuyuetixing, '开通')
                else:
                    self.etransferpage.zhouqiyuypinl.click()
                    t.sleep(1)
                    if every == 'weekly':
                        self.etransferpage.meizhou.click()  # 先改成每周
                        t.sleep(2)
                        self.etransferpage.yuyueriqi1.click()
                        t.sleep(1)
                        self.etransferpage.yuyueriqi2.click()  # 改成周一
                        t.sleep(1)
                        # 这里传了一个固定值
                        self.public_yuqijieshuriqi(date, yuyue='period')  # 设置预约是当天往后7天，如此提交时不会提示错误
                        t.sleep(1)
                        self.public_click_confirm(nflag=1, bank=bank)  # 检查一些fee
                        self.assertEqual(self.etransferpage.czhouqiyypinl.text.replace(' ', ''), '每周')
                        self.assertEqual(self.etransferpage.cfaqiri.text, '周一')
                    elif every == 'monthly':
                        self.etransferpage.meiyue.click()  # 先改成每月
                        t.sleep(1)
                        self.etransferpage.yuyueriqi3.click()
                        t.sleep(1)
                        self.etransferpage.yuyueriqi4.click()  # 改成2号
                        t.sleep(1)
                        # 这里传了一个固定值
                        self.public_yuqijieshuriqi(date, yuyue='period')  # 设置预约是当天往后7天，如此提交时不会提示错误
                        t.sleep(1)
                        self.public_click_confirm(nflag=1, bank=bank)  # 检查一些fee
                        self.assertEqual(self.etransferpage.czhouqiyypinl.text.replace(' ', ''), '每月')
                        self.assertEqual(self.etransferpage.cfaqiri.text, '2号')
                        self.etransferpage.cbackbtn.click()    #点击返回按钮
                        t.sleep(3)
                        self.etransferpage.yuyueriqi55.click()
                        self.etransferpage.yuyueriqi5.click()  # 改成月底
                        self.etransferpage.confirmbtn.click()
                        t.sleep(5)
                        self.assertEqual(self.etransferpage.cfaqiri.text, '月底')

                    self.assertEqual(self.etransferpage.cyuyuetixing.text, '关闭')  #前面两种情况都关闭
                #以下属于周期预约的验证点,写到这里
                self.assertEqual(self.etransferpage.czhouqiyyjieshuriqi.text, date)
                self.assertEqual(self.etransferpage.czhuanzhangfangshi.text, '预约转账')
                self.assertEqual(self.etransferpage.cyuyuefangs.text, '周期预约')
                self.assertEqual(self.etransferpage.cfukzhangh.text, self.fkzh2)   #检查确认页面的付款账号

            self.assertEqual(self.etransferpage.cyongtu.text, self.manualyongtu)
            self.assertEqual(self.etransferpage.cfukzhangh.text, self.fkzh2)  # 付款账号校验，确认结果页面的其他校验，在最后面
            self.public_transfer_confirm_and_click(bank)  # 确认页面的公共的元素的值，校验完后点击下一步

            self.public_transfer_submit_verify(bank)  # 在提交结果页面检查
            self.isElementExists(self.etransferpage.tjjiaoyichulcg)
            self.assertEqual(self.etransferpage.tjfukzhangh.text, self.fkzh2)
            self.assertEqual(self.etransferpage.tjfkfangshi.text, '预约转账')
            self.assertEqual(self.etransferpage.tjyongtu.text, self.manualyongtu)  # 全局变量与该页面的用途比对

            self.etransferpage.tjwangyinrzchax.click()
            t.sleep(5)
            #进入网银日志查询页面
            self.public_transfer_EjnlQry_verify

    @property
    def public_transfer_EjnlQry_verify(self):
        '''
        点击网银日志查询，校验生成一条该流水号的日志记录
        :return:
        '''
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.etransferwelpage.mainframe)
        self.driver.switch_to.frame(self.etransferpage.EjnlQryframe2)
        self.assertEqual(self.etransferpage.Ejnljiaoyiliushuihao.text.replace(' ', ''), self.arg_liushuihao)

    def public_transfer_confirm_and_click(self, bank):
        '''
        在确认结果页面，校验业务公共的验证点，并点击确认按钮
        :param bank:
        :return:
        '''
        self.isElementExists(self.etransferpage.jiaoyiqueren)   #交易确认变红色
        #付款人比对：
        self.assertEqual(self.etransferpage.cbizhong1.text, self.bizhong)
        if bank == 'self':
            # 收款人比对：
            self.assertEqual(self.etransferpage.cskrmingcheng.text, self.skrmc)  # 本行
            self.assertEqual(self.etransferpage.cskzhanghao.text, self.skrzh.replace(' ', ''))
            self.assertEqual(self.etransferpage.ckaihuhang.text, self.skrkhh)
            # 交易信息
            self.assertEqual(self.etransferpage.cfukuanjine1.text, self.fukuanjine)  # 本行
            self.assertEqual(self.etransferpage.cshouxufei.text, self.fee1)
        elif bank == 'other':
            # 收款人比对：
            self.assertEqual(self.etransferpage.cskrmingcheng.text, self.skrmc1)  # 跨行
            self.assertEqual(self.etransferpage.cskzhanghao.text, self.skrzh1.replace(' ', ''))
            self.assertEqual(self.etransferpage.ckaihuhang.text, self.skrkhh1)
            # 交易信息
            self.assertEqual(self.etransferpage.cfukuanjine1.text, self.khzzjine1)  # 跨行
            self.assertEqual(self.etransferpage.cshouxufei.text, self.fee2)

        #输入验证码:万能码
        self.etransferpage.cyanzhengma.send_keys('1111')
        t.sleep(2)
        self.etransferpage.cconfirmbtn2.click()          #跳转到提交结果页面
        t.sleep(8)

    def public_transfer_submit_verify(self, bank):
        '''
        在提交结果页面，校验功能的验证点，并点击到下一步
        :return:
        '''
        self.isElementExists(self.etransferpage.tijiaojieguo)
        self.isElementExists(self.etransferpage.tjliushuihao)      #获取一个流水号，后面授权那边要用
        self.arg_liushuihao = self.etransferpage.tjliushuihao.text     #给变量赋值
        self.etransferpage.tjzhankaixiangq.click()
        t.sleep(2)
        if bank == 'self':
            self.assertEqual(self.etransferpage.tjskzhangh.text, self.skrzh.replace(' ', ''))
            self.assertEqual(self.etransferpage.tjfkjine.text[0:-1], self.fukuanjine)  # 本行
            self.assertEqual(self.etransferpage.tjshouxufei.text[0:-1], self.fee1)
        elif bank == 'other':
            self.assertEqual(self.etransferpage.tjskzhangh.text, self.skrzh1.replace(' ', ''))
            self.assertEqual(self.etransferpage.tjfkjine.text[0:-1], self.khzzjine1)  # 本行
            self.assertEqual(self.etransferpage.tjshouxufei.text[0:-1], self.fee2)

    def public_input_payee(self, bank):
        '''
        付款金额：本行、跨行，产生不同的fee
        :return:
        '''
        payee = self.etransferpage.fukuanjine
        if bank == 'self':
            payee.send_keys(self.fukuanjine)  # 必输项
            self.assertEqual(self.jedx, self.etransferpage.jinedaxie.text)
        elif bank == 'other':
            payee.send_keys(self.khzzjine)
            self.assertEqual(self.jedx1, self.etransferpage.jinedaxie.text)

    def public_yuqijieshuriqi(self, date, yuyue):
        '''
        修改预期日期
        :return:
        '''
        # tommorrow = (datetime.datetime.now() + datetime.timedelta(days=deltadate)).strftime('%Y-%m-%d')
        js1 = "var time=document.getElementById('executeDate');time.readOnly=false;time.value='"+date+"'; "
        js2 = "var time=document.getElementById('EndDate');time.readOnly=false;time.value='"+date+"'; "
        # js2 = "var time=document.getElementById('EndDate');time.readOnly=false;time.value='" + tommorrow + "'; "
        if yuyue == 'once':
            self.driver.execute_script(js1)
        elif yuyue == 'period':
            self.driver.execute_script(js2)

    def public_click_confirm(self, nflag, bank):
        '''
        信息录入页面点击确认，检查fee
        :return:
        '''
        self.arg_yongtu =  self.etransferpage.finalinputyongtu.text
        self.etransferpage.confirmbtn.click()
        if nflag == 1:
            fee = self.etransferpage.fee.text
            yingshoufee = self.etransferpage.yingshoufee.text
            youhuifee = self.etransferpage.youhuifee.text
            if bank == 'self':
                self.assertEqual(self.fee1, fee)
                self.assertEqual(self.yingshoufee1, yingshoufee)
                self.assertEqual(self.youhuifee1, youhuifee)
            elif bank == 'other':
                self.assertEqual(self.fee2, fee)
                self.assertEqual(self.yingshoufee, yingshoufee)
                self.assertEqual(self.youhuifee, youhuifee)
            t.sleep(5)
            self.driver.switch_to.default_content()
            self.etransferpage.confirmmodal.click()  # ie专有的
            t.sleep(3)
            self.driver.switch_to.frame(self.etransferwelpage.mainframe)
            self.driver.switch_to.frame(self.etransferpage.frame2)
        elif nflag == 2:
            self.public_click_reset()
            t.sleep(2)

    def public_click_reset(self):
        '''
        最后点击重置按钮
        :return:
        '''
        print(1)
        self.etransferpage.bigresetbtn.click()
        self.assertEqual('请输入付款金额', self.etransferpage.fukuanjine.get_attribute('placeholder'))

    @property
    def public_shoukuanren_verify(self):
        '''
        快捷选择收款人后检查自动回显
        :return:
        '''
        account = self.etransferpage.shoukuanzhangh.get_attribute('value')
        self.assertEqual(self.skrzh, account)
        self.assertEqual(self.skrkhh, self.etransferpage.kaihuh.get_attribute('value'))  # 取开户行的值

    @property
    def public_choose_bank(self):
        '''
        选择银行，输入和点击操作
        :return:
        '''
        self.etransferpage.xuanzeshengf.click()
        t.sleep(1)
        self.etransferpage.jiangsuProvince.click()
        t.sleep(1)
        self.etransferpage.xuanzechengs.click()
        t.sleep(1)
        self.etransferpage.suzhouCity.click()
        self.etransferpage.bank.click()
        self.etransferpage.gongshangbank.click()
        self.etransferpage.keysearch.send_keys(self.key)
        self.etransferpage.lianhangh.send_keys(self.lhh)
        self.etransferpage.searchbtn.click()

    def public_input_shoukuanren(self, bank):
        '''
        输入收款人信息，纯手工，不包含输入手机号
        :return:
        '''
        if bank == 'self':
            self.etransferpage.shoukuanzhangh.send_keys(self.skrzh)  # 输入
            self.etransferpage.shoukuanrenmc.send_keys(self.skrmc)  # 输入
            self.etransferpage.kaihuh.click()
            t.sleep(1)
        elif bank == 'other':
            self.etransferpage.shoukuanzhangh.send_keys(self.skrzh1)  # 输入
            self.etransferpage.shoukuanrenmc.send_keys(self.skrmc1)  # 输入
            t.sleep(3)
            self.public_choose_bank
            self.etransferpage.resetbtn.click()  # 重置信息
            self.public_choose_bank
            kaihuh = self.etransferpage.bankname.text
            self.etransferpage.xuanze2.click()  # 选择第一条记录
            t.sleep(1)
            self.assertEqual(kaihuh, self.etransferpage.kaihuh.get_attribute('value'))  # 选择的跟回显的做比对


if __name__ == "main":
    unittest.main()
