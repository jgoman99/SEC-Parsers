# Note, we'll be using 'node' for xml and 'element' for html terminology
# Note: adding helpers for tree / root / node, so easier for less technical people
import xml.etree.ElementTree as ET


def print_xml_structure(node):
    def indent(level):
      return "|--" * level

    def print_element(element, level):
      print(indent(level) + element.tag)
      for child in element:
        print_element(child, level + 1)

    print_element(node, 0)


def get_text_from_node(node):
    text = ''
    if node.text is not None:
        text = node.text.strip()
    for child in node:
        text += get_text_from_node(child)
    
    return text

def save_xml(tree, file_path):
    tree.write(file_path, encoding='utf-8-sig', xml_declaration=True)