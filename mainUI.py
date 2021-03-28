import unittest
import os
import time
import HTMLTestRunner


def all_tests():
    '''获取所有要执行的测试用例'''

    # suite = unittest.TestSuite()    #实例化套件
    # suite.addTest(UserInterFaceTestCase('test_bluelog_reply'))    #按顺序加入测试方法，一个方法一个用例，class是testcase
    # suite.addTest(UserInterFaceTestCase('test_wenjuan'))

    # suite = unittest.TestSuite(unittest.makeSuite(Test1TestCase))    #把测试类一起装到套件里面，独立运行；不依赖顺序
    loader = unittest.TestLoader()
    # suite = unittest.loader.loadTestsFromTestCase(Test1TestCase)       #通过testLoader来加载测试类

    # suite = loader.loadTestsFromModule(test1)       #通过模块来导入用例，一个python文件包含多个class

    suite = loader.discover(start_dir=os.path.dirname(__file__), pattern='test_*.py', top_level_dir=None)  #批量执行test开头的py文件下的用例
    print(suite)
    return suite


def get_now_time():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))


def run():
    filename = os.path.join(os.path.dirname(__file__), 'report', get_now_time() + 'report.html')  #当前文件的path下的Report下的文件
    fp = open(filename, 'wb')
    if __name__ == '__main__':
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title='UI自动化测试报告',
                                               description='UI自动化测试报告详情',
                                               verbosity=2
                                               )
        runner.run(all_tests())


if __name__ == '__main__':
    run()