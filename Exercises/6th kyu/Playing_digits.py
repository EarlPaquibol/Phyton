# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


# def dig_pow(a, b):
#     temp = [int(e) for e in str(a)]
#     total = 0
#     for i, e in enumerate(temp, start=b):
#         total += e**i
#     return int(total/a) if total%a == 0 else -1


# print(dig_pow(92, 1))

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n), start=1):
     s += pow(int(c),i)
  return s/n if s%n==0 else -1



print(dig_pow(92, 1))
