from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []
        sections = node.text.split(delimiter)

        # no matching delimiter:
        if len(sections) % 2 == 0:
            raise Exception("invalid markdown, formatted section not closed")

        for i in range(len(sections)):
            # empty section:
            if sections[i] == "":
                continue
            # text section:
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes
