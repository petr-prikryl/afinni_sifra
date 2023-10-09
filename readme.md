# Afinní Šifra

Tento projekt implementuje afinní šifru v Pythonu, umožňující šifrování a dešifrování textu s nastavitelnými klíči.

## Popis

Afinní šifra je šifrovací metoda, která kombinuje dvě transformace: šifrování Caesarovou šifrou a lineární transformaci. Projekt umožňuje uživateli zadat vlastní klíče `a` a `b` pro šifrování.

## Funkce

Projekt zahrnuje následující funkce:

- `filter_input(text)`: Filtruje vstupní text od diakritiky, speciálních znaků a nahrazuje mezery.
- `encrypt(text, a, b)`: Zašifruje vstupní text s použitím zadaných klíčů `a` a `b`.
- `decrypt(text, a, b)`: Dešifruje vstupní text s použitím zadaných klíčů `a` a `b`.

## Instalace

1. Stáhněte nebo naklonujte tento repozitář do vašeho pracovního adresáře.
2. Ujistěte se, že máte nainstalovaný Python 3.x.
3. Instalujte potřebné knihovny pomocí příkazu `pip install -r requirements.txt`.

## Použití

Spusťte GUI aplikaci pomocí `python main.py`. Zadejte klíče `a` a `b`, napište text pro šifrování/dešifrování a klikněte na příslušné tlačítko pro šifrování/dešifrování.


## Licence

(c) 2023 Petr Přikryl