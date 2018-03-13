import hashlib

def sha256encode(message):
    return hashlib.sha256(message.encode()).hexdigest()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        message = sys.argv[1]
        hashstr = sha256encode(message);
        print(hashstr)
