from django.test import TestCase
from game.testingSystem.testingSystem import ProgramTest


class HomePageTest(TestCase):
    def templateTest(self):
        response = self.client.get('/')
        self.assertTemplateUsed('home.html')


class TestSystemTest(TestCase):
    #ProgramTest.run should return whatever shows up as program output
    #or the error message

    #ProgramTest.test should return consequence code - 0 for right anwser, 1 for
    #wrong anwser and 2 for error
    def testError(self):
        test = ProgramTest('print(dupa)','','')
        self.assertIn("NameError: name 'dupa' is not defined",test.run())
        self.assertEqual(2,test.test())

        test = ProgramTest('l = [1,2]\nprint(l[3])','','')
        self.assertIn("IndexError: list index out of range",test.run())
        self.assertEqual(2,test.test())


    def testWrongOutput(self):
        test = ProgramTest('n = int(input())\nprint(n ** 2 + 1)','2','4')
        self.assertEqual('5',test.run())
        self.assertEqual(1,test.test())


    def testCorrectOutput(self):
        test = ProgramTest('n = int(input())\nprint(n ** 2)','2','4')
        self.assertEqual('4',test.run())
        self.assertEqual(0,test.test())


    def testSanityChecks(self):
        test = ProgramTest('n = int(input())\nprint(n ** 2)','2','4')
        self.assertEqual(None,test.test())
