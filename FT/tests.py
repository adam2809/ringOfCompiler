from django.test import LiveServerTestCase
from selenium import webdriver

class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()


    def testHomePage(self):
        initialURL = self.live_server_url;
        self.browser.get(self.live_server_url)

        self.assertEqual('Ring of Compiler',self.browser.title)


        startButton = self.browser.find_element_by_tag_name('button-start')
        self.assertEqual(startButton.text,'Start game')

        self.assertEqual(self.live_server_url,initialURL + '/game')
