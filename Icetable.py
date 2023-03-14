from chempy import balance_stoichiometry 
from pprint import pprint
from sympy import symbols, solve
import pandas as pd
import matplotlib.pyplot as plt


def balancer(reactants, products):
    reac, prod = balance_stoichiometry(reactants, products)
    pprint("The balanced reactants are: " + str(dict(reac)))
    pprint("The balanced products are: " + str(dict(prod)))
    return dict(reac), dict(prod)

def format_x(coef):
    if coef == 1:
        return "+x"
    elif coef == -1:
        return '-x'
    elif coef > 1:
        return '+' + str(coef) + '*' + 'x'
    else:
        return str(coef) + '*x'

def format_compound(coef, compound):
    if abs(coef) == 1:
        return compound
    else:
        return str(abs(coef)) + compound

def format_equil(initial):
    if initial == 0:
        return ''
    else:
        return str(initial)

def multi(equil, pow):
    biggie = ''
    for idx, eqn in enumerate(equil):
        biggie += '(' + eqn + ')**' + str(abs(pow[idx])) +'*'
    return "(" + biggie[:-1] + ")"

def div(prod, reac):
    return "(" + prod + "/" + reac + ")"


# this is gonna ask the user for the reactant in the equation
reactants = []
products = []
text = input("Please enter your first reactant: ")
while text != '':
    reactants.append(text)
    text = input("Please enter another reactant or hit enter: ")

# this is gonna ask the user for the inital concentrations of the reactants
initial_reac = {}
for reactant in reactants:
    text = input("Please enter the inital concentration for " + reactant + ": ")
    initial_reac[reactant] = float(text)

# this is gonna ask the user for the products in the equation
text = input("Please enter your first product: ")
while text != '':
    products.append(text)
    text = input("Please enter another product or hit enter: ")

# this is gonna ask the user for the inital concentrations of the products
initial_prod = {}
for product in products:
    text = input("Please enter the inital concentration for " + product + ": ")
    initial_prod[product] = float(text)


# this is gonna ask for the equilibrium constant and Q value
Keq = input("Please enter your equilibrium constant: ")
reacq = input("Please enter your reaction quotient (Q): ")


reac, prod = balancer(reactants, products)

for key, value in reac.items():
    reac[key] = -value

x = symbols('x')

#the next bit of lines are used to create the actual ice table
cols = [""] + [format_compound(coef, compound) for compound, coef in reac.items()] + [format_compound(coef, compound) for compound, coef in prod.items()]
initial = ['[Initial] I'] + list(initial_reac.values()) + list(initial_prod.values())
change = ['[Change] C'] + [format_x(x) for x in reac.values()] + [format_x(x) for x in prod.values()]
equil = ['[Equilibrium] E'] + [format_equil(initial[idx]) + change[idx] for idx in range(1, len(initial))]

unformat_change = [''] + [format_x(x) for x in reac.values()] + [format_x(x) for x in prod.values()]
unformatted = [str(initial[idx]) + change[idx] for idx in range(1, len(initial))]
reac_eqn = unformatted[:len(reactants)]
prod_eqn = unformatted[len(reactants):]

roots = solve(div(multi(prod_eqn, list(prod.values())), multi(reac_eqn, list(reac.values()))) + "-" + str(Keq)) 
print(roots)

data = [initial, change, equil]
df = pd.DataFrame(data, columns=cols)
sel = df[cols]
table = plt.table(cellText=sel.values, colLabels=sel.columns, loc='center')
plt.axis('off')
plt.show()