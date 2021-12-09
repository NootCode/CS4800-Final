##############################################################
# UNIT TESTS
##############################################################
import unittest
import TextProcess

class TestTextProcess(unittest.TestCase):

    def test_MP4toWavtoText(self):
        filename = "TestFiles\helloTest.mp4"
        wavFile = TextProcess.convertToWav(filename)
        result = TextProcess.convertToText(wavFile)
        result = result.lower()
        text = "hello my name is andre i'm a third-year computer science student and have two years it programming experience"
        self.assertEqual(result, text)
        TextProcess.removeFiles()
    
    def test_AnalyzeCorrectandAppendtoTxt(self):
        text = ("Hello my name is Andre and I am a hardworking person." + 
            "I began CS 6 years ago and have 3 years of work experience")
        result = TextProcess.correctnessScore(text)
        self.assertGreaterEqual(result, .1)
        TextProcess.writeToFile(text, result, 15)

if __name__ == '__main__':
    unittest.main()
