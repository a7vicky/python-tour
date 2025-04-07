import os
def get_age():
    try:
        age = int(os.sys.argv[1])
    except IndexError:
        print("❌ No age provided.")
        return
    except ValueError:
        print("❌ Invalid age format. Please enter a number.")
        return
    try:
        # Simulating a potential error
        # For example, if age is negative
        if age < 0:
            raise ValueError("Age can't be negative.")
        print(f"You are {age} years old.")
    except ValueError as e:
        print("❌ Invalid input:", e)

if __name__ == "__main__":
    get_age()