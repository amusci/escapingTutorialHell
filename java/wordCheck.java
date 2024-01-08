private static int wordCheck(String str) {

    if (str == null || str.isEmpty()) {
        return 0;
    }

    String[] words = str.split(" ");
    return words.length;


}