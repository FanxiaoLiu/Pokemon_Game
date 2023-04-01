import os
import json
from Pokemon_class import Pokemon

class Parser:

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "poke_txt.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.poke_arr = []
        self.moves_arr = []

        ##Opens JSON file, initializes and saves it as a JSON object
        
        with open(abs_file_path, "r") as f:
            self.poke_obj = json.load(f)

        rel_path = "moves.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, "r") as f:
            self.moves_obj = json.load(f)


    def parse_poke(self):
        ## Reads the JSON object and gets pokemon data from it
        for x in self.poke_obj["pokemon"]:
            poke = Pokemon(x["name"],x["type"],x["ID"])
            self.poke_arr.append(poke)
        
        for x in self.poke_arr:
            print(x.display_details())

    def parse_moves(self):
        for x in self.moves_obj:
            pass

