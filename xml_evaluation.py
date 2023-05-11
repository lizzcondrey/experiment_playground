import xml.etree.ElementTree as ET

tree = ET.parse("./xml_resources/AACProjectSample-UML2.5XMI.xml")
root = tree.getroot()

print(f"nodes: {len(root)}")

xml_dump = open("xml_dump.txt", "w")
xml_dump.write(str(root))

for node in root:
    element_tag = f"tag: {node.tag}"
    element_text = f"text: {node.text}"
    element_attribute = f"attribute: {node.attrib}"
    xml_dump.writelines([element_tag, element_text, element_attribute])
xml_dump.close()
