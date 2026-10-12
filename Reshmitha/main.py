def read_secret():
    with open("secret.txt", "r") as f:
        password = f.read().strip()
    check(password)

def check(password):
    return password == "Secret123"

def main():
    read_secret()


if __name__ == "__main__":
    main()