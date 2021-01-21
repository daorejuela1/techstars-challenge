from django.shortcuts import render
from read_list.read_csv import read_csv_file, fill_schedule, add_mentor, generate_schedule
import os
from schedule import settings
from django.core.files.storage import default_storage
from django.shortcuts import redirect

complete_mentors = []
uncomplete_mentors = []
schedule = {}
mentors = {}
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
# Create your views here.


def generatenewview(filename):
    """
    function that generates a new schedule according to the input file

    args:
        filename: name of the .csv file

    Returns:
        schedule: schedule with the filled information according to the .csv
    """
    global schedule
    global mentors
    global complete_mentors
    global uncomplete_mentors
    complete_mentors = []
    uncomplete_mentors = []
    schedule = {}
    mentors = {}
    if not filename:
        filename = "techstar.csv"
    read_csv_file(filename, complete_mentors, uncomplete_mentors)
    schedule, mentors_bytime = generate_schedule(complete_mentors)
    schedule = fill_schedule(schedule, mentors_bytime)
    return schedule


def file_upload(request):
    """
    function that uploads a new file and stores it in the /tmp folder

    args:
        request: HTTP petition

    Returns:
        schedule: schedule with the filled information according to the .csv
    """
    global schedule
    global mentors
    global complete_mentors
    global uncomplete_mentors
    path = None
    if 'file' in request.FILES:
        save_path = os.path.join(
            settings.MEDIA_ROOT, 'uploads', str(request.FILES['file']))
        path = default_storage.save(save_path, request.FILES['file'])
    schedule = generatenewview(path)
    return schedule


def index(request):
    """
    principal function renders the base html and handles the POST petition
    to upload a new file or book new mentors

    args:
        request: HTTP petition

    Returns:
        schedule: schedule with the filled information according to the .csv
    """
    global schedule
    global mentors
    global complete_mentors
    global uncomplete_mentors

    if request.method == 'POST':
        if 'submit' in request.POST and request.POST.get('submit') == "Upload":
            schedule = file_upload(request)
        else:
            mentor = None
            for mentor in uncomplete_mentors:
                if mentor["name"] == request.POST.get('mentor_name'):
                    break
            if mentor:
                add_mentor(mentor, request.POST.get('day'),
                           request.POST.get('time'), schedule)
                uncomplete_mentors.remove(mentor)
    return render(request, 'base.html', {'schedule': schedule, 'weekdays': weekdays, 'uncomplete': uncomplete_mentors})
