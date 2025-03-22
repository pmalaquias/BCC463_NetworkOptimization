import os  # Módulo para manipulação de arquivos


def read_file(file_path):
    """Lê um arquivo de texto e retorna uma lista com as linhas do arquivo."""

    if not os.path.exists(file_path):
        """Verifica se o arquivo existe"""
        print(f"Erro: O arquivo '{file_path}' não foi encontrado!")
        return None # Retorna None se o arquivo não existir

    with open(file_path, "r") as f:
        """Abre o arquivo em modo de leitura"""
        rows = f.readlines()  # Lê todas as linhas do arquivo
    return [row.strip() for row in rows]  # Remove espaços extras