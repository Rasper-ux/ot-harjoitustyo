```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma_ja_yhteismaa
    Ruutu <|-- Asemat_ja_laitokset
    Ruutu <|-- Normaalit_kadut
    Sattuma_ja_yhteismaa "1" -- "1" Kortti
    Kortti "1" -- "1" Toiminto
    NormaalitKadut -- Toiminto
    NormaalitKadut : omistaja -- Pelaaja
    NormaalitKadut : talot
    NormaalitKadut : hotelli
    Vankila -- Toiminto
    Aloitusruutu -- Toiminto
    Asemat_ja_laitokset -- Toiminto
    Normaalit_kadut -- Toimito
    Pelaaja : rahaa
```
