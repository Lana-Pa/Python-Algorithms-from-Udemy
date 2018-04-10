# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
# We want to know whether the number is prime. If number is in the array, then it's prime.
# We might also want to know how many primes are smaller than number. 
# Pseudocode:
#
# 1.Let min = 0 and max = n-1.
# 2.If max < min, then stop: target is not present in array. Return -1.
# 3.Compute guess as the average of max and min, rounded down (so that it is an integer).
# 4.If array[guess] equals target, then stop. You found it! Return guess.
# 5.If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
# 6.Otherwise, the guess was too high. Set max = guess - 1.
# 7.Go back to step 2.

from math import trunc

def binary_search(arr, num):
    minn = 0
    maxx = len(arr)-1
    while minn < maxx:
        guess = trunc((minn+maxx)/2)    # count average          
        
        if arr[guess] == num:
            return guess
            
        elif arr[guess] < num:
            minn = guess + 1
            
        else:
            maxx = guess - 1
              
    else:
        return -1   #return -1 if number is not in array

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 
num = 10
index = binary_search(primes, num)

if index == -1:
    print 'Number',num,'is not prime'
else:
    print 'Number',num,'is prime'
    print index,'numbers are smaller than', num 
