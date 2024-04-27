MarvelsDB cards JSON data
=========

The goal of this repository is to store marvelsdb card data in a format that can be easily updated by multiple people and their changes reviewed.

## Validating and Formatting JSON

Steps have been verified with Python 2.7.x and 3.7.x.

#### Set Up Python Environment

The validation script requires python package `jsonschema` which can be installed using `pip` via `pip install jsonschema`. It is recommended that you use a virtual environment, but this is strictly optional.

```bash
# use a virtual environment (optional)
virtualenv venv
source venv/bin/activate
pip install jsonschema
```

If you see an error like _"No module named jsonschema"_ when running the script, you have not installed the `jsonschema` package correctly.

#### Run the Validation Script

To check the JSON files:

```bash
./validate.py

# or for more detailed output, include the --verbose flag

./validate.py --verbose
```

To check and apply formatting to JSON files:

```bash
./validate.py --fix_formatting

# or for more detailed output, include the --verbose flag

./validate.py --verbose --fix_formatting
```


#### Pack schema

* **code** - identifier of the pack. The acronym of the pack name, with matching case, except for Core Set. Examples: `"Core"` for Core Set.
* **name** - properly formatted name of the pack. Examples: `"Core Set"`
* **position** - number of the pack within the cycle. Examples: `1` for Core Set
* **released** - date when the pack was officially released by FFG. When in doubt, look at the date of the pack release news on FFG's news page. Format of the date is YYYY-MM-DD. May be `null` - this value is used when the date is unknown. Examples: `"2016-10-08"` for Core Set
* **size** - number of different cards in the pack. May be `null` - this value is used when the pack is just an organizational entity, not a physical pack.  Examples: `120` for Core Set

#### Card schema

* **attack** - Character's attack value. Format is integer or `null`. Possible values:
  * `null`: Shows up as dash or star depending on if **attack_text** is defined
  * -1: Shows up as X
  * 0+: Shows up as the given integer
* **attack_cost** - Cost for the character to attack (commonly, the amount of consequential damage)
* **attack_text** - Ability text associated with the character's attack  
* **back_flavor** - The flavor text on the back of a card
* **back_text** - The text on the back of a card
* **base_threat** - The starting threat on a card. By default, it is per hero.
* **base_threat_fixed** - Whether the **base_threat** is fixed and not per hero
* **boost** - The number of boost icons on a card
* **boost_text** - The associated ability text to resolve when flipping a card. This also indicates there's a star icon in the boost field.
* **code** - 5 digit card identifier. Consists of two zero-padded numbers: first two digits are the cycle position, last three are position of the card within the cycle (printed on the card).
* **cost** - Play cost of the card. Relevant for most cards. Possible values:
  * -1: Shows up as X
  * 0+: Shows up as the given integer
* **deck_limit** - The max number of the given card that can be in a deck
* **deck_requirements** - Alter-ego/hero only - describes the character's requirements for an investigator. e.g.:
  ```json
  "deck_requirements": [
    {
      "aspects": 2
    }
  ]
  ```
* **defense** - Character's defense value
* **double_sided** - Whether the card is a double sided card
* **duplicate_of** - A link to the original card code for duplicate cards in other packs
* **escalation_threat** - The acceleration threat to apply to main/side schemes. By default, it is per hero. Possible values:
  * -1: Shows up as X
  * 0+: Shows up as the given number
* **escalation_threat_fixed** - Whether the **escalation_threat** is fixed and not per hero
* **faction_code** - The faction code type for a card. Possible values:
  * `aggression`
  * `basic`
  * `campaign`
  * `encounter`
  * `hero`
  * `justice`
  * `leadership`
  * `pool`
  * `protection`
