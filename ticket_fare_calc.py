print("🚍 Welcome to the Bus Ticket Fare Calculator 🚍")
print("Base fare is ₹100. Age-based discounts apply.\n")

age = int(input("Enter your age: "))

if age < 0:
    print("❌ Invalid age! Please enter a valid number.")
elif age <= 5:
    print("👶 Age below 5: Ticket is FREE!")
    print("Final Fare: ₹0")
elif age <= 18:
    print("🧒 Child Fare (50% off)")
    print("Final Fare: ₹", 100 * 0.5)
elif age >= 60:
    print("👴 Senior Citizen Fare (70% off)")
    print("Final Fare: ₹", 100 * 0.3)
else:
    print("🧑 Regular Fare")
    print("Final Fare: ₹100")

