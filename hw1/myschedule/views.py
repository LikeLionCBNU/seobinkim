from django.shortcuts import render
from .models import Schedule

# Create your views here.

def home(request):
    schedules = Schedule.objects
    return render(request, 'myschedule/home.html', {'schedules':schedules})

def detail(request, schedule_id):
    schedule_detail = get_object_or_404(Schedule, pk=schedule_id)
    return render(request, 'myschedule/detail.html', {'schedule':schedule_detail})

def schedule_new(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.published_date = timezone.datetime.now()
            schedule.save()
            return redirect('detail', schedule_id=schedule.pk)
    else:
        form = ScheduleForm()
    return render(request, 'myschedule/schedule_new.html', {'form': form})

def schedule_edit(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk = schedule_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance = schedule)
        if form.is_valid():
            schedule = form.save(commit = False)
            schedule.published_date = timezone.datetime.now()
            schedule.save()
            return redirect('detail', schedule_id = schedule.pk)
    else:
        form = ScheduleForm(instance = schedule)
    return render(request, 'myschedule/schedule_edit.html', {'form': form})

def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule.delete()
    return redirect('home')
