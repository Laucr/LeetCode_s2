def fizz_buzz(n):
    ret = []

    def fizz(num):
        if num % 3 == 0:
            if num % 5 != 0:
                return "Fizz"
            else:
                return "FizzBuzz"
        else:
            return buzz(num)

    def buzz(num):
        if num % 5 == 0:
            return "Buzz"
        else:
            return str(num)
    for i in range(1, n + 1):
        ret.append(fizz(i))
    return ret

print fizz_buzz(15)