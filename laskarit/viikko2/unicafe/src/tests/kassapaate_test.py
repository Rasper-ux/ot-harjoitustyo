import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.kortti2 = Maksukortti(100)
    
    def test_kassapaatteen_rahamaara(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_edullisia_myyty_alussa(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaita_myyty_alussa(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassan_rahamaara_kasvaa_edullisen_lounaan_hinnalla_kun_tarpeeksi_kateista(self):
        self.kassa.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.4)

    def test_kassan_rahamaara_kasvaa_maukkaan_lounaan_hinnalla_kun_tarpeeksi_kateista(self):
        self.kassa.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1004.0)
    
    def test_vaihtorahan_suuruus_oikea_kateismaksulla_kun_rahat_riittaa_edulliseen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)

    def test_vaihtorahan_suuruus_oikea_kateismaksulla_kun_rahat_riittaa_maukkaaseen(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(420), 20)

    def test_myytyjen_edullisten_lounaiden_maara_kasvaa_kun_tarpeeksi_kateista(self):
        self.kassa.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassa.edulliset, 1)

    def test_myytyjen_maukkaiden_lounaiden_maara_kasvaa_kun_tarpeeksi_kateista(self):
        self.kassa.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kassan_rahamaara_ei_kasva_edullisen_lounaan_hinnalla_kun_ei_tarpeeksi_kateista(self):
        self.kassa.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kassan_rahamaara_ei_kasva_maukkaan_lounaan_hinnalla_kun_ei_tarpeeksi_kateista(self):
        self.kassa.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_vaihtorahan_suuruus_oikea_kateismaksulla_kun_rahat_ei_riita_edulliseen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)

    def test_vaihtorahan_suuruus_oikea_kateismaksulla_kun_rahat_ei_riita_maukkaaseen(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(350), 350)

    def test_myytyjen_edullisten_lounaiden_maara_ei_kasva_kun_ei_tarpeeksi_kateista(self):
        self.kassa.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassa.edulliset, 0)

    def test_myytyjen_maukkaiden_lounaiden_maara_ei_kasvaa_kun_ei_tarpeeksi_kateista(self):
        self.kassa.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullisen_lounaan_veloitus_kortilta_kun_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_maukkaan_lounaan_veloitus_kortilta_kun_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
    
    def test_myytyjen_edullisten_lounaiden_maara_kasvaa_kun_tarpeeksi_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassa.edulliset, 1)

    def test_myytyjen_maukkaiden_lounaiden_maara_kasvaa_kun_tarpeeksi_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kortin_rahamaara_ei_muutu_kun_ei_rahaa_edulliseen_lounaaseen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti2)    

        self.assertEqual(self.kortti2.saldo_euroina(), 1.0)

    def test_kortin_rahamaara_ei_muutu_kun_ei_rahaa_maukkaaseen_lounaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti2)

        self.assertEqual(self.kortti2.saldo_euroina(), 1.0)

    def test_myytyjen_edullisten_lounaiden_maara_ei_kasva_kun_ei_tarpeeksi_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti2)

        self.assertEqual(self.kassa.edulliset, 0)

    def test_myytyjen_maukkaiden_lounaiden_maara_ei_kasvaa_kun_ei_tarpeeksi_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti2)

        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullisen_lounaan_veloitus_kortilta_kun_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti2), False)

    def test_maukkaan_lounaan_veloitus_kortilta_kun_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti2), False)

    def test_kassassa_oleva_rahamaara_ei_muutu_ostettaessa_edullinen_lounas_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kassassa_oleva_rahamaara_ei_muutu_ostettaessa_maukas_lounas_kortilla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kortin_saldo_muuttuu_rahaa_ladattaessa_positiivisella_luvulla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)

        self.assertEqual(self.kortti.saldo_euroina(), 15.0)

    def test_kassan_rahamaara_muuttuu_rahaa_ladattaessa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1005.0)
    
    def test_kortin_saldo_muuttuu_rahaa_ladattaessa_ei_positiivisella_luvulla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -10)

        self.assertEqual(self.kortti.saldo_euroina(), 10.0)