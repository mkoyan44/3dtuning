import json,subprocess,os,sys
from jsmin import jsmin

import getSrc
with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"defination.json")), "r") as f:
    obj = json.loads(f.read())

if getSrc.getSeleniumSrv():
    cmd_t = ('java -jar {fileName} -port 4444')
    cmd = cmd_t.format(fileName=os.path.join(os.path.dirname(__file__),'selenium-server-standalone-3.11.0.jar')) 
    pSRV = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            shell=True
                           )
    
        
if obj[0]["platform"] == 'MAC':
    getSrc.getOSXsrc()
    

num_of_tests = len(obj)
for rep in range(1,11):

    for counter in range(num_of_tests):
        cmd_template = (
                'python osx.py --page_url {page_url} --test_id={test_id} --nb_repeat={nb_repeat}'
            )

        cmd = cmd_template.format(
                                  page_url="'http://www.3dtuning.com/en-US/tuning/range.rover/evoque.3.door/crossover.2012'",
                                  test_id=counter,
                                  nb_repeat=rep
                                  )
        p = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               shell=True
                               )
        p.wait()
        with open('report.log','a') as f:
            for line in p.stdout:
                sys.stdout.write(line)
                f.write(line)

        stdout_data, stderr_data = p.communicate()
        print(stdout_data)
