from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Registration, Assignment, Teacher
from operator import itemgetter


def index(request):
    if request.session.get('name') is not None:
        match = Registration.objects.get(Q(Registration=request.session.get('name')))
        msg = {'sr': match}
        return render(request, 'dbms/dashboard.html', msg)

    if request.session.get('fname') is not None:
        match = Teacher.objects.get(Q(Teacher_id=request.session.get('fname')))
        dt = Registration.objects.all()
        return render(request, 'dbms/faculty_dashboard.html', {'tm': match, 'sr': dt})
    return render(request, 'dbms/index.html')


def register(request):
    Name = request.POST['name'].upper()
    registration = request.POST['registration']
    Course = request.POST['course'].upper()
    Email = request.POST['email']
    pswd = request.POST['password']
    c_Password = request.POST['c_password']
    Gender = request.POST['radio']
    notification = {'note': 'Registered Successfully...!'}

    if pswd != c_Password:
        notification = {'note': 'Password did not match...!',
                        'name': Name,
                        'reg': registration,
                        'course': Course,
                        'email': Email
                        }
        return render(request, 'dbms/signup.html', notification)

    regis = Registration(
        Name=Name,
        Registration=registration,
        Course=Course,
        Email=Email,
        pswd=pswd,
        Gender=Gender
    )
    regis.save()
    return render(request, 'dbms/signup.html', notification)


def signin(request):
    if request.session.get('name') is not None:
        match = Registration.objects.get(Q(Registration=request.session.get('name')))
        msg = {'sr': match}
        return render(request, 'dbms/dashboard.html', msg)

    if request.session.get('fname') is not None:
        match = Teacher.objects.get(Q(Teacher_id=request.session.get('fname')))
        dt = Registration.objects.all()
        return render(request, 'dbms/faculty_dashboard.html', {'tm': match, 'sr': dt})
        #return HttpResponse("rrrrrrrrrr")
    return render(request, 'dbms/login.html')


def login(request):
    if request.session.get('name') is not None:
        match = Registration.objects.get(Q(Registration=request.session.get('name')))
        msg = {'sr': match}
        return render(request, 'dbms/dashboard.html', msg)

    if request.session.get('fname') is not None:
        match = Teacher.objects.get(Q(Teacher_id=request.session.get('fname')))
        dt = Registration.objects.all()
        return render(request, 'dbms/faculty_dashboard.html', {'tm': match, 'sr': dt})

    if request.method == 'POST':
        name = request.POST["s_register"]
        pswd = request.POST["s_password"]
        fname = request.POST["f_register"]
        fpswd = request.POST["f_password"]
        sf_login = request.POST["sf_login"]
        try:
            if 's_login' == sf_login:
                if name and pswd:
                    match = Registration.objects.get(Q(Registration=name))
                    if match.pswd == pswd:
                        msg = {'sr': match}
                        request.session['name'] = name
                        return render(request, 'dbms/dashboard.html', msg)
                    else:
                        return render(request, 'dbms/login.html')
                else:
                    return render(request, 'dbms/login.html')

            if 'f_login' == sf_login:

                if fname and fpswd:
                    Tmatch = Teacher.objects.get(Q(Teacher_id=fname))
                    if Tmatch.pswd == fpswd:
                        dt = Registration.objects.all().order_by('Registration')
                        request.session['fname'] = fname
                        return render(request, 'dbms/faculty_dashboard.html', {'sr': dt, 'tm': Tmatch})
                    else:
                        return render(request, 'dbms/login.html')
                else:
                    return render(request, 'dbms/login.html')

        except:
            return render(request, 'dbms/login.html')

    else:
        return render(request, 'dbms/login.html')


def student_login(request):
    return render(request, 'dbms/student_login.html')


def signup(request):
    return render(request, 'dbms/signup.html')


def dashboard(request):
        return redirect('login')


def student_profile(request):
    return redirect('login')


def faculty_dashboard(request):
    return redirect('login')


def f_dashboard(request):
    if request.method == "POST":
        f_logout = request.POST['c_btn']
        if 'f_logout' == f_logout:
            request.session.clear()
            return redirect('login')
    try:
        f_pass = request.POST['c_btn']
        subject_name = request.POST['subject_name']
        subject_code = request.POST['subject_code']

        dta = Assignment.objects.filter(Q(Course_code=subject_code))
        for i in dta:
            if i.Registration == f_pass:
                final_dta = Assignment.objects.filter(Q(Registration=i.Registration) & Q(Course_code=subject_code))
                return render(request, 'dbms/plane.html', {'noty': final_dta, 'subject_name': subject_name,
                                                           'subject_code': subject_code, 'rgst': f_pass})
        else:
            return render(request, 'dbms/plane.html', {'subject_name': subject_name, 'subject_code': subject_code})
    except:
        return redirect('login')


