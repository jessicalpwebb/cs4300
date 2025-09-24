#checking if number is odd,even, or zero w/out user input
def test_numbers():

    num = 5

    if num == 0:
        print("number is 0")
    elif num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

#Sieve of Eratosthenes algorithm
def test_primes():
    n = 3000 
    A = [True] * (n + 1)
    A[0] = A[1] = False
    count = 0 

    for i in range(2, n + 1):
        if A[i]:
            print(i, end=" ")
            count += 1

            if count == 10:
                break

            for j in range(i*i, n + 1, i):
                A[j] = False

test_primes()

# function to add first 100 numbers
def test_addnumbers():
    sum = 0
    inc = 0

    while inc <=100:
        sum = sum + inc
        inc = inc + 1
    
    print(sum)
test_addnumbers()