import zipfile
import tempfile
import shutil
import os
import xml.etree.ElementTree as ET

def fix_hyperlink_style_in_docx(docx_path):
    print(f"Modificando estilos en {docx_path}...")
    temp_dir = tempfile.mkdtemp()
    try:
        # Extraer todo el zip a un directorio temporal
        with zipfile.ZipFile(docx_path, 'r') as z:
            z.extractall(temp_dir)
        
        styles_path = os.path.join(temp_dir, 'word', 'styles.xml')
        if not os.path.exists(styles_path):
            print("Error: No se encontró word/styles.xml")
            return False
        
        # Leer y parsear styles.xml
        ET.register_namespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
        tree = ET.parse(styles_path)
        root = tree.getroot()
        namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        modified = False
        # Buscar el estilo Hyperlink
        for style in root.findall('.//w:style', namespaces):
            name_elem = style.find('w:name', namespaces)
            if name_elem is not None and name_elem.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val') == 'Hyperlink':
                rPr = style.find('w:rPr', namespaces)
                if rPr is None:
                    rPr = ET.SubElement(style, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr')
                
                # Modificar o añadir w:color
                color = rPr.find('w:color', namespaces)
                if color is None:
                    color = ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color')
                color.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '0563C1')
                # Eliminar themeColor para forzar el color estático
                if '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}themeColor' in color.attrib:
                    del color.attrib['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}themeColor']
                
                # Asegurar que esté subrayado
                u = rPr.find('w:u', namespaces)
                if u is None:
                    u = ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}u')
                u.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'single')
                
                print("Estilo Hyperlink modificado con éxito en el XML.")
                modified = True
                break
        
        if not modified:
            print("No se encontró el estilo Hyperlink para modificar.")
            return False
        
        # Guardar styles.xml modificado
        tree.write(styles_path, xml_declaration=True, encoding='utf-8')
        
        # Volver a comprimir en el docx original
        # Para evitar problemas con permisos o corrupción, creamos un nuevo zip temporal y lo reemplazamos
        backup_path = docx_path + '.bak'
        shutil.copyfile(docx_path, backup_path)
        
        try:
            with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z_new:
                for root_dir, dirs, files in os.walk(temp_dir):
                    for file in files:
                        full_path = os.path.join(root_dir, file)
                        rel_path = os.path.relpath(full_path, temp_dir)
                        z_new.write(full_path, rel_path)
            print("Archivo docx sobrescrito exitosamente.")
            if os.path.exists(backup_path):
                os.remove(backup_path)
            return True
        except Exception as e:
            print(f"Error al escribir el archivo zip: {e}")
            # Restaurar backup
            shutil.copyfile(backup_path, docx_path)
            os.remove(backup_path)
            return False
            
    finally:
        shutil.rmtree(temp_dir)

# Ejecutar sobre la plantilla del proyecto
template_path = '/home/erick-fcs/Documentos/universidad/trabajo_social/config/custom-template.docx'
fix_hyperlink_style_in_docx(template_path)
