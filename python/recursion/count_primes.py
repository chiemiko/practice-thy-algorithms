"""
Given an integer n, return the number of prime numbers that are strictly less than n.

ie
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""


class Solution:
    def is_divisible_by(self, numer, denom):
        if numer % denom == 0:
            return True
        else:
            return False

    def isprime(self, n):
        end = int(n**.5) + 1
        if n < 2:
            return False
        if n == 2:
            return True
        for num in range(2,end):

            if self.is_divisible_by(n, num) == True:
                return False
        
        return True

    def countPrimes(self, n: int) -> int:
        """ 
        
        0 1 2 3 4 5 6 7 8 9 10
        -----------
        0 0 1

        """
        def get_primes_less_than_recursion(i, curr_count):
            if i == n:
                return curr_count
            
            # print(f'i: {i}')
            # print(f'curr_count: {curr_count}')

            if self.isprime(i):
                curr_count += 1
            return get_primes_less_than_recursion(i+1, curr_count)
        
        return get_primes_less_than_recursion(i=1, curr_count=0)
        
# print(Solution().countPrimes(0) == 0)
# print(Solution().countPrimes(1) == 0)
print(Solution().countPrimes(10) == 4)

# O(n)