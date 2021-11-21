# Erforderliche Pakete

- pytube
- getestet auf Python 3.8

# Funktionsweise

Archivar läd alle Videos der übergebenen YT-Kanäle herunter.   
Für jeden Kanal wird ein eigener Ordner angelegt.   
Wenn für den Kanal schon etwas geladen wurde, werden nur neue Videos geladen.   

1. Das Programm liest die Kanäle aus, die in "channels.txt" gespeichert sind.
    1. Es gemeint die URL, die man findet, wenn man bei einem Kanal auf "Videos" klickt.
    2. Ein Kanal pro Zeile im Textfile.
   
# To Do

- sinnvolle Textausgaben, was das Programm tut.
- grafische Oberfläche
- Programm läuft im Hintergrund ->  automatische, regelmäßige Ausführung.