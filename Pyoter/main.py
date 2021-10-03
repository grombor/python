import coin_toss
from election_simulation import election


# number of simulation runs
n = 10000

# list of toss results
results = []

#############################
# fair coin toss simulation #
#############################

# simulate fair coin toss n times
for i in range(0, n):
    results.append(coin_toss.flip())

# print averange iteration
print("averange iterations: ")
print(sum(results)/len(results))


#######################
# election simulation #
#######################

# zeroing the results
results = 0

# starting simulation
for i in range(0, n):
    results += election()
print("\nPrecentage chances of win [in %]: ")
print((results/n)*100)
