import requests
import json
from unittest import result


def avgRotorSpeed(statusQuery, parentId):
    # Write your code here

    result = requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search?status=').json()
    #find the number of pages in the json data
    pages = result['total_pages']
    # create a list for the different rotor speeds found while iterating through the data
    runRotors = []
    #iterate through the pages of data with the statusQuery
    for page in range(1, pages + 1):
        request = requests.get(
            'https://jsonmock.hackerrank.com/api/iot_devices/search?status=' + statusQuery + '&page=' + str(
                page)).json()
        data = request['data']
        #pick up and print out the info for statusQuery and parentId in each page and append rotor speeds to runRotors
        for i in range(10):
            try:
                parents = data[i]['parent']['id']
                status = data[i]['status']
                rotorSpeed = data[i]['operatingParams']['rotorSpeed']


                if (parents == parentId):
                    print('parentId = ' + str(parents))
                    print('rotorSpeed = ' + str(rotorSpeed))
                    runRotors.append(rotorSpeed)
                    print(f'Running Rotors speeds: {runRotors}')
                    print(f'The Average rotor speed is:{sum(runRotors) // len(runRotors)}')
                #print 0 if there is not a match
                else:
                    print(0)
            except:
                pass
    return



avgRotorSpeed('RUNNING', 7)

