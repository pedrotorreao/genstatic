from textnode import TextNode, TextType
from fs_utils import copy_contents
from page_handler import generate_pages_recursive
import os
import sys

PROJECT_ROOT = r"/home/pedrotorreao/Documents/Projects/bootdev/genstatic"


def main():
    base_path = f"/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    src_path = r"/home/pedrotorreao/Documents/Projects/bootdev/genstatic/static"
    dst_path = r"/home/pedrotorreao/Documents/Projects/bootdev/genstatic/docs"

    copy_contents(src_path, dst_path)

    src_path = os.path.join(PROJECT_ROOT, "content")
    dst_path = os.path.join(PROJECT_ROOT, "docs")
    template_path = os.path.join(PROJECT_ROOT, "template.html")

    generate_pages_recursive(src_path, template_path, dst_path, base_path)


main()
