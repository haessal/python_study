import secrets

def generate_private_key():
    return secrets.randbits(256)

if __name__ == "__main__":
    i = generate_private_key()
    print(i)
