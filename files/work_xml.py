import xml.etree.ElementTree as ET

# Чтение файла
def parse_xml_et(fn):
    tree = ET.parse(fn)
    root = tree.getroot()
    print('Domain for: ' + root.attrib['name'])
    for child in root:
        print('\t' + child.attrib['name'], child.tag)

#parse_xml_et('./files_to_read/ef_author.xml')

# добавление XML-элемента в файл
def add_xml_element_et(fn, el, attr, val):
    tree = ET.parse(fn)
    root = tree.getroot()
    child = ET.Element(el)
    child.attrib[attr] = val
    root.append(child)
    tree.write(fn)

# add_xml_element_et('./files_to_read/ef_author.xml', 'domain', 'name', 'Java')

# изменение значения существующего узла
def change_xml_et(fn, el, attr, oldval, newval):
    tree = ET.parse(fn)
    root = tree.getroot()
    child = root.find('./' + el + "[@" + attr + "='" + oldval + "']")
    child.attrib[attr] = newval
    tree.write(fn)

change_xml_et('./files_to_read/ef_author.xml', 'domain', 'name', 'Java', 'TypeScript')
