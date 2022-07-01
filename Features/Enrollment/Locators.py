from selenium.webdriver.common.by import By


class Locators:
    # sign up page
    signup_page_link = By.XPATH, "//*[@id='lock-705']/div/div/div/a"
    email_field = By.CSS_SELECTOR, "#user_email"
    password_field = By.CSS_SELECTOR, '#password'
    signup_button = By.XPATH, "//input[@type='submit']"
    full_name_field = By.CSS_SELECTOR, '#user_name'
    agreement_check_box = By.ID, 'allow_marketing_emails'
    login_link = By.LINK_TEXT, 'Login'
    password_info = By.CLASS_NAME, '.tool-tip'
    sign_up_header = By.XPATH, '/html/body/main/div/h3'

    # sign up landing page
    resend_confirm_email_button = By.XPATH, "//button[@class='resend-confirmation-email-button']"
    user_gravatar = By.XPATH, "//img[@class='gravatar']"
    edit_profile_link = By.XPATH, '//*[@id="user-dropdown"]/li[1]/a'
    my_awesome_course_link = By.CLASS_NAME, '.course-box-image-container'
    enroll_in_course_button = By.XPATH, '//button[@name="button"]'
    continue_to_course_button = By.XPATH, '//*[@id="block-129630"]/center/a'
    take_home_instructions = By.CLASS_NAME, '.course-box-image'

