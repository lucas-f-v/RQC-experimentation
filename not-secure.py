from lxml import etree

# XML de exemplo com entidade externa
xml_data = '''
<!DOCTYPE data [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<data>
  <content>&xxe;</content>
</data>
'''

def parse_xml(xml_string):
    try:
        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml_string, parser)
        return root
    except etree.XMLSyntaxError as e:
        print("Erro ao fazer o parsing do XML:", e)

# Tentativa de analisar o XML
parsed_xml = parse_xml(xml_data)
if parsed_xml is not None:
    print(etree.tostring(parsed_xml, pretty_print=True).decode())
#teste