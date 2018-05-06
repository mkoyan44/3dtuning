import json,subprocess,os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"defination.json")), "r") as f:
    obj = json.loads(f.read())

num_of_tests = len(obj)
process = []
for counter in range(num_of_tests):
    cmd_template = (
        'python load_base.py --page_url {page_url} --remote_server {remote_server} --is_browserstack={is_browserstack} --test_id={test_id}'
        )

    cmd = cmd_template.format(
                              page_url="'http://www.3dtuning.com/en-US/tuning/range.rover/evoque.3.door/crossover.2012'",
                              remote_server="'http://surensargsyab1:ZDfpTUmpi5nEYS1rNC1n@hub.browserstack.com:80/wd/hub'",
                              is_browserstack=True,
                              test_id=counter
                              )
    process.append(subprocess.Popen(cmd, shell=True))

for counter in range(num_of_tests):
    process[counter].wait()
