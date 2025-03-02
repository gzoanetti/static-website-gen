from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    new_object = TextNode("Test text", TextType.BOLD, "http://www.example.com")
    print(new_object)
    new_object = HTMLNode("p", "A test paragraph", "a", {"href": "https://www.google.com"})
    print(new_object)

if __name__ == "__main__":
    main()
