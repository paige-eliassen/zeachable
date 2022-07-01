import pytest
import unittest
from parameterized import parameterized
from Utils.SeleniumUtil import SeleniumUtils
import logging
import TestBase.Constants as constants
from Features.Enrollment.Locators import Locators
from Features.Enrollment.Validators import Validators
from time import sleep
import random


class EnrollmentRegression(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.assrt = unittest.TestCase()
        self.locators = Locators()
        self.selenium = SeleniumUtils()
        self.selenium.go_to_url(constants.SIGNUP_URL)
        self.selenium.maximize_window()
        sleep(3)

    def fill_sign_up_form(self, full_name, email, password):
        self.selenium.fill_form(self.locators.full_name_field, str(full_name))
        self.selenium.fill_form(self.locators.email_field, str(email))
        self.selenium.fill_form(self.locators.password_field, str(password))
        self.selenium.click_element(self.locators.signup_button)

    def enroll_in_my_awesome_course(self):
        self.selenium.click_element(self.locators.my_awesome_course_link)
        self.selenium.click_element(self.locators.enroll_in_course_button)
        self.selenium.find_element(self.locators.continue_to_course_button)

    def enroll_in_take_home_course(self):
        self.selenium.click_element(self.locators.take_home_instructions)
        self.selenium.click_element(self.locators.enroll_in_course_button)
        self.selenium.find_element(self.locators.continue_to_course_button)

    def sign_up_and_enroll_in_my_awesome_course(self, pass_prefix, full_name):
        email = constants.EMAIL_PREFIX + str(random.randint(1, 100000)) + constants.EMAIL_SUFFIX
        password = pass_prefix + str(random.randint(1, 100000))
        self.fill_sign_up_form(full_name, email, password)
        self.enroll_in_my_awesome_course()

    def matching_profile_email(self, expected_email):
        self.selenium.click_element(self.locators.user_gravatar)
        self.selenium.click_element(self.locators.edit_profile_link)
        sleep(3)
        result = self.matching_string_in_page_source(expected_email)
        return result

    def matching_string_in_page_source(self, string):
        try:
            if string in self.selenium.get_page_source():
                return True
            else:
                return False
        except Exception as e:
            logging.debug("No match in page source:" + str(e))

    @parameterized.expand(constants.TEST_01_ENROLLMENT)
    def test_a_negative_cases_on_input_fields_singup(self, test_name, full_name, email, password):
        logging.debug("Executing test_a_negative_cases_on_input_fields_singup_" + test_name)
        try:
            if test_name == ('missing_full_name' or 'missing_password' or 'invalid_password_too_short'):
                email = constants.EMAIL_PREFIX + str(random.randint(1, 10000000)) + constants.EMAIL_SUFFIX
            self.fill_sign_up_form(full_name, email, password)
            sleep(5)
            expected_error_msg = constants.ERROR_MSG_MAP[test_name]
            page_source = self.selenium.get_page_source()
            result = Validators.validate_field_error_messages(expected_error_msg, page_source)
            if not result:
                pytest.fail("test_01_negative_use_cases_on_input_fields_enrollment_" + test_name + " has data failure")
        except Exception as e:
            pytest.fail(e)

    @parameterized.expand(constants.TEST_02_ENROLLMENT)
    def test_b_successful_sign_up(self, test_name, full_name, password):
        logging.debug("Executing test_b_successful_sign_up: " + test_name)
        try:
            email = constants.EMAIL_PREFIX + str(random.randint(1, 100000)) + constants.EMAIL_SUFFIX
            self.fill_sign_up_form(full_name, email, password)
            sleep(4)
            try:
                self.selenium.find_element(self.locators.resend_confirm_email_button)
            except Exception as e:
                pytest.fail(e)
            self.assrt.assertEquals(self.matching_string_in_page_source(constants.ERROR_MSG_MAP[email]), True)
        except Exception as e:
            logging.debug(str(e))

    @parameterized.expand(constants.TEST_03_ENROLLMENT)
    def test_c_click_out_empty_field_sign_up(self, test_name, field):
        logging.debug("Executing test_c_click_out_empty_field_sign_up: " + test_name)

        def actions(locator):
            self.selenium.click_element(locator)
            self.selenium.click_element(self.locators.sign_up_header)
        try:
            if field == 'full name':
                actions(self.locators.full_name_field)
            elif field == 'email':
                actions(self.locators.email_field)
            elif field == 'password':
                actions(self.locators.full_name_field)
            sleep(5)
            self.assrt.assertEquals(self.matching_string_in_page_source(constants.ERROR_MSG_MAP[test_name]), True)
        except Exception as e:
            logging.debug(e)

    @parameterized.expand(constants.TEST_04_ENROLLMENT)
    def test_d_successful_enrollment_new_user(self, test_name, full_name, pass_prefix, enrollment_complete_text):
        logging.debug("Executing test_d_successful_enrollment_new_user: " + test_name)
        try:
            self.sign_up_and_enroll_in_my_awesome_course(pass_prefix, full_name)
            result = self.matching_string_in_page_source(enrollment_complete_text)
            self.assrt.assertEquals(result, True)
        except Exception as e:
            logging.debug(str(e))

    @parameterized.expand(constants.TEST_05_ENROLLMENT)
    def test_e_successful_enrollment_user_enrolled_in_other_courses(self, test_name, full_name, pass_prefix,
                                                                     enrollment_complete_text_take_out,
                                                                     course_landing_page_text):
        logging.debug("Executing test_e_successful_enrollment_user_enrolled_in_other_courses: " + test_name)
        try:
            email = constants.EMAIL_PREFIX + str(random.randint(1, 100000)) + constants.EMAIL_SUFFIX
            password = pass_prefix + str(random.randint(1, 100000))
            self.fill_sign_up_form(full_name, email, password)
            self.enroll_in_take_home_course()
            res1 = self.matching_string_in_page_source(enrollment_complete_text_take_out)
            self.assrt.assertEquals(res1, True)
            self.selenium.go_to_url(constants.SIGNUP_URL)
            self.enroll_in_my_awesome_course()
            res2 = self.matching_string_in_page_source(course_landing_page_text)
            self.assrt.assertEquals(res2, True)
        except Exception as e:
            logging.debug(str(e))

    def tearDown(self) -> None:
        self.selenium.close()

    if __name__ == '__main__':
        unittest.main()
