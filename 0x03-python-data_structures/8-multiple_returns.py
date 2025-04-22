#!/usr/bin/python3
def multiple_returns(sentence):
    return ("Length: {:d} - First character: {}".format(len(sentence), sentence[:1]))
    
print(multiple_returns("At school, I learnt C!"))