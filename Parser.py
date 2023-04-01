import os
import json
from Pokemon_class import Pokemon

def parse():
    
    script_dir = os.path.dirname(__file__)
    rel_path = "poke_txt.json"
    abs_file_path = os.path.join(script_dir, rel_path)

    ##Opens JSON file, reads it and creates a pokemon class based on that data
    poke_arr = []
    
    with open(abs_file_path, "r") as f:
        readfile = json.load(f)
        for x in readfile["pokemon"]:
            poke = Pokemon(x["name"],x["type"],x["ID"])
            poke.set_stats(x["stats"][0],x["stats"][1],x["stats"][2])
            poke.set_CP(x["cp"])
            poke_arr.append(poke)
    
    for x in poke_arr:
        print(x.get_ID())
            


parse()