    public static bool DoubleLetters(string word)
    /* Create a function that takes a word and returns true if the word has two consecutive identical letters. */
    {

      for (int i = 0; i < word.Length - 1; i++) {

        if (word[i] == word[i + 1]) {
          return true;
        }
      }
      return false;

    }