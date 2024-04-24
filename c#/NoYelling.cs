        public static string NoYelling(string phrase) 
        /*

        Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.
        */
        {

            if (phrase.EndsWith('!'))
            {

                return phrase.TrimEnd('!') + '!';

            }
            else if (phrase.EndsWith('?'))
            {

                return phrase.TrimEnd('?') + '?';

            }

            return phrase;


        }