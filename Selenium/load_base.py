import sys, argparse, json,os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def getBrowserStackDefination():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"defination.json")), "r") as f:
        obj = json.loads(f.read())
    return obj

def load_page(page_url, remote_server):

    is_ok = True

    if is_browserstack is True:
        local_caps = {}
        local_caps["browserstack.debug"] = False
        local_caps["browserstack.networkLogs"] = False
        local_caps["browserstack.local"] = False
        caps = local_caps.copy()
        caps.update(getBrowserStackDefination()[int(test_id)])

    else:
        caps = DesiredCapabilities.CHROME

    driver = webdriver.Remote(
                                  command_executor = remote_server,
                                  desired_capabilities = caps
                            )
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    try:
        start_clock = int(time.time())
        driver.get(page_url)
        end_clock = int(time.time())
        elapsed_seconds = end_clock - start_clock
        print(
            "{} {} {} {} {}".format(elapsed_seconds, caps['os'], caps['os_version'], caps['browser'], caps['version'])
        )
        driver.close()
        driver.quit()

    except Exception as e:
        print("ERROR: get exception: %s" % (e))

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
                            '--test_id',
                            required=False,
                            default=0,
                            help="id of json test ",
                            type=int
    )

    parser.add_argument('--is_browserstack', required=False,
                        default=False,
                        help="Exec with browserstack",
                        type=str2bool
                        )

    l = parser.parse_args()

    page_url = l.page_url
    remote_server = l.remote_server
    test_id = l.test_id
    is_browserstack = l.is_browserstack

    # Run page loading test
    is_ok = load_page(page_url, remote_server)

    if is_ok is False:
        sys.exit(1)