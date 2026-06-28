import secrets
import string


def generate_password(length):
    # Define the character pools
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # !, @, #, $, etc.

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate a secure random password of the specified length
    password = "".join(secrets.choice(all_characters) for _ in range(length))

    return password


def main():
    print("--- Welcome to the Secure Password Generator ---")

    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("For better security, please choose a length of at least 4.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate the password
    password = generate_password(length)

    # Display the password
    print("\n------------------------------------------------")
    print(f"Your generated password is: {password}")
    print("------------------------------------------------")


if __name__ == "__main__":
    main()