#!/bin/bash

for i in `seq 1 10`;do

    # os x 10.11.6, Chrome Version 66.0.3359.139
    # executed in remote mac with selenium service hosted at .206
    echo "os x 10.11.6, Chrome Version 66.0.3359.139"
    python load_base.py --page_url "http://www.3dtuning.com/en-US/tuning/ascari/kz1r/coupe.2005" \
                        --remote_server "http://192.168.1.206:4444/wd/hub" \
                        --is_clean=True
done
for i in `seq 1 10`;do

    echo "Windows 10 , Version 66.0.3359.139"
    # Windows 10 , Version 66.0.3359.139
    # executed in remote mac with selenium service hosted at .203
    python load_base.py --page_url "http://www.3dtuning.com/en-US/tuning/ascari/kz1r/coupe.2005" \
                        --remote_server "http://192.168.1.203:4444/wd/hub" \
                        --is_clean=True
done
