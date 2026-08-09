import zipfile
import xml.etree.ElementTree as ET

docx_path = '/home/erick-fcs/Documentos/universidad/07_Ciclo/septimo_ciclo/thesis_project/double-informality-determinants-ecuador/docs/writing/tic/templates/custom_template.docx'

with zipfile.ZipFile(docx_path, 'r') as z:
    styles_xml = z.read('word/styles.xml')

root = ET.fromstring(styles_xml)
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Buscar el estilo Hyperlink en la plantilla de la tesis
for style in root.findall('.//w:style', namespaces):
    name_elem = style.find('w:name', namespaces)
    name = name_elem.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if name_elem is not None else "Sin nombre"
    if name == 'Hyperlink':
        print("Encontrado estilo Hyperlink en plantilla de la tesis:")
        print(ET.tostring(style, encoding='utf-8').decode('utf-8'))
