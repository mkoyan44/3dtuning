from selenium import webdriver
import time, json

json_name = "defination.json"
with open(json_name, "r") as f:
    obj = json.loads(f.read())
instance_caps= obj[int(0)]


# Mention any other capabilities required in the test
caps = instance_caps


# Sample selenium test
driver = webdriver.Remote(
    command_executor='http://surensargsyab1:ZDfpTUmpi5nEYS1rNC1n@hub.browserstack.com:80/wd/hub',
    desired_capabilities=caps
)
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)
start_clock = int(time.time())
driver.get("http://www.3dtuning.com/en-US/tuning/range.rover/evoque.3.door/crossover.2012")
end_clock = int(time.time())
elapsed_seconds = end_clock - start_clock
print(
    "{} {} {} {} {}".format(elapsed_seconds, caps['os'], caps['os_version'], caps['browser'], caps['version'])
)
driver.close()
driver.quit()

