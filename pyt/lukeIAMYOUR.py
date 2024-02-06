def relation_to_luke(name):
    relations = {'father': 'Darth Vader', 'sister': 'Leia', 'Brother in law': 'Han', 'Droid': 'R2D2'}
    for key, value in relations.items():

        if value == name:
            return "Luke, I am your " + key + '.'
    return "Did you input the wrong name? Luke doesn't know you at all."