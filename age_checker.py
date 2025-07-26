print("🧾 AGE CHECKER MENU")
print("1. Check Voting Eligibility")
print("2. Check Driving Eligibility")
print("3. Exit")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("✅ You are eligible to vote.")
    elif age >= 0:
        print("❌ You are NOT eligible to vote.")
    else:
        print("❌ Invalid age!")

elif choice == 2:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("✅ You are eligible to apply for a driving license.")
    elif age >= 16:
        print("🚦 You can ride a gearless scooter (with guardian approval).")
    elif age >= 0:
        print("❌ You are NOT eligible for any driving.")
    else:
        print("❌ Invalid age!")

elif choice == 3:
    print("👋 Exiting program. Goodbye!")

else:
    print("⚠️ Invalid choice! Please enter 1, 2, or 3.")
