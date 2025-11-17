from textnode import TextNode, TextType

# from htmlnode import HTMLNode


def main():
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn)

    # hn = HTMLNode("a", "search", None, {"href": "https://www.google.com","target": "_blank"})
    # print(hn)


main()
