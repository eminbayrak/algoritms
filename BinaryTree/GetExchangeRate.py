'''
Google | Phone | Currency Conversion

Question
Paramenters:

    array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
    an array containing a 'from' currency and a 'to' currency

Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
Your return value should be a number.

Example:
You are given the following parameters:

    Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
    To/From currency ['GBP', 'AUD']

Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.

Related problems:

    https://leetcode.com/problems/evaluate-division/

'''


from collections import defaultdict
from collections import deque


def getRatio(start, end, data):
    dict = defaultdict(list)
    for node in data:
        dict[node[0]].append([node[1], node[2]])
        dict[node[1]].append([node[0], 1.0 / node[2]])
    queue = deque()
    queue.append((start, 1.0))
    visited = set()
    while queue:
        currency, num = queue.popleft()
        if currency in visited:
            continue
        visited.add(currency)
        if currency in dict:
            values = dict.get(currency)
            next = {}
            for val in values:
                next[val[0]] = val[1]
            for key in next:
                if key not in visited:
                    if key == end:
                        return num * next[key]
                    queue.append((key, num * next[key]))
    return -1


data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
print(getRatio("GBP", "AUD", data))