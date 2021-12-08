##############################################################
# UNIT TESTS
##############################################################
import unittest
import main

class TestMain(unittest.TestCase):

    def test_textProcess(self):
        result = main.textProcess("Hello my name is Andre and I am a hardworking person." + 
            "I began CS 6 years ago and have 3 years of work experience")
        print("result is " + str(result))
        self.assertGreaterEqual(result, .1)

if __name__ == '__main__':
    unittest.main()
