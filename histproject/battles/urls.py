from django.urls import path, include

from histproject.battles.views import ListBattleView, CreateBattleView, DetailBattleView, UpdateBattleView, \
    DeleteBattleView

urlpatterns = [
    path('', ListBattleView.as_view(), name='battle_list'),
    path('new/', CreateBattleView.as_view(), name='battle_create'),
    path('<int:pk>/', include([
        path('', DetailBattleView.as_view(), name='battle_detail'),
        path('edit/', UpdateBattleView.as_view(), name='battle_edit'),
        path('delete/', DeleteBattleView.as_view(), name='battle_delete'),
    ]))
]

