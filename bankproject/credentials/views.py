from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import District, Branch, UserProfile
from .forms import UserDetails
from django.http import JsonResponse



# Create your views here.


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            return render(request, 'add_bridge.html')
        else:
            messages.info(request, 'Username/Password Invalid')
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        # fn = request.POST['first_name']
        # ln = request.POST['last_name']
        # em = request.POST['email']
        pw = request.POST['password']
        cpw = request.POST['password1']
        if pw == cpw:
            if User.objects.filter(username=un).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            # if User.objects.filter(email=em).exists():
            #     messages.info(request, "Email Address Taken")
            #     return redirect('register')
            else:
                user = User.objects.create_user(username=un, password=pw)  # first_name=fn, last_name=ln, email=em)
            user.save()
            messages.info(request, "User Created")
            return redirect('login')
        else:
            messages.info(request, "Password Mismatch")
            return redirect('register')
    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def addbridge(request):
    # usr = User.objects.get(id=id)
    return render(request, 'add_bridge.html')


def adddetails(request):
    # usr = User.objects.get(id=id)
    # districts = District.objects.all()
    # branches = Branch.objects.all()
    form = UserDetails(request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request, "User details saved")
        return redirect('adddetails')
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     dob = request.POST.get('dob')
    #     age = request.POST.get('age')
    #     gender = request.POST.get('gender')
    #     phone = request.POST.get('phone')
    #     address = request.POST.get('address')
    #     account_type = request.POST.get('account_type')
    #     materials = request.POST.get('materials')
    #     user = User.objects.create_user(name=name, dob=dob, age=age, gender=gender, phone=phone, address=address, account_type=account_type, materials=materials)
    #
    #     user.save()
    #     messages.info(request, "User details saved")
    #     return redirect('adddetails')
    return render(request, 'add_requirements.html', {'form': form})


def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)


# def dependentfield(request):
#     districts = District.objects.all()
#     branchs = Branch.objects.all()
#     selected_district_id = request.GET.get('country', '')
#     selected_branchs = Branch.objects.filter(district_id=selected_district_id)
#     return render(request, 'add_requirements.html', {'districts': districts, 'branchs': branchs, 'selected_branchs': selected_branchs})