def detail(request):
    if request.method == "POST":
        btn_ma610 = request.POST['c_btn']
        if 's_logout' == btn_ma610:
            request.session.clear()
            print(request.session.get('name'))
            return redirect('login')

    try:
        #std_name = request.POST["ss_name"]
        std_reg = request.POST["reg"]
        Sub1 = request.POST["ma_610"]
        Sub2 = request.POST["ma_611"]
        Sub3 = request.POST["ma_606"]
        Sub4 = request.POST["ma_609"]
        Sub5 = request.POST["ma_607"]
        Sub6 = request.POST["ma_608"]
        Sub7 = request.POST["ma_647"]
        Sub8 = request.POST["ma_690"]
        btn_ma610 = request.POST['c_btn']

        if 'ma610' == btn_ma610:
            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub1))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub1,
                                                                 'c_name': 'DSA Lab using OOP Concept'})

        elif 'ma611' == btn_ma610:
            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub2))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub2,
                                                                 'c_name': 'Database Management Systems Lab'})
        elif 'ma606' == btn_ma610:

            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub3))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub3,
                                                                 'c_name': 'Data Structures and Algorithms'})

        elif 'ma609' == btn_ma610:
            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub4))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub4,
                                                                 'c_name': 'Object Oriented Programming'})
        elif 'ma607' == btn_ma610:
            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub5))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub5,
                                                                 'c_name': 'Database Management Systems'})
        elif 'ma608' == btn_ma610:
            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub6))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub6,
                                                                 'c_name': 'Computational Mathematics'})
        elif 'ma647' == btn_ma610:
            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub7))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub7,
                                                                 'c_name': 'Cloud Computing'})
        elif 'ma690' == btn_ma610:
            match = Registration.objects.get(Q(Registration=std_reg))
            asgn = Assignment.objects.filter(Q(Registration=std_reg) & Q(Course_code=Sub8))
            return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_code': Sub8,
                                                                 'c_name': 'Seminar 1'})
    except:
        return redirect('login')


def final_submit(request):
    if request.session.get('name') is not None:
        if request.method == "POST":
            f_btn = request.POST["f_sub"]
            if 'final_logout' == f_btn:
                return redirect('login')
            try:
                if 'pdf_submit' == f_btn:
                    Name = request.POST['name']
                    Rgst = request.POST['reg']
                    Course_Name = request.POST['msg']
                    Course_Code = request.POST['c_code']
                    title = request.POST['title'].upper()
                    file_upload = request.FILES['doc_upload']

                    if title == "":
                        match = Registration.objects.get(Q(Registration=Rgst))
                        asgn = Assignment.objects.filter(Q(Registration=Rgst) & Q(Course_code=Course_Code))
                        return render(request, 'dbms/student_profile.html',
                                      {'mt': match, 'pdf': asgn, 'c_n': Course_Name,
                                       'c_c': Course_Code, 'note': '*mandatory field'})

                    pdf = Assignment(
                        Name=Name,
                        Registration=Rgst,
                        Course=Course_Name,
                        Course_code=Course_Code,
                        File=file_upload,
                        Project_title=title
                    )
                    pdf.save()

                    match = Registration.objects.get(Q(Registration=Rgst))
                    asgn = Assignment.objects.filter(Q(Registration=Rgst) & Q(Course_code=Course_Code))
                    return render(request, 'dbms/student_profile.html', {'mt': match, 'pdf': asgn, 'c_n': Course_Name,
                                                                         'c_c': Course_Code})
                else:
                    return redirect('login')
            except:
                return redirect('login')
        else:
            return redirect('login')
    else:
        notification = {'note': 'You must be Logged in...!!!'}
        return render(request, 'dbms/login.html', notification)


def btn_save(request):
    if request.method == "POST":
        f_button = request.POST["f_button"]
        if 'f_logout' == f_button:
            if request.method == "POST":
                f_logout = request.POST['f_button']
                if 'f_logout' == f_logout:
                    request.session.clear()
                    return redirect('login')

        rgst = request.POST['rgst']
        topic = request.POST['f_button']
        asgn = Assignment.objects.get(Q(Registration=rgst) & Q(Project_title=topic))
        msg = {'sr': asgn}
        print(asgn.Name)
        print(topic)
        return render(request, 'dbms/update.html', {'sr': asgn})


def update(request):
    if request.method == 'POST':
        f_btn = request.POST['f_button']
        if 'f_logout' == f_btn:
            if request.method == "POST":
                f_logout = request.POST['f_button']
                if 'f_logout' == f_logout:
                    request.session.clear()
                    return redirect('login')

        if 'submit' == f_btn:
            rgst = request.POST['rgst']
            Project_title = request.POST['Project_title']
            marks = request.POST['marks']
            asgn = Assignment.objects.get(Q(Registration=rgst) & Q(Project_title=Project_title))
            asgn.Status = marks
            #msg = {'noty': asgn}
            asgn.save()
            subject_name = request.POST['subject_name']
            subject_code = request.POST['subject_code']

            dta = Assignment.objects.filter(Q(Course_code=subject_code))
            for i in dta:
                if i.Registration == rgst:
                    final_dta = Assignment.objects.filter(Q(Registration=i.Registration) & Q(Course_code=subject_code))
                    return render(request, 'dbms/plane.html', {'noty': final_dta, 'subject_name': subject_name,
                                                               'subject_code': subject_code, 'rgst': rgst})
            else:
                return render(request, 'dbms/plane.html', {'subject_name': subject_name, 'subject_code': subject_code})



