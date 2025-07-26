print("🔌 Welcome to the Electricity Bill Generator 🔌")
print("\n  Rates:")
print("  • First 100 units – ₹5/unit")
print("  • Next 100 units (101–200) – ₹7/unit")
print("  • Above 200 units – ₹10/unit\n")

units = int(input("Enter total electricity units consumed: "))

if units < 0:
    print(" Invalid unit value! Units can't be negative.")
elif units <= 100:
    bill = units * 5
    print(" First 100 units slab applied.")
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print(" First 200 units slab applied.")
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print(" Full slab (Above 200 units) applied.")

if units >= 0:
    print(f" Total Bill Amount: ₹{bill}")
