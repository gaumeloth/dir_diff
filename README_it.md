# Progetto: Analizzatore di Differenze tra Cartelle

## Obiettivi

L'obiettivo principale è sviluppare uno strumento in Python che permetta agli utenti di analizzare e confrontare le strutture di file di due cartelle specificate. Lo strumento eseguirà una scansione ricorsiva delle cartelle e dei file, e fornirà un dettagliato resoconto delle differenze tra i file corrispondenti, insieme a statistiche e metadati relativi all'operazione.

---

## Funzionalità

1. **Selezione delle Cartelle**: L'utente fornirà i percorsi delle cartelle da confrontare.
2. **Analisi Ricorsiva**: Lo strumento eseguirà una scansione ricorsiva delle cartelle e delle sottocartelle.
3. **Confronto dei File**: Saranno confrontati i file corrispondenti nelle due strutture.
4. **File di Log**: Generazione di file di log dettagliati contenuti in una cartella dedicata.
5. **Statistiche**: Saranno fornite statistiche aggregate relative alle differenze tra i file.
6. **Metadati dell'Esecuzione**: Dettagli come data, ora e percorsi delle cartelle confrontate saranno inclusi.

---

## Strumenti Utilizzati

- **Python**: Il linguaggio di programmazione principale, scelto per la sua leggibilità, modularità e ampia libreria standard.
- **Git**: Per il controllo delle versioni e la collaborazione.
- **Framework di Test Unitari**: Per scrivere ed eseguire test unitari.

---

## Struttura del Progetto e Giustificazioni

La struttura del progetto è modularizzata in diversi file e moduli per promuovere la leggibilità del codice, la riusabilità e la facilità di manutenzione.

```plaintext
ProjectRoot/
|-- main.py                  (Punto di ingresso)
|-- directory_analyzer.py    (Analisi delle directory)
|-- file_comparator.py       (Confronto dei file)
|-- log_writer.py            (Scrittura dei log)
|-- statistics.py            (Calcolo delle statistiche)
|-- utils/                   (Funzioni di utilità)
|   |-- __init__.py
|   |-- utility_functions.py
|-- tests/                   (Test unitari)
|   |-- __init__.py
|   |-- test_directory_analyzer.py
|   |-- test_file_comparator.py
|   |-- test_log_writer.py
|   |-- test_statistics.py
```

### Giustificazioni:

- **Modularità**: Ogni componente è isolato in un modulo separato per facilitare la manutenzione e il testing.
- **Riusabilità**: I moduli possono essere facilmente riutilizzati in altri progetti o contesti.
- **Collaborazione**: Una struttura modularizzata facilita la collaborazione tra sviluppatori.
- **Scalabilità**: Aggiungere nuove funzionalità è più facile con una struttura modulare.

---

Con questo approccio, il progetto sarà ben organizzato e facilmente estendibile, permettendo una manutenzione e un'aggiunta di nuove funzionalità più agevoli nel tempo.
