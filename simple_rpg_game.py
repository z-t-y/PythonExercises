from random import randint
from sys import exit, version


class Player(object):
    def __init__(self, name):
        self.name = name
        self.blood_vol = randint(900, 2000)
        self.dead = False

    def be_attacked(self):
        decrease = randint(50, 200)
        if randint(1, 10) == randint(1, 10):
            crit = True
            print("暴击")
            decrease = randint(500, 1000)
        self.blood_vol -= decrease
        if self.blood_vol <= 0:
            self.dead = True


print("Simple Command Line RPG Game By Andy")
print("Copyright(c) all rights reserved")
print("Version: 1.0")
print("-" * 50)
print("游戏开始")
while True:
    num_of_players = input("输入玩家数量：")
    if num_of_players.isdigit():
        num_of_players = int(num_of_players)
        cnt = num_of_players
        break


players = []
for i in range(num_of_players):
    players.append(
        Player(input(f"输入玩家{i+1}的名字："))
    )


def mainloop():
    cnt = num_of_players
    while True:
        for player in players:
            if not player.dead:
                print(f"玩家{player.name}血量为{player.blood_vol}")
        for player in players:
            if not player.dead:
                attack_index = input(f"{player.name}请输入攻击对象的序号：")
                if attack_index.isdigit():
                    attack_index = int(attack_index)
                    pass
                else:
                    print("不符合攻击规范")
                    continue
                if attack_index == players.index(player) + 1:
                    print("不能自残")
                    continue
                attacked_player = players[attack_index - 1]
                if attacked_player.dead:
                    print("不能攻击已死亡的玩家")
                    continue
                attacked_player.be_attacked()
                if attacked_player.dead:
                    print(f"玩家{attacked_player.name}死亡")
                    cnt -= 1
                else:
                    print(f"{attacked_player.name}血量为{attacked_player.blood_vol}")
            if cnt == 1 and not player.dead:
                print(f"{player.name}获胜")
                exit(0)


if __name__ == "__main__":
    mainloop()
