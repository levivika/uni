from django.shortcuts import render, get_object_or_404, redirect
from .models import Club
from .forms import ClubForm


def clubs_list(request):
    clubs = Club.objects.all()
    return render(request, 'students/clubs_list.html', {'clubs': clubs})



def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    return render(request, 'students/club_detail.html', {'club': club})


def add_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clubs_list')
    else:
        form = ClubForm()

    context = {
        'form': form,
    }
    return render(request, 'students/add_club.html', context)



def edit_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            form.save()
            return redirect('clubs_list')
    else:
        form = ClubForm(instance=club)

    context = {
        'form': form,
        'club': club,
    }
    return render(request, 'students/edit_club.html', context)



def delete_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    if request.method == 'POST':
        club.delete()
        return redirect('clubs_list')

    return render(request, 'students/delete_club.html', {'club': club})
