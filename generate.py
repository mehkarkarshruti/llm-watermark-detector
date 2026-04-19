from watermark import is_green, SECRET_KEY, GAMMA

def analyze_text(text):
    words = text.split(" ")
    green_count = 0

    print("\nWORD ANALYSIS")
    for word in words:
        if is_green(word, SECRET_KEY, GAMMA):
            print(f"{word} -> GREEN")
            green_count += 1
        else:
            print(f"{word} -> RED")
    
    green_fraction = green_count / len(words)
    print(f"Green fraction: {green_fraction: .2f}")
    print(f"Watermarked: {green_fraction > GAMMA}")


text = "the quick brown fox jumps over the lazy dog"
analyze_text(text)