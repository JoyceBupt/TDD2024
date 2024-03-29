from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention "to-do" lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        # She types "Buy flowers" into a text box
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy flowers" as an item in a to-do list
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Buy flowers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了"Give a gift to Lisi"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy flowers', [row.text for row in rows])
        self.assertIn('2: Give a gift to Lisi', [row.text for row in rows])

        self.fail('Finish the test!')


if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
