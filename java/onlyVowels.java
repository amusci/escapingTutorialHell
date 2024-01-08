private static boolean onlyVowels(String str) {


    String vowels = "aeiou";
    for (int i = 0; i < str.length(); i++) {

        if (vowels.indexOf(str.charAt(i)) == -1) {

            return false;
        }

    }


    return true;
}
}