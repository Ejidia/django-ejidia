from django.shortcuts import render
from  home.models import TodoList

# Create your views here.

class Learner:
    def __init__(self,first_name, id_num, last_name,email,course, gender):
        self.first_name = first_name
        self.id_num = id_num
        self.last_name = last_name
        self.email = email
        self.course = course
        self.gender = gender
    #def homepage(request):
          #return render(request,"index.html")
ejidia = Learner(
            first_name ="Ejidia", 
            last_name="Uwabeza",
            id_num="1", 
            email="uwabeza@gmail.com",
            course="CSE",
            gender="F")
esther = Learner(
            first_name="Tumukunde",
            last_name="Esther",
            id_num="2",
            email="estt@gmail.com",
            course="Javascript",
            gender="F")

elaguha = Learner(
            first_name="Tumukunde",
            last_name="Elaguha",
            id_num="3",
            email="este@gmail.com",
            course="C++",
            gender="M")

elijah = Learner(
            first_name="Okok",
            last_name="Elijah",
            id_num="4",
            email="esta@gmail.com",
            course="Java",
            gender="M")
            
def homepage(request):
          allstudents=[ejidia,esther,elijah, elaguha]
          for each in allstudents:
                  print(each.last_name)    
          context ={"mylearners":allstudents}
          

          return render(request,"index.html",context)        
    

def viewlearnerpage(request): 
          return render(request, "viewlearner.html", )
          

"""

"""
def aboutpage(request):
        return render(request,"about.html")

def contactpage(request):
        return render(request,"contact.html")
def inventorypage(request):
        return render(request,"inventory.html")

def loginpage(request):
        return render(request,"login.html")

def todoPage (request):
        if request.method == "POST":
                data = request.POST
                task_name = data.get('task_name')
                description = data.get('description')
                due_date = data.get('due_date')
                priority = data.get('priority')
                is_complete =data.get('is_complete')

                new_task = TodoList()
                new_task.task_name = task_name
                new_task.description = description
                new_task.due_date = due_date
                new_task.priority = priority
                new_task.is_complete = is_complete 
                new_task.save()
                
        task_name = TodoList.objects.all()
        context = { 
                "tasks": task_name
                }

        return render(request, "todo.html", context)


