from django.db.models.signals import post_save, pre_save
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Autor

# nasz_sygnal = Signal(providing_args=['imie'])
#
# @receiver([post_save], sender=Autor)
# def autor_po_zapisaniu(sender, instance, **kwargs):
#     print('Wlasnie zapisalismy autora')
#     print(instance.imie)
#
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
