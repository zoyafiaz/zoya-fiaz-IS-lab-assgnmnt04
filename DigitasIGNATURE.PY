import hashlib

# Reuse RSA from Task 1
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keys():
    p = 11
    q = 13
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 7  # gcd(7,120)=1

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

def hash_message(msg):
    h = hashlib.sha256(msg.encode()).hexdigest()
    return int(h, 16)

def sign_message(msg, private_key):
    d, n = private_key
    hashed = hash_message(msg) % n   # FIXED: Reduce hash modulo n
    signature = pow(hashed, d, n)
    return signature

def verify_signature(msg, signature, public_key):
    e, n = public_key
    hashed = hash_message(msg) % n   # FIXED: Reduce hash modulo n
    decrypted_hash = pow(signature, e, n)
    return hashed == decrypted_hash

# === Testing ===

public_key, private_key = generate_keys()

message = "This is original message"
signature = sign_message(message, private_key)

print("Signature:", signature)
print("Verification:", verify_signature(message, signature, public_key))

# Test modification
modified = "This is Original message"
print("Verification After Modification:", verify_signature(modified, signature, public_key))