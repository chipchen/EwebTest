from testcase.public import LoginPageOp


class LoginPageTest(LoginPageOp):

    def test_login(self):
        self.login()
        self.logout()



