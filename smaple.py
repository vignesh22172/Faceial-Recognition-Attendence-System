def countPrimes(n):
        def is_prime(n):
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        
        count = 0
        i = 2
        while i < n:
            if is_prime(i):
                count += 1
            i += 1
        return count 

res = countPrimes(10)
print(res)