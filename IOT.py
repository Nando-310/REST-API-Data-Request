import requests
import json
from unittest import result


def avgRotorSpeed(statusQuery, parentId):
    result = requests.get(f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}').json()
    pages = result['total_pages']
    runRotors = []
    for page in range(1, pages + 1):
        request = requests.get(f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={page}').json()
        data = request['data']
        for item in data:
            try:
                parents = item['parent']
                if parents is None:
                    continue
                parents_id = parents['id']
                rotorSpeed = item['operatingParams']['rotorSpeed']
                if parents_id == parentId:
                    runRotors.append(rotorSpeed)
            except KeyError:
                pass
    if runRotors:
        return sum(runRotors) // len(runRotors)
    return 0



avgRotorSpeed('RUNNING', 7)

