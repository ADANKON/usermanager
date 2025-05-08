from .views import connexion, inscription, accueil, deconnexion

urlpatterns = [
    path('login/', connexion, name='login'),
    path('register/', inscription, name='register'),
    path('accueil/', accueil, name='accueil'),
    path('logout/', deconnexion, name='logout'),
]
