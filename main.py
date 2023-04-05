from multiprocessing import Process as proc
from Parser import *
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

    while True:
        print("1. Catch one")
        print("2. Fight one")
        print("3. Run away like a scaredy cat")
        action1 = int(input("What would you like to do with them?"))
        poke_choice1 = int(input("Alright! Which pokemon? (Enter the number)"))
        if action1 == 1:
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

def main():
    all_data = Parser()
    all_poke_data = all_data.poke_arr
    all_moves_data = all_data.moves_arr
    user_poke_data = all_data.user_arr
    users_data = all_data.users_arr
    print("Welcome to the Pokemon game.Please choose your login user.")
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
        users_data[user_i].pb = new_poke[0]
        all_data.user_arr.append(new_poke[1])
        all_data.update_user_poke()
    
    all_data.update_users()
    
    ##all_data.update_user_poke()


main()