from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text_content, text_type, text_url=None):
        self.text = text_content
        self.text_type = text_type
        self.url = text_url

    def __eq__(self, other):
        if other != None:
            return (
                (self.text == other.text)
                and (self.text_type == other.text_type)
                and (self.url == other.url)
            )

    def __repr__(self):
        # TextNode(TEXT, TEXT_TYPE, URL)
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node == None:
        raise Exception("Invalid TextNode.")

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("`", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise Exception("Invalid text type.")


# (self, tag, value, props=None)
