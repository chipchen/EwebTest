from base.page_objects import PageObject, PageElement, PageElements


class EtransferWelPage(PageObject):
    '''
    农商行企业网银转账服务-转账服务首页
    '''
    mainframe = 'mainTarget'

    etransfer_item = PageElement(id_='Transfer_wel', timeout=2)
    etrsferremittance = PageElement(id_='etrsferremittance', timeout=2)              #二级菜单，转账
    daibanjiaoyi = PageElement(xpath="//form[@id='mainform']//p", timeout=2)
    zuijinzhuanzhang = PageElement(xpath="//p[@class='ParagraphTitle']//span", timeout=2)
    kuaijiecaozuo = PageElement(xpath="//p[@class='ParagraphTitle'][3]", timeout=2)
    lable_qr = PageElement(id_='sectioncnt', timeout=2)
    searchbtn = PageElement(css="#asideIframeBox > div.asideSearchBox > div > img", timeout=2)

    frame2 = 'rightMainIframeTransfer_wel'

    woyaozhuanzhang = PageElement(xpath="//p[@class='fastOperationColTitle'][1]/span", timeout=2)
    woyaodaifa = PageElement(xpath="//p[@class='fastOperationColTitle'][2]/span", timeout=2)  #定位方式不对
    woyaochaxun = PageElement(xpath="//p[@class='fastOperationColTitle'][3]/span", timeout=2)
    weihuguanli = PageElement(xpath="//p[@class='fastOperationColTitle'][4]/span", timeout=2)

    daichulijiaoyi = PageElement(xpath="(//p[@class='fl']/span)[1]", timeout=2)  # 待处理交易
    bishu = PageElement(xpath="(//span[text()='笔'])[1]", timeout=2)
    yichulijiaoyi = PageElement(xpath="//span[text()='已处理交易']", timeout=2)
    # yichulijiaoyi2 = PageElement(xpath="(//p[@class='fl']/span)[2]", timeout=2)
    bishu2 = PageElement(xpath="(//span[text()='笔'])[2]", timeout=2)

    zanwuxgzzjl = PageElement(xpath="//p[text()='暂无相关转账记录']", timeout=2)
    zanwuxgzzjl2 = PageElements(css="#AAA > div > div > p", timeout=2)
    shoukuanzhangh = PageElement(xpath="(//table[@class='ui-table navigationTable'])/thead/tr/th[1]", timeout=2)
    zhanghumingc = PageElement(xpath="(//table[@class='ui-table navigationTable'])/thead/tr/th[2]", timeout=2)
    jiaoyijine = PageElement(xpath="(//table[@class='ui-table navigationTable'])/thead/tr/th[3]", timeout = 2)
    caozuo = PageElement(xpath="(//table[@class='ui-table navigationTable'])/thead/tr/th[4]", timeout=2)
    yijianzhuanz = PageElement(xpath="(//table[@class='ui-table navigationTable'])/tbody/tr[1]/td[4]/span[1]", timeout=2) #第一条


    zhuanzhanghuik = PageElement(xpath="//li[text()='转账汇款']", timeout=2)

    daifagongzi = PageElement(xpath="//li[contains(text(),'代发工资')]", timeout=2)
    gonghuidaifa = PageElement(xpath="//li[contains(text(),'工会代发')]", timeout=2)
    piliangdaikou = PageElement(xpath="//li[contains(text(),'批量代扣')]", timeout=2)

    jiaoyimingxichax = PageElement(xpath="//li[text()='交易明细查询']", timeout=2)
    daifagongzichax = PageElement(xpath="//li[text()='代发工资查询']", timeout=2)
    gonghuidaifachax = PageElement(xpath="//li[text()='工会代发查询']", timeout=2)
    piliangdaikouchax = PageElement(xpath="//li[text()='批量代扣查询']", timeout=2)
    peiduizhanghuchax = PageElement(xpath="//li[text()='配对账户查询']", timeout=2)
    hanghaochax = PageElement(xpath="//li[text()='行号查询']", timeout=2)

    yuyuezzchexiao = PageElement(xpath="//li[contains(text(),'预约转账撤销')]", timeout=2)
    zzyongtuweihu = PageElement(xpath="//li[contains(text(),'转账用途维护')]", timeout=2)
    shoukuanrenzhguanli = PageElement(xpath="//li[contains(text(),'收款人账户管理')]", timeout=2)

    #二级大菜单
    etransfer = PageElement(id_='etrsferremittance', timeout=2)  # mainframe下面的转账，大菜单
    einterbmanage = PageElement(id_='einterbmanage', timeout=2)  # mainframe下面，转账管理
    eagentpayeesalary = PageElement(id_='eagentpayeesalary', timeout=2)  # mainframe下面，代发服务
    ebatchbucklemgmt = PageElement(id_='ebatchbucklemgmt', timeout=2)  #批量代扣


