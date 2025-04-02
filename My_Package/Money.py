def interest(p, r, t, type):
    amount_ci = p*(1+(r/100))**t
    compund_interest  = amount_ci - p
    Simple_interest = (p*r*t)/100
    amount_si = ((p*r*t)/100) + p
    if type == 'ci':
        print(f"Your Amount after {t} years is ₹{amount_ci} and the amount of money earned is {compund_interest}")
    elif type == "si":
        print(f"Your Amount after {t} years is ₹{amount_si} and the amount of money earned is {Simple_interest}")

def Si(p, r, t):
    return (p*r*t)/100
def Ci(p, r, t):
    a = input("Enter the type of Compounding: ")
    if a == 'Annually' or 'annually':
        return (p * (1 + r / 100)**t) - p
    elif a == 'Half Yearly' or 'Half yearly' or 'half Yearly' or 'half yearly':
        return (p * (1 + r/200)**(2*t)) - p