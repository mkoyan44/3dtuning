import os
import numpy as np
import scipy as sp
import scipy.stats
import operator


def init_splitString(string):
    split  =  string.split(',')
    nb_repeat = split[0].split(':')[1]
    duration = split[1].split(':')[1]
    os_b = split[2].split(':')[1]
    os_version = split[3].split(':')[1]
    browser = split[4].split(':')[1]
    browser_version = split[5].split(':')[1]
    return nb_repeat,duration,os_b,os_version,browser,browser_version

def com_splitString(string):
    split  =  string.split(',')
    nb_repeat = split[0]
    duration = split[1]
    os_b = split[2]
    os_version = split[3]
    browser = split[4]
    browser_version = split[5]
    return nb_repeat,duration,os_b,os_version,browser,browser_version

def getDuration():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "report.log")), "r") as f:
        content  = f.read().splitlines()
        glb_dict = {}
        for line in content:
            data_dict = {}
            data_list = []
            tmp_nb_repeat, tmp_duration, tmp_os_b, tmp_os_version, tmp_browser , tmp_browser_version = init_splitString(line)
            for _line in content:
                nb_repeat, duration, os_b, os_version, browser, browser_version = init_splitString(_line)
                if tmp_os_b == os_b and tmp_browser == browser and tmp_browser_version == browser_version and tmp_os_version == os_version:
                    key = '{} {} {} {}'.format(
                        os_b,
                        os_version,
                        browser,
                        browser_version
                    )
                    data_list.append(duration)
                    data_dict[key] = data_list

            glb_dict.update(data_dict)
        return glb_dict

def mean_confidence_interval(data, confidence=0.95):
    data = [ int(i) for i in data ]
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    std = np.std(data)
    return m, m-h, m+h ,h, std

data = getDuration()
for k,v in data.items():
    m,m_h,m__h,h,std = mean_confidence_interval(v)
    out = 'Experiment:{}, avg:{}, avg-interval:{}, avg+interval:{}, interval:{} std:{} '.format(k,
                                                                                              round(m,2),
                                                                                              round(m_h,2),
                                                                                              round(m__h),
                                                                                              round(h,2),
                                                                                              round(std,2)
                                                                                       )

    with open('final-result.txt', 'a') as fs:
        fs.write(out + '\n')