### Budget App

An app to create a ledger of income and expenses based on categories.

#### Using the Budget App

Create deposits, withdrawals, and transfers.
Use `create_spend_chart([<List of categories>])` to print a chart of budget percentages.

#### Test Cases

```
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.withdraw(123.84, "dinner date")
food.withdraw(210.35, "family dinner")
food.withdraw(225.04, "rehearsal dinner")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(500, "deposit")
clothing.withdraw(12.85, "shirt")
clothing.withdraw(21.12, "jeans")
clothing.withdraw(220.00, "tuxedo")
bills = Category("Bills")
bills.deposit(2000, "deposit")
bills.withdraw(1250, "rent")
bills.withdraw(100, "water")
bills.withdraw(150, "cable")
bills.withdraw(95, "phone")
print(food, "\n")
print(clothing, "\n")
print(bills, "\n")

create_spend_chart([food, clothing, bills])
```

Will output:

```
*************Food*************
deposit                1000.00
groceries               -10.15
restaurant and more foo -15.89
dinner date            -123.84
family dinner          -210.35
rehearsal dinner       -225.04
Transfer to Clothing    -50.00
Total: 364.73

***********Clothing***********
Transfer from Food       50.00
deposit                 500.00
shirt                   -12.85
jeans                   -21.12
tuxedo                 -220.00
Total: 296.03

**************Bills***********
deposit                2000.00
rent                  -1250.00
water                  -100.00
cable                  -150.00
phone                   -95.00
Total: 405.00

Percentage spent by category
100|
 90|
 80|
 70|
 60|       o
 50|       o
 40|       o
 30|       o
 20| o     o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  B
     o  l  i
     o  o  l
     d  t  l
        h  s
        i
        n
        g
```

#### freeCodeCamp Disclaimer

This project was completed as part of [freeCodeCamp.org](https://www.freecodecamp.org)'s _Scientific Computing with Python_ course. This was a Certification Project, meaning [freeCodeCamp](https://www.freecodecamp.org) provided specifications and limited guidance and I was expected to code to meet certain test cases. The code presented here is my own.
