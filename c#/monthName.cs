    public static string MonthName(int num) 
    /*Create a function that takes a number (from 1 to 12) and returns its corresponding month name as a string. 
    For example, if you're given 3 as input, your function should return "March", because March is the 3rd month.*/
    {

        switch(num)
        {
            case 1:
               return "January";
            case 2:
                return "February";
            case 3:
                return "March";
            case 4:
                return "April";
            case 5:
                return "May";
            case 6:
                return "June";
            case 7:
                return "July";
            case 8:
                return "August";
            case 9:
                return"September";
            case 10:
                return"October";
            case 11:
                return "November";
            case 12:
                return "December";
            default:
                return "Invalid month number, please enter 1-12";

        }
    }