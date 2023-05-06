import random

questions = {'13.1: Vector Functions & Space Curves': [18, 19, 20, 41, 42],
             '13.2: Derivatives & Integrals of Vector Functions': [17, 19, 24, 25, 33],
             '*13.3: Arc Length & Curvature': [],
             '14.1: Functions of Several Variables': [37, 44],
             '14.2: Limits & Continuity': [],
             '14.3: Partial Derivatives': [],
             '14.4: Tangent Planes & Linear Approximation': [6, 11, 33, 34, 42, 45],
             '14.5: Chain Rule': [29, 34, 45, 47, 49, 51],
             '14.6: Directional Derivatives & Gradient Vector': [6, 9, 13, 20, 21, 22, 27, 28, 29, 35, 37, 39, 40, 43, 49, 50, 52, 53, 55, 56, 57],
             '14.7: Max & Min Values': [31, 33, 35, 39, 41, 43, 45, 51, 53],
             '14.8: Lagrange Multipliers': [13, 15, 17, 19, 21, 45],
             '15.1: Double Integrals over Rectangles': [13, 17],
             '15.2: Double Integrals over General Regions': [13, 15, 17, 19, 25, 27],
             '15.3: Double Integrals in Polar Coordinates': [13, 15, 19, 21, 23, 25, 31, 39],
             '15.4: Applications of Double Integrals': [],
             '15.5: Surface Area': [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 17, 23],
             '15.6: Triple Integrals': [13, 17, 19, 20, 21, 22],
             '15.7: Triple Integrals in Cylindrical Integrals': [17, 19, 21, 22, 27],
             '15.8: Triple Integrals in Spherical Integrals': [17, 19, 21, 23, 25, 27, 29, 35],
             '15.9: Change in Variables in Multiple Integrals': [19, 21, 23, 24],
             '16.1: Vector Fields': [21, 24],
             '16.2: Line Integrals': [13, 15, 19, 21, 29, 33],
             '16.3: The Fundamental Theorem for Line Integrals': [15, 17, 19, 21, 23, 25, 29]}

len_quest = len([problem for problems in questions.values() for problem in problems])

random_m = random.Random()
used = []


def get_problem():
    rand_chap = random_m.choice(list(questions.keys()))
    chap = questions[rand_chap]
    num_quest = len(chap) - 1
    if num_quest > 0:
        rand_quest = random_m.randint(0, num_quest)
        if ((rand_chap, chap[rand_quest]) not in used):
            used.append((rand_chap, chap[rand_quest]))
            print(used)
            print(rand_chap, chap[rand_quest])
        else:
            get_problem()
    else:
        get_problem()


while len(used) != len_quest:
    input("Press enter to receive a problem")
    get_problem()
