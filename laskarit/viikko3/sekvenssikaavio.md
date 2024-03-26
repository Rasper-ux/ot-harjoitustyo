```mermaid
 sequenceDiagram
    participant main
    participant rautatietori
    participant ratikka6
    participant bussi244
    participant laitehallinto
    participant lippu_luukku
    main ->> laitehallinto: HKLLaitehallinto()
    main ->> rautatietori: Lataajalaite()
    main ->> ratikka6: Lukijalaite()
    main ->> bussi244: Lukijalaite()
    main ->> laitehallinto: lisaa_lataaja(rautatetori)
    main ->> laitehallinto: lisaa_lukija(ratikka6)
    main ->> laitehallinto: lisaa_lukija(bussi244)
    main ->> lippu_luukku: osta_matkakortti("Kalle")
    lippu_luukku ->> kallen_kortti: Matkakortti(Kalle)
    activate rautatietori
    main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
    rautatietori ->> kallen_kortti: kasvata_arvoa(3)
    rautatietori -->> main;
    deactivate rautatietori
    activate ratikka6
    main ->> ratikka6: osta_lippu(kallen_kortti, 0)
    ratikka ->> kallen_kortti: arvo
    kallen_kortti -->> ratikka: 3
    ratikka ->> kallen_kortti: vahenna_arvoa(1.5)
    ratikka6 -->> main: True
    deactivate ratikka6
    activate bussi244
    main ->> bussi244: osta_lippu(kallen_kortti, 2)
    ratikka ->> kallen_kortti: arvo
    kallen_kortti -->> ratikka: 1.5
    ratikka6 -->> main: False
    deactivate bussi244
```
