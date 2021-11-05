from multiprocessing import Pool

def is_prime(number):
    if number == 2 or number == 3:
        return number, True
    if number % 2 == 0 or number < 2:
        return number, False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            continue
    return number, True

def calcular_primos(a, b):
    return filter(lambda x: x[1]==True, list(map(is_prime, range(a, b))))

if __name__ == '__main__':
    numbers = range(500000000)
    pool = Pool(processes=8)
    print(pool.map(is_prime, numbers)[-1])