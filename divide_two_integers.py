"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
给定两个整数分别作为被除数和除数，不能使用乘、除、模运算符.
返回dividend除以divisor的商.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2

注意:

返回结果必须介于[−2^31,  2^31 − 1]. 如果溢出就使用边界值.


解题思路：
由于不能使用乘除和模运算，就只有使用减运算符来完成了
最笨的方法当然是用除数一个个减，但是有些情况运算速度就过慢了，例如被除数为边界值，除数为1时
既然除数过小导致运算过慢，那就只有增大除数来解决了~~~

"""


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    res = 0 # 结果
    positive_num = (dividend > 0) is (divisor > 0) # 判断结果为正还是负
    left_border, right_border = -2 ** 31, 2 ** 31 - 1 # 返回值边界
    dividend, divisor = abs(dividend), abs(divisor)
    while dividend >= divisor:
        temp, i = divisor, 1 # 使用一个临时数进行减数运算
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1  # 同下
            temp <<= 1 # 值翻倍
    if not positive_num:
        res = -res
    return min(max(res, left_border), right_border)

print(divide(10, 3))