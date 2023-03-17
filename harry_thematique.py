import random

def harry_thematique():
    pts = 0
    nB1 = random.randint(1, 100)
    nB2 = random.randint(1, 100)
    operator = ['+', '-', '*', '/']
    nB3 = random.randint(0, 3)
    actualOperator = operator[nB3]

    if actualOperator == '/':
        responce = nB2 * nB1
        userResponce = input(f"Combien font  {responce} {actualOperator} {nB1} ? \n")
        userResponce = int(userResponce)
        if userResponce == nB2:
            pts += 1
            print("bravo")
        else :
            pts -= 1
            print("mince, la réponce était ", responce)
    else :
        userResponce = input(f"Combien font  {nB1} {actualOperator} {nB2} ? \n")
        userResponce = int(userResponce)
        responce = eval(f"{nB1} {actualOperator} {nB2}")
        int(responce)
        if userResponce == responce:
            pts += 1
            print("bravo")
        else :
            pts -= 1
            print(f"mince, la réponce était {responce}")
    return pts