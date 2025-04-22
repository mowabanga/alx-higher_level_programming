#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0): 
        return None
    else:
        return ("Length: {:d} - First character: {}".format(len(sentence), sentence[:1]))
    
print(multiple_returns("At school, I learnt C!"))