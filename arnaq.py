#!/usr/bin/env python3

import requests
import json
import time
import os

arn_url = os.getenv('ARN_URL') # 'https://www.swedavia.se/services/queuetimes/v2/airport/en/ARN/false'
vm_url = os.getenv('VM_URL') # 'http://localhost:8428/api/v1/import'
r = requests.get(arn_url)
data = r.json()

now = int(str(int(time.time())) + "000")
for queue in data['QueueTimesList']:
    #print(now + ';' + str(queue['Id']) + ';' +  queue['LongId'] + ';' + str(queue['CurrentProjectedQueueTime']) + ';' + queue['Interval'] + ';' + str(queue['Overflow']))
    #2023-06-02T15:13:32.344848;10;Security Arlanda Terminal 5 B;960;at least 25 min;True
    queue_id = queue['Id']
    queue_time = queue['CurrentProjectedQueueTime']
    queue_overflow = int(queue['Overflow'])
    post_data = {
        "metric": {
            "__name__": f"arnaq_{queue_id}",
            "job": "arnaq",
            "overflow": queue_overflow,
        },
        "values": [queue_time],
        "timestamps": [now],
    }
    r = requests.post(vm_url, json=post_data)
    print(r.status_code)


