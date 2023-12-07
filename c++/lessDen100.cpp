bool lessThan100(int a, int b) {

    int ans = a + b;
    if (ans >= 100) {
        return false;
    } else {
        return true;
    }
}