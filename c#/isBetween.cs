        public static bool isBetween(string first, string last, string word)

        {
            string[] words = {first, word, last};
            Array.Sort(words);

            


            return word == words[1];

            
        }