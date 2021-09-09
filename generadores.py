# Un generador es una funcion que tiene poderes especiales

def my_gen():
    a = 1
    yield a

    a = 2
    yield a

    a = 3
    yield a


my_first_gen = my_gen()
my_second_gen = my_gen()

print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))

# Generador que obtenga los 100 numeros pares
def challenge():
    for i in range(1,101):
        if i % 2 == 0:
            yield i

my_challenge = challenge()

for i in range(101):
    print(next(my_challenge))
        