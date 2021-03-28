from base.page_objects import PageObject, PageElement


class LoginPage(PageObject):
    '''
    农商行企业网银登录页面
    '''
    CifNo = PageElement(id_='CifNo', timeout=2)
    # CifNo = PageElement(xpath="//label[text()='请输入客户号']", timeout=3)
    UserId = PageElement(id_='UserId', timeout=2)
    # UserId = PageElement(xpath="//label[text()='请输入用户名']", timeout=3)
    Password = PageElement(id_='powerpass', timeout=2)
    input_VerifyCode = PageElement(id_='inputAuthCode', timeout=2)
    # input_VerifyCode = PageElement(xpath="//label[text()='请输入验证码']", timeout=3)
    authcode = PageElement(id_='authcode', timeout=2)             #随机码
    loginbtn = PageElement(id_='loginbtn', timeout=2)
    # loginbtn = PageElement(xpath="//div[text()='登录']")

