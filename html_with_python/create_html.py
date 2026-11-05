# create_html.py

import sys
from pathlib import Path

def init_html(title: str) -> str:
    """
    Creates a basic HTML page.

    Parameters
    - title (str): the string that will be tagged by `<title></title>`

    Returns
    - str: the basic HTML structure.
    """
    return (
        f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,   initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    
</body>
</html>
        """
            )

if __name__ == "__main__":

    file_name = sys.argv[1]
    new_html = init_html(file_name)

    diretorio_base = Path(
        r"C:\Users\conte\OneDrive\Documentos"
        r"\desenvolvimento_web_guanabara\html_css\exercicios\ex_001"
        )
    
    created_file = diretorio_base / f"{file_name}.html"

    created_file.write_text(new_html)

    









