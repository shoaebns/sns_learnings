def read_synonyms_file(word):
  

    synonyms = {}
    file_name = word + ".txt"
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                synonym_list = line.split()
                first_letter = synonym_list[0][0]
                synonyms[first_letter] = synonym_list[0:]
        return synonyms
    except FileNotFoundError:
        return None

def main():
    word = input()
    letter = input()

    synonyms = read_synonyms_file(word)
    
    if synonyms is not None:
        if letter in synonyms:
            for synonym in synonyms[letter]:
                print(synonym)
        else:
            print("No synonyms for {} begin with {}.".format(word, letter))
    else:
        print("File {} not found.".format(word + ".txt"))

if __name__ == "__main__":
    main()
