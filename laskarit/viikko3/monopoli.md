```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
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
    Sattuma_ja_yhteismaa -- Kortti
    Kortti -- Toiminto
    Normaalit_kadut -- Toiminto	
    Normaalit_kadut -- Pelaaja
    Normaalit_kadut -- Rakennus
    Rakennus -- Talot
    Rakennus -- Hotellit
    Vankila -- Toiminto
    Aloitusruutu -- Toiminto
    Asemat_ja_laitokset -- Toiminto
    Pelaaja -- Rahaa
```