class EtransferPage(PageObject):
    '''
    农商行企业网银转账服务-转账-转账汇款
    '''
    etrsferremittance = PageElement(xpath="//dd[@mname='转账汇款'][@class='activeDlColor']", timeout=2)   #三级菜单‘转账汇款’,mainframe下面
    etrsferremittance1 = PageElement(xpath="//dd[@mname='转账汇款']", timeout=2)
    singleTransfer_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='单笔转账']", timeout=2)    #最上方红色标签，在mainframe下面
    singleTransfer_tab_notactive = PageElement(xpath="//b[@id='SingleTransfer'][text()='单笔转账']", timeout=2)
    frame2 = 'rightMainIframeSingleTransfer'

    danbizhuanzhang_tab = PageElement(xpath="//span[@class='activeTab']", timeout=2)    #单笔转账的活标签
    piliangkuahzz_tab = PageElement(xpath="//span[text()='批量跨行转账']", timeout=2)   #批量转账标签非活

    # 第一步，信息录入红色
    xinxiluru = PageElement(xpath="//span[@class='activeColor'][text()='信息录入']", timeout=2)

    fukuanren = PageElement(xpath="//p[text()='付款人']", timeout=2)
    fukuanzhanghao = PageElement(xpath="//a[@data-target='PayerAcNoAlias']/span", timeout=2)
    switchzhangh = PageElement(xpath="//div[@id='PayerAcNoAlias']/a[2]", timeout=2)   #切到这个账号
    keyongyue = PageElement(id_='PayerBalanceId', timeout=2)          #.text
    zhanghumingc = PageElement(id_='PayerAcNameSpan', timeout=2)
    zhguishudchax = PageElement(xpath="//span[text()='账户归属地查询']", timeout=2)   #以下四个检查该弹窗
    quxiaobtn = PageElement(xpath="//div[@class='singleBtnBox clearfix']/p[text()='取消']", timeout=2)
    tanchuangzhangh = PageElement(xpath="//table[@class='ui-table']/tbody/tr[1]/td[2]", timeout=2)   #.text
    tanchuangkaihuhmc = PageElement(xpath="//table[@class='ui-table']/tbody/tr[2]/td[2]", timeout=2)
    bizhong = PageElement(id_='PayerCurrencyId', timeout=2)

    shoukuanren = PageElement(xpath="//p[text()='收款人']", timeout=2)
    shoukuanrenmc = PageElement(id_='PayeeAcNameAlias', timeout=2) #sendkey
    recentTrans = PageElement(xpath="//div[@id='recentTranInfo']/span[1]", timeout=2)       #保存最近转账的顺序是倒序
    shoukuanzhangh = PageElement(id_='PayeeAcNoAlias', timeout=2)
    kaihuh = PageElement(id_='PayeeBankDept', timeout=2)   #get_attribute(value)
    shoukrshoujih = PageElement(id_='teleNum', timeout=2)
    label = PageElement(xpath="//label[@for='savpayeeCheck']", timeout=2)

    #收款人
    xuanzeshoukrbtn = PageElement(xpath="//span[text()='选择收款人']", timeout=2)
    qiyemingc = PageElement(xpath="//a[@data-target='SelectCif']/span", timeout=2)          #.text，默认等于测试数据里面提供的
    shoukuanrfz = PageElement(xpath="//a[@data-target='GroupId']/span", timeout=2)           #.text,默认全部
    chax = PageElement(xpath="//p[text()='查询']", timeout=2)
    xuanze = PageElement(xpath="(//td[@class='operationTd']/a)[1]", timeout=2)     #收款人查询的第一条，选择按钮

    #选择银行
    xuanzeshengf = PageElement(xpath="//span[text()='请选择省份']", timeout=2)
    xuanzechengs = PageElement(xpath="//span[text()='请选择城市']", timeout=2)
    jiangsuProvince = PageElement(xpath="//a[text()='江苏省']", timeout=2)
    suzhouCity = PageElement(xpath="//a[text()='S-苏州市']", timeout=2)
    bank = PageElement(xpath="//span[text()='请选择']", timeout=2)
    gongshangbank = PageElement(xpath="//a[text()='中国工商银行']", timeout=2)
    keysearch = PageElement(id_='DeptNameSeach', timeout=2)    #搜索‘苏州分行’
    lianhangh = PageElement(id_='BankIdSeach', timeout=2)   #输入102305000017
    resetbtn = PageElement(xpath="//div[@id='chooseBankBox']/child::div[1]/input", timeout=2)
    searchbtn = PageElement(xpath="//input[@value='查询']", timeout=2)
    xuanze2 = PageElement(xpath="//span[text()='选择']", timeout=2)    #第一条记录
    bankname = PageElement(xpath="//table[@id='UnionDeptIdAlias']/tbody/tr[3]/td", timeout=2)   #.text

    #交易信息
    jiaoyixinxi = PageElement(xpath="//p[text()='交易信息']", timeout=2)
    fukuanjine = PageElement(xpath="//input[@placeholder='请输入付款金额']", timeout=2)
    danbixiane = PageElement(xpath="//span[text()='可用单笔限额：']/following-sibling::span", timeout=2)    #.text使用
    rileijixiane = PageElement(xpath="//span[text()='可用日累计限额：']/following-sibling::span", timeout=2)   #.text使用，assert的时候转换成数字然后做加减法
    shouxufbz = PageElement(xpath="//span[text()='手续费标准']", timeout=2)
    cancelbtn = PageElement(xpath="//p[text()='取消']", timeout=2)
    jinedaxie = PageElement(id_='fff', timeout=2)
    fee = PageElement(id_='fee', timeout=2)
    yingshoufee = PageElement(id_='receivableFee', timeout=2)    #应收手续费
    youhuifee = PageElement(id_='discountFee', timeout=2)    #优惠手续费
    xuanzeluru = PageElement(xpath="//label[text()='选择录入']", timeout=2)
    shoudongluru = PageElement(xpath="//label[text()='手动录入']", timeout=2)
    fukuanyongt = PageElement(xpath="//a[@data-target='RemarkAlias']/span[1]", timeout=2)    #默认.text是往来款
    fukuanyongtinput = PageElement(id_='RemarkAlias2', timeout=2)   #输入付款用途
    yongtu2 = PageElement(xpath="//div[@id='RemarkAlias']/a[last()]", timeout=2)   #div块下面的最后一个标签
    yongtuweihubtn = PageElement(xpath="//span[text()='用途维护']", timeout=2)
    zhuanzhangfs = PageElement(xpath="//label[text()='实时转账']", timeout=2)
    yuyuezhuanz = PageElement(xpath="//label[text()='预约转账']", timeout=2)
    zhuanzhangsm = PageElement(xpath="//span[text()='实时到账，具体到账时间以收款银行为准。']", timeout=2)
    zhuanzhangsm1 = PageElement(xpath="//span[text()='预约转账日期如遇节假日将不做转账处理']", timeout=2)
    yuyueriqi = PageElement(id_='executeDate', timeout=2)
    zhuanzshuom = PageElement(xpath="//span[text()='实时到账，具体到账时间以收款银行为准。']", timeout=2)
    tixing1 = PageElement(xpath="//span[text()='什么情况下不能及时到账']", timeout=2)
    tixing2 = PageElement(xpath="//span[text()='什么是智慧转账']", timeout=2)
    transferPinkPrompt = PageElement(xpath="//span[text()='什么是智慧转账']/following-sibling::div/span", timeout=2)
    transferPinkPrompt1 = PageElement(xpath="//span[text()='什么情况下不能及时到账']/following-sibling::div/span", timeout=2)
    danciyuyue = PageElement(xpath="//label[text()='单次预约']", timeout=2)
    zhouqiyuyue = PageElement(xpath="//label[text()='周期预约']", timeout=2)   #周期预约按钮
    yuyueriqi = PageElement(xpath="//input[@id='executeDate']", timeout=2)    #get_arribute(value)取到默认的日期
    gouxuank = PageElement(xpath="//label[@for='Schedulednotify']", timeout=2)  #默认不勾选
    tongzhisjh = PageElement(id_='mytel', timeout=2)   #勾选提醒则必须输入手机号
    #周期预约
    zhouqiyuypinl = PageElement(xpath="//span[text()='每日']", timeout=2)  #默认
    yuyueriqi = PageElement(xpath="//span[text()='每日']", timeout=2)   #默认
    meizhou = PageElement(xpath="//a[text()='每周']", timeout=2)   #改为每周
    yuyueriqi1 = PageElement(xpath="//span[text()='周日']", timeout=2)  #默认周日
    yuyueriqi2 = PageElement(xpath="//a[text()='周一']", timeout=2)  #改为周一
    meiyue = PageElement(xpath="//a[text()='每月']", timeout=2)   #改为每月
    yuyueriqi3 = PageElement(xpath="//span[text()='1号']", timeout=2)  # 默认1号
    yuyueriqi4 = PageElement(xpath="//a[text()='2号']", timeout=2)  # 默认1号,改成2号
    yuyueriqi55 = PageElement(xpath="//span[text()='2号']", timeout=2)  # 点击2号
    yuyueriqi5 = PageElement(xpath="//div[@id='freqDate']/a[last()]", timeout=2)    #改成月底
    #预约结束日期通过脚本发进去

    #在confirm之前，把确认页需要比对的数据都拿到：
    finalfkzh = PageElement(xpath="//a[@data-target='PayerAcNoAlias']/span", timeout=2)
    # 收款人,直接取已知传入数据
    # 交易信息
    finalinputyongtu = PageElement(xpath="//a[@data-target='RemarkAlias']/span", timeout=2)   #返回实际填写的用途
    manualinputyongtu = PageElement(xpath="//input[@id='RemarkAlias2']", timeout=2)   #手工输入用途的时候，get_attribute
    finalzhuanzhangfangshi = PageElement(xpath="//label[@for='radionow']", timeout=2)     #返回实际选择的转账方式

    confirmbtn = PageElement(xpath="//input[@value='确认']", timeout=2)
    bigresetbtn = PageElement(xpath="//input[@value='重置']", timeout=2)

    confirmmodal = PageElement(xpath="//p[@class='confirmModal'][text()='确定']", timeout=2)         #ie专有的弹框，在mainframe下

    #第二步，交易确认页
    jiaoyiqueren = PageElement(xpath="//span[@class='activeColor'][text()='交易确认']", timeout=2)

    #付款人
    cfukzhangh = PageElement(xpath="//div[@class='topAccountInfo'][1]/descendant::div/span", timeout=2)
    cbizhong1 = PageElement(xpath="(//div[@class='topAccountInfo'][1]/descendant::div/span)[2]", timeout=2)
    #收款人
    cskrmingcheng = PageElement(xpath="(//div[@class='topAccountInfo'][2]/descendant::div/span)[1]", timeout=2)
    cskzhanghao = PageElement(xpath="(//div[@class='topAccountInfo'][2]/descendant::div/span)[2]", timeout=2)
    ckaihuhang = PageElement(xpath="(//div[@class='topAccountInfo'][2]/descendant::div/span)[3]", timeout=2)
    #交易信息
    cfukuanjine1 = PageElement(xpath="(//div[@class='topAccountInfo'][3]/descendant::div/span)[1]", timeout=2)
    cshouxufei = PageElement(xpath="(//div[@class='topAccountInfo'][3]/descendant::div/span)[2]", timeout=2)
    cyongtu = PageElement(xpath="(//div[@class='topAccountInfo'][3]/descendant::div/span)[3]", timeout=2)
    czhuanzhangfangshi = PageElement(xpath="(//div[@class='topAccountInfo'][3]/descendant::div/span)[4]", timeout=2)
    cyuyuefangs = PageElement(xpath="(//div[@class='topAccountInfo'][3]/descendant::div/span)[5]", timeout=2)
    cyuyuezhuanzriqi = PageElement(xpath="(//div[@class='topAccountInfo'][3]/descendant::div/span)[6]", timeout=2)

    czhouqiyypinl = PageElement(xpath="//span[text()='周期预约频率：']/../following-sibling::div/span", timeout=2)  #每日、每周、每月
    czhouqiyyjieshuriqi = PageElement(xpath="//span[text()='周期预约结束日期：']/../following-sibling::div/span", timeout=2)
    cfaqiri = PageElement(xpath="//span[text()='发起日：']/../following-sibling::div/span", timeout=2)
    #如果前面输入了预约提醒手机号，那么就是“开通”，否则就是“关闭”
    cyuyuetixing = PageElement(xpath="//span[text()='预约提醒：']/../following-sibling::div/span", timeout=2)
    cwenxintis = PageElement(xpath="//p[text()='温馨提示：']/following-sibling::div/span", timeout=2)

    cyanzhengma = PageElement(xpath="//input[@name='validateCode']", timeout=2)

    cbackbtn = PageElement(xpath="//input[@value='返回']", timeout=2)
    cconfirmbtn2 = PageElement(xpath="//input[@value='确认']", timeout=2)

    #第三部，提交结果页
    tijiaojieguo = PageElement(xpath="//span[@class='activeColor'][text()='提交结果']", timeout=2)

    tjjiaoyichulcg = PageElement(xpath="//p[text()='交易处理成功']", timeout=2)
    tjjiaoyiyishoul = PageElement(xpath="//p[text()='交易已受理，资金具体到账时间请咨询收款银行']", timeout=2)
    tjliushuihao = PageElement(xpath="//table[@class='ui-table']/tbody/tr[2]/td[1]")
    tjzhankaixiangq = PageElement(xpath="//span[text()='展开详情']", timeout=2)
    tjshouqixiangq = PageElement(xpath="//span[text()='收起详情']", timeout=2)

    tjfukzhangh = PageElement(xpath="(//div[@class='transferRightCaption'])[1]/span", timeout=2)
    tjskzhangh = PageElement(xpath="(//div[@class='transferRightCaption'])[2]/span", timeout=2)

    tjfkjine = PageElement(xpath="(//div[@class='transferRightCaption'])[3]/span", timeout=2)
    tjfkfangshi = PageElement(xpath="(//div[@class='transferRightCaption'])[4]/span", timeout=2)
    tjshouxufei = PageElement(xpath="(//div[@class='transferRightCaption'])[5]/span", timeout=2)
    tjyongtu = PageElement(xpath="(//div[@class='transferRightCaption'])[6]/span", timeout=2)

    tjjixuzhuanz = PageElement(xpath="//span[text()='继续转账']", timeout=2)
    tjwangyinrzchax = PageElement(xpath="//span[text()='网银日志查询']", timeout=2)
    tjbackbtn = PageElement(xpath="//p[text()='返回首页']", timeout=2)

    #网银日志查询 客户服务-查询打印-网银日志查询
    #mainframe下
    EjnlQry = PageElement(xpath="//dd[@id='EjnlQry'][@class='activeDlColor']", timeout=2)       #网银日志查询三级菜单,活动菜单
    EjnlQry_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='网银日志查询']", timeout=2)  #红色活动标签
    #frame2下
    EjnlQryframe2 = 'rightMainIframeEjnlQry'
    Ejnljiaoyiliushuihao = PageElement(xpath="//th[text()='交易流水号']/../../tr[2]/td/a", timeout=2)    #流水号
    Ejnljiaoyiriqi = PageElement(xpath="//th[text()='交易流水号']/../../tr[2]/td[2]", timeout=2)
    Ejnljiaoyileixing = PageElement(xpath="//th[text()='交易流水号']/../../tr[2]/td[3]", timeout=2)
    Ejnljiaoyijine = PageElement(xpath="//th[text()='交易流水号']/../../tr[2]/td[4]", timeout=2)


