# -*-coding:Latin-1 -*
import os # On importe le module os

def mon_decorateur(fonction):
    """Notre décorateur : il va afficher un message avant l'appel de la
    fonction définie"""
    
    def fonction_modifiee():
        """Fonction que l'on va renvoyer. Il s'agit en fait d'une version
        un peu modifiée de notre fonction originellement définie. On se
        contente d'afficher un avertissement avant d'exécuter notre fonction
        originellement définie"""
        
        print("Attention ! On appelle {0}".format(fonction))
        return fonction()
    return fonction_modifiee

@mon_decorateur
def salut():
    print("Salut !")

salut()

"""
@mon_decorateur
def salut():
...
revient au même, pour Python, que le code :
def salut():
    ...

salut = mon_decorateur(salut)"""

def obsolete(fonction_origine):
    """Décorateur levant une exception pour noter que la fonction_origine
    est obsolète"""
    
    def fonction_modifiee():
        raise RuntimeError("la fonction {0} est obsolète !".format(fonction_origine))
    return fonction_modifiee
#---------------------------------------------------------------
"""Pour gérer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre
de secondes écoulées depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour
s'exécuter"""

import time

def controler_temps(nb_secs):
    """Contrôle le temps mis par une fonction pour s'exécuter.
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""
    
    def decorateur(fonction_a_executer):
        """Notre décorateur. C'est lui qui est appelé directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""
        
        def fonction_modifiee():
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""
            
            tps_avant = time.time() # Avant d'exécuter la fonction
            valeur_renvoyee = fonction_a_executer() # On exécute la fonction
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format( \
                        fonction_a_executer, tps_execution))
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur

@controler_temps(4)
def attendre():
    input("Appuyez sur Entrée...")

attendre()    




os.system("pause")
