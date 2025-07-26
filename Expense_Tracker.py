import numpy as np

# Pre-decided categories (can be edited easily)
expense_heads = np.array(["Rent", "Food", "Bills", "Travel", "Fun", "Misc"])

def get_expense_data(categories):
    data = []
    print("\nMonth-wise Kharcha Input:")
    for item in categories:
        try:
            amount = float(input(f"  {item} ka kharcha: ₹"))
        except ValueError:
            print("  Invalid input. Defaulting to ₹0.")
            amount = 0.0
        data.append(amount)
    return np.array(data)

def show_summary(categories, data):
    total = data.sum()
    average = data.mean()
    max_index = data.argmax()
    min_index = data.argmin()

    print("\n🧾 Your Monthly Expense Summary")
    print("-" * 40)
    for i in range(len(categories)):
        print(f"{categories[i]:<12} : ₹{data[i]:>7.2f}")
    print("-" * 40)
    print(f"{'Total':<12} : ₹{total:>7.2f}")
    print(f"{'Average':<12} : ₹{average:>7.2f}")
    print(f"Most Spent On  : {categories[max_index]} (₹{data[max_index]:.2f})")
    print(f"Least Spent On : {categories[min_index]} (₹{data[min_index]:.2f})")

def start_tracker():
    print("=" * 38)
    print("      WELCOME TO EXPENSE TRACKER")
    print("=" * 38)
    user_expenses = get_expense_data(expense_heads)
    show_summary(expense_heads, user_expenses)

if __name__ == "__main__":
    start_tracker()
