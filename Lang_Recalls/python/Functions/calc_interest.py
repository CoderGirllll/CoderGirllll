def calc_interest(P, T, R = .06):
    A = P*(1 + (R*T))
    return A
print(calc_interest(5000, 2))