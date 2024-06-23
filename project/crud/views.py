from django.shortcuts import render, redirect
from django. contrib.auth.decorators import login_required
from .models import Todo
from django.contrib import messages

# Create your views here.
@login_required
def dashboard_view(request):
    try:
        id = request.user.id
        data = Todo.objects.filter(user=id).order_by('-id')
        return render(request, 'display_todo.html', {'data' : data}) 
    except:
        return render(request, 'display_todo.html', {'data' : data})

@login_required
def add_view(request):
    if request.method == 'POST':
        try:
            user = request.user
            task_name = request.POST.get('task_name')
            task_description = request.POST.get('task_description')
            file = request.FILES.get('file')
            image = request.FILES.get('image')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            status = request.POST.get('status')

            Todo.objects.create(user=user, task_name=task_name, task_description=task_description, file=file, 
                                image=image, start_date=start_date, end_date=end_date, status=status)
            
            messages.success(request, "record added sucessfully !")
            return redirect('/dashboard')
        except:
            messages.error(request, "all field are required !")
            return render(request, 'add_todo.html')
    else:
        return render(request, 'add_todo.html')
    


@login_required
def update_view(request, id):
    try:
        data = Todo.objects.get(id=id)
        return render(request, 'update_todo.html', {'data' : data})
    except:
        return render(request, 'update_todo.html', {'data' : data})
    

@login_required
def save_view(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('user')
            task_name = request.POST.get('task_name')
            task_description = request.POST.get('task_description')
            file = request.FILES.get('file')
            image = request.FILES.get('image')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            status = request.POST.get('status')

            todo = Todo.objects.get(id=id)
            todo.task_name = task_name
            todo.task_description = task_description
            todo.start_date = start_date
            todo.end_date = end_date
            todo.status = status
            if file:
                todo.file = file
            if image:
                todo.image = image
                 
            todo.save()


            messages.success(request, "record update sucessfully !")
            return redirect('/dashboard')
        except:
            messages.error(request, "all field are required !")
            return render(request, 'update_todo.html')
        

@login_required
def delete_view(request, id):
    try:
        Todo.objects.filter(id=id).delete()
        messages.success(request, "record delete sucessfully !")
        return redirect('/dashboard')
    except:
        return redirect('/dashboard')