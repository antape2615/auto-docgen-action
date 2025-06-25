import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_doc(function_code: str, language="Python") -> str:
    prompt = f"""
                    Eres un experto en desarrollo. Documenta la siguiente función en formato Markdown.

                    Lenguaje: {language}
                    Código: Devuelve una descripción clara del propósito, parámetros y retorno.
                    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Eres un asistente que documenta código de forma precisa."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]