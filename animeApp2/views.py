from django.shortcuts import render, get_object_or_404
from .models import Program, People

def my_edu(request):
    program = Program.objects.get(pk=1)
    # supervisor = People.objects.get(pk=7)
    # manager = People.objects.get(pk=8)
    # my_info = People.objects.get(pk=9)
    classmates = People.objects.exclude(pk__in=[7, 8, 9])
    people = People.objects.all()
    
    group = request.GET.get('group', '')
    if group == 'office':
        people = people.filter(pk__in=[7, 8])
    elif group == 'me':
        people = people.filter(pk=9)
    elif group == 'students':
        people = people.exclude(pk__in=[7, 8, 9])
    name = request.GET.get('name', '')
    surname = request.GET.get('surname', '')
    patronymic = request.GET.get('patronymic', '')
    email = request.GET.get('email', '')
    phone_ends = request.GET.get('phone_ends', '')
    
    if surname:
        people = people.filter(surname__icontains=surname)
        
    if name:
        people = people.filter(name__icontains=name)
        
    if patronymic:
        people = people.filter(patronymic__icontains=patronymic)

    if email:
        people = people.filter(email__icontains=email)

    if phone_ends:
        people = people.filter(phone__endswith=phone_ends)
    
    sort_by = request.GET.get("sort")
    sort_dir = request.GET.get("dir", "asc")
    if sort_by == "surname":
        if sort_dir == "asc":
             people = people.order_by('surname')
        else:
            people = people.order_by('-surname')            
    context = {
        'program': program,
        'classmates': classmates,
        'people': people,
        'group': group,
        'sort_by': sort_by,
        'sort_dir': sort_dir,
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'email': email,
        'phone_ends': phone_ends,
        }
    return render(request, 'my_edu.html', context)