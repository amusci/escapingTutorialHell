        public static string[] IsFourLetters(string[] arr) 
        /* Create a function that takes an array of strings and returns the words that are exactly four letters.*/
        {
            List<string> fourLetterWord = new List<string>();
            foreach (string word in arr) {
                if (word.Length == 4) {

                    fourLetterWord.Add(word);

                }


            }

            return fourLetterWord.ToArray();
        }