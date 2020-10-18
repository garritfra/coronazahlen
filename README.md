# Heutige Coronazahlen in Deutschland

`coronazahlen.py` listet den 7-tages-Inzidenz Wert aller Landkreise Deutschlands,
und speichert diesen in eine Excel-Tabelle.

Primär wird dieses script dafür verwendet, die Zahlen Deutschlandweit über einen langen Zeitraum zu vergleichen.

## Verwendung

```sh
# Abhängigkeiten installieren
pip install -r requirements.txt

# Ausführen
python coronazahlen.py
```

### Cross-kompilieren von MacOS/Linux -> Windows

Für die cross-kompilierung wird Docker verwendet:

```sh
# .spec generieren
docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux "pyinstaller --onefile coronazahlen.py"

# .exe bauen
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
```
