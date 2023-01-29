## Magični kvadrat

Magični kvadrat je matrica dimenzija n x n čiji su elementi brojevi, čiji se zbir svih brojeva u svakoj koloni, svakom redu i u oba dijagonalna reda jednak.

### Funkcija `magic_square`


*Postoji biblioteka u Python-u za generisanje i proveru magičnih kvadrata. Ova biblioteka omogućava kreiranje različitih tipova magičnih kvadrata korišćenjem različitih brojeva, uključujući i pare brojeve, i pruža funkcije za proveru da li neki kvadrat zadovoljava kriterijume magičnosti.*

`pip install magic_square` [PyPi](https://pypi.org/project/magic_square/).


Funkcija `magic_square` kreira magični kvadrat pomoću sledećeg procesa:

1. Proverava da li je uneti broj n paran. Ukoliko jeste, funkcija vraća poruku da unesete neparan broj.

2. Inicijalizuje matricu `magic_square` sa nulama dimenzija n x n.

3. Postavlja početnu vrednost `magic_number` na 1 i poziciju prvog broja u matrici `magic_square` na vrh srednje kolone.

4. U petlji se pomeraju pozicije u matrici `magic_square` koristeći sledeći algoritam: ako se dođe do kraja matrice, idemo na početak matrice, a ako se dođe do zauzetog polja, idemo na sledeće.

5. Ukoliko se dođe do slobodnog polja, postavlja se `magic_number` i inkrementira se za 1.

### Funkcija `print_magic_square`

Funkcija `print_magic_square` ispisuje (prikazuje) matricu `magic_square` u komandnoj konzoli.