        public static int letterDistance(string str1, string str2)

        /* Given two words, the letter distance is calculated by taking the absolute value of the difference in character codes and summing up the difference.

        If one word is longer than another, add the difference in lengths towards the score.

        To illustrate:

        letterDistance("house", "fly") = dist("h", "f") + dist("o", "l") + dist("u", "y") + dist(house.Length, fly.Length)

        = |104 - 102| + |111 - 108| + |117 - 121| + |5 - 3|
        = 2 + 3 + 4 + 2
        = 11 
        */

        {
            int result = 0;
            int n = Math.Min(str1.Length, str2.Length);
            for(int i = 0; i < n; i++)
            {
                result += Diff(str1[i], str2[i]);
            }
            return result + Math.Abs((str1.Length - str2.Length));
        }


        public static int Diff(char a, char b)

        {
            int diff = (int)a - (int)b;
            return Math.Abs(diff);
        }