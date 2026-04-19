from watermark import detect

text = input("Enter text to analyze: ")
result = detect(text)
print("Result: ", result)