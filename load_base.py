import sys, argparse

from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait


def load_page(page_url, remote_server, max_load_seconds,is_clean):
    is_ok = True
    driver = webdriver.Remote(command_executor = remote_server,
                              desired_capabilities=DesiredCapabilities.CHROME)

    def get_clear_browsing_button(driver):
        """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
        return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')

    def clear_cache(driver, timeout=60):
        """Clear the cookies and cache for the ChromeDriver instance."""
        # navigate to the settings page
        driver.get('chrome://settings/clearBrowserData')

        # wait for the button to appear
        wait = WebDriverWait(driver, timeout)
        wait.until(get_clear_browsing_button)

        # click the button to clear the cache
        get_clear_browsing_button(driver).click()

        # wait for the button to be gone before returning
        wait.until_not(get_clear_browsing_button)

    try:

        if is_clean is True:
            # Cleanup cache
            driver.delete_all_cookies()
            clear_cache(driver)

        print("Open page: %s" % (page_url))
        page_url = "{}//{}:{}@{}".format(page_url.split('//')[0], 'mkoyan44', 'Class123456', page_url.split('//')[1])
        start_clock = int(time.time())


        # load page
        driver.get(page_url)

        end_clock = int(time.time())
        elapsed_seconds = end_clock - start_clock

        if elapsed_seconds > max_load_seconds:
            print("ERROR: page load is too slow. It took %s seconds, more than %d seconds." \
                  % ("{:.2f}".format(elapsed_seconds), max_load_seconds))
            is_ok = False

        else:
            print("Page load took: %s seconds." % ("{:.2f}".format(elapsed_seconds)))

        save_screenshot_filepath = "%s/%s-%s.png" % \
                                   ("/tmp", datetime.now().strftime('%Y-%m-%d_%H%M%S'),
                                    page_url.rstrip("/").split("/")[-1])

        driver.get_screenshot_as_file(save_screenshot_filepath)

    except Exception as e:
        print("ERROR: get exception: %s" % (e))
        is_ok = False
    finally:
        driver.close()
        # quit session
        driver.quit()

    return is_ok

if __name__ == '__main__':

    def str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    parser = argparse.ArgumentParser()

    parser.add_argument(
                            '--page_url',
                            required=True,
                            help="URL for the web page to test",
                            type=str
                        )

    parser.add_argument(
                            '--remote_server',
                            required=False,
                            default="http://127.0.0.1:4444/wd/hub",
                            help="Remote selenium server to run the test",
                            type=str
                        )

    parser.add_argument(
                            '--max_load_seconds',
                            required=False,
                            default=100,
                            help="If page load takes too long, quit the test",
                            type=int
                        )

    parser.add_argument('--is_clean', required=False,
                        default=False,
                        help="Exec with clean caches and cookes",
                        type=str2bool
                        )

    l = parser.parse_args()
    page_url = l.page_url
    remote_server = l.remote_server
    max_load_seconds = l.max_load_seconds
    is_clean = l.is_clean

    # Run page loading test
    is_ok = load_page(page_url, remote_server, max_load_seconds,is_clean)

    if is_ok is False:
        sys.exit(1)