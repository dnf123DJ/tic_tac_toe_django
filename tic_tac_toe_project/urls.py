"""
URL configuration for tic_tac_toe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tic_tac_toe.views import (
    start_game,
    make_move,
    get_board_state,
    get_scores,
    get_game_log,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('start_game/<str:player2>/', start_game, name='start_game'),
    path('make_move/<int:game_id>/<int:position>/', make_move, name='make_move'),
    path('get_board_state/<int:game_id>/', get_board_state, name='get_board_state'),
    path('get_scores/', get_scores, name='get_scores'),
    path('get_game_log/<int:game_id>/', get_game_log, name='get_game_log'),
]
