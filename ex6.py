from random import randint, random
from sys import exit, version


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hp = randint(900, 2000)
        if self.name == "意大利炮":
            self.hp = 100000 # :P
        self.dead = False

    def be_attacked(self, attacker=''):
        decrease = randint(50, 200)
        if self.lucky() or attacker == "意大利炮":  # hiahiahia :P
            print("暴击")
            decrease = randint(500, 1000)
        self.hp -= decrease
        if self.hp <= 0:
            self.dead = True

    def lucky(self):
        if randint(1, 10) == randint(1, 10):
            return True
        return False

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


def describe_players():
    for player in players:
        if not player.dead:
            print(f"玩家{player.name}血量为{player.hp}")


def mainloop():
    counter = num_of_players
    while True:
        describe_players()
        # 新一轮攻击开始
        for player in players:
            if not player.dead:
                attack_index = input(f"{player.name}请输入攻击对象的序号：")
                # 检查用户输入是否为整数
                if attack_index.isdigit():
                    attack_index = int(attack_index)
                    pass
                else:
                    print("不符合攻击规范")
                    continue
                # 检查自残情况
                if attack_index == players.index(player) + 1:
                    print("不能自残")
                    continue
                # 检查攻击死亡玩家
                attacked_player = players[attack_index - 1]
                if attacked_player.dead:
                    print("不能攻击已死亡的玩家")
                    continue
                attacked_player.be_attacked(player.name)
                if attacked_player.dead:
                    print(f"玩家{attacked_player.name}死亡")
                    counter -= 1  # 将存活数量 - 1
                else:
                    print(f"{attacked_player.name}血量为{attacked_player.hp}")
            if counter == 1 and not player.dead:
                print(f"{player.name}获胜")
                input("按下<Enter>键结束游戏")
                exit(0)
        # 中场休息 增加hp
        print('补充能量'.center(20, '-'))

        for player in players:
            if not player.dead:
                eat_increase = randint(20, 40)
                if player.lucky() or player.name == "冬泳怪鸽":
                    eat_increase = randint(1000, 2000)
                    print(f"{player.name}运气爆棚，", end='')
                player.hp += eat_increase
                print(f"玩家{player.name}增加血量{eat_increase}")
        print('补充能量完毕'.center(20, '-'))


if __name__ == "__main__":
    mainloop()
