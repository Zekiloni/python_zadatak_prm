## Magicni kvadrat

Magicni kvadrat je matrica dimenzija n x n čiji su elementi brojevi, tako da se zbir svake vrste, kolone i dijagonale jednako.

### Funkcija `magic_square`

Funkcija `magic_square` kreira magicni kvadrat pomoću sledećeg procesa:

1. Proverava da li je uneti broj n paran. Ukoliko jeste, funkcija vraća poruku da unesite neparan broj.

2. Inicijalizuje matricu `magic_square` sa nulama dimenzija n x n.

3. Postavlja početnu vrednost `magic_number` na 1 i poziciju prvog broja u matrici `magic_square` na vrh srednje kolone.

4. U petlji se pomeraju pozicije u matrici `magic_square` koristeći sledeći algoritam: ako se dođe do kraja matrice, idemo na početak matrice, a ako se dođe do zauzetog polja, idemo na sledeće.

5. Ukoliko se dođe do slobodnog polja, postavlja se `magic_number` i inkrementira se za 1.

### Funkcija `print_magic_square`

Funkcija `print_magic_square` ispisuje (prikazuje) matricu `magic_square` u komandnoj konzoli.