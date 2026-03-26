# split and join


def split_and_join(line):
    
    word = line.split() # this is a string -> ['this', 'is', 'a', 'string']
    return "-".join(word)


if __name__ == "__main__":
    line = input("Enter a string: ") # this is a string -> this-is-a-string
    result = split_and_join(line)
    print(result)
