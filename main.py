import os
import subprocess
from docgen import parser, llm_client, word_writer

REPO_PATH = "."  # Ruta actual
MODIFIED_EXT = [".py"]

def get_modified_files() -> list:
    result = subprocess.run(["git", "diff", "--name-only", "HEAD~1", "HEAD"],
                            capture_output=True, text=True)
    files = result.stdout.splitlines()
    return [f for f in files if any(f.endswith(ext) for ext in MODIFIED_EXT)]

def main():
    print("🔍 Buscando archivos modificados...")
    files = get_modified_files()
    if not files:
        print("No hay archivos relevantes modificados.")
        return

    doc = word_writer.load_or_create_document()

    for file in files:
        print(f"📄 Procesando archivo: {file}")
        functions = parser.extract_modified_functions(file)
        for name, code in functions:
            print(f"🤖 Generando documentación para: {name}")
            doc_text = llm_client.generate_doc(code)
            word_writer.update_function_doc(doc, name, doc_text)
    
    word_writer.save_document(doc)
    print("✅ Documentación actualizada en docs/documentation.docx")

if __name__ == "__main__":
    main()
