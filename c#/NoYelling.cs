        public static string NoYelling(string phrase) 
        /*

        Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.
        */
        {
            string result = "";

            string[] splitString = phrase.Split(' ');

            int lengthOfSplitString = splitString.Length;
            int lengthOfLastSplit = splitString[lengthOfSplitString - 1].Length;

            for (int i = 0; i < lengthOfSplitString - 1; i++)
            {

                result += splitString[i] + " ";

            }

            int count = 0;
            for (int i = 0; i < lengthOfLastSplit; i++)
            {

                if (count > 0  && splitString[lengthOfSplitString - 1][i] == '!' ||count > 0 && splitString[lengthOfSplitString - 1][i]== '?')
                {



                }
                else if (count == 0  && splitString[lengthOfSplitString - 1][i] == '!' ||count == 0 && splitString[lengthOfSplitString - 1][i] == '?')
                {

                    count ++;
                    result += splitString[lengthOfSplitString - 1][i];

                }
                else 
                {

                    result += splitString[lengthOfSplitString - 1][i];

                }
            }

            return result;
        }