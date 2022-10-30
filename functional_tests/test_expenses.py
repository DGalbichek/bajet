import time

from django.test import LiveServerTestCase
from selenium import webdriver


class NewExpenseTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def test_can_add_expense_and_see_it_on_recents_list(self):
        self.browser.get(self.live_server_url)

        # notice 'Expenses Home' in title and header
        self.assertIn('Expenses Home', self.browser.title)
        header_text = self.browser.find_element('tag name', 'h1').text
        self.assertIn('Expenses Home', header_text)

        # type name of expense "Grocery shopping"
        name_inputbox = self.browser.find_element('id', 'id_name')
        self.assertEqual(name_inputbox.get_attribute('placeholder'), 'Enter new expense')
        name_inputbox.send_keys('Grocery shopping')

        # type total paid and hit 'Add'
        amount_inputbox = self.browser.find_element('id', 'id_amount')
        amount_inputbox.send_keys('12.34')
        self.browser.find_element('id', 'id_new_expense_add').click()

        # recently added expenses now lists "Grocery shopping"
        time.sleep(1)
        table = self.browser.find_element('id', 'id_recent_expenses_table')
        rows = table.find_elements('tag name', 'tr')
        self.assertTrue(
            any('Grocery shopping' in row.text for row in rows),
            'New expense did not appear on recents list'
        )

        # quick form reset to blank
        name_inputbox = self.browser.find_element('id', 'id_name')
        self.assertEqual(name_inputbox.get_attribute('value'), '')
        amount_inputbox = self.browser.find_element('id', 'id_amount')
        self.assertEqual(amount_inputbox.get_attribute('value'), '')
