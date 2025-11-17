import re
from enum import Enum

from textnode import TextNode, TextType
from node_handler import split_nodes_delimiter


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


"""
Create a function extract_markdown_images(text) that takes raw markdown text and returns a list of 
tuples. Each tuple should contain the alt text and the URL of any markdown images.
"""


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


"""
Create a similar function extract_markdown_links(text) that extracts markdown links instead of images. 
It should return tuples of anchor text and URLs.
"""


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text

        imgs = extract_markdown_images(node_text)
        if len(imgs) == 0:
            new_nodes.append(node)
            continue

        for img in imgs:
            segments = node_text.split(f"![{img[0]}]({img[1]})", 1)
            if len(segments) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if segments[0] != "":
                new_nodes.append(TextNode(segments[0], TextType.TEXT))
            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            node_text = segments[1]

        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text

        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            segments = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(segments) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if segments[0] != "":
                new_nodes.append(TextNode(segments[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = segments[1]

        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)

    split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    split_nodes = split_nodes_delimiter(split_nodes, "_", TextType.ITALIC)
    split_nodes = split_nodes_delimiter(split_nodes, "`", TextType.CODE)
    split_nodes = split_nodes_link(split_nodes)
    split_nodes = split_nodes_image(split_nodes)

    return split_nodes


def markdown_to_blocks(doc):
    doc_blocks = list()
    if doc:
        doc_spl = doc.split("\n\n")
        for doc_block in doc_spl:
            if doc_block != "":
                doc_block = doc_block.strip()
                doc_blocks.append(doc_block)

    return doc_blocks


def block_to_block_type(block: str):
    if block.startswith("#"):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("-"):
        return BlockType.UNORDERED_LIST
    if block.startswith("1."):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
