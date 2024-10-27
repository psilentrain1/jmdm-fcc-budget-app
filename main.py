class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": amount * -1, "description": description})
            return True

    def get_balance(self):
        balance = sum([x["amount"] for x in self.ledger])
        return balance

    def transfer(self, amount, toCategory):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append(
                {"amount": amount * -1, "description": f"Transfer to {toCategory.name}"}
            )
            toCategory.ledger.append(
                {"amount": amount, "description": f"Transfer from {self.name}"}
            )
            return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def get_total_spent(self):
        expenses = []
        for x in self.ledger:
            if x["amount"] < 0:
                expenses.append(x["amount"] * -1)
        return sum(expenses)

    def __str__(self):
        heading = ""
        transaction_list = []
        transactions = ""
        chars = 30 - len(self.name)
        if chars % 2:
            heading = self.name.rjust(int(chars / 2 + 1.5) + len(self.name), "*").ljust(
                30, "*"
            )
        else:
            heading = self.name.rjust(int(chars / 2) + len(self.name), "*").ljust(
                30, "*"
            )

        for x in self.ledger:
            desc = str(x["description"])[:23]
            amount = "{:.2f}".format(x["amount"]).rjust(30 - len(desc), " ")

            transaction_list.append(desc + amount + "\n")

        transactions = "".join(transaction_list)
        return str(f"{heading}\n{transactions}Total: ") + "{:.2f}".format(
            self.get_balance()
        )


def create_spend_chart(categories):

    numberCategories = len(categories)
    categoryNames = []
    categoryNamesPad = []
    categoryTotals = []
    categoryPercentages = []

    line100 = ""
    line90 = ""
    line80 = ""
    line70 = ""
    line60 = ""
    line50 = ""
    line40 = ""
    line30 = ""
    line20 = ""
    line10 = ""
    line0 = ""

    for x in categories:
        categoryNames.append(x.name)
        categoryTotals.append(x.get_total_spent())
    nameLen = len(max(categoryNames, key=len))
    for x in categoryNames:
        categoryNamesPad.append(x.ljust(nameLen, " "))
    totalSpend = sum(categoryTotals)
    for x in categoryTotals:
        categoryPercentages.append(int((x / totalSpend) * 10) * 10)

    barFull = "o  "
    barNone = "   "
    for p in categoryPercentages:
        line100 = (line100 + barFull) if p == 100 else (line100 + barNone)
        line90 = (line90 + barFull) if p >= 90 else (line90 + barNone)
        line80 = (line80 + barFull) if p >= 80 else (line80 + barNone)
        line70 = (line70 + barFull) if p >= 70 else (line70 + barNone)
        line60 = (line60 + barFull) if p >= 60 else (line60 + barNone)
        line50 = (line50 + barFull) if p >= 50 else (line50 + barNone)
        line40 = (line40 + barFull) if p >= 40 else (line40 + barNone)
        line30 = (line30 + barFull) if p >= 30 else (line30 + barNone)
        line20 = (line20 + barFull) if p >= 20 else (line20 + barNone)
        line10 = (line10 + barFull) if p >= 10 else (line10 + barNone)
        line0 = (line0 + barFull) if p >= 0 else (line0 + barNone)

    underline = "".ljust(numberCategories * 3, "-")
    vertTitlePad = "     "
    vertTitles = ""
    yAxis = 0
    while yAxis < nameLen:
        vertTitles = vertTitles + vertTitlePad
        for n in categoryNamesPad:
            vertTitles = vertTitles + n[yAxis] + "  "
        vertTitles = vertTitles + "\n"
        yAxis += 1
    vertTitles = vertTitles[:-1]

    finalString = f"Percentage spent by category\n100| {line100}\n 90| {line90}\n 80| {line80}\n 70| {line70}\n 60| {line60}\n 50| {line50}\n 40| {line40}\n 30| {line30}\n 20| {line20}\n 10| {line10}\n  0| {line0}\n    -{underline}\n{vertTitles}"

    print(finalString)


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
