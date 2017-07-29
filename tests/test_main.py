import unittest
from broadlink2mqtt import main
 
class TestMain(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_number(self):
        self.assertEqual( main.get_number(), 3)
 
if __name__ == '__main__':
    unittest.main()

