##############################################################
# UNIT TESTS
##############################################################
import unittest
import TextProcess

class TestTextProcess(unittest.TestCase):

    def test_correctnessScore(self):
        result = TextProcess.correctnessScore("Hello my name is Andre and I am a hardworking person." + 
            "I began CS 6 years ago and have 3 years of work experience")
        print("result is " + str(result))
        self.assertGreaterEqual(result, .1)
    
    def test_convertToText(self):
        filename = "TestFiles\helloTest.wav"
        result = TextProcess.convertToText(filename)
        result = result.lower()
        text = "hello my name is andre i'm a third-year computer science student and have two years it programming experience"
        self.assertEqual(result, text)

if __name__ == '__main__':
    unittest.main()
