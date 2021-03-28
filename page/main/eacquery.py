from base.page_objects import PageObject, PageElement, PageElements


class EacqueryPage(PageObject):
    '''
    农商行企业网银账户管理-账户查询
    '''
    zhanghuguanli_bigtab = PageElement(xpath="//li[@class='rowMainMenuActiveliColor']/a[contains(text(),'账户管理')]", timeout=2)
    mainframe = 'mainTarget'

    jiaoyimingxichax_sidebar = PageElement(xpath="//dd[@mname='交易明细查询'][@class='activeDlColor']", timeout=2)
    duozhanghmingxchax_sidebar = PageElement(xpath="//dd[@mname='多账号交易明细查询']", timeout=2)
    zhuanzmingxichax_sidebar = PageElement(xpath="//dd[@mname='转账明细查询']", timeout=2)
    tongyishitchax_sidebar = PageElement(xpath="//dd[@mname='统一视图查询']", timeout=2)
    #从转账服务点击交易明细跳转过来时，交易明细查询tab是active
    jiaoyimingxcx_tab = PageElement(xpath="//p[@class='activeCrumbNavigation']/b[text()='交易明细查询']", timeout=2)

    frame2 = 'rightMainIframeActTrsQry'
    jiaoyimingxchax_title = PageElement(xpath="//p[@class='ParagraphTitle'][text()='交易明细查询']", timeout=2)
