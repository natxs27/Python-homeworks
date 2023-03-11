Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Explain the results.
>>> x = 5
>>> x == 5 and 3 #3 - x ma wartość 5, więcfunkcja and zwraca True dla x == 5, po czym podaje wartość po and
3
>>> x == 4 and 3 # False - x ma wartość 5, funkcja zwraca False dla x == 5 i nie liczy dalej
False
>>> 3 and x == 5 # True - funkcja ocenia argument po and ponieważ 3 nie daje False, x jest ma wartość 5 więc x == 5 zwraca True, natomiast przy x == 4 zwraca False
True
>>> 3 and x == 4 # False
False
>>> isinstance(True, int) # True
True
