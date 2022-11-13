# Visualisation sur le genre musical

## But

La visualisation portera sur les genres musicaux triés en hiérarchie, contenant des musiques avec des insultes.

La technique de visualisation employée sera le Sunburst Diagram.

## Description des fichiers présents (utilisation dans l'ordre)

1. [script_making_finalcsv.R](https://github.com/KevayneCst/InformationVisualisation/blob/main/musical_genre/script_making_finalcsv.R) : A partir des données brutes de wasabi (trouvables [ici](https://github.com/micbuffa/WasabiDataset#overview), 3 premiers liens (sons, artistes, albums)) extractions, filtres et fusion des 3 tables pour en garder une seule qui sera une base commune aux différentes techniques de visualisation. Contient environ 84k lignes correspondant à des musiques différentes
   - [final.csv](https://github.com/KevayneCst/InformationVisualisation/blob/main/musical_genre/final.csv) : Données générées par le point précédent
2. [script_making_genrecountedcsv.R](https://github.com/KevayneCst/InformationVisualisation/blob/main/musical_genre/script_making_genrecountedcsv.R) : Regroupement et somme des musiques sur le même genre musical pour être exploité plus tard
   - [genre_counted.csv](https://github.com/KevayneCst/InformationVisualisation/blob/main/musical_genre/genre_counted.csv) : Données générées par le point précédent
3. [script_genre_python.py](https://github.com/KevayneCst/InformationVisualisation/blob/main/musical_genre/script_genre_python.py) : Pour trier l'ensemble des genres présents (en les récupérants sur les données du point n°2) dans une hiérarchie établie manuellement.
4. [script_json_python.py](https://github.com/KevayneCst/InformationVisualisation/blob/main/musical_genre/script_json_python.py) : Pour lier la hiérarchie et les données réelles (celles données au point n°2) pour en créer un fichier JSON, qui sera utilisé par d3js
