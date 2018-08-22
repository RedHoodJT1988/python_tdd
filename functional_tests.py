from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Bryan has learned about an awesome to-do list app. So he
    # goes to the homepage to see what it's all about.
    self.browser.get('http://localhost:8000')
    # He notices the page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title) 
    self.fail('Finish the test!')

    # He is invited to enter a to-do item straight away
    # He types "Buy Red Devil GPU" into the text box (Bryan's hobby
    # is gaming)

    # When he hits enter, the page updates, and now the page lists
    # "1: Buy Red Devil GPU" as an item in a to-do list

    # There is still a text box inviting him to add another item. He
    # enters "Await the arrival of GPU"

    # The page updates again, and now shows both items on his list.

    # Bryan wonders whether the site will remember his list. Then he sees
    # that the site has generated a unique URL for him -- there is some
    # explanatory text to that effect.

    # He visits the URL - his to-do list is still there.

    # Content he decides to call it a night.

if __name__ == '__main__':
  unittest.main(warnings='ignore')