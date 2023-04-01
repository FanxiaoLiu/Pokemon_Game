import os
import json
from Pokemon_class import Pokemon
from PokeMove import Move

class Parser:

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "poke_txt.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.poke_arr = []
        self.moves_arr = []
        self.user_arr = []

        ##Opens JSON file, initializes and saves it as a JSON object
        
        with open(abs_file_path, "r") as f:
            self.poke_obj = json.load(f)

        rel_path = "moves.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, "r") as f:
            self.moves_obj = json.load(f)

        rel_path = "user_poke.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, "r") as f:
            self.user_obj = json.load(f)
        
        self.parse_poke()

        self.parse_moves()


    def parse_poke(self):
        ## Reads the JSON object and gets pokemon data from it
        for x in self.poke_obj["pokemon"]:
            poke = Pokemon(x["name"],x["type"],x["ID"])
            self.poke_arr.append(poke)
        
        ##for x in self.poke_arr:
            ##x.display_details()

    def parse_moves(self):
        for x in self.moves_obj["moves"]:
            move = Move(x["id"],x["name"],x["damage"],x["special_effects"],x["type"])
            self.moves_arr.append(move)
        
        for x in self.moves_arr:
            print(x.id)

    def parse_poke_user(self):
        for x in self.user_obj["pokemon"]:
            for y in self.poke_arr:
                if x["poke_id"] == y.get_ID():
                    new_poke = Pokemon(y.name,y.type,y.get_ID())
                    new_poke.set_stats(x["stats"][0],x["stats"][1],x["stats"][2])
                    new_poke.set_CP(x["cp"])
                    self.user_arr.append(new_poke)

        for x in self.user_arr:
            x.display_details()
        for y in self.poke_arr:
            y.display_details()


