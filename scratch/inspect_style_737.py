import zipfile
import xml.etree.ElementTree as ET

docx_path = '/home/erick-fcs/Documentos/universidad/trabajo_social/docs/vaults/Tarea_afiche/index.docx'

with zipfile.ZipFile(docx_path, 'r') as z:
    styles_xml = z.read('word/styles.xml')

root = ET.fromstring(styles_xml)
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Buscar el estilo con styleId="737"
style_737 = None
for style in root.findall('.//w:style', namespaces):
    if style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}styleId') == '737':
        style_737 = style
        break

if style_737 is not None:
    print("Estilo 737:")
    print(ET.tostring(style_737, encoding='utf-8').decode('utf-8'))
else:
    print("Estilo 737 no encontrado.")

# También listemos los estilos que tengan colores específicos
print("\nEstilos de carácter en el documento:")
for style in root.findall('.//w:style', namespaces):
    name_elem = style.find('w:name', namespaces)
    name = name_elem.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if name_elem is not None else "Sin nombre"
    style_id = style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}styleId')
    style_type = style.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}type')
    
    # Imprimir si es de tipo "character"
    if style_type == 'character':
        color_elem = style.find('.//w:color', namespaces)
        color = color_elem.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') if color_elem is not None else "Sin color"
        print(f"ID: {style_id} | Nombre: {name} | Color: {color}")
