class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # in python every number return True except 0
        # return ['Fizz' *(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,n+1)]

        result = []
        
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                result.append('FizzBuzz')
            elif i%3==0:
                result.append('Fizz')
            elif i%5==0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
        