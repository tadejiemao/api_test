import unittest

## 用例包裹方法

def setUpModule():
    print("== setUpModule ==")

def tearDownModule():
    print("== tearDownModule ==")
    
class TestClass1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("-- setUpClass --")
#         super(TestClass1, cls).setUpClass()    

    @classmethod
    def tearDownClass(cls):
#         super(TestClass1, cls).tearDownClass() 
        print("-- tearDownClass --")
    
    def setUp(self):
        print(".. setUp ..")
    
    def tearDown(self):
        print(".. tearDown ..")
    
    def test_a(self):
        print("a")
    
    def test_B(self):
        print("B")                    

class TestClass2(unittest.TestCase):
    def test_A(self):
        print("A")

if __name__ == '__main__':
    unittest.main()       