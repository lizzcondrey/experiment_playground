import xml.etree.ElementTree as ET

tree = ET.parse("./xml_resources/AACProjectSample-UML2.5XMI.xml")
root = tree.getroot()

tags = []
type_attributes = []

xml_dump = open("xml_dump4.txt", "w")


def get_element_components(element: ET.Element) -> list[str]:
    """
    Helper function for getting the element's tag, text, and attribute from
    the XML.
    """
    element_tag = f"tag: {element.tag} \n"
    element_text = f"text: {element.text} \n"
    element_attribute = f"attribute: {element.attrib} \n"

    if element.tag not in tags:
        tags.append(element.tag)

    if "}type" in str(element.attrib):
        type_attributes.append(element.attrib)

    return [element_tag, element_text, element_attribute]


def add_root_elements(root: ET.Element) -> None:
    """
    Method to take the returned tag, text, and attribute of the root element
    and append it to the file.
    """
    root_elements = get_element_components(root)
    xml_dump.write("root data \n")
    xml_dump.writelines(root_elements)


def add_node_elements(root: ET.Element) -> None:
    """
    Method to take the returned tag, text, and attribute of the node element
    and append it to the file.
    """
    for node in root:
        node_elements = get_element_components(node)
        xml_dump.write("node data \n")
        xml_dump.writelines(node_elements)


def add_node_children_elements(node: ET.Element) -> None:
    """
    Method to take the returned tag, text, and attribute of a node child
    element and append it to the file.
    """
    for child in node.iter():
        child_elements = get_element_components(child)
        xml_dump.write("node children data \n")
        xml_dump.writelines(child_elements)


root_elements = add_root_elements(root)
node_elements = add_node_elements(root)

for node in root:
    node_children_elements = add_node_children_elements(node)

xml_dump.close()

print("finished processing nodes and node children")
