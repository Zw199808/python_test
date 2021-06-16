import ddt
import unittest


Data = [
    {'name':"keep learing"},
    {'age':18},
    {'address':"深圳地区"}
]
@ddt.ddt
class TestModel(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('testcase starting')
    @classmethod
    def tearDownClass(self) -> None:
        print('testcase ending')

    @ddt.data(Data)
    def test_DataDriver(self, Data):
        print("DDT数据驱动实战演示：", Data)


if __name__ == '__main__':
    unittest.main()
