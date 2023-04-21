from django.http import JsonResponse, HttpResponse 
from datetime import datetime
from threading import Thread
import time
from django.shortcuts import render

from .process.store_dijoncteur import dijoncteur_coupe
from .process.store_Temp_actuel import tempActuel
from .process.store_Temp_choisi import tempChoisi
from .process.chaudiere.store import chaudiereAllumee

from .process.controlleur.core import controlleur


def dijoncteurThread():
  global dijoncteur_coupe
  global tempActuel
  global tempChoisi
  global chaudiereAllumee

  for num in range(1,6):
    time.sleep(1)
    print(num)
  dijoncteur_coupe = True
  tempActuel = 24
  tempChoisi = 27
  chaudiereAllumee = True

  print("Fini !")

Thread(target=dijoncteurThread).start()
 
def index(request):
  global dijoncteur_coupe
  global tempActuel
  global tempChoisi
  global chaudiereAllumee

  now = datetime.now()

  if dijoncteur_coupe:
    dijoncteur_status = "Coupé"
  else:
    dijoncteur_status = "Non coupé"
  if chaudiereAllumee:
    chaudiere_status = "Allumée"
  else:
    chaudiere_status = "Eteinte"

  context = {
    'dijoncteur': dijoncteur_status,
    'temperatureActuelle': tempActuel,
    'temperatureChoisi': tempChoisi,
    'chaudiere': chaudiere_status,
    'now': now }
  
  return render(request, 'base.html', context)
