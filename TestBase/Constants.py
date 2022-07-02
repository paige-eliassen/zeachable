# Constant Data / Test Data

# if this weren't a takehome assessment I would build a test base and this url would be an environment variable
SIGNUP_URL = 'https://takehome.zeachable.com/sign_up'
EMAIL_PREFIX = 'johnsmith'
EMAIL_SUFFIX = '@gmail.com'

ERROR_MSG_MAP = {'01_invalid_email': 'Email is Invalid',
                     '02_existing_email': 'Email is already in use. Please log in to your account.',
                     '03_invalid_password_too_short': 'Please fill in all the fields.',
                     '04_missing_full_name': 'Please fill in all the fields.',
                     '05_missing_password': 'Please fill in all the fields.',
                     '06_missing_email': 'Please fill in all the fields.',
                     '07_missing_all_fields': 'Please fill in all the fields.',
                     '10_click_out_empty_full_name': 'This field is required',
                     '11_click_out_empty_email': 'This field is required',
                     '12_click_out_empty_password': 'This field is required'
                     }

TEST_01_ENROLLMENT = [['01_invalid_email', 'John Smith', 'johnsmith123', 'johnsm'],
                           ['02_existing_email', 'John Smith', 'johnsmith123@gmail.com', 'johnsm'],
                           ['03_invalid_password_too_short', 'John Smith', '', 'j'],
                           ['04_missing_full_name', '', '', 'johnsm'],
                           ['05_missing_password', 'John Smith', '', ''],
                           ['06_missing_email', 'John Smith', '', 'johnsm'],
                           ['07_missing_all_fields', '', '', '']]

TEST_02_ENROLLMENT = [['08_happy_path_marketing_emails', 'John Smith', 'johnsm'],
                      ['09_happy_path_no_marketing_emails', 'John Smith', 'johnsm']]

TEST_03_ENROLLMENT = [['10_click_out_empty_full_name', 'full name'],
                      ['11_click_out_empty_email', 'email'],
                      ['12_click_out_empty_password', 'password']]

TEST_04_ENROLLMENT = [['13_enroll_new_user', 'John Smith', 'qwerty', 'Thanks for enrolling in this course!']]

TEST_05_ENROLLMENT = [['14_enrollment_user_enrolled_in_other_course', 'John Smith', 'qwerty',
                       'Thanks for enrolling in this course!', 'Welcome to this Awesome Test']]