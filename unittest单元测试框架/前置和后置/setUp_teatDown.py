import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('测试用例执行之前要做的事')

    def test_isupper(self):
        self.assertTrue('FOO'.endswith('O'))
        self.assertFalse("Foo".isupper())
        print('第一条测试用例')

    def test_strendswich(self):
        self.assertEqual('foo'.endswith('o'),True)
        print('第二条测试用例')

    def tearDown(self):
        print('每条测试用例执行完毕后的操作。。。')


if __name__ == '__main__':
    unittest.main()