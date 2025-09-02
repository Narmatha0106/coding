def count_words(text):
    words = text.split()
    return len(words)

def main():
    print("📝 Word Counter")
    text = input("Enter your text: ")
    word_count = count_words(text)
    print(f"\nTotal number of words: {word_count}")

if __name__ == "__main__":
    main()
