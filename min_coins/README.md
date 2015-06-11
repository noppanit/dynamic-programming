# Minimum change problem.

The problem is to find the minimum number of coins to give change. Here's the full version of problem.

Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it’s not possible to select coins in such a way that they sum up to S.

## Algorithm

```
Set Min[i] equal to Infinity for all of i
Min[0]=0

For i = 1 to S
For j = 0 to N - 1
   If (Vj<=i AND Min[i-Vj]+1<Min[i])
Then Min[i]=Min[i-Vj]+1

Output Min[S]
```

## Reference

- [Dynamic Programming](http://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html)
