    public static object[] RemoveDups(object[] str) 
    /* Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).*/
    {

        object[] result = str.Distinct().ToArray();

        return result;


      
    }