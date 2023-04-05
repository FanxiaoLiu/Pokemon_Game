import os
import json
from Pokemon_class import Pokemon
from PokeMove import Move
from UserObj import User

class Parser:

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "poke_txt.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.poke_arr = []
        self.moves_arr = []
        self.user_arr = []
        self.users_arr = []

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

        rel_path = "users.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, "r") as f:
            self.users_obj = json.load(f)
        
        self.parse_poke()

        self.parse_moves()

        self.parse_poke_user()
        
        self.parse_users()

    def update_user_poke(self):
        self.user_obj["pokemon"] = []
        for x in self.user_arr:
            id = x.pokeid
            cp = x.CP
            stats = x.stats

            data = {
                'poke_id': id,
                'cp': cp,
                'stats': stats
            }
            self.user_obj["pokemon"].append(data)
        self.write_to_user_file()
    
    def update_users(self):
        self.users_obj["users"] = []
        for x in self.users_arr:
            id = x.id
            name = x.name
            lvl = x.lvl
            pb = x.pb

            data = {
                'id': id,
                'name': name,
                'lvl': lvl,
                'pokeballs': pb
            }
            self.users_obj["users"].append(data)
        self.write_to_users_file()

    def parse_poke(self):
        ## Reads the JSON object and gets pokemon data from it
        for x in self.poke_obj["pokemon"]:
            poke = Pokemon(x["name"],x["type"],x["ID"])
            moveset_arr = []
            for y in x["Moveset"]:
                moveset_arr.append(y["id"])
            poke.set_moveset(moveset_arr)
            self.poke_arr.append(poke)
        
        ##for x in self.poke_arr:
            ##x.display_details()

    def parse_moves(self):
        for x in self.moves_obj["moves"]:
            move = Move(x["id"],x["name"],x["damage"],x["special_effects"],x["type"])
            self.moves_arr.append(move)

    def parse_poke_user(self):
        for x in self.user_obj["pokemon"]:
            for y in self.poke_arr:
                if x["poke_id"] == y.get_ID():
                    new_poke = Pokemon(y.name,y.type,y.get_ID())
                    new_poke.set_stats(x["stats"][0],x["stats"][1],x["stats"][2])
                    new_poke.set_CP(x["cp"])
                    new_poke.set_moveset(y.moveset)
                    self.user_arr.append(new_poke)

    def write_to_user_file(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "user_poke.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, "w") as f:
            json_string = json.dumps(self.user_obj, indent=4)
            f.write(json_string)

    def parse_users(self):
        for x in self.users_obj["users"]:
            self.users_arr.append(User(x["id"],x["name"],x["lvl"],x["pokeballs"]))
        
        for x in self.users_arr:
            print(x.id)

    def write_to_users_file(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "users.json"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, "w") as f:
            json_string = json.dumps(self.users_obj, indent=4)
            f.write(json_string)