from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Reservation
from .forms import ReservationForm
from django.urls import reverse

# トップページ: 会議室の選択ボタンを表示
def room_selection(request):
    rooms = Room.objects.all()
    return render(request, 'reservations/room_selection.html', {'rooms': rooms})

# 選択された会議室の予約リストを表示
def room_reservation_list(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    reservations = Reservation.objects.filter(room=room).order_by('start_time')
    return render(request, 'reservations/room_reservation_list.html', {'room': room, 'reservations': reservations})

# 予約フォームページ
def create_reservation(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.save()
            return redirect(reverse('room_reservation_list', args=[room_id]))
    else:
        form = ReservationForm()
    return render(request, 'reservations/create_reservation.html', {'form': form, 'room': room})
