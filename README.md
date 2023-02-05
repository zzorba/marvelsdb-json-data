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
* **code** - 5 digit card identifier. Consists of two zero-padded numbers: first two digits are the cycle position, last three are position of the card within the cycle (printed on the card).
* cost - Play cost of the card. Relevant for all cards except agendas and titles. May be `null` - this value is used when the card has a special, possibly variable, cost.
* **deck_limit**
* deck_requirements - Alter-ego/hero only - describes the character's requirements for an investigator. e.g.:
  ```json
  "deck_requirements": [
    {
      "aspects": 2
    }
  ]
  ```
* **defense** - Character's defense value
* **escalation_threat** - The acceleration threat to apply to main/side schemes. Possible values:
  * -1: Shows up as X
  * 0+: Shows up as the given number
* **faction_code**
* flavor
* **hand_size** - Character's hand size
* **health** - Character's health
* illustrator
* **is_unique**
* **name**
* octgn_id
* **pack_code**
* **position**
* **quantity**
* **recover** - Character's recover value
* **resource_[energy|mental|physical|wild]** - Amount of resources of the given type
* **subname** - Subname associated with a character (e.g. `Carol Danvers` is a subname for `Captain Marvel`)
* text
* **thwart** - Character's thwart value. Format is integer or `null`. Possible values:
  * `null`: Shows up as dash or star depending on if **thwart_text** is defined
  * -1: Shows up as X
  * 0+: Shows up as the given integer
* **thwart_cost** - Cost for the character to thwart (commonly, the amount of consequential damage)
* **thwart_text** - Ability text associated with the character's thwart
* **traits** - List of traits following the pattern `Trait1. Trait2.`
* **type_code** - Type of the card. Possible values (in quotes): 
  * `hero`
  * `alter_hero`
  * `ally` 
  * `event` 
  * `support` 
  * `upgrade`
  * `resource` 
  * `villain` 
  * `obligation`
  * `main_scheme`  
  * `side_scheme`
  * `minion`
  * `attachment`
  * `treachery`

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

These can be used in a card's `text` section.

* `[boost]`
* `[energy]`
* `[mental]`
* `[per_hero]`
* `[physical]`
* `[wild]`

#### Translations

To merge new changes in default language in all locales, run the CoffeeScript script `update_locales`.

Pre-requisites:
 * `node` and `npm` installed
 * `npm -g install coffee-script`

Usage: `coffee update_locales.coffee`
