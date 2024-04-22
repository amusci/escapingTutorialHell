        public static bool IsValidPhoneNumber(string str) 

        /* Create a function that accepts a string and returns true if it's in the format of a proper phone number and false if it's not. Assume any number between 0-9 (in the appropriate spots) will produce a valid phone number.

        This is what a valid phone number looks like:

        (123) 456-7890
        */

        {
            string format = "(###) ###-####";
            int correctFormatLength = format.Length;

            if (str.Length != correctFormatLength) return false;
            

            if (str[0] != '(' || !char.IsDigit(str[1]) || !char.IsDigit(str[2]) || !char.IsDigit(str[3]) || str[4] != ')' || str[5] != ' ' || !char.IsDigit(str[6]) ||
                !char.IsDigit(str[7]) || !char.IsDigit(str[8]) || str[9] != '-' || !char.IsDigit(str[10]) || !char.IsDigit(str[11]) || !char.IsDigit(str[12]) || !char.IsDigit(str[13]))
            {
                return false;
            }

            return true;
        }