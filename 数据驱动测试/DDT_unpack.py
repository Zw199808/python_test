import unittest
import ddt

Data = [
    ['admin','admin','登录失败'],
    ['admin','admin123','登录成功'],
    ['','','登录失败'],
]
@ddt.ddt
class TestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('testcase starting')
    @classmethod
    def tearDownClass(cls) -> None:
        print('testcase ending')

    @ddt.data(*Data)
    @ddt.unpack
    def test_DataDriver(self,account,pwd,msg):
        print('ddt数据驱动演示：',account)
        print('ddt数据驱动演示：',pwd)
        print('ddt数据驱动演示：',msg)


if __name__ == '__main__':
    unittest.main()