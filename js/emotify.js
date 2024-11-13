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

    if (words[2] === "smile") {

        return "Make me :D"

    } else if (words[2] === "grin") {

        return "Make me :)"

    } else if (words[2] === "sad") {

        return "Make me :(";

    } else if (words[2] === "mad") {

        return "Make me :P";

    }

	
}
