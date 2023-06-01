from django.shortcuts import render, redirect
from .models import Membre
from django.contrib.auth import authenticate, login

def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        mot_de_passe = request.POST.get('mot_de_passe')
        
        membre = Membre(nom=nom, mot_de_passe=mot_de_passe)
        membre.save()
        
        return render(request, 'connexion.html')
    
    return render(request, 'inscription.html')


def connexion(request):
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom')
        print(nom_utilisateur)
        mot_de_passe = request.POST.get('mot_de_passe')
        print(mot_de_passe)

        # Vérifier les informations d'identification avec authenticate()
        membre = authenticate(request, username="damien", password="damien")
        print(membre)
        if membre is not None:
            # Informations d'identification valides, connecter l'utilisateur
            login(request, membre)
            return redirect('confirmation_connexion')
        else:
            # Informations d'identification invalides, afficher un message d'erreur
            message_erreur = "Nom d'utilisateur ou mot de passe incorrect"
            return render(request, 'connexion.html', {'message_erreur': message_erreur})

    return render(request, 'connexion.html')