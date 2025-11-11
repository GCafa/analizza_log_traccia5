# Specifica

Scrivere un programma Python che legge una lista di log anonimizzati.
Ciascun elemento della lista di log è costituito dalle seguenti otto informazioni:

- Data/Ora
- Identificativo unico dell’utente
- Contesto dell’evento
- Componente
- Evento
- Descrizione
- Origine
- Indirizzo IP

La lista di log è memorizzata in un file JSON. Ogni log è una lista contenente le otto informazioni riportate sopra.

L'obiettivo è quello di estrarre alcune informazioni dalla lista di log e salvarle in un file in formato JSON.

Estrarre le seguenti informazioni:

- per ogni data:
  - quanto utenti diversi hanno eseguito un accesso;
  - quanti eventi diversi sono associati a quella data.

# Linee guida per lo sviluppo del codice

- decidere la struttura dati più adatta a rappresentare le informazioni di uscita richieste tenendo anche conto che tali informazioni devono essere salavate in formato JSON;
- il percorso e il nome del file di ingresso e di uscita non devono essere scritti nel codice, ma l'utente deve poterli fornire al momento di eseguire il programma; procedere analogamente per fornire al programma eventuali altre informazioni necessarie per la sua esecuzione; prevedere dei valori di default in modo da semplificare l'esecuzione di test; valutare la modalità più conveniente per l'utente per fornire al programma tali informazioni;
- dividere opportunamente il codice in funzioni richiamate da un breve script; commentare tutte le funzioni introdotte descrivendo sinteticamente:
  - la loro funzione;
  - il ruolo di eventuali parametri;
  - eventuali risultati restituiti.
- se opportuno dividere il codice in più file (non importa se di ridotte dimensioni).

# Bonus

Il rispetto di uno o più dei seguenti requisiti riceverà una valutazione particolarmente positiva:

- gestione di eccezioni che possono verificarsi durante l'esecuzione;
- utilizzo della classe `Tabella2D_RO` (nel file `utilities/griglia_di_liste_RO.py`) per memorizzare la lista di log ed estrarre le informazioni richieste.
