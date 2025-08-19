def feed(l):
    return 1
l=['1...100','101...200','201...300','301..400']
print(l)
#----------------
def feed(l):
    yield l
l=['1...100','101...200','201...300','301..400']
load=feed(l)
print(load)
#----------------
def feed(l):
    for i in l:
        yield i
l=['1...100','101...200','201...300','301..400']
load=feed(l)
print(next(load))
print(next(load))   
print(next(load))   
print(next(load))
#-----------------
def simple_generator():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End")
gen=simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
