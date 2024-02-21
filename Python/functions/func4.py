
def func(*argv):
    for word in argv:
        print(word, end=' ')
    print()


func("Hi", "How", "Are", "You", "?")
func("Hello", "World")
