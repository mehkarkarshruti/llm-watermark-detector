import hashlib

SECRET_KEY = "aiengineer"
GAMMA = 0.5

def is_green(word, secret_key = SECRET_KEY, gamma = GAMMA):
    hash_value = int(hashlib.md5((secret_key + word).encode()).hexdigest(), 16)

    return (hash_value % 100) < (gamma * 100)

def detect(text, secret_key = SECRET_KEY, gamma = GAMMA):
    words = text.split(" ")
    green_count = 0

    for word in words:
        if is_green(word, secret_key, gamma):
            green_count += 1
    
    total = len(words)
    green_fraction = green_count / total

    is_watermarked = green_fraction > gamma

    return {
        "green_fraction": green_fraction,
        "is_watermarked": is_watermarked
    }
