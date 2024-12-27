# Function to check if a string is a palindrome
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Main function
def main():
    print("Palindrome Checker")
    input_string = input("Enter a word or phrase: ")
    
    if is_palindrome(input_string):
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")

# Run the program
if __name__ == "__main__":
    main()
