# Podstwy korzystania z GIT

## konfiguracja

	git config --global user,name=<nazwa>
	git config --global usar.email=

## tworzenie nowego repozytorium

W katalogu projektu pieszemy:

	git init

## branch
Gałąź

master
devel

git branch # sprawdza jaki to branch
git checkout -b nazwa_brancha
 
## commit

punky przywracania

By utworzyć commit, musimy

0. Sprwadzenie obecnego stanu

	git status
	
1. Dodać pliki, które chcemy mieć w commicie

	git add ścieżka do pliku
	
można dodać wszystkie pliki:
	
	git add . 
	
a na koniec commit
	
	git commit
	
	git commit -m "Prosta zmiana"