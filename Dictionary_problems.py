'''

@Author: Joshikaran.k

@Date: 2024-01-19 12:18:50

@Last Modified by: Joshikaran.k

@Last Modified time: 2021-02-11 12:18:59

@Title : array problems in datastructure

'''

Dict = {'z': 10, 'f': 9,
		'u': 15, 'l': 2, 'p': 32}


'''1. Write a Python script to sort (ascending and descending) a dictionary by value.
'''

def dicts(Dict):
    Keys = list(Dict.keys())
    Keys.sort()
    sorted_dict = {i: Dict[i] for i in Keys}
    print(sorted_dict)

dicts(Dict)

