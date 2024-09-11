import json
import re
import os
import enum

class CharacterType(enum.Enum):
    TOWNSFOLK = 0
    OUTSIDER = 1
    MINION = 2
    DEMON = 3
    TRAVELER = 4

class Character():

    TYPE_TO_STRING = {
        CharacterType.TOWNSFOLK: "Townsfolk",
        CharacterType.OUTSIDER: "Outsider",
        CharacterType.MINION: "Minion",
        CharacterType.DEMON: "Demon",
        CharacterType.TRAVELER: "Traveler",
    }
    TEAM_TO_TYPE = {
        "townsfolk": CharacterType.TOWNSFOLK,
        "outsider": CharacterType.OUTSIDER,
        "minion": CharacterType.MINION,
        "demon": CharacterType.DEMON,
        "traveler": CharacterType.TRAVELER,
    }

    def __init__(self, name, character_type, ability):

        self.name = name
        self.character_type = character_type
        self.ability = ability
    
    def __str__(self):
        return f"{self.name} ({Character.TYPE_TO_STRING[self.character_type]}): {self.ability}"

def extractCharactersFromJson(file):
    characters = []
    edition = json.load(file)
    for i in range(1, len(edition)):
        character = edition[i]
        characters.append(Character(character["name"], Character.TEAM_TO_TYPE[character["team"]], character["ability"]))
    
    return characters

def printAllCharacters(file):
    for character in extractCharactersFromJson(file):
        print(character)

def getAllCharactersFromAllJsons():
    characters = []
    for filename in [each for each in os.listdir(os.getcwd()) if each.endswith('.json')]:
        with open(filename, "rb") as file:
            characters += extractCharactersFromJson(file)
    return characters
    
def printAllCharactersFromAllJsons():
    characters = getAllCharactersFromAllJsons()
    for character in characters:
        print(character)

def mergeAllJsons(outfilename):
    new_json = [{"id":"_meta","name":"Hyper's Stuff","author":"Hyper (Automated Merge)","almanac":"Ask Hyper for them."}]
    for filename in [each for each in os.listdir(os.getcwd()) if each.endswith('.json')]:
        if filename != outfilename:
            with open(filename, "rb") as file:
                characters = json.load(file)[1:]
                new_json += characters
    with open(outfilename + ".json", "w") as file:
        json.dump(new_json, file, indent=4)
            

if __name__ == "__main__":
    mergeAllJsons("merged")
