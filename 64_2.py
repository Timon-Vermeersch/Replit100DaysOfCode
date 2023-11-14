class Job:
    jobTitle :str
    salary: float
    hoursWorked: int

    def __init__(self,jobTitle,salary,hoursWorked):
        self.jobTitle = jobTitle
        self.salary = salary
        self.hoursWorked = hoursWorked
    def jobPrint(self):

        print(f"{self.jobTitle} makes {self.salary} with {self.hoursWorked} hours workedd\n")

class Doctor(Job):
    experience : str
    speciality : str

    def __init__(self,jobTitle,salary,hoursWorked,experience,speciality):
        self.jobTitle = jobTitle
        self.salary = salary
        self.hoursWorked = hoursWorked
        self.experience = experience
        self.speciality = speciality


    def dokterPrint(self):
        print(f"{self.jobTitle} makes {self.salary} with {self.hoursWorked} hours worked, has {self.experience} years experience and is specialised in {self.speciality}.\n")

class Teacher(Job):
    subject : str
    position : str

    def __init__(self,jobTitle,salary,hoursWorked,subject,position):
        self.jobTitle = jobTitle
        self.salary = salary
        self.hoursWorked = hoursWorked
        self.subject = subject
        self.position = position
    
    def teacherPrint(self):
        print(f"{self.jobTitle} makes {self.salary} with {self.hoursWorked} hours worked, as a {self.position} in subject {self.subject}.\n")



while __name__ == "__main__":
    geerje = Doctor("Dokter",10000,48,10,"cardio")
    sara = Teacher("Leerkracht",500,56,"Planner/Teacher","economie")
    sybe = Job("Advocaat", 2000,20,)

    geerje.dokterPrint()
    sara.teacherPrint()
    sybe.jobPrint()


