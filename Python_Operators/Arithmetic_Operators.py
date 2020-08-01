a = "Operators are used to perform operations on variables and values.\\\
Python divides the operators in the following groups:\\\
\n "+" \\\
\n Assignment operators\\\
\n Comparison operators\\\
\n Logical operators\\\
\n Identity operators\\\
\n Membership operators\\\
\n Bitwise operators "
print(a)
# if condition with arithmetic operator.
# x = (5 > 3 or 5 > 10)
print("Enter Value")
x = input()
x = int(x)
# if 5 > 3 or 5 > 10:
if (x > 3 | x < 10):
    print("At least one of the statements are True")
else:
    print("None of the statements are True")
