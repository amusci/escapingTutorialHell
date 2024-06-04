'''

Given a square matrix (i.e. same number of rows as columns),

its trace is the sum of the entries in the main diagonal

(i.e. the diagonal line from the top left to the bottom right).

As an example, for:

[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

... the trace is 1 + 5 + 9 = 15.
'''

def trace(lst):
    ans = []

    for i in range(len(lst)):
        ans.append(lst[i][i])

    return sum(ans)