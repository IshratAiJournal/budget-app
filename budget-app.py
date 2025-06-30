# -------------------------------------------------
#  Budget App – Category class
# -------------------------------------------------
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt  = f"{entry['amount']:>7.2f}"
            items += f"{desc:<23}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


# -------------------------------------------------
#  create_spend_chart  (function – NOT in class)
# -------------------------------------------------
def create_spend_chart(categories):
    """
    Returns a bar chart of percentage spent by category
    with exact spacing to satisfy FreeCodeCamp tests.
    """

    # Step 1 – total spent per category
    spent = []
    for cat in categories:
        s = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(s)
    total_spent = sum(spent)

    # Step 2 – percentages rounded down to nearest 10
    percents = [int((x / total_spent) * 10) * 10 for x in spent]

    # Step 3 – bar lines 100 → 0
    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for p in percents:
            chart += " o " if p >= level else "   "
        chart += " \n"

    # Step 4 – dash line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Step 5 – vertical names (FreeCodeCamp‑exact spacing)
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "     "                        # 5 leading spaces
        for cat in categories:
            char = cat.name[i] if i < len(cat.name) else " "
            row += char + "  "               # char + two spaces
        if i < max_len - 1:                  # newline on every row except last
            chart += row + "\n"
        else:                                # last row: no newline
            chart += row
    return chart


# -------------------------------------------------
#  Quick manual test (optional)
# -------------------------------------------------
if __name__ == "__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    food.deposit(900, "deposit")
    food.withdraw(105.55, "groceries")
    food.withdraw(33.40, "restaurant")

    clothing.deposit(900, "deposit")
    clothing.withdraw(75.25, "jeans")
    clothing.withdraw(25.75, "t-shirt")

    auto.deposit(900, "deposit")
    auto.withdraw(15.00, "gas")
    auto.withdraw(35.00, "oil change")

    print(create_spend_chart([food, clothing, auto]))
