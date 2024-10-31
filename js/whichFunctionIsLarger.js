function whichIsLarger(f, g) {

    if (f() > g()) {

        return "f";
        
    } else if (g() > f()) {

        return "g";

    } else {

        return "neither"

    }
	
}