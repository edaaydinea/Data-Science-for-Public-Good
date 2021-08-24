# Enter your code here. Read input from STDIN. Print output to STDOUT
number = int(input())

countries = set()

for i in range(number):
    countries.add(input())
    
print(len(countries))