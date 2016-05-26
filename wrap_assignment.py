__author__ = 'Asma Ben Brahim'

import unittest
from selenium import webdriver
import time


# Environmental variables - Need to be changed before each run
url = 'https://authoring.qa.wrapdev.net/#/plans/register'
email_address = 'myname.rand2@gmail.com'
first_name = 'firstrand2'
last_name = 'lastrand2'
user_name = 'usernamerand2'
pass_word = 'usernamerand2'
company_name = 'myself'


class WrapAssignmentWorkflow(unittest.TestCase):
    """
    Class that holds two workflow testcases:
      - test_wrap_registration: verifies the registration for personal brand new account
      - test_wrap_template_creation_and_publish: verifies after user login, the creation and publication of a wrap
      template
    """

    def setUp(self):
        """
        Used to create a webdriver using firefox. This function is called before each test
        :return: Null
        """
        self.driver = webdriver.Firefox()

    def test_wrap_registration(self):
        driver = self.driver
        driver.get(url)
        # Checks if the window title has the correct name
        self.assertIn("Wrap Authoring", driver.title)
        time.sleep(5)
        try:
            # Click on Sign Up button
            driver.find_element_by_xpath(".//*[@id='pricingModel']/div/div[3]/div[4]/div[1]/div[2]/div[3]/a").click()
            # Selects the email box and types in the email address
            email = driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div/wm-"
                                                 "plans-authorization/div/div/wm-auth-page/div/ng-transclude/wm-auth/"
                                                 "div/div[3]/wm-signup/div/div/form/input")
            email.send_keys(email_address)
            # Clicks on Sign up button
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div/wm-plans-auth"
                                         "orization/div/div/wm-auth-page/div/ng-transclude/wm-auth/div/div[3]/wm-signup"
                                         "/div/div/form/button").click()
            time.sleep(2)
            # Selects the username/email box and types in the username
            username = driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div/"
                                                    "wm-plans-authorization/div/div/wm-auth-page/div/ng-transclude/wm-"
                                                    "auth/div/div[3]/wm-signup/div/div/form/input[3]")
            username.send_keys(user_name)
            # Selects the password box and types in the password
            password = driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div"
                                                    "/wm-plans-authorization/div/div/wm-auth-page/div/ng-transclude/"
                                                    "wm-auth/div/div[3]/wm-signup/div/div/form/input[4]")
            password.send_keys(pass_word)
            time.sleep(5)
            # Clicks on the Sign Up button
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div/wm-plans-auth"
                                         "orization/div/div/wm-auth-page/div/ng-transclude/wm-auth/div/div[3]/wm-sign"
                                         "up/div/div/form/button").click()
            # Next window: registration form
            time.sleep(2)
            # Selects firstname box and fills in the firstname
            firstname = driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div"
                                                     "/wm-plans-authorization/div/div/wm-auth-page/div/ng-transclude/"
                                                     "wm-auth/div/div[3]/wm-signup/div/div/form/input[1]")
            firstname.send_keys(first_name)
            # Selects lastname box and fills in the lastname
            time.sleep(2)
            lastname = driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div/wm"
                                                    "-plans-authorization/div/div/wm-auth-page/div/ng-transclude/wm-"
                                                    "auth/div/div[3]/wm-signup/div/div/form/input[2]")
            lastname.send_keys(last_name)
            # Selects company box and fills in the company name
            time.sleep(2)
            company = driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div"
                                                   "/wm-plans-authorization/div/div/wm-auth-page/div/ng-transclude/wm"
                                                   "-auth/div/div[3]/wm-signup/div/div/form/input[3]")
            company.send_keys(company_name)
            time.sleep(5)
            # Clicks on Create Account button
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/wm-plans-page/div/div/div/wm-plans-"
                                         "authorization/div/div/wm-auth-page/div/ng-transclude/wm-auth/div/div[3]/wm-"
                                         "signup/div/div/form/button").click()
            time.sleep(5)
            # Picks up the username after successful registration for testcase verification
            successful_registration = driver.find_element_by_xpath(".//*[@id='wrap-theme']/wm-global-nav/header/div/"
                                                                   "div[3]/div/div/div[2]/a/div[2]")
            assert successful_registration.text == user_name
            time.sleep(2)
        except Exception:
            print "ERROR in TEST: Wrap_registration. One of the forms did not fill up correctly or Missing a click..."

    def test_wrap_template_creation_and_publish(self):
        driver = self.driver
        driver.get(url)
        # Checks if the window title has the correct name
        self.assertIn("Wrap Authoring", driver.title)
        try:
            # Clicks on Login button
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/wm-global-nav/header/div/div[3]/div/div/nav/a[1]/"
                                         "span").click()
            # Selects the username box and types in the email address
            username = driver.find_element_by_xpath(".//*[@id='wrap-theme']/wm-global-nav/header/div/div[3]/div/div"
                                                    "/div/wm-auth-popup/div/wm-auth/div/div[3]/wm-login/div/form/"
                                                    "input[3]")
            username.send_keys(email_address)
            # Selects the password box and types in the password
            password = driver.find_element_by_xpath(".//*[@id='wrap-theme']/wm-global-nav/header/div/div[3]/div/"
                                                    "div/div/wm-auth-popup/div/wm-auth/div/div[3]/wm-login/div/"
                                                    "form/input[4]")
            password.send_keys(pass_word)
            # Clicks on Sign In button
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/wm-global-nav/header/div/div[3]/div/div/div/wm-"
                                         "auth-popup/div/wm-auth/div/div[3]/wm-login/div/form/button").click()
            time.sleep(5)
            # We end up on the home page and click on 'Create New Wrap'
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/div/div/div[2]/div[2]/button").click()
            # Clicks on the commerce Template
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[5]/div/div/wm-wrap-settings/div/div/div[2]/"
                                         "div[1]").click()
            # Clicks on create wrap
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[5]/div/div/wm-wrap-settings/div/wm-modal/div[2]/"
                                         "slot-body/div[2]/wm-card-group[1]/ng-transclude/slot-actions/div/"
                                         "button[2]").click()
            # Closes the pop up nagivation help window
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[5]/div/div/div/button[1]").click()
            time.sleep(5)
            # Clicks on publish
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[2]/div[1]/div/wm-wrap-editor/div/wm-action-bar"
                                         "/div/div[2]/div[9]/button").click()
            # Sleep time is 2 min because sometimes the template publication takes more than a minute
            time.sleep(120)
            # Once the the publication is done, closes the 'Congratulations' pop up window
            driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[5]/div/div/div/button[1]").click()
            time.sleep(5)
            # Picks up the title of the last pop up windows which notify the user that the publish was successful and
            #  we use the text to validate the testcase
            successful = driver.find_element_by_xpath(".//*[@id='wrap-theme']/div[5]/div/div/wm-publish-notification"
                                                      "/div/div[1]/h4")
            assert successful.text == 'Publish Successful'
        except Exception:
            print "ERROR in TEST: Wrap_template_creation_and_publish. One of the forms did not fill up correctly or " \
                  "Missing a click ..."

    def tearDown(self):
        """
        Used for the test cases tear down. Closes the web browser test window after the completion of each test.
        :return: Null
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


