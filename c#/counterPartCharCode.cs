        public static int CounterpartCharCode(char symbol) 
        /* Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.*/
        {

            if (char.IsUpper(symbol))

            {

                return (int) char.ToLower(symbol);

            }

            else if (char.IsLower(symbol))

            {

                return (int) char.ToUpper(symbol);

            }

            else {


                return (int) symbol;

            }
            
        }