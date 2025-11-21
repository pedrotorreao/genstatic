from textnode import TextNode, TextType
from fs_utils import copy_contents

# from htmlnode import HTMLNode


def main():
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(tn)

    src_path = r"/home/pedrotorreao/Documents/Projects/bootdev/genstatic/static"
    dst_path = r"/home/pedrotorreao/Documents/Projects/bootdev/genstatic/public"

    copy_contents(src_path, dst_path)

    # hn = HTMLNode("a", "search", None, {"href": "https://www.google.com","target": "_blank"})
    # print(hn)


main()
