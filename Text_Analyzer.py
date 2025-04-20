import streamlit as st

def analyze_text(text):
    length = len(text)
    
    words = text.split()
    num_words = len(words)
    
    vowels = 'aeiou'
    num_vowels = sum(1 for char in text.lower() if char in vowels)
    
    return {
        'length': length,
        'num_words': num_words,
        'num_vowels': num_vowels,
    }

def search_and_replace(text, search_word, replace_word):
    return text.replace(search_word, replace_word)

def main():
    st.title("Text Analyzer")

    text = st.text_area("Enter your paragraph here")

    if text:
        st.header("Text Analysis")
        result = analyze_text(text)
        st.write(f"*Total Characters:* {result['length']}")
        st.write(f"*Total Words:* {result['num_words']}")
        st.write(f"*Total Vowels:* {result['num_vowels']}")

        st.header("Search and Replace")
        search_word = st.text_input("Enter a word to search for")
        replace_word = st.text_input("Enter a word to replace with")
        if search_word and replace_word:
            modified_text = search_and_replace(text, search_word, replace_word)
            st.write(f"*Modified Paragraph:* {modified_text}")

        st.header("Case Conversion")
        st.write(f"*Uppercase:* {text.upper()}")
        st.write(f"*Lowercase:* {text.lower()}")

        st.header("Type Casting")
        word_count_str = str(result['num_words'])
        vowel_count_str = str(result['num_vowels'])
        st.write(f"*Word Count (string):* {word_count_str}")
        st.write(f"*Vowel Count (string):* {vowel_count_str}")

        st.header("Operator")
        if result['num_words'] > 0:
            avg_word_length = result['length'] / result['num_words']
            st.write(f"*Average Word Length:* {avg_word_length}")
        else:
            st.write("Cannot calculate average word length for an empty paragraph")

        st.header("Python Keywords")
        if "Python" in text:
            st.write("The paragraph contains the word 'Python'")
        else:
            st.write("The paragraph does not contain the word 'Python'")

        st.header("Comparison Operator")
        if result['num_words'] > 10:
            st.write("The paragraph has more than 10 words")
        else:
            st.write("The paragraph has less than or equal to 10 words")

    else:
        st.error("Please enter a paragraph")

if __name__ == "__main__":
    main()
