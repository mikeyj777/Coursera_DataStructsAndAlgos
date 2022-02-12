# Uses python3
import sys
import copy
import numpy as np

winners = []
solns = {}
def calculator(target, n=1, calc_chain = []):
    global winners, solns
    calc_chain.append(n)
   
    if n == target:
        winners.append(calc_chain)
        for i in calc_chain:
            if i in solns.keys():
                if len(calc_chain[i:]) < len(solns[i]):
                    solns[i] = [i] + calc_chain[i:]
            else:
                solns[i] = [i] + calc_chain[i:]
    if n < target:
        inputs = [n + 1, n * 2, n * 3]
        if min(inputs) <= target:
            for inp in inputs:
                if inp <= target:
                    if inp in solns.keys():
                        if solns[inp][-1] == target:
                            calc_chain.extend(solns[inp])
                            winners.append(calc_chain)
                    else:
                        calculator(target, inp, copy.deepcopy(calc_chain))

def calc_handler(n):
    calculator(n)
    shortest_chain = np.inf
    shortest_idx = -1
    for i in range(len(winners)):
        if len(winners[i]) < shortest_chain:
            shortest_chain = len(winners[i])
            shortest_idx = i
    return winners[shortest_idx]




# input = sys.stdin.read()
# n = int(input)

n = 5

output = calc_handler(n)
print(len(output) - 1)
for x in output:
    print(x, end=' ')
