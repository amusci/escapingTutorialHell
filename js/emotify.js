/*

Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words smile, grin, sad and mad with their corresponding emoticons.
word emoticon

smile	:D
grin	:)
sad	    :(
mad	    :P
*/

function emotify(str) {

    const words = str.split(' ');

    let emotify = {

        "smile": ":D",
        "grin": ":)",
        "sad": ":(",
        "mad": ":P"

    }

    return "Make me " + emotify[words[2]]

	
}
