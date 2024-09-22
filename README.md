# Kirja-arvostelusovellus

Sovelluksen perusominaisuudet kuten rekisteröiminen, kirjautuminen ja kirja-arvosteluiden kirjoitus ja lukeminen onnistuu. Myöhemmässä versiossa arvosteluihin voi myös kommentoida ja arvosteluita pystyy hakea kirjan nimellä. Myös ylläpitäjän toiminnot puuttuu nykyisessä versiossa. Lopuksi olisi tarkoituksena parantaa sovelluksen ulkonäköä.

# Käynnistysohjeet

Kloonaa repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon `.env` tiedosto ja määritä sen sisältö seuraavanlaisesti:

> `DATABASE_URL=<tietokannan-paikallinen-osoite>`
>
> `SECRET_KEY=<salainen-avain>`

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

> `$ python3 -m venv venv`
>
> `$ source venv/bin/activate`
>
> `$ pip install -r ./requirements.txt`

Määritä vielä tietokannan skeema komennolla:

> `$ psql < schema.sql`

Nyt voit käynnistää sovelluksen komennolla:

> `$ flask run`