import unittest
from programy.parser.template.nodes import *
from test.parser.template.graph.test_graph_client import TemplateGraphTestClient


class TemplateGraphSraixTests(TemplateGraphTestClient):

    def test_sraix_template_params_as_attribs(self):
        template = ET.fromstring("""
            <template>
                <sraix host="hostname" botid="testbot" hint="test query" apikey="1234567890" service="/ask">
                    Ask this question
                </sraix>
            </template>
            """)
        ast = self.parser.parse_template_expression(template)

    def test_sraix_template_params_as_children(self):
        template = ET.fromstring("""
            <template>
                <sraix>
                    <host>hostname</host>
                    <botid>testbot</botid>
                    <hint>test query</hint>
                    <apikey>1234567890</apikey>
                    <service>/ask</service>
                    Ask this question
                </sraix>
            </template>
            """)
        ast = self.parser.parse_template_expression(template)

if __name__ == '__main__':
    unittest.main()
