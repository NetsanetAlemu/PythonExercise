class Solution(object):
    def fizzBuzz(self, n):
        result = []
        if 1 <= n <= 10000:
            for i in range(1, n + 1):
                if i % 3 == 0 and i % 5 == 0:
                    result.append('FizzBuzz')
                elif i % 3 == 0:
                    result.append('Fizz')
                elif i % 5 == 0:
                    result.append('Buzz')
                else:
                    result.append(str(i))
        return result
        

try:
    n = int(input('Enter a natural number less than 10,000: '))
except ValueError as e:
    print(e)
else:
    solution1 = Solution()
    print(solution1.fizzBuzz(n))
    
