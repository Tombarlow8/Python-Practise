


def e_sieve(value):
    ''''Sieve_of_Eratosthenes'
       Prints all the prime numbers upto 'value' and returns a list
       >>> print(e_sieve(20))
       ... [2, 3, 5, 7, 11, 13, 17, 19]
    '''
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    prime_list = []
    p = 2
    prime_list.append(p)
    prime_list.append(5)
    for num in range(p,value):
        if num % p != 0 and num != p and num % 5 != 0 and num != 5:
            prime_list.append(num)

    p = 3
    while p*p < value:
        for number in prime_list:  
            if number != p and number % p == 0:   
                prime_list.remove(number)
                
        p +=1

    return prime_list

print(e_sieve(100))
