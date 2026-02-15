import json
import uuid

runFile = 'hercules.json'
pack_code = 'hercules'

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
            print("An exception occurred: " + item['code'])

    for item1 in updated_data:
        try:
            if 'duplicate_of' not in item1.keys() and len(item1['code']) > 5 and str(item1['code'])[4:5] != 'a':
                for item2 in updated_data:
                    if item2['code'] == str(item1['code'])[0:5] + 'a':
                        item1['octgn_id'] = item2['octgn_id']
        except KeyError:
            print("An exception occurred: " + item1['code'])


with open('./pack/' + runFile, 'w') as outfile:
    json.dump(updated_data, outfile, indent=4, sort_keys=True)
        
