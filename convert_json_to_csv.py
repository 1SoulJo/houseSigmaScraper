import json
import csv

src_file = 'data_2021.json'
dst_file = 'data_2021.csv'
csv_head = [
    'house_type_name', 'house_type', 'house_style', 'com_name', 'muni_name',
    'bedroom', 'bedroom_plus', 'washroom', 'parking', 'price',
    'price_sold', 'area', 'date_start', 'date_end', 'list_days',
    'score_school', 'score_rent', 'score_growth', 'sold_month'
]

with open(src_file, 'r') as f:
    d = json.load(f)

    with open(dst_file, 'w', newline='', encoding='utf-8') as f2:
        writer = csv.writer(f2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(csv_head)
        for i in d:
            writer.writerow([i['house_type_name'],
                             i['house_type'],
                             i['house_style'],
                             i['community_name'],
                             i['municipality_name'],
                             i['bedroom'],
                             i['bedroom_plus'],
                             i['washroom'],
                             i['parking']['total'],
                             i['price_int'],
                             i['price_sold_int'],
                             i['house_area']['estimate'],
                             i['date_start'],
                             i['date_end'],
                             i['list_days'],
                             i['scores']['school'],
                             i['scores']['rent'],
                             i['scores']['growth'],
                             i['sold_month']
                             ])
    print('done')
