import sys
import re
import fitz  # Importa PyMuPDF

def generar_diccionario(pdf_path, salida_txt="diccionario_john.txt"):
    """
    Extrae palabras y números de un PDF y genera un diccionario para John the Ripper.

    Args:
        pdf_path (str): Ruta al archivo PDF de entrada.
        salida_txt (str): Ruta al archivo de texto de salida.
    """
    palabras_seleccionadas = set()
    numeros_encontrados = set()

    # Expresiones regulares para encontrar palabras y números
    patron_palabra = re.compile(r'\b[a-zA-Z]{5,12}\b')  # Palabras de 5 a 12 letras
    patron_numero = re.compile(r'\b\d+\b')  # Números enteros

    try:
        # Abre el documento PDF
        documento = fitz.open(pdf_path)
        print(f"PDF '{pdf_path}' abierto correctamente. Procesando {len(documento)} páginas...")

        # Itera sobre cada página del PDF
        for numero_pagina in range(len(documento)):
            pagina = documento.load_page(numero_pagina)
            texto_crudo = pagina.get_text()

            # Encuentra todas las palabras que coincidan con el patrón
            palabras_pagina = patron_palabra.findall(texto_crudo)
            # Convierte a minúsculas y añade al conjunto para evitar duplicados
            palabras_seleccionadas.update([palabra.lower() for palabra in palabras_pagina])

            # Encuentra todos los números en la página
            numeros_pagina = patron_numero.findall(texto_crudo)
            numeros_encontrados.update(numeros_pagina)

        documento.close()
        print(f"Extracción completada. Se encontraron {len(palabras_seleccionadas)} palabras únicas y {len(numeros_encontrados)} números únicos.")

        # Genera las combinaciones de palabras y números
        combinaciones = set()
        for palabra in palabras_seleccionadas:
            # Añade la palabra por sí sola
            combinaciones.add(palabra)
            for numero in numeros_encontrados:
                # Combina la palabra con cada número (palabra + número)
                combinaciones.add(palabra + numero)
                # Combina el número con la palabra (número + palabra)
                combinaciones.add(numero + palabra)

        print(f"Se generaron {len(combinaciones)} combinaciones únicas.")

        # Escribe todas las combinaciones en el archivo de texto
        with open(salida_txt, 'w', encoding='utf-8') as archivo_salida:
            for combinacion in sorted(combinaciones):
                archivo_salida.write(combinacion + '\n')

        print(f"¡Diccionario generado con éxito! Guardado en: '{salida_txt}'")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica que se proporcione la ruta del PDF como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <ruta_al_archivo_pdf>")
        sys.exit(1)
    
    archivo_pdf = sys.argv[1]
    generar_diccionario(archivo_pdf)
