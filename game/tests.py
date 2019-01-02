from django.test import TestCase
from django.conf import settings
from django.urls import get_resolver

from game.models import Task, Test
from game.testingSystem.testingSystem import ProgramTest

from time import sleep



class HomePageTest(TestCase):
    def templateTest(self):
        response = self.client.get('/')
        self.assertTemplateUsed('home.html')


class TimeLimitTest(TestCase):
    TEST_TIME_LIMIT = 1

    def setUp(self):
        self.OG_TIME_LIMIT = settings.TIME_LIMIT
        settings.TIME_LIMIT = self.TEST_TIME_LIMIT


    def tearDown(self):
        settings.TIME_LIMIT = self.OG_TIME_LIMIT


    def testTimeLimit(self):
        Task.objects.create(pk=1,
        problemName='Find Extra One',
        problemDesciption='You have n distinct points on a plane, none of them lie on OY axis. Check that there is a point after removal of which the remaining points are located on one side of the OY axis.',
        inputDesription='The first line contains a single positive integer n (2 ≤ n ≤ 105).\nThe following n lines contain coordinates of the points. The i-th of these lines contains two single integers xi and yi (|xi|, |yi| ≤ 109, xi ≠ 0). No two points coincide.',
        outputDescription='Print "Yes" if there is such a point, "No" — otherwise.\nYou can print every letter in any case (upper or lower).'
        )

        Test.objects.create(input='3\n1 1\n-1 -1\n2 -1',
        output='Yes',
        task=1
        )
        Test.objects.create(input='4\n1 1\n2 2\n-1 1\n-2 2',
        output='No',
        task=1
        )

        self.client.get('/')
        response = self.client.get('/new',follow = True)
        sleep(2)
        self.assertTrue(any('timeout' in str(fun) for fun in \
                                  list(get_resolver(None).reverse_dict.keys())))


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
