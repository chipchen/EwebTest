import autoit


class ProcessControl(object):
    '''
    AutoIt进程相关操作
    '''

    def __init__(self, processName):
        '''
        Constructor
        '''
        self.processName = processName

    def close(self):
        '''
        :description 终止某个进程
        :return 1:成功; 0:失败.
        '''
        return autoit.process_close(self.processName)

    def exists(self):
        '''
        :description 检查指定进程是否存在
        :return PID:成功; 0:进程不存在.
        '''
        return autoit.process_exists(self.processName)