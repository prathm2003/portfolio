from django.shortcuts import render, redirect
from .models import cont_collection

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Name: {name}, Email: {email}, Message: {message}")
    
        record = {
            "name": name,
            "email": email,
            "message": message,
        }

        try:
            cont_collection.insert_one(record)
            print("Data inserted successfully.")
            return render(request, 'index.html' ,{'success': True}) 
        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")
        
    return render(request, 'index.html' ,{'success': False})  # Adjust template if necessary