class AgentPayeeSalaryPage(PageObject):
    '''
    农商行企业网银转账服务-代发服务-代发工资
    '''
    daifagongzi_sidebar = PageElement(xpath="//dd[@mname='代发工资'][@class='activeDlColor']", timeout=2)
    daifagongzi_sidebar1 = PageElement(xpath="//dd[@mname='代发工资']", timeout=2)
    # 从转账服务点代发工资跳转到这里，代发工资标签active
    daifagongzi_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='代发工资']", timeout=2)  # 在mainframe下面红色标签

    frame2 = 'rightMainIframeAgentPayeeSalary'
    daifagongzi = PageElement(xpath="//p[text()='代发工资'][@class='fl progressMenuBoxTitle']", timeout=2)  #在frame2下面


class ETrsAgentSalaryPage(PageObject):
    '''
    农商行企业网银转账服务-代发服务-工会代发
    '''
    gonghuidaif_sidebar = PageElement(xpath="//dd[@mname='工会代发'][@class='activeDlColor']", timeout=2)
    gonghuidaif_sidebar1 = PageElement(xpath="//dd[@mname='工会代发']", timeout=2)
    gonghuidaif_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='工会代发']", timeout=2) #红色标签激活

    frame2 = 'rightMainIframeeTrsAgentSalary'
    gonghuidaifa = PageElement(xpath="//p[text()='工会代发'][@class='fl progressMenuBoxTitle']", timeout=2)


