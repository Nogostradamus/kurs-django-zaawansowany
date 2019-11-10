from django.db.models.signals import post_save, pre_save
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Autor
import logging

autor_log = logging.getLogger("autor_log")
autor_log.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('logs/autor.log')
log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
autor_log.addHandler(log_handler)

# nasz_sygnal = Signal(providing_args=['imie'])
#
@receiver([post_save], sender=Autor)
def autor_po_zapisaniu(sender, instance, **kwargs):
    print('Wlasnie zapisalismy autora')
    print(instance.imie)
    autor_log.info("Ktos stworzyl autora " + instance.imie + " "+ instance.nazwisko)

# @receiver([pre_save], sender=Autor)
# def autor_przed_zapisaniem(sender, instance, **kwargs):
#     print('Wlasnie mamy zapisac autora')
#     print(instance)
#
# @receiver(request_finished)
# def strona_wczytana(sender, **kwargs):
#     print("Strona sie wczytala")
#
# @receiver(nasz_sygnal)
# def podane_imie(sender, **kwargs):
#     print("Podane imie", kwargs.get('imie'))
