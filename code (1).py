import sys

def main():
    expenses = []
    categories = ["Food", "Travel", "Academics", "Entertainment", "Misc"]
    
    print("--- Welcome to the Student Expense Tracker ---")
    
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. Get Spending Summary")
        print("4. Find Highest & Lowest Expense")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                print(f"Categories: {categories}")
                cat = input("Enter category: ").capitalize()
                
                if cat not in categories:
                    print("Category not found. Added to 'Misc'.")
                    cat = "Misc"
                
                # Storing as a dictionary (Data Structure)
                expenses.append({"amount": amount, "category": cat})
                print("Expense added successfully!")
            except ValueError:
                print("Invalid input! Please enter a numeric value for the amount.")

        elif choice == '2':
            if not expenses:
                print("\nNo expenses recorded yet.")
            else:
                print("\n--- Expense List ---")
                for i, exp in enumerate(expenses, 1):
                    print(f"{i}. {exp['category']}: ${exp['amount']}")

        elif choice == '3':
            if not expenses:
                print("\nNo data to summarize.")
            else:
                total = sum(item['amount'] for item in expenses)
                print(f"\nTotal Spending: ${total:.2f}")
                print(f"Average Expense: ${total/len(expenses):.2f}")

        elif choice == '4':
            if not expenses:
                print("\nNo data available.")
            else:
                # Logic for finding Min and Max (Core Problem Solving)
                amounts = [e['amount'] for e in expenses]
                print(f"Highest Expense: ${max(amounts)}")
                print(f"Lowest Expense: ${min(amounts)}")

        elif choice == '5':
            print("Exiting tracker. Happy budgeting!")
            sys.exit()

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
