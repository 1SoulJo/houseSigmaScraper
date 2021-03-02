import json
import requests
import sys

REQ = {
    'id_listing': [
    ],
    'lang': 'en_US',
    'province': 'ON'
}
year = '2017'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = 'https://housesigma.com/bkv2/api/listing/preview/many'
headers = {'content-type': 'application/json',
           'Authorization': 'Bearer 202101287q8vkio1djpj423g2d2lp04m6o',
           'User-Agent': user_agent}
result = []


def collect():
    with open('listing_ids_{}.txt'.format(year), 'r') as f1:
        d = f1.read().splitlines()

        global result
        if len(result) == 0:
            f = open('data_{}.json'.format(year))
            result = (json.load(f))

        for i, line in enumerate(d[len(result):], start=len(result)):
            REQ['id_listing'] = [line.rstrip()]
            try:
                r = requests.post(url, data=json.dumps(REQ), headers=headers)
                data = json.loads(r.content)
                result.append(data['data']['houseList'][0])
            except requests.ConnectionError:
                continue
            if i % 100 == 0:
                print('Collecting : {}'.format(i))
                with open('data_{}.json'.format(year), 'w') as f:
                    json.dump(result, f, indent=2)
    return


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     year = sys.argv[1]
    # collect()
    with open('data_2020.json', 'r') as f:
        d = json.load(f)
        print(len(d))
