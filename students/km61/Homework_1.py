#task1------------------------------------------------------------
"""�������� ���������, ������� ��������� ��� ����� � ������� �� �����. ������ ����� �������� � ��������� ������."""
a = int(input())

b = int(input())

c = int(input())

s = a + b + c

print(s)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""�������� ���������, ������� ��������� ����� ���� ������� � ������������� ������������ � ������� ��� �������. ������ ����� �������� � ��������� ������. """
a = int(input())

b = int(input())

c = a * b * (1/2)

print(c)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""�������� ���������, ������� ������������ ������������, ������ ����� Hello, ��������� ��� � ����� ���������� �� �������:  """
print('Hello, ' + input() + '!')

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""�������� ���������, ������� ��������� ����� ����� � ������� �����, ����������� ������������ � ������� (������� �����!).  """
a = int(input())

print('The next number for the number',a, 'is', a+1)

print('The previous number for the number',a, 'is', a-1)

#-----------------------------------------------------------------


#task5------------------------------------------------------------
""" n ���������� ����� k ����� �������, ����������� ������� �������� � ��������. ������� ����� ���������� ������� ���������? ������� ����� ��������� � ��������? ��������� �������� �� ���� ����� n � k � ������ ������� ������� ���������� ����� (��� �����). """
n = int(input())

k = int(input())

a = k // n

b = k % n

print(a,b)

#-----------------------------------------------------------------


#task6------------------------------------------------------------
""" ������� ������� ���������� ������ ������ ������� ������ �������. ������� ��� �������� ����� ����������� � ��� ����, ���������� ����� ������ ����� a, � ���������� ����� ��������� � ���� b. ���������� ������� � ������ ���� ����� N. �������� ������ ����������� ������� �������� �������, �� ����������� � ������ ���, ������, �� ����������� � �.�.� (��. �������). ����� ����, ����� ������ ����� ���� �������� ������� ��������, ����� ���������� ����� ������ ������ ���� l

. ������ ������ ���� ����� ������ ��� ���� �������?

��������� �������� �� ���� ������ ����������� ����� a
, b, l � N - ������ � ����� ������� - � ������ ������� ���� ����� - ������� ����� ������. """
a = int(input())

b = int(input())

l = int(input())

N = int(input())

c = a + (2 * a + 2 * b) * (N - 1) + 2 * l

print(c)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""� ����� ������ ������� ��� ����� �������������� ������. ��� ��� ������� �� ���������� � ��� �������� � ���� � �� �� �����, ���� ������ �������� ������� ��� ������� ������ � ������ � ��� ����� �����. �� ������ ������ ����� ������ �� ������ ���� ��������. �������� ���������� �������� � ������ �� ��� �������. ������� ����� ����� �������� ���� ����� �� ������� �� ���� ��������? ��������� �������� �� ���� ��� ����������� �����: ���������� �������� � ������ �� ���� �������.  """
b = int(input())

c = int(input())

s = a // 2 + b // 2 + c // 2 + (a % 2) + (b % 2) + (c % 2)

print(s)

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""���� ����� n. � ������ ����� ������ n �����. ����������, ������� ����� � ����� ����� ���������� ����������� ���� � ���� ������. ��������� ������ ������� ��� �����: ���������� ����� (�� 0 �� 23) � ���������� ����� (�� 0 �� 59). ������, ��� ����� n ����� ���� ������, ��� ���������� ����� � ������.  """
n = int(input())

a = n // 60

b = n % 60

c = a % 24

print (c,b)

#-----------------------------------------------------------------
