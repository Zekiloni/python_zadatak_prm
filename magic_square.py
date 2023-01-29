def magic_square(n):
    if n % 2 == 0:
        print("Unesite neparan broj.")
        return None
    
    magic_square = [[0 for x in range(n)] for y in range(n)]

    magic_square = [[0 for x in range(n)] for y in range(n)]

    row = n - 1
    col = n // 2
    magic_number = 1

    while magic_number <= n * n:
        if row == -1 and col == n:  # idemo na sledeću liniju
            col = n - 2
            row = 0
        else:
            if col == n:  # idemo na sledeću kolonu
                col = 0
            if row == -1:  # idemo na sledeću liniju
                row = n - 1
            if col == -1:  # idemo na sledeću kolonu
                col = n - 1

        if row >= n or col >= n:  # proveravamo da li se nalazimo u granicama
            col = (col + 1) % n
            row = (row + 1) % n
            continue

        if magic_square[row][col]:  # ako je polje zauzeto idemo na sledeće
            col -= 1
            row += 1
            continue
        else:
            magic_square[row][col] = magic_number
            magic_number += 1

        col += 1
        row -= 1  # pomeramo se po magičnom kvadratu

    return magic_square


def print_magic_square(square):	
    n = len(square)
    for row in range(n):
        for col in range(n):
            print(square[row][col], end="\t")
        print("")


n = int(input("Unesite željene dimenzije magičnog kvadrata: "))
print(magic_square(n))
print_magic_square(magic_square(n))
