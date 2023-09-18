##    Obiettivi

L'obiettivo principale è sviluppare uno strumento in Python che permetta agli utenti di analizzare e confrontare le strutture di file di due cartelle specificate. Lo strumento eseguirà una scansione ricorsiva delle cartelle e dei file, e fornirà un dettagliato resoconto delle differenze tra i file corrispondenti, insieme a statistiche e metadati relativi all'operazione.
---
##    Funzionalità

1. **Selezione delle Cartelle**: L'utente fornirà i percorsi delle cartelle da confrontare.
2. **Analisi Ricorsiva**: Lo strumento eseguirà una scansione ricorsiva delle cartelle e delle sottocartelle.
3. **Confronto dei File**: Saranno confrontati i file corrispondenti nelle due strutture.
4. **File di Log**: Generazione di file di log dettagliati contenuti in una cartella dedicata.
5. **Statistiche**: Saranno fornite statistiche aggregate relative alle differenze tra i file.
6. **Metadati dell'Esecuzione**: Dettagli come data, ora e percorsi delle cartelle confrontate saranno inclusi.
---
##  Indice
- [Obiettivi](#obiettivi)
- [Funzionalità](#funzionalità)
- [Indice](#indice)
- [Sezione Tecnica](#sezione-tecnica)
- [# Strumenti Utilizzati](## -strumenti-utilizzati)
- [Struttura del Progetto](#struttura-del-progetto)
- [# Dettagli sui Componenti e le loro Funzioni](## -dettagli-sui-componenti-e-le-loro-funzioni)
- [src/: Codice sorgente](#src/:-codice-sorgente)
- [locales/: Contiene i file per la localizzazione in diverse lingue.](#locales/:-contiene-i-file-per-la-localizzazione-in-diverse-lingue.)
- [tests/: Test unitari](#tests/:-test-unitari)
- [docs/: Documentazione](#docs/:-documentazione)
- [localizations/: README multi-lingua](#localizations/:-readme-multi-lingua)
- [README.md: README principale](#readme.md:-readme-principale)
- [.gitignore: File da ignorare](#.gitignore:-file-da-ignorare)
- [requirements.txt: Dipendenze](#requirements.txt:-dipendenze)
- [LICENSE: Licenza](#license:-licenza)
- [# Perché questa Suddivisione?](## -perché-questa-suddivisione?)
- [# File di Requisiti](## -file-di-requisiti)
- [# Utilizzo](## -utilizzo)
- [# Rationale per Questo Approccio](## -rationale-per-questo-approccio)
- [# Fase di Test](## -fase-di-test)
- [# Rationale per Queste Decisioni](## -rationale-per-queste-decisioni)
- [# Struttura e Funzionamento dei Moduli](## -struttura-e-funzionamento-dei-moduli)
- [# directory_analyzer.py](## -directory_analyzer.py)
- [# file_comparator.py](## -file_comparator.py)
- [# log_writer.py](## -log_writer.py)
- [# main.py](## -main.py)
- [# statistics.py](## -statistics.py)
- [# utils/utility_function.py](## -utils/utility_function.py)
- [File di Requisiti](#file-di-requisiti)
- [Fase di Test](#fase-di-test)
- [Struttura e Funzionamento dei Moduli](#struttura-e-funzionamento-dei-moduli)
- [Stato di Sviluppo del Progetto](#stato-di-sviluppo-del-progetto)
##     Sezione Tecnica

Questa sezione fornisce dettagli tecnici sul progetto, inclusi gli strumenti utilizzati, i file di requisiti, le fasi di test e la struttura dei moduli.

##    # Strumenti Utilizzati


- **Python**: Il linguaggio di programmazione principale, scelto per la sua leggibilità, modularità e ampia libreria standard.
- **Git**: Per il controllo delle versioni e la collaborazione.
- **Framework di Test Unitari**: Per scrivere ed eseguire test unitari.
---
##     File di Requisiti

Il progetto utilizza diversi file di requisiti per gestire le dipendenze in vari ambienti:

1. **requirements.txt**: Contiene le dipendenze necessarie per l'ambiente di produzione.
2. **requirements-dev.txt**: Contiene le dipendenze necessarie per l'ambiente di sviluppo. Include tutte le dipendenze di `requirements.txt`.
3. **requirements-test.txt**: Contiene le dipendenze necessarie per eseguire i test. Include tutte le dipendenze di `requirements.txt`.
4. **requirements-all.txt**: Contiene una combinazione di tutte le dipendenze sopra elencate. Utilizzato per l'installazione locale quando si eseguono sia sviluppo che test.

##     Fase di Test

La fase di test è un componente cruciale del ciclo di vita dello sviluppo software. Questa sezione descrive gli strumenti utilizzati, come funzionano e perché sono stati scelti.

##     Struttura e Funzionamento dei Moduli

## 
## Stato di Sviluppo del Progetto

### Funzioni Implementate

- **Analisi delle directory**: Scansiona le directory e genera una rappresentazione strutturale.
- **Confronto dei file tramite hashing**: Utilizza algoritmi di hashing per confrontare i file nelle directory.
- **Generazione di log**: Registra le operazioni effettuate durante l'analisi.
- **Statistiche di base**: Fornisce metriche di base sulle differenze tra le directory.

### Funzioni da Implementare (con Priorità)

1. **Confronto Avanzato tra File (Alta Priorità)**: 
   - **Dettagli**: Implementare un metodo di confronto più dettagliato simile a `git diff`.
   - **Motivazione**: Fornire una differenziazione più dettagliata tra i file, utile in contesti di sviluppo.
  
2. **Supporto per File di Configurazione (Media Priorità)**: 
   - **Dettagli**: Permettere agli utenti di specificare le impostazioni attraverso un file di configurazione.
   - **Motivazione**: Aumentare la flessibilità e l'usabilità del tool.
  
3. **Internazionalizzazione (Bassa Priorità)**: 
   - **Dettagli**: Aggiungere il supporto per altre lingue oltre all'inglese e all'italiano.
   - **Motivazione**: Rendere il tool accessibile a una base di utenti più ampia.

### Note per gli Sviluppatori

Questo progetto è in fase attiva di sviluppo. Si prega di seguire le linee guida per la contribuzione se si è interessati a migliorare questo strumento.
##  Utilizzo

Per utilizzare questo strumento, eseguire il seguente comando:

```bash
python main.py --dir1 /path/to/dir1 --dir2 /path/to/dir2
```

## Esempio

```bash
python main.py --dir1 ./example1 --dir2 ./example2
```
---
##     Struttura e Funzionamento dei Moduli

##
### Struttura dei Dati e Algoritmi

- **Struttura dei Dati**: Utilizza una mappa chiave-valore per memorizzare i metadati dei file durante la scansione.
- **Algoritmi di Confronto**: Utilizza algoritmi di hashing per una comparazione rapida dei file.
- **Diff Testuale**: Implementa l'algoritmo di Longest Common Subsequence (LCS) per il confronto testuale.


---
##     File di Requisiti

Il progetto utilizza diversi file di requisiti per gestire le dipendenze in vari ambienti:

1. **requirements.txt**: Contiene le dipendenze necessarie per l'ambiente di produzione.
2. **requirements-dev.txt**: Contiene le dipendenze necessarie per l'ambiente di sviluppo. Include tutte le dipendenze di `requirements.txt`.
3. **requirements-test.txt**: Contiene le dipendenze necessarie per eseguire i test. Include tutte le dipendenze di `requirements.txt`.
4. **requirements-all.txt**: Contiene una combinazione di tutte le dipendenze sopra elencate. Utilizzato per l'installazione locale quando si eseguono sia sviluppo che test.

##     Fase di Test

La fase di test è un componente cruciale del ciclo di vita dello sviluppo software. Questa sezione descrive gli strumenti utilizzati, come funzionano e perché sono stati scelti.

##     Struttura e Funzionamento dei Moduli

## 
## Stato di Sviluppo del Progetto

### Funzioni Implementate

- **Analisi delle directory**: Scansiona le directory e genera una rappresentazione strutturale.
- **Confronto dei file tramite hashing**: Utilizza algoritmi di hashing per confrontare i file nelle directory.
- **Generazione di log**: Registra le operazioni effettuate durante l'analisi.
- **Statistiche di base**: Fornisce metriche di base sulle differenze tra le directory.

### Funzioni da Implementare (con Priorità)

1. **Confronto Avanzato tra File (Alta Priorità)**: 
   - **Dettagli**: Implementare un metodo di confronto più dettagliato simile a `git diff`.
   - **Motivazione**: Fornire una differenziazione più dettagliata tra i file, utile in contesti di sviluppo.
  
2. **Supporto per File di Configurazione (Media Priorità)**: 
   - **Dettagli**: Permettere agli utenti di specificare le impostazioni attraverso un file di configurazione.
   - **Motivazione**: Aumentare la flessibilità e l'usabilità del tool.
  
3. **Internazionalizzazione (Bassa Priorità)**: 
   - **Dettagli**: Aggiungere il supporto per altre lingue oltre all'inglese e all'italiano.
   - **Motivazione**: Rendere il tool accessibile a una base di utenti più ampia.

### Note per gli Sviluppatori

Questo progetto è in fase attiva di sviluppo. Si prega di seguire le linee guida per la contribuzione se si è interessati a migliorare questo strumento.
##  Utilizzo

Per utilizzare questo strumento, eseguire il seguente comando:

```bash
python main.py --dir1 /path/to/dir1 --dir2 /path/to/dir2
```

## Esempio

```bash
python main.py --dir1 ./example1 --dir2 ./example2
```
---
##     File di Requisiti

Il progetto utilizza diversi file di requisiti per gestire le dipendenze in vari ambienti:

1. **requirements.txt**: Contiene le dipendenze necessarie per l'ambiente di produzione.
2. **requirements-dev.txt**: Contiene le dipendenze necessarie per l'ambiente di sviluppo. Include tutte le dipendenze di `requirements.txt`.
3. **requirements-test.txt**: Contiene le dipendenze necessarie per eseguire i test. Include tutte le dipendenze di `requirements.txt`.
4. **requirements-all.txt**: Contiene una combinazione di tutte le dipendenze sopra elencate. Utilizzato per l'installazione locale quando si eseguono sia sviluppo che test.

##     Fase di Test

La fase di test è un componente cruciale del ciclo di vita dello sviluppo software. Questa sezione descrive gli strumenti utilizzati, come funzionano e perché sono stati scelti.

##     Struttura e Funzionamento dei Moduli

## 
## Stato di Sviluppo del Progetto

### Funzioni Implementate

- **Analisi delle directory**: Scansiona le directory e genera una rappresentazione strutturale.
- **Confronto dei file tramite hashing**: Utilizza algoritmi di hashing per confrontare i file nelle directory.
- **Generazione di log**: Registra le operazioni effettuate durante l'analisi.
- **Statistiche di base**: Fornisce metriche di base sulle differenze tra le directory.

### Funzioni da Implementare (con Priorità)

1. **Confronto Avanzato tra File (Alta Priorità)**: 
   - **Dettagli**: Implementare un metodo di confronto più dettagliato simile a `git diff`.
   - **Motivazione**: Fornire una differenziazione più dettagliata tra i file, utile in contesti di sviluppo.
  
2. **Supporto per File di Configurazione (Media Priorità)**: 
   - **Dettagli**: Permettere agli utenti di specificare le impostazioni attraverso un file di configurazione.
   - **Motivazione**: Aumentare la flessibilità e l'usabilità del tool.
  
3. **Internazionalizzazione (Bassa Priorità)**: 
   - **Dettagli**: Aggiungere il supporto per altre lingue oltre all'inglese e all'italiano.
   - **Motivazione**: Rendere il tool accessibile a una base di utenti più ampia.

### Note per gli Sviluppatori

Questo progetto è in fase attiva di sviluppo. Si prega di seguire le linee guida per la contribuzione se si è interessati a migliorare questo strumento.
##  Utilizzo

Per utilizzare questo strumento, eseguire il seguente comando:

```bash
python main.py --dir1 /path/to/dir1 --dir2 /path/to/dir2
```

## Esempio

```bash
python main.py --dir1 ./example1 --dir2 ./example2
```
---
##     File di Requisiti

Il progetto utilizza diversi file di requisiti per gestire le dipendenze in vari ambienti:

1. **requirements.txt**: Contiene le dipendenze necessarie per l'ambiente di produzione.
2. **requirements-dev.txt**: Contiene le dipendenze necessarie per l'ambiente di sviluppo. Include tutte le dipendenze di `requirements.txt`.
3. **requirements-test.txt**: Contiene le dipendenze necessarie per eseguire i test. Include tutte le dipendenze di `requirements.txt`.
4. **requirements-all.txt**: Contiene una combinazione di tutte le dipendenze sopra elencate. Utilizzato per l'installazione locale quando si eseguono sia sviluppo che test.

##     Fase di Test

La fase di test è un componente cruciale del ciclo di vita dello sviluppo software. Questa sezione descrive gli strumenti utilizzati, come funzionano e perché sono stati scelti.

##     Struttura e Funzionamento dei Moduli

## 
## Stato di Sviluppo del Progetto

### Funzioni Implementate

- **Analisi delle directory**: Scansiona le directory e genera una rappresentazione strutturale.
- **Confronto dei file tramite hashing**: Utilizza algoritmi di hashing per confrontare i file nelle directory.
- **Generazione di log**: Registra le operazioni effettuate durante l'analisi.
- **Statistiche di base**: Fornisce metriche di base sulle differenze tra le directory.

### Funzioni da Implementare (con Priorità)

1. **Confronto Avanzato tra File (Alta Priorità)**: 
   - **Dettagli**: Implementare un metodo di confronto più dettagliato simile a `git diff`.
   - **Motivazione**: Fornire una differenziazione più dettagliata tra i file, utile in contesti di sviluppo.
  
2. **Supporto per File di Configurazione (Media Priorità)**: 
   - **Dettagli**: Permettere agli utenti di specificare le impostazioni attraverso un file di configurazione.
   - **Motivazione**: Aumentare la flessibilità e l'usabilità del tool.
  
3. **Internazionalizzazione (Bassa Priorità)**: 
   - **Dettagli**: Aggiungere il supporto per altre lingue oltre all'inglese e all'italiano.
   - **Motivazione**: Rendere il tool accessibile a una base di utenti più ampia.

### Note per gli Sviluppatori

Questo progetto è in fase attiva di sviluppo. Si prega di seguire le linee guida per la contribuzione se si è interessati a migliorare questo strumento.
##  Utilizzo

Per utilizzare questo strumento, eseguire il seguente comando:

```bash
python main.py --dir1 /path/to/dir1 --dir2 /path/to/dir2
```

## Esempio

```bash
python main.py --dir1 ./example1 --dir2 ./example2
```
---

## Documentazione del Codice

### `directory_analyzer.py`
- `scan_directory(directory_path)`: Scansiona una directory e restituisce una lista di file e sottodirectory.
- `filter_files(file_list, directory_path, extension=None, min_size=None, max_size=None, modified_after=None)`: Filtra i file in base a vari criteri.
Librerie Utilizzate: `os, time`

### `file_comparator.py`
- `hash_file(file_path, algorithm='md5')`: Genera un hash per un file.
- `compare_files(file1_path, file2_path, algorithm='md5')`: Confronta gli hash di due file.
- `text_diff(file1_path, file2_path)`: Confronto testuale tra file.
Librerie Utilizzate: `hashlib, difflib`

### `log_writer.py`
- `write_log(message, log_level)`: Scrive un log.
- `format_log_entry(log_entry)`: Formatta una voce di log.
Librerie Utilizzate: `logging`

...


---

## Requisiti

- **Requisiti Principali**: `requirements.txt` - Include le principali dipendenze come PyYAML.
- **Requisiti per lo Sviluppo**: `requirements-dev.txt` - Include strumenti per lo sviluppo come flake8 e black.
- **Requisiti per i Test**: `requirements-test.txt` - Include dipendenze per i test, come pytest e pytest-cov.
- **Tutti i Requisiti**: `requirements-all.txt` - Include una combinazione di tutte le dipendenze elencate sopra.

Per installare tutte le dipendenze, eseguire:
```bash
pip install -r requirements-all.txt
```

---

## Utilizzo

### Struttura del Comando
```bash
python main.py --dir1 <path_to_dir1> --dir2 <path_to_dir2> [opzioni]
```

### Esempi
- **Confronto Base**: 
```bash
python main.py --dir1 ./example1 --dir2 ./example2
```
- **Confronto con Filtro per Estensione**:
```bash
python main.py --dir1 ./example1 --dir2 ./example2 --ext .txt
```
...

