import os
import json
from Pokemon_class import Pokemon

def parse(cp,iv,stats):
    
    script_dir = os.path.dirname(__file__)
    rel_path = "poke_txt.json"
    abs_file_path = os.path.join(script_dir, rel_path)

    ##Opens JSON file, reads it and creates a pokemon class based on that data

    with open(abs_file_path, "r") as f:
        readfile = json.load(f)
        print(readfile["pokemon"][0]["ID"])


parse()