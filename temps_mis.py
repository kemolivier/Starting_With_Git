# -*-coding:Latin-1 -*
import os # On importe le module os

def mon_decorateur(fonction):
    """Notre d�corateur : il va afficher un message avant l'appel de la
    fonction d�finie"""
    
    def fonction_modifiee():
        """Fonction que l'on va renvoyer. Il s'agit en fait d'une version
        un peu modifi�e de notre fonction originellement d�finie. On se
        contente d'afficher un avertissement avant d'ex�cuter notre fonction
        originellement d�finie"""
        
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
revient au m�me, pour Python, que le code :
def salut():
    ...

salut = mon_decorateur(salut)"""

def obsolete(fonction_origine):
    """D�corateur levant une exception pour noter que la fonction_origine
    est obsol�te"""
    
    def fonction_modifiee():
        raise RuntimeError("la fonction {0} est obsol�te !".format(fonction_origine))
    return fonction_modifiee
#---------------------------------------------------------------
"""Pour g�rer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre
de secondes �coul�es depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour
s'ex�cuter"""

import time

def controler_temps(nb_secs):
    """Contr�le le temps mis par une fonction pour s'ex�cuter.
    Si le temps d'ex�cution est sup�rieur � nb_secs, on affiche une alerte"""
    
    def decorateur(fonction_a_executer):
        """Notre d�corateur. C'est lui qui est appel� directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""
        
        def fonction_modifiee():
            """Fonction renvoy�e par notre d�corateur. Elle se charge
            de calculer le temps mis par la fonction � s'ex�cuter"""
            
            tps_avant = time.time() # Avant d'ex�cuter la fonction
            valeur_renvoyee = fonction_a_executer() # On ex�cute la fonction
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'ex�cuter".format( \
                        fonction_a_executer, tps_execution))
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur

@controler_temps(4)
def attendre():
    input("Appuyez sur Entr�e...")

attendre()    




os.system("pause")
