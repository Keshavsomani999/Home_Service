from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Labours,Contact,Orders,Project,ReviewRating
from django.contrib.auth.models import User,auth
from .forms import ReviewForm
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from twilio.rest import Client
MERCHANT_KEY = 'uUXHfPG3u7Y5tV43'

# Create your views here.

def index(request):
    labour = Labours.objects.all()
    project = Project.objects.all()
    return render(request, 'index.html',{'project':project,  'labour':labour})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid crentials')
            print(messages)
            return redirect('login')
    else:
        return render(request, 'login.html')


def accinfo(request):
    user = request.user

    return render(request, 'Accountinfo.html',{'user' : user})

def register(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
       email = request.POST['email']

       if password1 == password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,'username Taken')
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'Email Taken')
               return redirect('register')
           else:
               
               subject = "Greetings"
               msg     = "hii nice of you to join " + " Register Successfully "
               to      = email
               res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
               user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
               user.save();
               print('user created')
               return redirect('login')
       else:
           messages.info(request, 'password not matching')
           return redirect('login')

       return redirect('/')

    else:
        return render(request, 'login.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')

        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()


    return render(request, 'contacts.html')



def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html',{'project':projects})


def Maintenance_service(request):
    labours = Labours.objects.all()
    return render(request, 'Maintenance_service.html', {'lab': labours})


def Wiring_service(request):
    labours = Labours.objects.all()
    return render(request, 'Wiring_service.html', {'lab': labours})


def Tiling_service(request):
    labours = Labours.objects.all()
    return render(request, 'Tiling_service.html', {'lab': labours})

def Audio_visual_service(request):
    labours = Labours.objects.all()
    return render(request, 'Audio_visual_service.html', {'lab': labours})


def Electrial_service(request):
    labours = Labours.objects.all()
    return render(request, 'Electrial_service.html', {'lab': labours})


def Plumbing_service(request):
    labours = Labours.objects.all()
    return render(request, 'Plumbing_service.html', {'lab': labours})


def handyman(request,myid):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        labour = request.POST.get("labour", '')
        state = request.POST.get("state", '')
        city = request.POST.get("city", '')
        zip = request.POST.get("zip", '')
        phone = request.POST.get("phone", '')
        test = request.POST.get("test", '')
        price = request.POST.get("price", '')

        order = Orders(name=name, email=email, address=address, message=message, labour=labour, state=state, city=city, zip=zip, phone=phone, test=test, price=price)
        order.save()
        account_sid = 'AC4ff948ab3352c5bba49d798d556b567d'
        auth_token = '9257b8b13676e28169424c3c3153794d'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                        body=f'Hi, {name} your order has been placed Great job',
                                        from_='+16205298550',
                                        to='+91'+ phone 
                                    )
        thank = True
        id = order.id
        review = ReviewRating.objects.all()
        labour = Labours.objects.filter(id=myid)
        return render(request, 'handyman.html', {'lab': labour[0],'thank':thank,'id':id,'review':review})
       
    review = ReviewRating.objects.all()
    labour = Labours.objects.filter(id=myid)
    return render(request, 'handyman.html', {'lab': labour[0],'review':review})


@csrf_exempt
def handlerequest(request):
    #paytm send request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        print("sdsd" ,response_dict[i])
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order Successfull')
        else:
            print('order was not success full' + response_dict['RESPMSG'])
    return render(request,'paymentstatus.html',{'response': response_dict})






def AboutUs(request):
    return render(request, 'AboutUs.html')


def services(request):
    return render(request, 'services.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def test(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get("message", '')


        order = Orders(name=name, email=email, subject=subject, message=message)
        order.save()
    return render(request, 'test.html')



def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
