from multiprocessing import Process as proc
from data.Parser import *
from Pokemon_class import Pokemon
import random as rand

def find_wild(user_poke,poke,moves,cp_cap,user):
    poke_arr = []
    for x in range(0,3):
        randnum = rand.randint(0,len(poke)-1)
        randpoke = Pokemon(poke[randnum].name,poke[randnum].type,poke[randnum].pokeid)
        randpoke.set_CP(rand.randint(20,cp_cap))
        randpoke.set_stats(rand.randint(7,15),rand.randint(7,15),rand.randint(7,15))
        randpoke.set_moveset(poke[randnum].moveset)
        poke_arr.append(randpoke)
    print("BAM! Three Pokemon jump out of the grass: ") 
    counter = 1
    for x in poke_arr:
        print(counter, ". Name: ", x.name, "\tCP: ", x.CP, "\tStats (Atk,Def,HP): ", x.stats)
        counter += 1
    print(" ")

    while True:
        print("1. Catch one")
        print("2. Fight one")
        print("3. Run away like a scaredy cat\n")
        action1 = int(input("What would you like to do with them? (Enter number of action)"))
        poke_choice1 = int(input("Alright! Which pokemon? (Enter the number): "))
        if action1 == 1: ## Actions for catching a pokemon
            if len(user_poke) < 12:
                if user.pb > 0:
                    user.pb -= 1
                    high_poke = 0
                    for x in user_poke:
                        if x.CP >= high_poke:
                            high_poke = x.CP
                    cp_diff = poke_arr[poke_choice1-1].CP - high_poke
                    chances = 0.05
                    if cp_diff > 0:
                        if cp_diff < 50:
                            chances = 0.60
                        elif cp_diff < 300:
                            chances = 0.4
                        elif cp_diff < 500:
                            chances = 0.2
                        elif cp_diff < 800:
                            chances = 0.1
                    elif cp_diff == 0:
                        chances = 0.60
                    else:
                        if cp_diff > -50:
                            chances = 0.60
                        elif cp_diff > -300:
                            chances = 0.7
                        elif cp_diff > -500:
                            chances = 0.8
                        elif cp_diff > -800:
                            chances = 0.9
                        else:
                            chances = 0.95
                    randchance = float(rand.randint(1,100))
                    if randchance <= (chances * 100):
                        print("You have successfully caught the pokemon!")
                        return user.pb,poke_arr[poke_choice1-1]
                    else:
                        print("Oh no! The Pokemon fled! Skill issue tbh...")
                        return user.pb
                else:
                    print("Please get some more pokeballs through battling.")
                    return None
            else:
                print("You cannot catch anymore pokemon as your party is already full. Please release some first.")
                return None
        elif action1 == 2:
            print("Current pokemon in your party:")
            print("---------------------------------")
            counter = 1
            for x in user_poke:
                poke_name = ""
                for y in poke:
                    if x.pokeid == y.pokeid:
                        poke_name = y.name
                print(counter, ". Name: ", poke_name, "\tCP: ", x.CP, "\tStats (ATK, DEF, HP): ", x.stats)
                counter += 1
            poke_choice_battle = int(input("Which pokemon would you like to choose to battle for you? (Please input the number): "))
            print("\nGreat choice! May the battle begin...")
            user_stats = user_poke[poke_choice_battle-1].stats
            user_cp = user_poke[poke_choice_battle-1].CP
            user_moveset = user_poke[poke_choice_battle-1].moveset
            user_name = user_poke[poke_choice_battle-1].name
            wild_stats = poke_arr[poke_choice1-1].stats
            wild_cp = poke_arr[poke_choice1-1].CP
            wild_moveset = poke_arr[poke_choice1-1].moveset
            wild_name = poke_arr[poke_choice1-1].name

            user_hp = float(user_stats[2]) * user_cp
            wild_hp = float(wild_stats[2]) * wild_cp

            print("Available Moves: ")
            counter = 1
            poke_moves = []
            for x in user_moveset:
                move_name = ""
                move_dmg = 0
                move_spec_eff = ""
                for y in moves:
                    if x == y.id:
                        move_name = y.name
                        move_dmg = y.dmg
                        move_spec_eff = y.spec_eff
                        poke_moves.append(y)
                print(counter, ". ", move_name, "\tDamage Modifier: ", move_dmg, "\tSpecial Effect: ", move_spec_eff)
                counter += 1
            wildisburnt = 0
            userisburnt = 0

            while user_hp > 0 and wild_hp > 0:

                print("--------------------------------")
                print("Your HP: ", round(user_hp,2))
                print("Wild HP: ", round(wild_hp,2))
                print("--------------------------------")
                poke_moves_choice = int(input("Which move would you like to use? (Please input the number): "))
                poke_moves_choice = poke_moves[poke_moves_choice-1]
                wild_moves = []
                for x in wild_moveset:
                    for y in moves:
                        if x == y.id:
                            wild_moves.append(y)
                wild_move = wild_moves[rand.randint(0,len(wild_moves)-1)]
                wild_dmg = (wild_move.dmg * wild_stats[0] * wild_cp) / 100
                user_dmg = (poke_moves_choice.dmg * user_stats[0] * user_cp) / 100
                
                user_hp -= wild_dmg
                wild_hp -= user_dmg

                wild_burn = burn_detection(poke_moves_choice.spec_eff)
                user_burn = burn_detection(wild_move.spec_eff)

                if isinstance(wild_burn,int) and wildisburnt == 0:
                    random = rand.randint(0,100)
                    if random <= (wild_burn * 100):
                        wildisburnt = 0.2 - wild_burn
                
                if isinstance(user_burn,int) and userisburnt == 0:
                    random = rand.randint(0,100)
                    if random <= (user_burn * 100):
                        wildisburnt = 0.2 - wild_burn
                
                if wildisburnt != 0:
                    print("You have burned the wild pokemon!")
                    wild_hp -= float(wild_stats[2]) * wild_cp * wildisburnt
                
                if userisburnt != 0:
                    print("Your pokemon has been burned!")
                    user_hp -= float(user_stats[2]) * user_cp * userisburnt
                
            if wild_hp <= 0 and user_hp <= 0:
                print("You have defeated the wild pokemon! You have gained 1 Pokeball as a reward! Your pokemon has also gained 20 CP!")
                return user.pb+1,poke_choice_battle-1
            elif wild_hp <= 0:
                print("You have defeated the wild pokemon! You have gained 1 Pokeball as a reward! Your pokemon has also gained 20 CP!")
                return user.pb+1,poke_choice_battle-1
            elif user_hp <= 0:
                print("You have been defeated by the wild pokemon! He steals 1 Pokeball from you :(")
                return user.pb-1
        elif action1 == 3:
            print("You run away like a scaredy cat! Pokemon aren't that scary, come on...")
            return None
                    

