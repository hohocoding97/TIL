def power(base, exponent):
    if exponent == 1:
        return base
    else:
        return power(base,exponent-1)*base
result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8

# 모든 자릿수 더하기 함수
def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return sum_of_digits(number//10) + number%10
result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6

