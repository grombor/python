from random import randrange


def flip():
    # last_toss_result takes random value: 1 or 2
    last_toss_result = randrange(1, 3, 1)

    # actual_toss_result takes random value: 1 or 2
    actual_toss_result = randrange(1, 3, 1)

    # set iteration counter value to 0
    iteration_counter = 0

    while True:
        # start counting loop iterations from 1
        iteration_counter += 1

        # if the toss result will be the same (heads, heads or tails, tails) then flip again
        if last_toss_result == actual_toss_result:
            last_toss_result = actual_toss_result
            actual_toss_result = randrange(1, 3, 1)

        # if toss result will be different then return iteration counter as coin toss counter value
        else:
            # return value of iterations and break the loop
            return iteration_counter
