import zipfile
import xml.etree.ElementTree as ET

docx_path = '/home/erick-fcs/Documentos/universidad/trabajo_social/docs/vaults/Tarea_afiche/index.docx'

with zipfile.ZipFile(docx_path, 'r') as z:
    doc_xml = z.read('word/document.xml')

root = ET.fromstring(doc_xml)
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Buscar fragmentos de texto
for t in root.findall('.//w:t', namespaces):
    if t.text and ('meyer' in t.text.lower() or '2003' in t.text or 'chinchilla' in t.text.lower()):
        # Encontrar el elemento run ancestro w:r
        # E imprimir el xml de su entorno (por ejemplo, del párrafo w:p o hyperlink w:hyperlink)
        print(f"Texto encontrado: '{t.text}'")
        # Busquemos el ancestro hyperlink si existe
        # Para simplificar, busquemos el párrafo w:p que contiene este w:t
        
# Imprimamos un trozo del XML alrededor de "meyer"
doc_xml_str = doc_xml.decode('utf-8')
idx = doc_xml_str.find('meyer')
if idx != -1:
    print("\nXML alrededor de 'meyer':")
    print(doc_xml_str[max(0, idx-500):idx+500])
