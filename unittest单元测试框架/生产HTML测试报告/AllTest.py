import os, time, unittest
import HTMLTestRunner


def getAllCase():
    # 获取所有的测试模块

    testSuite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), 'TestCase'), pattern='test*.py')
    return testSuite


def RunMain():
    # 生成测试报告，写入指定的Reports目录

    fp = open(os.path.join(os.path.dirname(__file__), 'Reports', 'resultReport.html'), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python+Selenium自动测试实战', description = '基于Python语言UI自动化测试')

    runner.run(getAllCase())


if __name__ == '__main__':
    RunMain()