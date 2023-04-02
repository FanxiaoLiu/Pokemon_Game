from multiprocessing import Process as proc
from Parser import *

def main():
    all_data = Parser()
    all_poke_data = all_data.poke_arr
    all_moves_data = all_data.moves_arr
    all_data.update_user_poke()

main()