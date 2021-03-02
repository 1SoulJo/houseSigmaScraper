import json
import requests
from req_data import REQ

# Parameters
year = '2017'
initial_zoom = 14
all_ids = []
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = 'https://housesigma.com/bkv2/api/search/mapsearchv2/listing2'
headers = {'content-type': 'application/json',
           'User-Agent': user_agent}


def getCluster(zoom, req=REQ, recursive=False):
    req['zoom'] = zoom
    req['sold_days'] = 'Y{}'.format(year)
    r = requests.post(url, data=json.dumps(req), headers=headers)
    data = json.loads(r.content)
    ret = data['data']['list']

    if zoom == initial_zoom:
        item_cnt = 0
        for c in ret:
            item_cnt += c['count']
        print('Total listing items : {}'.format(item_cnt))

    print('Scanning - lat : {} long : {} - lat : {} long {}'
          .format(req['lat1'], req['lon1'], req['lat2'], req['lon2']))

    if recursive and zoom < 18:
        lat_m = (req['lat1'] + req['lat2']) / 2
        lon_m = (req['lon1'] + req['lon2']) / 2
        r1 = req.copy()
        r1['lat2'] = lat_m
        r1['lon2'] = lon_m
        r2 = req.copy()
        r2['lon1'] = lon_m
        r2['lat2'] = lat_m
        r3 = req.copy()
        r3['lat1'] = lat_m
        r3['lon2'] = lon_m
        r4 = req.copy()
        r4['lat1'] = lat_m
        r4['lon1'] = lon_m
        ret += getCluster(zoom + 2, req=r1, recursive=True)
        ret += getCluster(zoom + 2, req=r2, recursive=True)
        ret += getCluster(zoom + 2, req=r3, recursive=True)
        ret += getCluster(zoom + 2, req=r4, recursive=True)

    return ret


def main():
    clusters = getCluster(initial_zoom, recursive=True)
    for c in clusters:
        for i in c['ids']:
            if i not in all_ids:
                all_ids.append(i)
    print('all ids : {}'.format(len(all_ids)))
    with open('listing_ids_{}.txt'.format(year), 'w') as f:
        for item_id in all_ids:
            f.write('{}\n'.format(item_id))


if __name__ == '__main__':
    main()

