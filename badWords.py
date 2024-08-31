import os
def save_words_to_file(words, filename="words.txt"):

    x = read_words_from_file()
    with open(filename, "a",encoding="utf-8") as file:
        for word in words:
            if word in x:
               pass
            else:
                file.write(f"{word}\n")  # Efficiently write words with newlines
def reset():
   os.remove("./words.txt")
   with open("words.txt", "x") as file:
            pass

def read_words_from_file(filename="words.txt"):
  

  words = []
  try:
    with open(filename, "r") as file:
      words = file.readlines()
  except FileNotFoundError:
    print(f"File '{filename}' not found.")
    try:
        with open(filename, "x") as file:
            pass  # Create the file (empty by default)
    except FileExistsError:
        pass

  # Remove trailing newlines from each word
  words = [word.strip() for word in words]
  return words


def add_word(word, filename="words.txt"):
 
  with open(filename, "a") as file:
    file.write(f"{word}\n")  # Add word with newline character

def remove_word(word, filename="words.txt"):
  

  # Read existing words
  with open(filename, "r") as file:
    existing_words = file.readlines()

  # Remove target word (if found)
  filtered_words = [w for w in existing_words if w.strip() != word]  # Strip trailing whitespace

 

  # Save filtered words
  with open(filename, "w") as file:
    file.writelines(filtered_words)



