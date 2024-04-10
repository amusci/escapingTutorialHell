    public static bool XO(string str) 
    {
        string lower = str.ToLower();
        int xCount = 0;
        int oCount = 0;
        

        for (int i = 0; i < str.Length; i++) {

            if (lower[i] == 'x') {

                xCount++;

            }
            else if (lower[i] == 'o') {

                oCount++;

            }
        }
        return (xCount == oCount);
      
    }