from textnode import TextNode, TextType

def main():
    new_object = TextNode("Test text", TextType.BOLD, "http://www.example.com")
    print(new_object)

if __name__ == "__main__":
    main()
