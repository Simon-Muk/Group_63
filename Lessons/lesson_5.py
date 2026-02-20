class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"<Money amount={self.amount}>"

    # eq -> ==
    def __eq__(self, other):
        print(other)
        if self.amount == other.amount:
            return True
        return False


money_simon = Money(100)
money_igor = Money(200)
print(money_simon)
print(money_igor)
