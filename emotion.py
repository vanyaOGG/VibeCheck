from transformers import pipeline
from preprocess import preprocess

classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def predict_emotion(text):
    tokens = preprocess(text)
    cleaned = " ".join(tokens)
    result = classifier(cleaned)
    return result[0]["label"], round(result[0]["score"], 2)

sentences = [
    ("I am so happy today, everything is going great!", "joy"),
    ("I feel so lonely and empty inside.", "sadness"),
    ("I am furious about what happened, this is unacceptable!", "anger"),
    ("I am terrified of what might happen next.", "fear"),
    ("I cherish you deeply, my heart is so full of love for you.", "love"),
    ("I was completely stunned, I had absolutely no idea this would happen.", "surprise"),
    ("I am so scared right now, I cannot stop trembling with fear.", "fear"),
    ("Today was perfect, I feel absolutely wonderful.", "joy"),
    ("I have been crying all day thinking about the loss.", "sadness"),
    ("This makes me so angry I could scream.", "anger"),
]

correct = 0
results = []

for text, expected in sentences:
    label, score = predict_emotion(text)
    is_correct = label == expected
    if is_correct:
        correct += 1
    results.append((text, label, score, expected, is_correct))
    status = "✓" if is_correct else "✗"
    print(f"Text     : {text}")
    print(f"Expected : {expected}")
    print(f"Predicted: {label} ({score}) {status}")
    print()

print(f"Result: {correct}/10 correct")

with open("results.txt", "w") as f:
    for text, label, score, expected, is_correct in results:
        status = "Correct" if is_correct else "Wrong"
        f.write(f"Text     : {text}\n")
        f.write(f"Expected : {expected}\n")
        f.write(f"Predicted: {label} ({score}) - {status}\n\n")
    f.write(f"Final Score: {correct}/10\n")    