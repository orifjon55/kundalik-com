from django.db import models

class School(models.Model): #maktab
    fullname = models.CharField(max_length=30)
    about = models.TextField()

    def __str__(self):
        return self.fullname
    
class Rating(models.Model):  #baho
    price = models.CharField(max_length=30)

    def __str__(self):
        return self.price

class Grade(models.Model): #sinf
    grade = models.CharField(max_length=10)
    
    def __str__(self):
        return self.grade

class Diary(models.Model): #kundalik
    rating = models.ForeignKey(Rating,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str (self.rating)

class Task_table(models.Model): #dars jadvali
    table = models.TextField()

    def __str__(self):
        return self.table

class Principal(models.Model): #zamdiriktor
    fullname = models.CharField(max_length=100)
    create_data = models.DateField(auto_now_add=True)
    table = models.ForeignKey(Task_table,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.fullname
    
class Student(models.Model): #o'quvchi
    fullname = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    interest = models.TextField()
    grade = models.ForeignKey(Grade,on_delete=models.SET_NULL,null=True)
    school = models.ForeignKey(School,on_delete=models.SET_NULL,null=True)
    diary = models.ForeignKey(Diary,on_delete=models.CASCADE,null=True)
    task_table = models.ForeignKey(Task_table,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
     return f"Grade: {self.grade}, Fullname: {self.fullname}"

class Teacher(models.Model): #oqituvchi
    fullname = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE,null=True)
    lesson_table = models.TextField()
    lesson = models.TextField()
    task_table = models.ForeignKey(Task_table,on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

class Assignment(models.Model): #vazifa
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title

class AssignmentStatus(models.Model): #vazifa satusi
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assignments_status')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='statuses')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.fullname} - {self.assignment.title} - {'Bajarildi' if self.completed else 'Bajarilmagan'}"
    
class Family(models.Model): #ota ona
    fullname = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School,on_delete=models.CASCADE, null=True)
    asgiment = models.ForeignKey(AssignmentStatus, on_delete=models.CASCADE, null=True)
    teacher = models.ManyToManyField(Teacher, name='teacher_family')
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE, null=True)
    tastable = models.ManyToManyField(Task_table, name='table_family')
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null = True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fullname