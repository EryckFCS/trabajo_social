import zipfile
import xml.etree.ElementTree as ET

docx_path = '/home/erick-fcs/Documentos/universidad/trabajo_social/config/custom-template.docx'

with zipfile.ZipFile(docx_path, 'r') as z:
    styles_xml = z.read('word/styles.xml')

root = ET.fromstring(styles_xml)
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Buscar estilos que tengan name "Hyperlink"
for style in root.findall('.//w:style', namespaces):
    name_elem = style.find('w:name', namespaces)
    if name_elem is not None and name_elem.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') == 'Hyperlink':
        print("Encontrado estilo Hyperlink:")
        print(ET.tostring(style, encoding='utf-8').decode('utf-8'))
