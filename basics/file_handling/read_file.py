try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("❌ The file was not found.")
except IOError:
    print("❌ An I/O error occurred.")
finally:
    print("✅ File operation attempted.")