private static int vowelCheck(String str) {


    int count = 0;

    for (int i = 0; i < str.length(); i++) {

        if (str.charAt(i) == 'a' || str.charAt(i) == 'e'
                || str.charAt(i) == 'i' || str.charAt(i) == 'o'
                || str.charAt(i) == 'u' || str.charAt(i) == 'y') {

            count++;
        }



    }


    return count;
}