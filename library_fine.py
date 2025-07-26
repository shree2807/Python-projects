print("Library Fine Calculator")
print("------------------------")
print("Fine Rules:")
print("  - No fine for 0 days")
print("  - ₹2 per day for 1–5 days")
print("  - ₹5 per day for 6–10 days")
print("  - ₹10 per day after 10 days\n")

days = int(input("Enter number of overdue days: "))

if days < 0:
    print("Invalid input! Days cannot be negative.")
elif days == 0:
    print("No fine. Book returned on time.")
    print("Total Fine: ₹0")
elif days <= 5:
    fine = days * 2
    print("You are", days, "days late. Fine: ₹2 per day.")
    print("Total Fine: ₹", fine)
elif days <= 10:
    fine = (5 * 2) + ((days - 5) * 5)
    print("You are", days, "days late. ₹2/day for first 5 days, ₹5/day for next days.")
    print("Total Fine: ₹", fine)
else:
    fine = (5 * 2) + (5 * 5) + ((days - 10) * 10)
    print("You are", days, "days late.")
    print("₹2/day for 1–5 days, ₹5/day for 6–10 days, ₹10/day after that.")
    print("Total Fine: ₹", fine)
