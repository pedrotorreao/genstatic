import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_neq1(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is A text node", "bold")
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "link")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "italic")
        self.assertEqual(node.url, None)

    def test_text_type_eq(self):
        node1 = TextNode("Test", "bold")
        node2 = TextNode("Test", "bold")
        self.assertEqual(node1.text_type, node2.text_type)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
