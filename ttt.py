# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.facebook.com/login/identify?ctx=recover&lwv=120&lwc=1348028&ars=facebook_login")
    wd.get("https://www.facebook.com/")
    wd.find_element_by_id("email").click()
    wd.find_element_by_id("email").clear()
    wd.find_element_by_id("email").send_keys("wefergeagwergw")
    wd.find_element_by_id("pass").click()
    wd.find_element_by_id("pass").clear()
    wd.find_element_by_id("pass").send_keys("ergergreg")
    wd.find_element_by_id("u_0_2").click()
    wd.find_element_by_id("email_container").click()
    wd.find_element_by_xpath("//div[@id='loginform']/div[2]").click()
    wd.find_element_by_id("pass").click()
    wd.find_element_by_id("pass").clear()
    wd.find_element_by_id("pass").send_keys("sdaegverserg")
    wd.find_element_by_id("loginbutton").click()
    wd.find_element_by_link_text("Recover Your Account").click()
    wd.find_element_by_id("identify_email").click()
    wd.find_element_by_id("identify_email").clear()
    wd.find_element_by_id("identify_email").send_keys("sdavgaerdgsverg")
    wd.find_element_by_id("did_submit").click()
    wd.find_element_by_id("u_0_2").click()
    wd.find_element_by_link_text("Cancel").click()
    wd.find_element_by_link_text("Facebook").click()
    wd.find_element_by_link_text("Forgot account?").click()
    wd.find_element_by_link_text("Cancel").click()
    ActionChains(wd).double_click(wd.find_element_by_css_selector("div.clearfix.loggedout_menubar")).perform()
    wd.find_element_by_link_text("Facebook").click()
    wd.find_element_by_id("u_0_c").click()
    wd.find_element_by_id("u_0_c").clear()
    wd.find_element_by_id("u_0_c").send_keys("ergasegvrdzvdfv")
    wd.find_element_by_id("u_0_e").click()
    wd.find_element_by_id("u_0_e").clear()
    wd.find_element_by_id("u_0_e").send_keys("sdafergsegr")
    wd.find_element_by_id("u_0_h").click()
    wd.find_element_by_id("u_0_h").clear()
    wd.find_element_by_id("u_0_h").send_keys("eargerg")
    wd.find_element_by_id("u_0_h").click()
    wd.find_element_by_id("u_0_h").clear()
    wd.find_element_by_id("u_0_h").send_keys("eargergsergesdvegrfg")
    wd.find_element_by_id("u_0_o").click()
    wd.find_element_by_id("u_0_o").send_keys("\\65")
    wd.find_element_by_id("u_0_o").click()
    wd.find_element_by_id("u_0_o").clear()
    wd.find_element_by_id("u_0_o").send_keys("eragsdfgeragergesd")
    wd.find_element_by_id("u_0_o").click()
    wd.find_element_by_id("u_0_o").clear()
    wd.find_element_by_id("u_0_o").send_keys("eragsdfgeragergesdregsveragerg")
    wd.find_element_by_css_selector("label._58mt").click()
    if not wd.find_element_by_id("u_0_9").is_selected():
        wd.find_element_by_id("u_0_9").click()
    wd.find_element_by_id("u_0_u").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
