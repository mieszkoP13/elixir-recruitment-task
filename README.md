# Zadanie Rekrutacyjne Elixir

## Treść zadania

Mamy dwie encje: **Order** i **OrderItem**.

```
+-------------+           +--------------+
|   ORDER     | 1       * |  ORDER ITEM  |
+-------------+-----------+--------------+
| net_total   |           | net_price    |
| tax         |           | quantity     |
| total       |           | net_total    |
|             |           | total        |
+-------------+           +--------------+
```

**Order**
- `net_total` – wartość netto zamówienia
- `tax` – całkowita kwota podatku
- `total` – wartość brutto zamówienia

**OrderItem**
- `net_price` – cena netto 1 sztuki towaru (podane)
- `quantity` – ilość sztuk (podane)
- `net_total` – wartość netto pozycji
- `total` – wartość brutto pozycji

## Typy danych w bazie

| Pole | Typ SQL | Opis |
|------|---------|----------|
| `net_price` | `DECIMAL(10,2)` | Dokładna wartość pieniężna |
| `quantity` | `INTEGER` | Liczba sztuk |
| `net_total` | `DECIMAL(10,2)` | Obliczana wartość netto |
| `total` | `DECIMAL(10,2)` | Obliczana wartość brutto |
| `tax` | `DECIMAL(10,2)` | Kwota podatku |


### Dlaczego warto używać `Decimal`?

- `Decimal` przechowuje dokładne wartości dziesiętne, bez błędów float.
- W finansach **dokładność jest ważna**, nawet 1 grosz ma znaczenie.
- Możemy kontrolować **ilość miejsc po przecinku** i sposób zaokrąglania.

## Jak uruchomić

### Demo w main

```bash
python main.py
```

Wyświetli przykładowe obliczenia:
```
Netto zamówienia: 350.00
Podatek: 80.50
Brutto zamówienia: 430.50
```

### Testy

```bash
python -m unittest test_models.py
```

Oczekiwany wynik:
```
----------------------------------------------------------------------
Ran n test in Xs
OK
```
