from random import randint

player1 = "John"
player2 = "Jack"

def valid_name(name):
    if name in [player1, player2]:
        return True
    print(f"Choose between {player1} and {player2}")

def is_in_range(take, pencils):
    try:
        take = int(take)
    except ValueError:
        return print("Possible values: '1', '2' or '3'")
    if take not in range(1, 4):
        return print("Possible values: '1', '2' or '3'")
    if pencils - take < 0:
        return print("Too many pencils were taken")
    return True

def is_pos_num(num):
    res = "The number of pencils should be"
    try:
        num = int(num)
    except ValueError:
        return print(f'{res} numeric')
    if not num > 0:
        return print(f'{res} positive')
    return True

def bot_move(pencils):
    # print('pencils remaining:', pencils)
    if pencils == 1:
        return 1
    des = range(1, 100, 4)
    if (pencils - 3) in des:
        # print(pencils - 3, '-3 in des')
        return 3
    if (pencils - 2) in des:
        # print(pencils - 2, '-2 in des')
        return 2
    if (pencils - 1) in des:
        # print(pencils - 1, '-1 in des')
        return 1
    # print('rand')
    return randint(1,3)
  
while True:
    pencils = input("How many pencils would you like to use:")
    if is_pos_num(pencils):
        pencils = int(pencils)
        while True:
            name = input(f"Who will be the first ({player1}, {player2}):")
            if valid_name(name):
                print(f"{'|' * pencils}")
                while pencils > 0:
                    if name == player1:
                        take = input(f"{name}'s turn:")
                    else:
                        print(f"{name}'s turn:")
                        take = bot_move(pencils)
                        print(take)
                    if is_in_range(take, pencils):
                        pencils -= int(take)
                        print(f"{'|' * pencils}")
                        name = name == player1 and player2 or player1
                print(f'{name} won!')
                break
        break