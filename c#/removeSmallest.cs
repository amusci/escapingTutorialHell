        public static int[] RemoveSmallest(int[] values) 
        {
            /* A museum wants to get rid of some exhibitions.
            
            Katya, the interior architect, comes up with a plan to remove the most boring exhibitions.
            
            She gives them a rating, and removes the one with the lowest rating. Just as she finishes rating the exhibitions, she's called off to an important meeting. She asks you to write a program that tells her the ratings of the items after the lowest one is removed.

            Create a function that takes an array of integers and removes the smallest value.
            */
            if (values.Length == 1 || values.Length == 0)
            {

                return new int [0];

            }

            int minValue = values.Min();
            int minIndex = Array.IndexOf(values, minValue);

            return values.Where((val, indx) => indx != minIndex).ToArray();
            
                
        }