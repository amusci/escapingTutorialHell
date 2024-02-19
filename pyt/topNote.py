"""

Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] }

and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

"""


def top_note(student):

    notes = student["notes"]
    name = student["name"]
    top_note = max(notes)


    return {"name":name, "top_note":top_note}