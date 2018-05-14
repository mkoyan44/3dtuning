import json, subprocess, os, sys
from jsmin import jsmin

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "cases.json")), "r") as f:
    obj = json.loads(jsmin(f.read()))

num_of_tests = len(obj)
for rep in range(6, 11):
    for counter in range(num_of_tests):

        cmd_template = (
            'python browserstack.py --page_url {page_url} --remote_hub {remote_hub} --test_id={test_id} --nb_repeat={nb_repeat}'
        )

        cmd = cmd_template.format(
            page_url="'http://www.3dtuning.com/en-US/tuning/range.rover/evoque.3.door/crossover.2012'",
            remote_hub="'http://surensargsyab1:ZDfpTUmpi5nEYS1rNC1n@hub.browserstack.com:80/wd/hub'",
            test_id=counter,
            nb_repeat=rep
        )
        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             shell=True
                             )
        p.wait()
        with open('report.log', 'a') as f:
            for line in p.stdout:
                sys.stdout.write(line)
                f.write(line)

        stdout_data, stderr_data = p.communicate()
        print(stdout_data)
