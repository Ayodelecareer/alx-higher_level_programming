#!/usr/bin/python3
def multiple_returns(texts):
    if len(texts) == 0:
        return (0, None)
    else:
        return (len(texts), texts[0])
