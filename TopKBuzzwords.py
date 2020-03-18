numToys = 6
topToys = 3
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]


import re
import heapq


def topKBuzzwords(numToys, topToys, toys, numQuotes, quotes):
    memo = dict([toy, [0,0]] for toy in toys)
    for quote in quotes:
        words = quote.lower().split()
        quote_once = dict([toy, True] for toy in toys)
        # TODO:
        # words = re.findall('\w+', quote.lower())
        for word in words:
            word = re.sub('[^a-z]', '', word)
            if word in memo:
                memo[word][0] += 1
                memo[word][1] += quote_once[word]
                quote_once[word] = False
    print(memo)

    if topToys > numToys:
        output = []
        for toy in memo:
            if memo[toy][0] != 0:
                output.append((memo[toy][0], memo[toy][1], toy))
        output.sort(reverse=True)
        return [toy[2] for toy in output]

    tmp = []
    output = []
    for toy in memo:
        tmp.append((-memo[toy][0], -memo[toy][1], toy))
    heapq.heapify(tmp)
    for _ in range(topToys):
        output.append(heapq.heappop(tmp)[2])
    return output

'''
Time Complexity: O(N * M); N = number of total quotes, M = maximum number of words in a quote (among all quotes)
----
- While creating toy_freq_quote dict, we go through all quotes and check each word of every quote.
    - This takes O(N * M) time

- While doing heapify operation, we will have at the most T number of elements in the list
    - Here, T = total number of toys.
    - This T value will be much less compared to N*M

- Heapify will take O(T) time
- After that we will perform heappop() for K times. Here K = number of topToys.
- Hence heappop will take O(K logT) for K elements

- So overall time is: O(N*M) + O(T) + O(K logT)
    - Now, K (topToys) ≤ T (totalToys)

- Therefore, time is: O(N*M) + O(T) + O(T logT)
    - As discussed above, T will be much less than M*N

- Hence, overall time complexity is O(N * M)


Space Complexity: O(T); T = total number of toys
----
- In case where each toy from the toys list is present in the quptes, toy_freq_quote will be of size O(T)
- Similarly, heap will also have T elements at the most
'''


print(topKBuzzwords(numToys, topToys, toys, numQuotes, quotes))
