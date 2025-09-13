def greet_user(name):
    print(f"Hello {name}!")

def main():
    user_name = input("What's your name?")
    greet_user(user_name)
    
if __name__ == "__main__":
    main()