class AgentQryPayeeSalaryPage(PageObject):
    '''
    农商行企业网银转账服务-代发服务-代发工资查询
    '''
    daifagongzichax_sidebar = PageElement(xpath="//dd[@mname='代发工资查询'][@class='activeDlColor']", timeout=2)  # 代发工资查询
    daifagongzichax_sidebar1 = PageElement(xpath="//dd[@mname='代发工资查询']", timeout=2)
    # 从转账服务点代发工资查询跳转到这里，代发工资查询标签active
    daifagongzichx_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='代发工资查询']", timeout=2)

    frame2 = 'rightMainIframeAgentQryPayeeSalary'
    daifagongzichax = PageElement(xpath="//p[@class='ParagraphTitle'][text()='代发工资查询']", timeout=2)


class ETrsAgentSalaryQryPage(PageObject):
    '''
    农商行企业网银转账服务-代发服务-工会代发查询
    '''
    gonghuidaifchax_sidebar = PageElement(xpath="//dd[@mname='工会代发查询'][@class='activeDlColor']", timeout=2)
    gonghuidaifchax_sidebar1 = PageElement(xpath="//dd[@mname='工会代发查询']", timeout=2)
    gonghuidaifchax_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='工会代发查询']", timeout=2)
    frame2 = 'rightMainIframeeTrsAgentSalaryQry'
    gonghuidaifchax = PageElement(xpath="//p[@class='ParagraphTitle'][text()='工会代发查询']", timeout=2)


