import requests
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()
SF_API_BULKS = os.getenv('SF_API_BULKS')
headers = {'User-Agent': 'ScryFetcher/0.1', 'Accept': '*/*'}

def get_dcbulk():
    bulk_response = requests.get(SF_API_BULKS, headers=headers)
    print(f"bulk_response: {bulk_response}")
    time.sleep(0.1)

    bulk_response = bulk_response.json()
    response_data = bulk_response.get("data")
    dc_uri = response_data[2].get("uri")

    dc_response = requests.get(dc_uri, headers=headers)
    print(f"dc_response: {dc_response}")
    time.sleep(0.1)

    dc_response = dc_response.json()

    return dc_response

def get_acbulk():
    bulk_response = requests.get(SF_API_BULKS, headers=headers)
    print(f"bulk_response: {bulk_response}")
    time.sleep(0.1)

    bulk_response = bulk_response.json()
    response_data = bulk_response.get("data")
    ac_uri = response_data[3].get("uri")

    ac_response = requests.get(ac_uri, headers=headers)
    print(f"ac_response: {ac_response}")
    time.sleep(0.1)

    ac_response = ac_response.json()

    return ac_response

def get_bulk_json():
    bulk_response = requests.get(SF_API_BULKS, headers=headers)
    print(f"bulk_response: {bulk_response}")
    time.sleep(0.1)

    with open("./json_dump/misc/api_bulk.json", "w", encoding="utf-8") as outfile:
        outfile.write(bulk_response.text)

def get_type_jsons():
    SF_CATALOG_SUPER        = os.getenv("SF_CATALOG_SUPER")
    SF_CATALOG_CARD         = os.getenv("SF_CATALOG_CARD")
    SF_CATALOG_ARTIFACT     = os.getenv("SF_CATALOG_ARTIFACT")
    SF_CATALOG_BATTLE       = os.getenv("SF_CATALOG_BATTLE")
    SF_CATALOG_CREATURE     = os.getenv("SF_CATALOG_CREATURE")
    SF_CATALOG_ENCHANTMENT  = os.getenv("SF_CATALOG_ENCHANTMENT")
    SF_CATALOG_LAND         = os.getenv("SF_CATALOG_LAND")
    SF_CATALOG_PLANESWALKER = os.getenv("SF_CATALOG_PLANESWALKER")
    SF_CATALOG_SPELL        = os.getenv("SF_CATALOG_SPELL")

    supertype_res = requests.get(SF_CATALOG_SUPER, headers=headers)
    print(f"supertype_res: {supertype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/super_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(supertype_res.text)

    cardtype_res = requests.get(SF_CATALOG_CARD, headers=headers)
    print(f"cardtype_res: {cardtype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/card_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(cardtype_res.text)

    artifacttype_res = requests.get(SF_CATALOG_ARTIFACT, headers=headers)
    print(f"artifacttype_res: {artifacttype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/artifact_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(artifacttype_res.text)

    battle_res = requests.get(SF_CATALOG_BATTLE, headers=headers)
    print(f"battle_res: {battle_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/battle_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(battle_res.text)

    creaturetype_res = requests.get(SF_CATALOG_CREATURE, headers=headers)
    print(f"creaturetype_res: {creaturetype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/creatue_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(creaturetype_res.text)

    enchantmenttype_res = requests.get(SF_CATALOG_ENCHANTMENT, headers=headers)
    print(f"enchantmenttype_res: {enchantmenttype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/enchantment_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(enchantmenttype_res.text)

    landtype_res = requests.get(SF_CATALOG_LAND, headers=headers)
    print(f"landtype_res: {landtype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/land_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(landtype_res.text)

    planeswalkertype_res = requests.get(SF_CATALOG_PLANESWALKER, headers=headers)
    print(f"planeswalkertype_res: {planeswalkertype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/planeswalker_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(planeswalkertype_res.text)

    spelltype_res = requests.get(SF_CATALOG_SPELL, headers=headers)
    print(f"spelltype_res: {spelltype_res}")
    time.sleep(0.1)
    with open("./json_dump/misc/spell_type.json", "w", encoding="utf-8") as outfile:
        outfile.write(spelltype_res.text)
