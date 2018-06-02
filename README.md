# Dijkstra si Warshall Aplicat pe un Graph orientat

## Cristian Marin Lemeni

## June 2, 2018

```
Abstract
In acest proiect am creat un program care iti spune, pentru parterul facultatii, cum poti
ajunge de la o sala la alta.
```
## 1 Introducere

Pentru a realiza acest scop am folosit algroritmul lui Dijkstra pentru cel mai scurt drum. De
asemenea am implementat si algoritmul lui Floyd Warshall pentru a obtine toate drumuriile.

## 2 Exemple

Cand pornesti programul acesta de intreaba unde doresti sa ajungi si de unde pornesti. De exemplu
vrei sa ajungi la sala 031 si esti langa 050a. Dupa ce introduci aceste informatii in program
algoritmul va selecta cel mai scurt drum si anume mergi pana la intrare, iar apoi mergi in fata
pana la AM unde faci la stanga si mai mergi putin.

## 3 Probleme cu acest proiect

Am avut mari dificultati in a implemnta algoritmul lui Warshall deoarece acesta are nevoie sa aiba
acces de la un nod la toate restul. Pentru a putea face acest lucru am declarat o constanta care sa
o ia ca valoare cand nu are margine pe care sa mearga.

## 4 Structura programului

Programul este impartit in doua parti. In prima pare sunt definiti cei doi algoritmi, iar in cea de
a doua parte este definit graph-ul.

## 5 Posibile imbunatatiri pe viitor

Acest proiect poate fi imbunatati daca adaugam etaje suplimentare, crescand numarul de noduri
considerabil.

## 6 Referinte

Dijkstra, E. W. "A note on two problems in connexion with graphs" 1959, publicat in Numerische Mathematik
Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L. "Introduction to Algorithms (1st ed.)" 1990 publicat in MIT Press and McGraw-Hill


