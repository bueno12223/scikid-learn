import random 

def_dice = [n for n in range(6)]

def throw_dice(number_of_shots, dice=def_dice):
    return [random.choice(dice) for x in range(number_of_shots)]

def main():
    number_of_shots = 3
    number_of_tries = 10000
    target_shot = 1

    shots = [throw_dice(number_of_shots) for x in range(number_of_tries)]
    shots_with_target = len(list(filter(lambda shot: target_shot not in shot, shots)))
    probability = shots_with_target / number_of_tries

    print(f'Probabilidad de no obtener amenos un {target_shot} en {number_of_tries} tiros = {probability}')


if __name__ == "__main__":
    main()




