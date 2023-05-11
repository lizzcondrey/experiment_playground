import xml.etree.ElementTree as ET

# Get root of XML file
tree = ET.parse("./xml_resources/AACProjectSample-UML2.5XMI.xml")
root = tree.getroot()

# Lists of components worth tracking
tags = []
type_attributes = []
requirements = []
element_ids = []
attributes = []

# Files for storing parsed data
xml_dump = open("xml_dump.txt", "w")
tags_dump = open("tags_dump.txt", "w")
types_dump = open("types_dump.txt", "w")
requirements_dump = open("requirements_dump.txt", "w")
ids_dump = open("ids_dump.txt", "w")
attributes_dump = open("attributes_dump.txt", "w")


def get_element_components(element: ET.Element) -> list[str]:
    """
    Helper function for getting the element's tag, text, and attribute from
    the XML.
    """
    element_tag = f"tag: {element.tag} \n"
    element_text = f"text: {element.text} \n"
    element_attribute = f"attribute: {element.attrib} \n"

    return [element_tag, element_text, element_attribute]


def sort_element_components(element: ET.Element) -> None:
    """
    Helper function for sorting an element's components.
    Generates list entries of key value pairs with the key being the
    original element and pertinent value
    """
    if element.tag not in tags:
        tags.append(element.tag)

    for key, value in element.attrib.items():
        if "type" in key:
            type_attributes.append(f"{element}: {element.attrib[key]}")
        
        if "Requirement" in value:
            requirements.append(f"{element}: {value}")

        if "id" in key:
            element_ids.append(f"{element}: {element.attrib[key]}")
    
        if key not in attributes:
            attributes.append(f"{element}: {key}")


def add_root_elements(root: ET.Element) -> None:
    """
    Method to take the returned tag, text, and attribute of the root element
    and append it to the file.
    """
    root_elements = get_element_components(root)
    sort_element_components(root)
    xml_dump.write("root data \n")
    xml_dump.writelines(root_elements)


def add_node_elements(root: ET.Element) -> None:
    """
    Method to take the returned tag, text, and attribute of the node element
    and append it to the file.
    """
    xml_dump.write("node data \n")
    for node in root:
        node_elements = get_element_components(node)
        sort_element_components(node)
        xml_dump.writelines(node_elements)


def add_node_children_elements(node: ET.Element) -> None:
    """
    Method to take the returned tag, text, and attribute of a node child
    element and append it to the file.
    """
    xml_dump.write("node children data \n")
    for child in node.iter():
        child_elements = get_element_components(child)
        sort_element_components(child)
        xml_dump.writelines(child_elements)


def add_parsed_components(component_type: str, components_list: list) -> None:
    """
    Method to add parsed components to pertinent file.
    """
    components_list.sort()
    for list_entry in components_list:
        exec(f"{component_type}_dump.write(f'{list_entry} \\n')")
    
    exec(f"{component_type}_dump.close()")


# Adding elements to xml parse file
root_elements = add_root_elements(root)
node_elements = add_node_elements(root)
for node in root:
    node_children_elements = add_node_children_elements(node)

add_parsed_components("tags", tags)
add_parsed_components("types", type_attributes)
add_parsed_components("requirements", requirements)
add_parsed_components("ids", element_ids)
add_parsed_components("attributes", attributes)

# tags.sort()
# for tag in tags:
#     tags_dump.write(f"{tag} \n")

# for type_attribute in type_attributes:
#     types_dump.write(f"{type_attribute} \n")

# for requirement in requirements:
#     requirements_dump.write(f"{requirement} \n")

# for element_id in element_ids:
#     ids_dump.write(f"{element_id} \n")

# attributes.sort()
# for attribute in attributes:
#     attributes_dump.write(f"{attribute} \n")

# Closing parsed data files
# xml_dump.close()
# tags_dump.close()
# types_dump.close()
# requirements_dump.close()
# ids_dump.close()

print("finished processing nodes and node children")
