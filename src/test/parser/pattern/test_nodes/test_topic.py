from test.parser.pattern.test_nodes.base import PatternTestBaseClass
from programy.parser.pattern.nodes import *

class PatternTopicNodeTests(PatternTestBaseClass):
    def test_init(self):
        node = PatternTopicNode()
        self.assertIsNotNone(node)

        self.assertFalse(node.is_root())
        self.assertFalse(node.is_priority())
        self.assertFalse(node.is_wildcard())
        self.assertFalse(node.is_zero_or_more())
        self.assertFalse(node.is_one_or_more())
        self.assertIsNotNone(node.children)
        self.assertFalse(node.has_children())

        self.assertTrue(node.equivalent(PatternTopicNode()))
        self.assertEqual(node.to_string(), "TOPIC [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(0)]")

    def test_topic_to_root(self):
        node1 = PatternRootNode()
        node2 = PatternTopicNode()

        with self.assertRaises(ParserException) as raised:
            node1.can_add(node2)
        self.assertEqual(str(raised.exception), "Cannot add topic node to root node")

    def test_multiple_topics(self):
        node1 = PatternTopicNode()
        node2 = PatternTopicNode()

        with self.assertRaises(ParserException) as raised:
            node1.can_add(node2)
        self.assertEqual(str(raised.exception), "Cannot add topic node to topic node")
