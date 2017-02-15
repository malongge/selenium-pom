from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common import action_chains, keys


# This is the base page which defines attributes and methods that all other pages will share


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

        self.driver.implicitly_wait(5)
        self.timeout = 30


# This class represents the login page which defines attributes and methods associated with the login page


class LoginPage(BasePage):
    email = (By.CSS_SELECTOR, "#hder_login_form_new > input[name='name']")
    password = (By.CSS_SELECTOR, "#hder_login_form_new > input[name='password']")
    loginError = (By.ID, 'jy_alert_content')
    submitButton = (By.CSS_SELECTOR, "button.btn_login.sprite")

    def set_email(self, email):
        emailElement = self.driver.find_element(*LoginPage.email)
        emailElement.send_keys(email)

    def login_error_displayed(self):
        notifcationElement = self.driver.find_element(*LoginPage.loginError)
        return notifcationElement.is_displayed()

    def set_password(self, password):
        pwordElement = self.driver.find_element(*LoginPage.password)
        pwordElement.send_keys(password)

    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPage.submitButton)
        submitBttn.click()

    def login(self, email, password):
        self.set_password(password)
        self.set_email(email)
        self.click_submit()


import unittest
import time


class loginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.jiayuan.com/')

        # self.driver.find_element_by_tag_name('body').send_keys(keys.F12)
        # self.driver.execute_script("document.getElementsByTagName('body')[0].click()")

    def tearDown(self):
        self.driver.close()

    def test_login_incorrect_password(self):
        login_page = LoginPage(self.driver)
        login_page.login('test@email.com', 'password123')
        assert login_page.login_error_displayed()

    def test_login_incorrect_email(self):
        login_page = LoginPage(self.driver)
        login_page.login('test123@email.com', 'password')
        assert login_page.login_error_displayed()

    def test_login_blank_password(self):
        login_page = LoginPage(self.driver)
        login_page.login('test@email.com', '')
        assert login_page.login_error_displayed()

    def test_login_blank_email(self):
        login_page = LoginPage(self.driver)
        login_page.login('', 'password')
        assert login_page.login_error_displayed()
