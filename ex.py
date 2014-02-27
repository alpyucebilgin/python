import os
clear = lambda : os.system('clear')
clear()

# basic string op
hello = "Hello World"
print hello +' -- Last Letter:'+  hello[-1] + ' and length is:' + str(len(hello))

# List
list = [ "this", "is" ,"list" ]
list[0:0] = ["list", "insert", "here"]
# delete from list
list[4:] = []
del list[3]
print list

# range(10) generates list with 1 to 10 ints
# basic for loop
tempStr = ''
for w in list:
     tempStr += w + " " + str(len(w)) + " "
print tempStr

# functions
def fib(n): # print fib series until integer n
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
fib(200)

# filter
print "Numbers between 2-25, NOT divisble by 2 or 3",
def f(n):
    return n % 2 != 0 and n % 3 != 0
print filter(f, range( 2, 25 ))

# iterating in loops
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v, " ",
print ""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v, " ",
