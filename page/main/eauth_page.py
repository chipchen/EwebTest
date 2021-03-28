from base.page_objects import PageObject, PageElement


class EauthPage(PageObject):
    '''
    农商行企业网银交易授权-交易授权
    '''
    mainframe = 'mainTarget'
    frame2 = 'rightMainIframeAuthListt'
    frame3 = 'Detail'                    #看起来没有用到，是一个display=none的空间
    # jiaoyishouquan_title = PageElement(xpath="//p[text()='交易授权']")           #在frame2下
    jiaoyishouquan = PageElement(xpath="//p[@class='ParagraphTitle']", timeout=2)
    jiaoyishouquan_tag = PageElement(id_="AuthListt")      #在mainTarget下面
    qizhiriqi = PageElement(xpath="//span[text()='起止日期：']")           #未授权的tab下有这个字段
    shenheqizhiriqi = PageElement(xpath="//span[text()='审核起止日期：']")      #已授权的tab下有这个字段

