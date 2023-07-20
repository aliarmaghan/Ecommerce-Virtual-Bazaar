from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password not match")
            return render(request, 'signup.html')
        
        try:
            if User.objects.get(email = email):
                messages.info(request, "Email already exist")
                return render(request, 'signup.html')
        except Exception as e:
            print(e)

        user = User.objects.create_user(fullname,email,password)
        user.save()
        return HttpResponse("User Created", email)
    return render(request,"signup.html")


def handlelogin(request):
    return render(request,"authentication/login.html")



def handlelogout(request):
    return redirect('/auth/login')