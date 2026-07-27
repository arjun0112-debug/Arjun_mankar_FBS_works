### Numeric 

#1.int
var = 10

#2.float
var = 3.13

#3.complex
var = 10 + 5j #Real + Imaginary
print(type(var))

### text 

#1. str
var = 'First"bit solutions'
var = "Firstbit solutions"
var = """This is first line.
this is second line."""
print(type(var))

### Sequential

#1. list
var = [10,20,30,40,50]

#2.tuple

var= (10,20,30,40,50)
var = 10,20,30,40,50

#3.range
var = range(1,1000)
print(type(var))

###Set type
#1. set
var = {10,20,30,40,50}

#2.frozenset
var = frozenset({10,20,30,40,50})
var = frozenset([10,20,30,40,50])
print(type(var))


###Mappping
#1 dict
var = {'id':101,'name': 'Arjun', 'sal':300000}
print(type(var))


###other
#1. bool
var = True

#2. None
var = None

print(type(var))