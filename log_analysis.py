from collections import defaultdict


def analyze_logs(logs):
    """
    Questa funzione processa una lista di log ed estrae informazioni raggruppate per data,
    incluso il numero di utenti distinti e eventi distinti per ogni giorno.

    Args:
        logs (list): Lista di log, dove ogni log è una lista/tupla con formato:
                     [data_ora, user_id, ..., ..., ..., evento]
                     - Indice 0: timestamp (formato "YYYY-MM-DD HH:MM:SS")
                     - Indice 1: ID utente
                     - Indice 4: tipo di evento

    Returns:
        dict: Dizionario con le statistiche aggregate per data.
              Formato: {
                  "YYYY-MM-DD": {
                      "utenti_distinti": int,
                      "eventi_distinti": int
                  },
                  ...
              }
              Le date sono ordinate cronologicamente.

    """
    # Dizionari per tracciare utenti ed eventi univoci per data
    # Uso set per garantire unicità automatica
    users_per_date = defaultdict(set)
    events_per_date = defaultdict(set)

    # Processa ogni log entry
    for i, log in enumerate(logs):
        # Valida la struttura del log
        if not isinstance(log, (list, tuple)) or len(log) < 5:
            raise ValueError(
                f"Log alla posizione {i} non ha il formato corretto. "
                f"Atteso almeno 5 elementi, ricevuti {len(log) if isinstance(log, (list, tuple)) else 'tipo non valido'}"
            )

        # Estrai i campi necessari
        data_ora = log[0]
        user_id = log[1]
        evento = log[4]
        # Valida che i campi non siano None o vuoti
        if not data_ora or not user_id or not evento:
            raise ValueError(
                f"Log alla posizione {i} contiene campi vuoti o None"
                )

        # Estrai solo la data dal timestamp (formato "YYYY-MM-DD")
        # Separa data e ora usando lo spazio come delimitatore
        data = data_ora.split(" ")[0]
        # Aggiungi l'utente e l'evento ai set corrispondenti alla data
        users_per_date[data].add(user_id)
        events_per_date[data].add(evento)
    # Costruisci il dizionario di output con le statistiche aggregate
    output = {}

    # Itera sulle date in ordine cronologico
    for data in sorted(users_per_date.keys()):
        output[data] = {
            "utenti_distinti": len(users_per_date[data]),  # Conta utenti unici
            "eventi_distinti": len(events_per_date[data])  # Conta eventi unici
        }

    return output
