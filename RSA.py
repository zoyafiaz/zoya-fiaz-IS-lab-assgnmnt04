# ===== TASK 1: SIMPLE RSA WITHOUT LIBRARIES =====

# function to compute gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# function to compute modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 0 :
            pass
    return d

# key generation using small primes
def generate_keys():
    p = 11
    q = 13
    n = p * q
    phi = (p - 1) * (q - 1)

    # choose e
    e = 7  # gcd(7,120)=1 so it's valid

    # compute d
    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# encryption
def encrypt(msg, public_key):
    e, n = public_key
    cipher = [(ord(ch) ** e) % n for ch in msg]
    return cipher

# decryption
def decrypt(cipher, private_key):
    d, n = private_key
    plain = "".join([chr((c ** d) % n) for c in cipher])
    return plain

# testing
public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Zoya"
ciphertext = encrypt(message, public_key)
print("Encrypted:", ciphertext)

decrypted = decrypt(ciphertext, private_key)
print("Decrypted:", decrypted)