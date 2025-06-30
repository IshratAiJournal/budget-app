# Budget App 💰📊

This is **Project 3** from FreeCodeCamp’s *Scientific Computing with Python* certification.

### 📖 What it does
This project builds a simple budgeting system using **Python classes**.  
You can create budget categories (like Food, Clothing, etc.), track spending, and generate a **text-based chart** showing spending percentages.

### 🔧 Features

- ✅ Create and name budget categories  
- 💵 Deposit and withdraw funds  
- 🔁 Transfer money between categories  
- 📊 Generate a spend chart (in text format)

### 🧠 Skills practiced

- Object-Oriented Programming (OOP) in Python  
- Classes, methods, and constructors  
- Data handling with lists and dictionaries  
- String formatting and logic  
- Percentage calculations

### 🔁 Example Usage

```python
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.transfer(50, clothing)

print(food)
print(clothing)

print(create_spend_chart([food, clothing]))
