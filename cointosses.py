def toss_coin():
    total_heads = 0
    total_tails = 0
    for attempts in range (5000):
        import random
        random_num = random.random()
        if random_num > .5:
            total_heads += 1
            faceup = "head"
        else:
            total_tails += 1
            faceup = "tail"



        print "Attempt #" + str(attempts + 1) + ": Throwing a coin... It's a " + faceup + "! ... Got " + str(total_heads) + " head(s) so far and " + str(total_tails) + " tail(s) so far"

toss_coin()