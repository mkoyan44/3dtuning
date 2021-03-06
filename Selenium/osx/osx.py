# -*- coding: utf-8 -*-

from selenium import webdriver
import time, json,sys,argparse
import os,shutil,pwd,grp

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

uid = pwd.getpwnam("a.mkoyan").pw_uid
gid = grp.getgrnam("admin").gr_gid

def getBrowserStackDefination():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"defination.json")), "r") as f:
        obj = json.loads(f.read())
    return obj

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def changePermission(path,umask):
    for root, dirs, files in os.walk(path):
      for momo in dirs:
        os.chmod(os.path.join(root, momo), umask)
      for momo in files:
        os.chmod(os.path.join(root, momo), umask)

def changeOwnership(path,uid,gid):
    for root, dirs, files in os.walk(path):
      for momo in dirs:
        os.chown(os.path.join(root, momo), uid, gid)
      for momo in files:
        os.chown(os.path.join(root, momo), uid, gid)

def load_page(page_url):
    driver = webdriver
    obj = getBrowserStackDefination()[int(test_id)]
    if obj["platform"] == "MAC" and obj["browserName"] == 'chrome':
        if os.path.exists('/Applications/Google Chrome.app/'):
            shutil.rmtree('/Applications/Google Chrome.app/')
        cwd = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        brPath = '{}/osx-chrome-releases/{}'.format(cwd,obj["version"])
        print(brPath)
        copytree(brPath,'/Applications/')
        changePermission('/Applications/Google Chrome.app',755)
        driver = webdriver.Chrome(executable_path='/Applications/Google Chrome.app/Contents/MacOS/chromedriver')

    elif obj["platform"] == "MAC" and obj["browserName"] == 'firefox':
        if os.path.exists('/Applications/Firefox.app/'):
            shutil.rmtree('/Applications/Firefox.app/')
        cwd = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        brPath = '{}/osx-firefox-releases/{}'.format(cwd,obj["version"])
        copytree(brPath,'/Applications/')

        #sys.path.append('/Applications/Firefox.app/Contents/MacOS/')

        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        caps = firefox_capabilities.copy()
        caps.update(getBrowserStackDefination()[int(test_id)])


        driver = webdriver.Firefox(
                                    firefox_binary='/Applications/Firefox.app/Contents/MacOS/firefox',
                                    executable_path='/Applications/Firefox.app/Contents/MacOS/geckodriver',
                                    capabilities=caps

        )

    start_clock = int(time.time())
    driver.get(page_url)

    wait = WebDriverWait(driver, 50)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'callenge-body')]")))

    end_clock = int(time.time())
    elapsed_seconds = end_clock - start_clock
    print(
        "{} {} {} {} {} {}".format(nb_repeat,elapsed_seconds,obj["platform"], obj['os'], obj['browserName'], obj['version'])
    )
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
    test_id = l.test_id
    nb_repeat = l.nb_repeat

    # Run page loading test
    is_ok = load_page(page_url)

    if is_ok is False:
        sys.exit(1)