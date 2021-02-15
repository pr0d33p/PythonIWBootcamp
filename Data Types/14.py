def add_tags(tag, item):
    startTag = "<{}>".format(tag)
    endTag = "</{}>".format(tag)
    result = startTag + item + endTag
    return result

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))