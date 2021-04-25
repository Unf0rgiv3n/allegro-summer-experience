# Allegro Summer E-xperience - Zad3

![1](https://user-images.githubusercontent.com/38940717/115964641-bee53f00-a525-11eb-8045-804144f67100.jpg)

##Instalacja

Wymagania:

Python 3.7+

VirtualENV ```pip install virtualenv```

1. Pobieramy repozytorium
2. Następnie w folderze w którym wypakowaliśmy pliki (wszystkie komendy wykonujemy tam gdzie jest setup.py)
3. Tworzymy virtualenv 

Linux:
```python3 -m venv venv```
Windows:
```py -3 -m venv venv```

3. Aktywujemy virtualenv

Linux:
``` . venv/bin/activate ```
Windows:
```venv\Scripts\activate```

4. ```pip install -e .```

5. ```flask run```

6. Wchodzimy na stronę ```http://127.0.0.1:5000/```

Uwaga:

Gdyby nie działały komendy w powershellu to trzeba przestawić ExecutionPolicy

Ustawiamy na chwilę uruchamiana virtualenv (przed):

```Set-ExecutionPolicy RemoteSigned```

potem wracamy do standardowego w systemie

```Set-ExecutionPolicy Restricted```

##Opis

Aplikacja używa miniframeworka Flask oraz biblioteki Requests.

Użyte źródła:

https://flask.palletsprojects.com/en/1.1.x/

https://docs.github.com/en/rest

##Założenia/uwagi

-Przyjąłem, że skoro dla każdego ma istnieć możliwość wylistowania repozytoriów i sumy gwiazdek to mówimy tylko o publicznych repozytoriach, w klasie API dodałem możliwość przekazania tokena z GitHuba w celu możliwości zwiększenia ilości requestów w ciągu godziny (zgodnie z dokumentacją na stronie GitHub)

-Należałoby dopisać testy jednostkowe do kodu, ale z powodu małego doświadczenia z testami to się na to nie zdecydowałem w momencie pisania

-Poprawić frontend aplikacji, dodać paginację wyników - wszystkie wyniki są prezentowane na jednej stronie np dla microsoftu będzie to ok. 4 tys rekordów.

-Dodać możliwość wpisania tokenu na stronie, żeby nie musiec wpisywać go w kodzie

Dziękuje za poświęcony czas i smacznej kawusi życzę ☕ :)