* **flavor** - The flavor text on a card
* **hand_size** - Character's hand size
* **health** - Character's health. By default, it is fixed.
* **health_per_hero** - Whether the **health** is per hero
* **illustrator** - The name(s) of the artist(s) on the card
* **is_unique** - Whether the card is unique
* **name** - The name of the card
* **octgn_id** - A UUID required for each card
* **pack_code** - The code for the card's pack. Possible values found in `packs.json`.
* **permanent** - Whether the card is permanent
* **position** - The position of the card in the pack
* **quantity** - The quantity of the given card found in a pack
* **recover** - Character's recover value
* **resource_[energy|mental|physical|wild]** - Amount of resources of the given type
* **scheme_acceleration** - The acceleration amount on schemes
* **scheme_crisis** - The number of crisis icons on a scheme
* **scheme_hazard** - The number of hazard icons on a scheme
* **set_code** - The code for the card's set. Possible values found in `sets.json`.
* **set_position** - The position of the card in the set
* **stage** - The stage number on a villain or main scheme. Possible values:
  * `null`: There is no stage for the villain or main scheme
  * 0+: Shows up as the given integer
* **subname** - Subname associated with a character (e.g. `Carol Danvers` is a subname for `Captain Marvel`)
* **text** - The text on a card
* **threat** - The target threat on a card before it advances. By default, it is per hero.
* **threat_fixed** - Whether the **threat** is fixed and not per hero
* **thwart** - Character's thwart value. Possible values:
  * `null`: Shows up as dash or star depending on if **thwart_text** is defined
  * -1: Shows up as X
  * 0+: Shows up as the given integer
* **thwart_cost** - Cost for the character to thwart (commonly, the amount of consequential damage)
* **thwart_text** - Ability text associated with the character's thwart
* **traits** - List of traits following the pattern `Trait1. Trait2.`
* **type_code** - Type of the card. Possible values (found in `types.json`):
  * `ally`
  * `alter_ego`
  * `attachment`
  * `environment`
  * `event`
  * `hero`
  * `main_scheme`
  * `minion`
  * `obligation`
  * `resource`
  * `side_scheme`
  * `support`
  * `treachery`
  * `upgrade`
  * `villain`

## JSON text editing tips

Full description of (very simple) JSON format can be found [here](http://www.json.org/), below there are a few tips most relevant to editing this repository.

#### Non-ASCII symbols

When symbols outside the regular [ASCII range](https://en.wikipedia.org/wiki/ASCII#ASCII_printable_code_chart) are needed, UTF-8 symbols come in play. These need to be escaped using `\u<4 letter hexcode>`.

To get the 4-letter hexcode of a UTF-8 symbol (or look up what a particular hexcode represents), you can use a UTF-8 converter, such as [this online tool](http://www.ltg.ed.ac.uk/~richard/utf-8.cgi).

#### Quotes and breaking text into multiple lines

To have text spanning multiple lines, use `\n` to separate them. To have quotes as part of the text, use `\"`.  For example, `"flavor": "\"I'd run if I were you.\"\n - Scott Lang",` results in following flavor text:

> *"I'd run if I were you."*
> *- Scott Lang*

#### Game Symbols

These can be used in a card's `text` section. It will get converted to the appropriate icon.

* `[boost]`
* `[cost]`
* `[energy]`
* `[mental]`
* `[per_hero]`
* `[physical]`
* `[star]`
* `[unique]`
* `[wild]`

#### Translations

To merge new changes in default language in all locales, run the CoffeeScript script `update_locales`. You could install dependency locally or you could use docker.

##### Local installation
Pre-requisites:
 * `node` and `npm` installed
 * `npm -g install coffee-script`

Usage: 

`coffee update_locales.coffee`

##### Docker
Pre-requisites:
 * [Docker](https://www.docker.com/)

Usage:

```
docker run -it --rm -v "$PWD":/usr/src/app  -w /usr/src/app node:22 npm install

docker run -it --rm -v "$PWD":/usr/src/app  -w /usr/src/app node:22 ./node_modules/coffee-script/bin/coffee update_locales.coffee
```