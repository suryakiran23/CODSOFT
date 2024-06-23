import random
import string

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length should be at least 1")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def include_characters():
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == 'yes'
    
    return include_uppercase, include_digits, include_punctuation

def build_character_set(include_uppercase, include_digits, include_punctuation):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    return characters

def generate_password(length, characters):
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    length = get_user_input()
    
    # Ask user which types of characters to include
    include_uppercase, include_digits, include_punctuation = include_characters()
    
    # Build the character set based on user preferences
    characters = build_character_set(include_uppercase, include_digits, include_punctuation)
    
    # Generate the password
    password = generate_password(length, characters)
    
    # Display the password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
