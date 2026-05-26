def clean_text(text):
    punctuation = ".,!?;:\"'()[]{}-_/\\"
    text = text.lower()
    cleaned = ""
    for ch in text:
        if ch not in punctuation:
            cleaned += ch
    return cleaned


def count_words(text):
    freq = {}
    for word in text.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


MOOD_WORDS = ["happy", "sad", "stressed", "hyped", "angry",
              "tired", "excited", "bored", "calm", "anxious"]

def find_mood_words(sentence):
    cleaned = clean_text(sentence)
    words = cleaned.split()
    found = []
    for mood in MOOD_WORDS:
        if mood in words:
            found.append(mood)
    print("Mood words found:", found)
    return found


def top_5_words(text):
    cleaned = clean_text(text)
    freq = count_words(cleaned)
    ranked = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
    top5 = ranked[:5]
    print("Top 5 words:", top5)
    return top5


def test_clean_text():
    samples = [
        "I am SO happy today!!!",
        "Why are you so STRESSED, bro?",
        "Calm down... it's fine.",
    ]
    print("== clean_text tests ==")
    for s in samples:
        print(repr(s), "->", repr(clean_text(s)))
    print()


def analyse_file(filename):
    print("== File analysis ==")
    with open(filename, "r") as f:
        for line in f:
            sentence = line.strip()
            if sentence == "":
                continue
            print("-" * 40)
            print("Original :", sentence)
            print("Cleaned  :", clean_text(sentence))
            find_mood_words(sentence)
            top_5_words(sentence)


if __name__ == "__main__":
    test_clean_text()
    analyse_file("sentences.txt")