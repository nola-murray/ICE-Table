""" Things we need:
1. The chemical reaction equation with coefficients
2. The initial concentrations of the reactants and products
3. The change which is minus for reactants and plus for products (coefficient * x)
4. equilibrium values which is initial - change"""

from chempy import balance_stoichiometry 
from pprint import pprint


def balancer(reactants, products):
    reac, prod = balance_stoichiometry(reactants, products)
    pprint("The balanced reactants are: " + str(dict(reac)))
    pprint("The balanced products are: " + str(dict(prod)))
    return dict(reac), dict(prod)


# this is gonna ask the user for the reactant in the equation
reactants = set()
products = set()
text = input("Please enter your first reactant: ")
while text != '':
    reactants.add(text)
    text = input("Please enter another reactant or hit enter: ")

# this is gonna ask the user for the inital concentrations of the reactants
initial_reac = {}
for reactant in reactants:
    text = input("Please enter the inital concentration for " + reactant + ": ")
    initial_reac[reactant] = float(text)

# this is gonna ask the user for the products in the equation
text = input("Please enter your first product: ")
while text != '':
    products.add(text)
    text = input("Please enter another product or hit enter: ")

# this is gonna ask the user for the inital concentrations of the products
initial_prod = {}
for product in products:
    text = input("Please enter the inital concentration for " + product + ": ")
    initial_prod[product] = float(text)

# this is gonna ask for the equilibrium constant
Keq = input("Please enter your equilibrium constant: ")

reac, prod = balancer(reactants, products)

for key, value in reac.items():
    reac[key] = -value

print(reac)
print(prod)