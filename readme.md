generate.py:

Erzeugt die csv-Testdaten im Ordner "data" aus bivariater normalverteilter Zufallsvariable
Der Korrelationskoeff. ist dabei auch normalverteilt mit mu = 0.95 und std = 0.1  
du kannst hier bei Bedarf die Anzahl der Files sowie die Samplegröße variieren

find.py (das eigentliche Skript):
    - loop über alle Files in "data"
    - lineare Regression der Testdaten
    - if R² größer als ein Schwellenwert (Plot grün)
    - else (Plot rot)
    
requirements:
pip install numpy matplotlib scikit-learn

alle Plots werden in "plots" gespeichert