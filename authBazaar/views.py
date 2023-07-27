from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.models import User
# email send
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .utils import generate_token,TokenGenerator
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError 
from django.core.mail import EmailMessage
from django.conf import settings
# login Authenticate 
from django.contrib.auth import authenticate,login,logout

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
                messages.info(request, "Email already in use")
                return render(request, 'signup.html')
        except Exception as e:
            pass

        user = User.objects.create_user(fullname,email,password)
        user.is_active = False
        user.save()
        email_subject ="Activate Your Account"
        message = render_to_string('activate.html',{
            'user' : user,
            'domain' : '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : generate_token.make_token(user),

        })        
        email_message = EmailMessage(
            email_subject,message,settings.EMAIL_HOST_USER,[email],
        )
        email_message.send()
        messages.success(request, "Activate your Acount by clicking on link sent to your email")
        return redirect('/auth/login/')
    return render(request, "signup.html")

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None

        if user is not None and generate_token.check_token (user, token):
            user.is_active=True
            user.save()
            messages.info(request, "Account Activated Successfully") 
            return redirect('/auth/login/')
        return render(request, 'activate fail.html')




def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser =authenticate(username = username, password = userpassword)

        if myuser is not None:
            login(request,myuser)
            # messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login')

    return render(request,'login.html')



def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')