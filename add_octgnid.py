import json
import uuid

runFile = 'qsv_encounter.json'

with open('./pack/' + runFile) as json_file:
    data = json.load(json_file)
    updated_data = data.copy()
    for item in updated_data:
        try:
            if 'octgn_id' not in item.keys():
                item['octgn_id'] = str(uuid.uuid4())
        except KeyError:
            print("An exception occurred: " + item['name'])

    for item in updated_data:
        try:
            if len(item['code']) > 5 and str(item['code'])[4:5] != 'a':
                for items in updated_data:
                    if items['code'] == str(item['code'])[0:5] + 'a':
                        item['octgn_id'] = items['octgn_id']
        except KeyError:
            print("An exception occurred: " + item['name'])


with open('./pack/' + runFile, 'w') as outfile:
    json.dump(updated_data, outfile, indent=4, sort_keys=True)
        