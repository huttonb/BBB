class lanParser():
    def __init__(self, spell):
        sad = False
    # The lexer works by giving it a set of code, it can use regex to determine whether or not it's a key-word

    def lexer(self, lex):
        keyword = True;
        # if Keyword send it to the correct function
        if keyword:
            # Convert lex to the same name as the function
            func_name = 'bb' + str(lex)
            # calls the method, then returns
            # Getattr attaches a method to func, returning it with () calls it,
            # if it can't find the function name, it assigns lambda to it, which is error
            func = getattr(self, func_name, lambda: "Keyword Error: Could not find keyword")

            return func()

    def bbwhile(self):
        print("-While Detected-")
        return

    def bbfor(self, arg):
        print("For detected")
        return

    def bbint(self, arg):
        print("Int detected")
        return


l = lanParser("howdy")
l.lexer("while")

# For custom variables a dictionary is used to store the string name to the actual variable that it creates for it.
