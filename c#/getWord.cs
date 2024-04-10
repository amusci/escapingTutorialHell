        public static string GetWord(string left, string right)
        /*A word has been split into a left part and a right part.
        Re-form the word by adding both halves together,
        changing the first character to an uppercase letter.*/
        {
            char c = left[0];
            string start = char.ToUpper(c).ToString();
            left = left.Substring(1);

            return start + left + right;
        }