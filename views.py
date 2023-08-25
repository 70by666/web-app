def index():
    with open('templates/index.html') as tmp:
        return tmp.read()
    

def blog():
    with open('templates/blog.html') as tmp:
        return tmp.read()
