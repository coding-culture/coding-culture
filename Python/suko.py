from z3 import *


def is_valid(guess):
    used = []
    for d in guess.decls():
        if guess[d] in used:
            return False
        else:
            used.append(guess[d])
    return True


def main():

    s = Solver()
    # impliment the variables

    a = Int('a')#h
    b = Int('b')#i
    c = Int('c') #a
    d = Int('d') #b
    e = Int('e')#c
    f = Int('f')#d
    g = Int('g')#e
    h = Int('h')#f
    i = Int('i')#g

    # new instance of z3's solver

    # add in the constraints
    s.add(a + b + c + f == 20)
    s.add(d + e == 8)
    s.add(g + h + i == 17)
    s.add(a + b + d + e == 14)
    s.add(b + c + e + f == 23)
    s.add(d + e + g + h == 19)
    s.add(e + f + h + i == 26)
    s.add(And(a > 0, b > 0, c > 0, d > 0, e > 0, f > 0, g > 0, h > 0, i > 0))
    s.add(And(a < 10, b < 10, c < 10, d < 10, e < 10, f < 10, g < 10, h < 10, i < 10))

    possibles = []
    while s.check() == sat:
        # print (s.model())
        possibles.append(s.model())
        s.add(Or(a != s.model()[a], b != s.model()[b], c != s.model()[c], d != s.model()[d],
         e != s.model()[e], f != s.model()[f], g != s.model()[g], h != s.model()[h], i != s.model()[i]))


    for model in possibles:
        if is_valid(model):
            print(model)
            exit()

if __name__ == '__main__':
    main()
