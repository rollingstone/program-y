from test.parser.pattern.test_nodes.base import PatternTestBaseClass
from programy.parser.pattern.nodes import *
from programy.parser.template.nodes import TemplateNode


class PatternTemplateNodeTests(PatternTestBaseClass):

    def test_init(self):

        node = PatternTemplateNode(TemplateNode())
        self.assertIsNotNone(node)

        self.assertFalse(node.is_root())
        self.assertFalse(node.is_priority())
        self.assertFalse(node.is_wildcard())
        self.assertFalse(node.is_zero_or_more())
        self.assertFalse(node.is_one_or_more())
        self.assertIsNotNone(node.children)
        self.assertFalse(node.has_children())

        self.assertTrue(node.equivalent(PatternTemplateNode(TemplateNode())))
        self.assertEqual(node.to_string(), "PTEMPLATE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(1)] ")

    def test_template_to_root(self):
        node1 = PatternRootNode()
        node2 = PatternTemplateNode(TemplateNode())

        with self.assertRaises(ParserException) as raised:
            node1.can_add(node2)
        self.assertEqual(str(raised.exception), "Cannot add template node to root node")

    def test_multiple_templates(self):
        node1 = PatternTemplateNode(TemplateNode())
        node2 = PatternTemplateNode(TemplateNode())

        with self.assertRaises(ParserException) as raised:
            node1.can_add(node2)
        self.assertEqual(str(raised.exception), "Cannot add template node to template node")


