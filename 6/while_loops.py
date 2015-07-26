n  = 1000
numbers = range(2, n)
results = []
while numbers:
    i = numbers[0]
    results.append(i)
    for number in numbers:
        if number % i == 0:
            numbers.remove(number)
 
print numbers
print len(results)