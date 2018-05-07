import sys, argparse, json,os
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def get_chrome_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')

def clear_chrome_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_chrome_clear_browsing_button())

    # click the button to clear the cache
    get_chrome_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_chrome_clear_browsing_button)


profile = FirefoxProfile()
profile.set_preference('browser.cache.disk.enable', False)
profile.set_preference('browser.cache.memory.enable', False)
profile.set_preference('browser.cache.offline.enable', False)
profile.set_preference('network.cookie.cookieBehavior', 2)

driver = webdriver.Remote(
                                  command_executor = 'http://127.0.0.1:4444/wd/hub',
                                  desired_capabilities = DesiredCapabilities.FIREFOX
                            )

# Cleanup cache
driver.delete_all_cookies()

start_clock = int(time.time())

# load page
driver.get("http://www.3dtuning.com/en-US/tuning/ascari/kz1r/coupe.2005")

end_clock = int(time.time())
elapsed_seconds = end_clock - start_clock

print(elapsed_seconds)


