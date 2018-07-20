from random import choice as select
from random import randint as rint
from time import sleep as delay

from names import get_full_name as name

players = []
while players != ['exit']:
    print("PythonRoyale")
    players = input().split('/')
    if players[0] == 'auto':
        count = int(players[1])
        players = []
        while len(players) != count:
            n = name()
            if n not in players:
                players.append(name())


    def alive():
        return len(players)


    def define_gun(zgun_a, ac, gun):
        if rint(1, 10) != 5:
            action = zgun_a
            selection = select(players)
            if action == ac:
                killer = select(players)
                while killer == selection:
                    killer = select(players)
                print(killer + ' killed ' + selection + " with a", gun, end = ' ')
                players.remove(selection)
        else:
            action = gun_a
            selection = select(players)
            if action == ac:
                print(selection + " commited suicide with a", gun, end = ' ')
                players.remove(selection)


    def define_action(act_a, ac, phrase):
        action = act_a
        selection = select(players)
        if action == ac:
            killer = select(players)
            while killer == selection:
                killer = select(players)
            print(phrase.replace("$k", killer).replace("$s", selection), end = ' ')


    while alive() != 1:
        gun_a = rint(1, 31)
        define_gun(gun_a, 1, 'Glock G29 Pistol.')
        define_gun(gun_a, 2, 'Ruger MK III Pistol.')
        define_gun(gun_a, 3, 'Desert Eagle Pistol.')
        define_gun(gun_a, 4, 'Glock G29 Pistol.')
        define_gun(gun_a, 5, 'DPMS Oracle Rifle.')
        define_gun(gun_a, 6, 'M-16 Rifle.')
        define_gun(gun_a, 7, 'Ruger AR-556 Rifle.')
        define_gun(gun_a, 8, 'Mossberg 590A1 Shotgun.')
        define_gun(gun_a, 9, 'Kel-Tec KSG Shotgun.')
        define_gun(gun_a, 10, 'M-14 Rifle.')
        define_gun(gun_a, 11, 'Uzi SMG.')
        define_gun(gun_a, 12, 'AK-47 Rifle.')
        define_gun(gun_a, 13, 'Thompson SMG.')
        define_gun(gun_a, 14, 'UMP-45 SMG.')
        define_gun(gun_a, 15, 'UMP9 SMG.')
        define_gun(gun_a, 16, 'Groza Rifle.')
        define_gun(gun_a, 17, 'AWM Sniper Rifle.')
        define_gun(gun_a, 18, 'knife.')
        define_gun(gun_a, 19, 'bow.')
        define_gun(gun_a, 20, 'crossbow.')
        define_gun(gun_a, 29, 'car.')
        define_action(gun_a, 21, "$k is watching $s.")
        define_action(gun_a, 22, "$k is teaming with $s.")
        define_action(gun_a, 23, "$k is talking with $s.")
        define_action(gun_a, 23, "$k almost hit $s.")
        define_action(gun_a, 24, "$s is sleeping.")
        define_action(gun_a, 25, "$s is building a base.")
        define_action(gun_a, 26, "$s is climbing a tree.")
        define_action(gun_a, 27, "$s is eating.")
        define_action(gun_a, 28, "$s is searching for food.")
        define_action(gun_a, 30, "$s is tired.")
        define_action(gun_a, 31, "$s is running away from $k.")
        print("Alive:", alive())
        delay(rint(1, 153) / 100)
    print("Winner:", players[0])