class BatchBucklePage(PageObject):
    '''
    农商行企业网银转账服务-批量代扣
    '''
    piliangdaik_sidebar = PageElement(xpath="//dd[@mname='批量代扣'][@class='activeDlColor']", timeout=2)
    piliangdaik_sidebar1 = PageElement(xpath="//dd[@mname='批量代扣']", timeout=2)
    piliangdaik_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='批量代扣']", timeout=2)

    frame2 = 'rightMainIframeBatchBuckle'
    shougongluru = PageElement(xpath="//span[text()='手工录入'][@class='payeeAccMenuActive']", timeout=2)    #点击批量代扣进来默认是手工录入active
    wenjianshangc = PageElement(xpath="//span[text()='文件上传']", timeout=2)    #点击批量代扣进来默认文件上传tab不是active
    daikouxinxi = PageElement(xpath="//p[text()='代扣信息'][@class='ParagraphTitle']", timeout=2)


class BatchBuckleQryPage(PageObject):
    '''
    农商行企业网银转账服务-批量代扣-批量代扣结果查询
    '''
    piliangdaikjgchax_sidebar = PageElement(xpath="//dd[@mname='批量代扣结果查询'][@class='activeDlColor']", timeout=2)
    piliangdaikjgchax_sidebar1 = PageElement(xpath="//dd[@mname='批量代扣结果查询']", timeout=2)
    piliangdaikjgchax_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='批量代扣结果查询']", timeout=2)
    frame2 = 'rightMainIframeBatchBuckleQry'
    piliangdaikchax = PageElement(xpath="//p[@class='ParagraphTitle'][text()='批量代扣查询']", timeout=2)


