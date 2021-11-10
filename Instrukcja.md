# Instrukcja deploymentu backendu
1. Budujemy wybrane środowisko XCM z użyciem TeamCity. Należy pamiętać, że w przypadku, niektórych zmian nie jest konieczne budowanie wszystkich części środowiska. Z reguły jest to tylko WebAPI (konfiguracja dostępna w zakładce Parameters).
2. W polu Env należy wybrać docelowe środowisko (testing).
3. Po wykonaniu builda, uruchamiamy cmd.
4. Łączymy się ze środowiskiem testowym z użyciem następującego polecenia:

```
ssh testing.xopero.com -p 222 -l uzytkownik
```
5. Po poprawnym połączeniu, przechodzimy do lokalizacji, w której zapisane są wszystkie skrypty:
```
cd /usr/local/bin
```
6. Używając poniższej komendy jesteśmy w stanie wylistować dostępne skrypty:
```
ls
```
7. W zależności od tego, które elementy XCM zostały przebudowane, należy uruchomić poszczególne skrypty w celu przebudowania wersji środowiska testowego.

Web Api:
```
sudo ./xcm_webapi
```

Conductor:
```
sudo ./xcm_conductor
```

Smtp:
```
sudo ./xcm_smtp
```

S3 Storage:
```
sudo ./scm_s3_storage
```

8. Po poprawnym wykonaniu skryptu część backendowa jest gotowa do testowania.

# Instrukcja deploymentu frontendu

1. Przechodzimy do lokalizacji, w której znajduje się nasze lokalne repozytorium panelu XCM.
2. Przechodzimy do poniższej lokalizacji:
```
...\src\environments
```
3. Edytujemy z użyciem np. Notepada++ plik o nazwie
```
environment.prod.ts
``` 
W polu url wstawiamy docelowy adres URL naszego środowiska testowego. Poniżej znajduje się przykładowa konfiguracja:
```
export const environment = {
  production: true,
  api: {
    url: 'https://xcm.testing.xopero.com',
    timeout: 3000,
  },
  app_config: {
    title: 'Xopero Cloud Management',
    shortTitle: 'Xopero Cloud Management'
  }
};
```
4. Po zapisaniu zmian, wracamy do katalogu głownego repozytorium panelu.
5. W oknie, w którym znajduje się adres katalogu wpisujemy komendę:
```
powershell
```
6. Po uruchomieniu powershella budujemy frontend z użyciem komendy:
```
npm run build
```
7. Po pomyślnym zbudowaniu panelu, kopiujemy zawartość pliku
```
.../dist/xopero-cloud-panel-v2/*
```
8. Następnie uruchamiamy program WinSCP, w którym wpisujemy dane logowania takie jak w przypadku logowania się z użyciem SSH przy deploymencie backendu.
```
Nazwa hosta: testing.xopero.com
Numer portu: 222
Nazwa użytkowniak: <użytkownik>
Haslo: <haslo>
```
9. Tworzymy nowy folder w lokalizacji
```
/home/<nazwa_uzytkownika>/*
```
10. Po utworzeniu folderu do jego zawartości wklejamy wcześniej skopiowaną zawartość.
11. Uruchamiamy CMD i łączymy się ze środowiskiem testowym z użyciem następującego polecenia:

```
ssh testing.xopero.com -p 222 -l uzytkownik
```
12. Po poprawnym połączeniu należy wczyścić poprzeniu zdeployowane środowisko z użyciem poniższej komedny:

```
sudo rm /var/www/xcm.testing.xopero.com/*
```
oraz
```
sudo rm -r /var/www/xcm.testing.xopero.com/assets/
```
13. Do naszej lokalizacji docelowej należy przekopiować pliki z katalogu /home/<nazwa_uzytwkonika>/<nazwa_utworzenego_folder>/* z użyciem komendy:
```
cp -a /home/<nazwa_uzytkownika>/<nazwa_utworzenego_folder>/* /var/www/xcm.testing.xopero.com/
```
14. Ostatnim krokiem jest wpisanie poniższych komend:
```
sudo restorecon -R /var/www/xcm.testing.xopero.com/*
```
oraz
```
sudo restorecon -R /var/www/xcm.testing.xopero.com/
```
15. Po uruchomieniu przeglądarki i wpisaniu adresu docelowego warto jest odświeżyć cache poprzez wciśnięcie kombinacji
```
CTRL + F5
```