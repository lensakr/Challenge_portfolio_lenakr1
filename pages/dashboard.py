from pages.base_page import BasePage


class Dashboard(BasePage):
    login_button_xpath="//*[@id='login']"
    password_button_xpath="//*[@id='password]"
    remind_password_xpath="//*[@id='_net']/form/div/div[1]/a"
    MuiCardContent_root_xpath="//*[text()=""]"
    Sign_in_xpath="//*[@id="__next"]/form/div/div[2]/button/span[1]"
    MuiCardActions_xpath="//*[@id="__next"]/form/div/div[2]"

