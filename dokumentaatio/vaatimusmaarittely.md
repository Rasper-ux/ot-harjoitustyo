# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla ylläpitäjien eli valmentajien on mahdollista lisätä joukkuelleen tapahtumia, eli harjoituksia tai pelejä, kalenteriin ja nähdä, kuinka moni on tulossa paikalle. Pelaajat eli käyttäjät voivat ilmoittautua tapahtumiin IN jos pääsevät paikalle tai OUT jos eivät.

## Käyttäjät

Sovelluksessa on ylläpitäjiä eli valmentajia ja käyttäjiä eli pelaajia

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Ylläpitäjä ja käyttäjä voivat luoda järjestelmään käyttäjätunnuksen
  - Rekisteröityessä ilmoitetaan onko rekisteröityjä ylläpitäjä vai käyttäjä
    - Jos ilmoittaa olevansa ylläpitäjä, kysytään rekisteröityessä joukkueen salasanaa
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä
- Ylläpitäjä ja käyttäjä voivat kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos ylläpitäjää tai käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen

- Käyttäjä näkee joukkueensa tapahtumat, joihin pystyy ilmoittautumaan
- Ylläpitäjä voi luoda uuden tapahtuman
  - Luotu tapahtuma näkyy ylläpitäjille ja käyttäjille
- Ylläpitäjä voi tarkastella, kuinka moni käyttäjä on tapahtumaan IN ja kuinka moni OUT
- Käyttäjä voi merkitä itsensä tapahtumiin IN tai OUT
- Ylläpitäjä ja käyttäjä voivat kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Sovellukseen pystyy lisämään useampia joukkueita
- Ylläpitäjä voi editoida tapahtuman tietoja
- Käyttäjä pystyy lisämään syyn tapahtumasta poisjäämiselleen
- Lisätään tapahtumaan kenttä, johon on mahdollista merkitä tarkempia tapahtumaan liittyviä tietoja
- Käyttäjätunnuksen poisto
