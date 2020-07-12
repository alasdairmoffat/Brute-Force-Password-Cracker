import hashlib


def import_from_file(filename):
    with open(filename, "r") as f:
        contents = f.read().split("\n")

    return contents


def hash_password(password):
    return hashlib.sha1(str.encode(password)).hexdigest()


def crack_sha1_hash(hash, use_salts=False):
    top_passwords = import_from_file("top-10000-passwords.txt")

    if use_salts:
        salts = import_from_file("known-salts.txt")
        for password in top_passwords:
            for salt in salts:
                if hash == hash_password(password + salt) or hash == hash_password(
                    salt + password
                ):
                    return password

    else:
        for password in top_passwords:
            if hash == hash_password(password):
                return password

    return "PASSWORD NOT IN DATABASE"

