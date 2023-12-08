from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TicTacToeGame

class TicTacToeGameViewsTestCase(TestCase):
    def setUp(self):
        # Creamos dos usuarios
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

        # Creamos un juego de prueba
        self.game = TicTacToeGame.objects.create(player1='user1', player2='user2', current_player='user1')

        # Creamos el cliente
        self.client = Client()

        # Obtenemos tokens para los usuarios
        self.token_user1 = self.get_user_token(self.user1)
        self.token_user2 = self.get_user_token(self.user2)

    def get_user_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_start_game(self):
        # Incluimos el token en el encabezado Authorization
        response = self.client.post('/start_game/user2/', HTTP_AUTHORIZATION=f'Bearer {self.token_user1}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

    def test_make_move(self):
        # Incluimos el token en el encabezado Authorization
        response = self.client.post(f'/make_move/{self.game.id}/0/', HTTP_AUTHORIZATION=f'Bearer {self.token_user1}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

    def test_get_board_state(self):
        # Incluimos el token en el encabezado Authorization
        response = self.client.get(f'/get_board_state/{self.game.id}/', HTTP_AUTHORIZATION=f'Bearer {self.token_user1}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

    def test_get_scores(self):
        # Incluimos el token en el encabezado Authorization
        response = self.client.get('/get_scores/', HTTP_AUTHORIZATION=f'Bearer {self.token_user1}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('player', response.json())

    def test_get_game_log(self):
        # Incluimos el token en el encabezado Authorization
        response = self.client.get(f'/get_game_log/{self.game.id}/', HTTP_AUTHORIZATION=f'Bearer {self.token_user1}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('log', response.json())
