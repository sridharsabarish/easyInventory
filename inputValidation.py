# Some simple Input Validation initially
validateString = lambda x: x.isalpha() or x.isdigit() and x!=''
validateNumber = lambda x: x.isdigit() and x!=''
validateFloat = lambda x: x.isdigit() and x!=''