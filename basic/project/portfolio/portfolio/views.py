from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import About 
from django.contrib import messages
import random
import re
from django.core.signing import Signer
#from django.core.mail import send_mail
from django.core.mail import send_mail
from datetime import datetime
from django.utils.html import format_html


# def demo(request):
#     title = "this is a demo html"
#     name = "Mamun"
#     product_name = ['p1','p2','p3']
#     data = {"t":title,"name":name,'prod':product_name}
    
#     #print("this is root url function")
#     return render(request,'portfolio.html',data)

def home(request):
    data = About.objects.first()
    context_data = {'d':data}

    #print("this is root url function")
    return render(request,'portfolio.html',context_data)


def demo1(request):
    a = 10 
    b = 12
    c = a + b
    #print("this is root url function")
    return HttpResponse(c)
def login_admin (request):
    email=request.POST.get("email")
    password= request.POST.get("pass")
    log_data = About.objects.get(Email=email)
    
    if(log_data.password==password and log_data.v_status=='1'):
        request.session['user_id']=log_data.id
        request.session['user_name']=log_data.Name
        return redirect('about')
    else:
        return redirect('login')
    return render(request,'admin/about.html')

def login (request):
    if 'user_id' in request.session:
        return redirect('about')
    else:
        return render(request,'login.html')

def logout (request):
    request.session.flush()
    return redirect('login')
    

def about_index(request):
    # if 'user_id' in request.session:
    all_data = About.objects.all()
    
    msg = messages.get_messages(request)
    print(msg)


    data = {'d':all_data,'msg':msg}

    return render(request,'admin/about.html',data)
    # else:
    #     return redirect('login')

def reg_confirm(request):
    return render(request,'reg_conf.html')

def email_verify(request,id):
    data = About.objects.get(v_c=id)
    #data = get_object_or_404(About, v_c=id)
    bool_ver = False
    if data.v_status=="0":
        bool_ver = False
        
        data.v_status = 1
        data.save()
        
        #return HttpResponse("This is zero")
    else:
        bool_ver = True

    bool_dic = {'d': bool_ver}
    return render(request,'success.html',bool_dic)

def about_insert(request):
    

    Name = request.POST.get('uname')
    Date_of_Birth = request.POST.get('dob')
    Phone = request.POST.get('phone')
    Email = request.POST.get('email')
    Years_of_Experiences = request.POST.get('exp')
    No_of_Happy_Customers = request.POST.get('no_cust')
    No_of_Projects_Finished = request.POST.get('no_project')
    No_of_Awards = request.POST.get('no_of_awards')
    Description = request.POST.get('desc')
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y-%I:%M %p")
    password= request.POST.get('password')
    pattern = r"^[a-zA-Z0-9_.]+gmail.com$"

    if not all([Name, Date_of_Birth, Phone, Email, Years_of_Experiences, No_of_Happy_Customers, 
                No_of_Projects_Finished, No_of_Awards, Description]):
        messages.success (request,"The field can not be empty")
        #return HttpResponse("Error: All fields must be filled.")

    # else:    
        # if not re.match(pattern,email):
        #     massages.succass(request,"You email is not gmail")
        # elif len(phone)!=11:
        #     massages.succass(request,"You Mobile numbar must have 11 digit")
        # else:
        #     data = About.objects.all()
        #     about_odj = About()
        #     len_data = len(data)
        #     if(len_data>=1):
        #         massages.succass(request,"You can not entry more then one data")
    current_time = datetime.now().strftime("%H:%M:%S")
    print (current_time.split(':'))
    h,m,s = map(int,current_time.split(':'))
    t_s = h*3600 + m*60 + s
    random_number = random.choices('1234567890',k=4)
    random_number = ''.join(random_number)
    t_s = str (t_s)
    v_c = t_s + random_number
    signer = Signer()
    encrypted_value = signer.sign(v_c).split(":")[1]

    link =f"<p>Congratulations Mr {Name} ! For registering as a user in our Portfolio System. To confirm the registration </p><a href= 'http://127.0.0.1:8000/admin/user/email_verification/"+encrypted_value+"' target='_blank'>please chick this activation link/a>"

    send_mail(f"Mr. {Name} please confirm your Registration - portfolio panel",encrypted_value,'mdmamunislam908571@gmail.com',[Email],html_message=link)
        # send_mail(f"Mr. {name} please confirm your Registration - portfolio panel",encrepted_value,'mdmamunislam908571@gmail.com',[email])
    print(encrypted_value)
    # else:
    about_odj = About()


            
    about_odj.Name = Name
    about_odj.Birthday = Date_of_Birth
    about_odj.Phone = Phone
    about_odj.Email = Email
    about_odj.No_Years_of_Experiences = Years_of_Experiences
    about_odj.No_Happy_Customers = No_of_Happy_Customers
    about_odj.No_Project_Finished = No_of_Projects_Finished
    about_odj.No_Digital_Awards = No_of_Awards
    about_odj.description = Description
    about_odj.date_time = formatted_datetime
    about_odj.v_c = encrypted_value
    about_odj.v_status = 0
    about_odj.password = password
    about_odj.save()


        
            


    return redirect('reg_conf')

def edit_index(request,id):
    data = About.objects.get(id=id)
    d = {'data':data}
    return render (request,'admin/edit.html',d)


def about_edit(request):
    
    id = request.POST.get("id")
    Name = request.POST.get('uname')
    Date_of_Birth = request.POST.get('dob')
    Phone = request.POST.get('phone')
    Email = request.POST.get('email')
    Years_of_Experiences = request.POST.get('exp')
    No_of_Happy_Customers = request.POST.get('no_cust')
    No_of_Projects_Finished = request.POST.get('no_project')
    No_of_Awards = request.POST.get('no_of_awards')
    Description = request.POST.get('desc')
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y-%I:%M %p")

    about_odj = About.objects.get(id=id)

    
    about_odj.Name = Name
    about_odj.Birthday = Date_of_Birth
    about_odj.Phone = Phone
    about_odj.Email = Email
    about_odj.No_Years_of_Experiences = Years_of_Experiences
    about_odj.No_Happy_Customers = No_of_Happy_Customers
    about_odj.No_Project_Finished = No_of_Projects_Finished
    about_odj.No_Digital_Awards = No_of_Awards
    about_odj.description = Description
    about_odj.date_time = formatted_datetime
    about_odj.save()

    return redirect('about')

def delete_index(request,id):
    data = About.objects.get(id=id)
    data.delete()
    return redirect("about")