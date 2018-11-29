from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from game.models import Task, Test

from time import time
MAX_WAIT = 10

class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()


    def testGame(self):
        self.browser.get(self.live_server_url)

        self.assertEqual('Ring of Compiler',self.browser.title)

        startButton = self.browser.find_element_by_tag_name('button')
        self.assertEqual(startButton.text,'Start Game')

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

        startButton.submit()

        Task.objects.create(pk=2,
                            problemName='Test problem',
                            problemDesciption='just for tests',
                            inputDesription='this is oooonly a test',
                            outputDescription='FUNctional tests'
                           )

        Test.objects.create(input='input for testing',
                            output='TEST',
                            task=2
                           )

        #insert solution with error, dont change task,  print error message
        #in output and get consequence 2
        inputField = self.browser.find_element_by_id('codemirror-textarea')
        inputField.send_keys('print(dupa)')
        submitButton = self.browser.find_element_by_tag_name('button')
        submitButton.click()

        while(True):
            waitStart = time()
            try:
                inputField = self.browser.find_element_by_id('codemirror-textarea')
                break
            except StaleElementReferenceException as e:
                if time() - waitStart > MAX_WAIT:
                    raise e
                    print('Waiting for the page to load')
        self.assertEqual(inputField.text,'print(dupa)')

        #TODO changed the id of the consequences box but no idea what im doing
        #so this might cause problems
        consequencesBox = self.browser.find_element_by_id('interpretfieldcons')
        self.assertIn('Consequence 2', consequencesBox.text)

        taskNameBox = self.browser.find_element_by_id('taskName')
        self.assertEqual(taskNameBox.text,'Find Extra One')

        outputBox = self.browser.find_element_by_id('interpretfield')
        self.assertIn("NameError: name 'dupa' is not defined",outputBox.text)

        #insert wrong answser, dont change task,print program output in output
        #and get consequence 1


        inputField.send_keys("print('dupa')")
        submitButton = self.browser.find_element_by_tag_name('button')
        submitButton.click()

        inputField = self.browser.find_element_by_id('codemirror-textarea')
        self.assertEqual(inputField.text, "print('dupa')")

        consequencesBox = self.browser.find_element_by_id('interpretfieldcons')
        self.assertIn('Consequence 1', consequencesBox.text)

        taskNameBox = self.browser.find_element_by_id('taskName')
        self.assertEqual(taskNameBox.text,'Find Extra One')

        #The output here should be roughly like this:
        #TEST 1:
        #{output of users program}``
        #for input:
        #{input from Test database table}
        #
        #TEST 2:
        #{output of users program}
        #for input:
        #{input from Test database table}
        outputBox = self.browser.find_element_by_id('interpretfield')
        self.assertIn('dupa',outputBox.text)
        self.assertIn('TEST 2',outputBox.text)

        #insert good solution should output program output in output,
        #get conequence 0 and serve new task
        code = \
        '''n = int(input())
        l = []
        for i in range(n)
            l.append(input())
        if n == 3:
            print('Yes')
        else:
            print('No')'''
        inputField.send_keys(code)
        submitButton = self.browser.find_element_by_tag_name('button')
        submitButton.click()

        inputField = self.browser.find_element_by_id('codemirror-textarea')
        self.assertEqual(inputField.text, '')

        consequencesBox = self.browser.find_element_by_id('interpretfieldcons')
        self.assertIn('Consequence 0', consequencesBox.text)

        taskNameBox = self.browser.find_element_by_id('taskName')
        self.assertEqual(taskNameBox.text,'Test problem')

        outputBox = self.browser.find_element_by_id('interpretfield')
        self.assertIn('Yes',outputBox.text)
        self.assertIn('TEST 2',outputBox.text)
