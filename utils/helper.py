import os
import xml.dom.minidom
import pandas as pd
import datetime


class Helper(object):        #读取配置信息的小工具，一些配置信息在xml文件

    def base_dir(self, filename, folder='data'):
        '''
        返回文件路径
        :param filename:
        :param folder:
        :return:
        '''
        # print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), folder, filename))
        return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), folder, filename)

    def get_now_datetime(self):
        '''获取当前时间'''
        return datetime.date.today()

    def get_screenshot_dir(self, folder='screenshot'):
        dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), folder)
        sub_dir = str(self.get_now_datetime())
        path = dir+"\\"+sub_dir
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.exists(path):
            os.mkdir(path)
        return path, timestamp

    def getXmlData(self, value):           #返回xml文件中第一个节点的内容
        '''
        获取xml单节点中的数据
        :param value:xml文件中单节点的名称
        '''
        # pwd = os.path.split(os.path.realpath(__file__))[0]     #这是helper.py真正的路径，切换过来才能找到data路径
        # os.chdir(pwd)
        # os.chdir(os.path.pardir)   #切换到上一级目录
        # os.chdir('data')      #切换到data目录
        # # print(os.getcwd())
        dom = xml.dom.minidom.parse(self.base_dir(filename='ui.xml'))    #打开xml文档
        db = dom.documentElement            #得到文档元素对象
        name = db.getElementsByTagName(value)    #结点名字
        name1 = db.getElementsByTagName(value)
        nameValue = name[0]     #结点的值，如果有多个name结点，表示第一个name结点的值
        name1Value = name1[0]
        # print(nameValue.firstChild.data)
        return nameValue.firstChild.data

    def readExcel(self, filename):
        '''
        读取excel表格的数据并返回
        :param rowx:在excel中的行数
        :param filename:excel文件名称
        :return:
        '''
        data = pd.read_excel((self.base_dir(filename)))
        # dd = data.head()
        # print('获取的值:\n{0}'.format(dd))
        test_data = []
        for i in data.index.values:
            row_data = data.loc[i, ['seqNo','version','apiname','priority','methods','host','path','headers','parameter','expect']].to_dict()
            test_data.append(row_data)
        # print('最终数据是：\n{0}'.format(test_data))
        return test_data


if __name__ == '__main__':
    a = Helper()
    a.get_screenshot_dir()
    a.getXmlData('url')
    a.readExcel(filename='apidata.xls')
