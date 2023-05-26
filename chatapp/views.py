from django.shortcuts import render,HttpResponse,redirect                
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from langchain.document_loaders import TextLoader
from chatapp.models import Admin,AppUser
from langchain.indexes import VectorstoreIndexCreator
from dotenv import load_dotenv
import os
import openai

load_dotenv()
api_key=os.environ["OPENAI_API_KEY"] = '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'
def index(request):
    return render(request,"base.html")

# def signup(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         pass1=request.POST['pass1']
        
#         user=User.objects.create_user(name, email, pass1)
#         user.save()
#         messages.success(request,"signup succesfully!!!")
#         return redirect('login')
#     return render(request,"adminSide/signup.html")

        
        
def admin_login(request):
 if request.method == 'POST':
    lname=request.POST['lname']
    lpass=request.POST['lpass']
    
    user=User.objects.get(username=lname)
    if user is not None:
        login(request, user)
        messages.success(request, "login succesfully!!!")
        return render(request,"adminSide/index.html")
    else:
        messages.error(request, "invalid user....")
        return redirect('login')
 return render(request,"adminSide/login.html")
            
def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')   

def upload(request):
    if request.method == 'POST':
        name = request.POST['name']
        file = request.POST['file'] 
         
        detail = Admin(name=name,file=file)
        detail.save()
        messages.success(request,"file uploaded")
        return render(request,"adminSide/index.html")
    messages.error(request,"file uploading failed")
    return render(request,"adminSide/index.html")

def view_history(request):
    chatbot_response = None
    if api_key is not  None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('ans')
        prompt = user_input
        
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = prompt,
            max_tokens = 256,
            temperature = 0.5
        )
        print(response)
        chatbot_response = response["choices"][0]["text"]
    return render(request,"adminSide/chatbox.html",{"response":chatbot_response})

def read_file(req):
    file2 = open('formData.txt','r')
    file3 = file2.read()
    return HttpResponse(file3)
    
def user_signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        
        user=AppUser(name, email, pass1)
        user.save()
        messages.success(request,"signup succesfully!!!")
        return redirect('login')
    return render(request,"adminSide/signup.html")

def user_login(request):
 if request.method == 'POST':
    lname=request.POST['lname']
    lpass=request.POST['lpass']
    
    user=AppUser.objects.get(username=lname)
    if user is not None:
        login(request, user)
        messages.success(request, "login succesfully!!!")
        return render(request,"adminSide/index.html")
    else:
        messages.error(request, "invalid user....")
        return redirect('login')
 return render(request,"adminSide/login.html")   