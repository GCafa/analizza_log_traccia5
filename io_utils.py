import json
from pathlib import Path


def load_logs(filepath):
    """
      Carica i log da un file JSON.

      Args:
          filepath (str): Percorso del file JSON contenente i log.

      Returns:
          list: Lista di log caricati dal file JSON.
    """
    try:
        file_path = Path(filepath)

        if not file_path.exists():
            raise FileNotFoundError(f"Il file '{filepath}' non esiste")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"Il file '{filepath}' deve contenere una lista di log")

        return data
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Errore nel parsing del file '{filepath}': {e.msg}",
            e.doc,
            e.pos
        )

def save_output(data, filepath):
    """
       Salva i dati in un file JSON.

       Args:
           data (dict): Dizionario contenente i dati da salvare.
           filepath (str): Percorso del file JSON di output.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)