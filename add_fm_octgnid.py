import sys
import json
import uuid
import os
import argparse

# -------------------------------
# Explications :
# --packcode permet de choisir dynamiquement le code du pack à traiter.
# Le script ajoute les octgn_id dans packs_fanmade.json, puis dans les fichiers
# {pack_code}.json et {pack_code}_encounter.json du dossier ./pack/
# Les traces affichent chaque étape et chaque ajout d'octgn_id.
# -------------------------------

# Ajout de l'argument --packcode pour spécifier le code du pack à traiter
parser = argparse.ArgumentParser(description="Ajoute les octgn_id aux fichiers d'un pack fanmade Marvel Champions.")
parser.add_argument('--packcode', type=str, required=True, help="Code du pack à traiter (ex: snowbird_by_hax)")
args = parser.parse_args()

# Vérifie la présence de l'argument --packcode
if not args.packcode:
    print("Erreur : l'argument --packcode est obligatoire. Exemple : --packcode snowbird_by_hax")
    sys.exit(1)

# Le code du pack est maintenant passé en argument
pack_code = args.packcode
pack_file = f'{pack_code}.json'
pack_encounter_file = f'{pack_code}_encounter.json'  # fichier encounter associé


def update_cards_file(file_path, pack_octgn_id, pack_id):
    """Met à jour les octgn_id dans un fichier de cartes et écrit le résultat."""
    if not os.path.exists(file_path):
        print(f"Fichier {file_path} non trouvé, passage au suivant.")  # TRACE
        return
    print(f"Ouverture du fichier {file_path}")  # TRACE
    with open(file_path, encoding="utf-8") as json_file:
        data = json.load(json_file)
        updated_data = data.copy()
        for item in updated_data:
            try:
                if 'duplicate_of' not in item.keys():
                    item['octgn_id'] = pack_octgn_id + pack_id + str('00' + str(item['position']))[-3:]
                    print(f"Ajout octgn_id {item['octgn_id']} à la carte {item.get('name', item.get('code', '???'))}")  # TRACE
            except KeyError:
                print("An exception occurred: " + item.get('name', item.get('code', '???')))
        for item in updated_data:
            try:
                if len(item['code']) > 5 and str(item['code'])[4:5] != 'a':
                    for items in updated_data:
                        if items['code'] == str(item['code'])[0:5] + 'a':
                            item['octgn_id'] = items['octgn_id']
                            print(f"Copie octgn_id {items['octgn_id']} de {items.get('name', items.get('code', '???'))} vers {item.get('name', item.get('code', '???'))}")  # TRACE
            except KeyError:
                print("An exception occurred: " + item.get('name', item.get('code', '???')))
    print(f"Écriture du fichier {file_path}")  # TRACE
    with open(file_path, 'w', encoding="utf-8") as outfile:
        json.dump(updated_data, outfile, indent=4, sort_keys=True)


print(f"Ouverture du fichier packs_fanmade.json")  # TRACE
with open('./packs_fanmade.json', encoding="utf-8") as json_file:
    pack_data = json.load(json_file)
    updated_data = pack_data.copy()
    for item in updated_data:
        if item['code'] == pack_code:
            try:
                if 'octgn_id' not in item.keys():
                    item['octgn_id'] = str(uuid.uuid4())
                    print(f"Ajout octgn_id {item['octgn_id']} au pack {item['code']}")  # TRACE
                    pack_octgn_id = str(item['octgn_id'])[0:30]
                    pack_id = str('00' + str(item['cgdb_id']))[-3:]
                else:
                    pack_octgn_id = str(item['octgn_id'])[0:30]
                    pack_id = str('00' + str(item['cgdb_id']))[-3:]
            except KeyError:
                print("An exception occurred: " + item['code'])

print(f"Écriture du fichier packs_fanmade.json")  # TRACE
with open('./packs_fanmade.json', 'w', encoding="utf-8") as outfile:
    json.dump(updated_data, outfile, indent='\t', sort_keys=True)

# Mise à jour des deux fichiers de cartes associés au pack
update_cards_file(f'./pack/{pack_file}', pack_octgn_id, pack_id)
update_cards_file(f'./pack/{pack_encounter_file}', pack_octgn_id, pack_id)


