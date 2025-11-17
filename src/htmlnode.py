class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            "Child classes will override this method to render themselves as HTML."
        )

    def props_to_html(self):
        s = ""
        if self.props is None:
            return s

        for key, value in self.props.items():
            curr_prop_str = f' {key}="{value}"'
            s += curr_prop_str
        return s

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return f"{self.value}"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        if not self.children:
            raise ValueError("All parent nodes must have valid children arguments.")

        html_str = ""
        for child in self.children:
            html_str += (
                f"<{child.tag}{child.props_to_html()}>{child.value}</{child.tag}>"
            )

        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