class PairAccountQueryPage(PageObject):
    '''
    农商行企业网银转账服务-转账管理-配对账户查询
    '''
    peiduizhanghchax_sidebar = PageElement(xpath="//dd[@mname='配对账户查询'][@class='activeDlColor']", timeout=2)
    peiduizhanghchax_sidebar1 = PageElement(xpath="//dd[@mname='配对账户查询']", timeout=2)
    peiduizhanghchax_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='配对账户查询']", timeout=2)
    frame2 = 'rightMainIframePairAccountQuery'
    peiduizhanghchax = PageElement(xpath="//p[@class='ParagraphTitle'][text()='配对账户查询']", timeout=2)


class BankCodeQryPage(PageObject):
    '''
    农商行企业网银转账服务-转账管理-行号查询
    '''
    hanghaochax_sidebar = PageElement(xpath="//dd[@mname='行号查询'][@class='activeDlColor']", timeout=2)
    hanghaochax_sidebar1 = PageElement(xpath="//dd[@mname='行号查询']", timeout=2)
    hanghaochax_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='行号查询']", timeout=2)
    frame2 = 'rightMainIframeBankCodeQry'
    hanghaochax = PageElement(xpath="//p[@class='ParagraphTitle'][text()='行号查询']", timeout=2)


class ETransferNotRealTimePage(PageObject):
    '''
    农商行企业网银转账服务-转账管理-预约转账撤销
    '''
    yuyuezzchex_sidebar = PageElement(xpath="//dd[@mname='预约转账撤销'][@class='activeDlColor']", timeout=2)
    yuyuezzchex_sidebar1 = PageElement(xpath="//dd[@mname='预约转账撤销']", timeout=2)
    yuyuezzchex_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='预约转账撤销']", timeout=2)
    frame2 = 'rightMainIframeETransferNotRealTime'
    yuyuezzchex = PageElement(xpath="//p[@class='ParagraphTitle'][text()='预约转账撤销']", timeout=2)


class EtrspurposemgmtPage(PageObject):
    '''
    农商行企业网银转账服务-转账管理-转账用途维护
    '''
    zhuanzytweih_sidebar = PageElement(xpath="//dd[@mname='转账用途维护'][@class='activeDlColor']", timeout=2)
    zhuanzytweih_sidebar1 = PageElement(xpath="//dd[@mname='转账用途维护']", timeout=2)
    zhuanzytweih_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='转账用途维护']", timeout=2)
    frame2 = 'rightMainIframeetrspurposemgmt'
    zhuanzytweih = PageElement(xpath="//p[@class='ParagraphTitle mar-bt30'][text()='转账用途维护']", timeout=2)


class PayeeBookManageMgrPage(PageObject):
    '''
    农商行企业网银转账服务-转账管理-收款人账户管理
    '''
    shoukrzhguanl_sidebar = PageElement(xpath="//dd[@mname='收款人账户管理'][@class='activeDlColor']", timeout=2)
    shoukrzhguanl_sidebar1 = PageElement(xpath="//dd[@mname='收款人账户管理']", timeout=2)
    shoukrzhguanl_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='收款人账户管理']", timeout=2)
    frame2 = 'rightMainIframePayeeBookManageMgr'
    shoukuanrzhguanli_tab2 = PageElement(xpath="//span[@class='payeeAccMenuActive'][text()='收款人账户管理']", timeout=2)
    fenzuguanli_tab = PageElement(xpath="//span[text()='分组管理']", timeout=2)   #非active
    chaxunjieguo = PageElement(xpath="//p[@class='ParagraphTitle'][text()='查询结果']", timeout=2)










