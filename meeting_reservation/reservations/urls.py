from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_selection, name='room_selection'),  # トップページ（会議室選択画面）
    path('room/<int:room_id>/', views.room_reservation_list, name='room_reservation_list'),  # 会議室の予約リスト
    path('room/<int:room_id>/reserve/', views.create_reservation, name='create_reservation'),  # 予約ページ
]
