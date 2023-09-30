import json
import uuid

runFile = 'deadpool_encounter.json'
pack_code = 'deadpool'

with open('./packs.json') as json_file:
    pack_data = json.load(json_file)
    updated_data = pack_data.copy()
    for item in updated_data:
        if item['code'] == pack_code:
            try:
                if 'octgn_id' not in item.keys():
                    item['octgn_id'] = str(uuid.uuid4())
                    pack_octgn_id = str(item['octgn_id'])[0:30]
                    pack_id = str('00' + str(item['cgdb_id']))[-3:]
                else:
                    pack_octgn_id = str(item['octgn_id'])[0:30]
                    pack_id = str('00' + str(item['cgdb_id']))[-3:]
            except KeyError:
                print("An exception occurred: " + item['code'])

with open('./packs.json', 'w') as outfile:
    json.dump(updated_data, outfile, indent='\t', sort_keys=True)


with open('./pack/' + runFile) as json_file:
    data = json.load(json_file)
    updated_data = data.copy()
    for item in updated_data:
        try:
            if 'duplicate_of' not in item.keys():
                item['octgn_id'] = pack_octgn_id + pack_id + str('00' + str(item['position']))[-3:]
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
        
