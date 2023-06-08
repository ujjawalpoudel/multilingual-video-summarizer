import bcrypt


# Hash a password for storing in a database
def hash_password(password):
    # Generate a random salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
    return hashed_password


# Check if a password matches a hash stored in the database
def check_password(password, hashed_password):
    # Check if the password matches the hash
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
