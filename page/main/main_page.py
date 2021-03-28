from base.page_objects import PageObject, PageElement


class MainPage(PageObject):
    '''
    农商行企业网银首页-现管客群
    '''
    etransfer = PageElement(link_text='转账服务', timeout=2)
    etransfer1 = PageElement(id_='etranfer', timeout=2)
    efinance = PageElement(link_text='贷款服务', timeout=2)

    logout_btn = PageElement(xpath="//li[text()='安全退出']")