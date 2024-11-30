from django.urls import path, include

from histproject.battles.views import ListBattleView, CreateBattleView, DetailBattleView, UpdateBattleView, \
    DeleteBattleView, CreateCountryView

urlpatterns = [
    path('', ListBattleView.as_view(), name='battle_list'),
    path('country/', CreateCountryView.as_view(), name='country'),
    path('new/', CreateBattleView.as_view(), name='battle_create'),
    path('<int:pk>/', include([
        path('', DetailBattleView.as_view(), name='battle_detail'),
        path('edit/', UpdateBattleView.as_view(), name='battle_edit'),
        path('delete/', DeleteBattleView.as_view(), name='battle_delete'),
    ]))
]

