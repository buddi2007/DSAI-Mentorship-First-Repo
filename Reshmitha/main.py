def read_secret():
    with open("password.txt", "r") as f:
        password = f.read().strip()
    check(password)


def check(password):
    return True

def main():
    read_secret()


if __name__ == "__main__":
    main()