def burn_detection(spec_eff):
    if spec_eff == "Light Burn":
        return 0.05
    elif spec_eff == "Medium Burn":
        return 0.02
    elif spec_eff == "Heavy Burn":
        return 0.01
    else:
        return None

def main():
    all_data = Parser()
    all_poke_data = all_data.poke_arr
    all_moves_data = all_data.moves_arr
    user_poke_data = all_data.user_arr
    users_data = all_data.users_arr
    print("Welcome to the Pokemon game. Please choose your login user.")
    for x in range(0,len(users_data)):
        print(x+1,". Name: ", users_data[x].name, "\tID: ", users_data[x].id)
    usr_choice = int(input("Please input the number of your user based on the numbers above or 0 to create a new user: "))
    current_user = 0
    if usr_choice == 0:
        name = input("Please input the name of the new user: ")
        id = users_data[-1].id + 1
        new_user = User(id,name,1,0)
        users_data.append(new_user)
        current_user = users_data[-1]
    else:
        current_user = users_data[usr_choice-1]
    
    while True:

        wildyesno = int(input("Would you like to proceed to the wild? (1 for yes, 0 for no (0 Would exit the game and save your progress), 2 for releasing a Pokemon): "))

        if wildyesno == 1:
            pass
        if wildyesno == 2:
            pass
        else:
            break

        new_poke = find_wild(user_poke_data,all_poke_data,all_moves_data,300,current_user)

        if new_poke == None:
            pass
        elif isinstance(new_poke,int):
            user_i = 0
            for x in range(0,len(users_data)):
                if users_data[x].id == current_user.id:
                    user_i = x
            users_data[user_i].pb = new_poke
        else:
            user_i = 0
            for x in range(0,len(users_data)):
                if users_data[x].id == current_user.id:
                    user_i = x
            data1,data2 = new_poke
            if isinstance(data2,int):
                all_data.user_arr[data2].power_up(20)
                users_data[user_i].pb = data1
                all_data.update_user_poke()
            else:
                users_data[user_i].pb = data1
                all_data.user_arr.append(data2)
                all_data.update_user_poke()
        
        all_data.update_users()
    
    ##all_data.update_user_poke()


main()