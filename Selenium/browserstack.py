import argparse
import jsmin

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import time, json,os,sys


def getBrowserStackDefination():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"cases.json")), "r") as f:
        obj = json.loads(jsmin.jsmin(f.read()))
    return obj

def load_page(page_url, remote_hub,test_id,nb_repeat):

    local_caps = {}
    local_caps["browserstack.debug"] = False
    local_caps["browserstack.networkLogs"] = False
    local_caps["browserstack.local"] = False
    caps = local_caps.copy()
    caps.update(getBrowserStackDefination()[int(test_id)])


    # Sample selenium test
    driver = webdriver.Remote(
        command_executor=remote_hub,
        desired_capabilities=caps
    )
    start_clock = int(time.time())

    driver.get(page_url)
    wait = WebDriverWait(driver, 50)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'callenge-body')]")))

    end_clock = int(time.time())
    elapsed_seconds = end_clock - start_clock
    print(
        "nb_Repeat:{},duration:{},os:{},os_version:{},browser:{},browser_version:{}".format(
                nb_repeat,
                elapsed_seconds,
                caps['os'],
                caps['os_version'],
                caps['browser'],
                caps['browser_version']
        )
    )

    driver.close()
    driver.quit()

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
                            '--remote_hub',
                            required=True,
                            help="URL for the web page to test",
                            type=str
                        )


    parser.add_argument(
                            '--test_id',
                            required=False,
                            default=0,
                            help="id of json test ",
                            type=int
    )


    parser.add_argument(
                            '--nb_repeat',
                            required=False,
                            default=1,
                            help="id of json test ",
                            type=int
    )


    l = parser.parse_args()

    page_url = l.page_url
    remote_hub = l.remote_hub
    test_id = l.test_id
    nb_repeat = l.nb_repeat


    is_ok = load_page(page_url,remote_hub,test_id,nb_repeat)

    if is_ok is False:
        sys.exit(1)