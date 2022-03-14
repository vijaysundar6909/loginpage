


def stud(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        mail = request.POST['email']


