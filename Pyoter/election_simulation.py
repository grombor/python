from random import randrange

#result list
election_result = []

def region_result(n):
    # compare chance (n) with 0-100 random number
    if n >= randrange(0, 101):
        # if candidate won the election in the region, return 1
        return 1
    else:
        # else return 0
        return 0

def election():
    # generate the list with 3 election results based on precentage chance of win
    election_result.append(region_result(87))
    election_result.append(region_result(65))
    election_result.append(region_result(17))

    #return election_result, value 1 means that candidate won
    if sum(election_result) > 1:
        return 1
    else:
        return 0
