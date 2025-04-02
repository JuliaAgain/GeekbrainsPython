"""Напишите прогр, кото выводит на экран числа от 1 до 100.
Вместо чисел, кратных трех, выводить fizz.
кратных пяти buzz
кратно трем и пяти : fizzbuzz"""

print(*("FizzBuzz" if i%15==0
     else "Fizz" if i%3==0
     else "Buzz" if i%5 ==0
     else i
     for i in range(1, 101)))