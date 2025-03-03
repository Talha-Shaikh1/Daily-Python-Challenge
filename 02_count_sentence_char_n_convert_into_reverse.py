def count_words():
    # Get sentence input from user
    sentence = input("Enter a sentence: ")
    
    # Split sentence into words and count them
    words = sentence.split()
    total_words = len(words)
    
    # Print the results
    print(f"Total words: {total_words}")
    
    # Print words in reverse order
    reversed_sentence = " ".join(words[::-1])
    print(f"Reversed words: {reversed_sentence}")

# Run the program
if __name__ == "__main__":
    count_words()