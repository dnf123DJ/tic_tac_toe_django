from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import TicTacToeGame, PlayerProfile
from .serializers import TicTacToeGameSerializer

@api_view(['POST'])
@login_required
def start_game(request, player2):
    player1 = request.user.username
    game = TicTacToeGame(player1=player1, player2=player2, current_player=player1)
    game.save()
    serializer = TicTacToeGameSerializer(game)
    update_game_log(game, f"Game started: {player1} vs {player2}")
    return JsonResponse(serializer.data)

@api_view(['POST'])
@login_required
def make_move(request, game_id, position):
    game = get_object_or_404(TicTacToeGame, id=game_id)

    if game.current_player != request.user.username:
        return JsonResponse({'error': 'Not the current player\'s turn'})

    if position < 0 or position > 8 or game.board[position] != ' ':
        return JsonResponse({'error': 'Invalid move'})

    player = request.user.username 
    if player == game.player1 :
        player_symbol = 'X'
    else :
        player_symbol = 'O'
        
    if player_symbol != game.board[position] and ' ' != game.board[position]:
        return JsonResponse({'error': 'Not your symbol'})

    game.board = game.board[:position] + player_symbol + game.board[position + 1:]
    game.moves += 1

    winner = check_winner(game.board)

    if winner == 'X':
        winner = game.player1
    elif winner == 'O':
        winner = game.player2

    if winner:
        game.winner = winner
        update_score(winner)
        update_game_log(game, f"Player {winner} wins!")
    elif game.moves == 9:
        game.is_draw = True
        update_game_log(game, "The game is a draw.")
    else:
        game.current_player = game.player1 if player == game.player2 else game.player2

    serializer = TicTacToeGameSerializer(game)
    game.game_state = serializer.data
    game.save()

    return JsonResponse(serializer.data)

@api_view(['GET'])
@login_required
def get_board_state(request, game_id):
    game = get_object_or_404(TicTacToeGame, id=game_id)
    serializer = TicTacToeGameSerializer(game)
    return JsonResponse(serializer.data)

@api_view(['GET'])
@login_required
def get_scores(request):
    player = request.user.username
    scores = {
        'player': player,
        'score': PlayerProfile.objects.get(user=request.user).score,
        'games_played': TicTacToeGame.objects.filter(Q(player1=player) | Q(player2=player)).count(),
    }
    return JsonResponse(scores)

@api_view(['GET'])
@login_required
def get_game_log(request, game_id):
    game = get_object_or_404(TicTacToeGame, id=game_id)
    return JsonResponse({'log': game.log.split('\n')})

def update_game_log(game, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    game.log += f"{timestamp} - {message}\n"
    game.save()

def check_winner(board):
    for i in range(3):
        if board[i*3] == board[i*3 + 1] == board[i*3 + 2] != ' ':
            return board[i*3]
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]

    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]

    return None

def update_score(winner):
    player_score = PlayerProfile.objects.filter(user__username=winner).first()
    if player_score:
        player_score.score += 1
        player_score.save()
    else:
        PlayerProfile.objects.create(user=User.objects.get(username=winner), score=1)

