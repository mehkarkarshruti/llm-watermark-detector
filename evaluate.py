from watermark import detect, SECRET_KEY, GAMMA 
from watermark import is_green


sentences = [
    "the cat sat on the mat",
    "artificial intelligence is changing the world",
    "hi this is a test",
    "language models can generate human like text",
    "watermarking is used to detect ai generated content",
    "the quick brown fox jumps over the lazy dog"
]

print(f" {'Sentence': <50} | {'Green%':<10} | {'Watermark'}")
print("-" * 80)

for sentence in sentences:
    result = detect(sentence, SECRET_KEY, GAMMA)
    green_percentage = round(result["green_fraction"] * 100, 1)
    watermarked = result['is_watermarked']
    print(f" {sentence: <50} | {green_percentage}%{'':6} | {watermarked}")