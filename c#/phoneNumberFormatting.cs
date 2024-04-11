        public static string FormatPhoneNumber(int[] numbers)
        /* Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).*/ 
        {
            string format = "(XXX) XXX-XXXX";

            for (int i = 0; i < numbers.Length; i++) 
            {

                char digit = numbers[i].ToString()[0];
                int index = format.IndexOf("X");

                if (index != -1)
                {

                    format = format.Remove(index, 1).Insert(index, digit.ToString()); 

                }

            }

            return format;
        
        }