

Trying to count up ways to break an array of integers to three non-empty subarrays of equal sum.
1 <= n <= 5 * 10 ^ 6 where n is array size.
abs(a[i]) <= 10 ^ 9 where a[i] is array element.

Big-O for the algorithm is O(n) because there are three unnested loops so we can get rid of the constant in O(3n).
Also we don't consider if statements and variables assignment as each of them has a constant time - O(1).

P.S.: Using standard io.
