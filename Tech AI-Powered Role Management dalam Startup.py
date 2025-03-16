#Tech: AI-Powered Role Management dalam Startup

#Nama: Willy Syifa Luthfia
#NIM : 123140071

class Employee:
    # Kelas induk Employee dengan atribut dasar
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.task_completed = task_completed
    
    def work(self):
        # Metode kerja (akan dioverride oleh subclass)
        pass
    
    def evaluate_performance(self):
        # Mengukur produktivitas berdasarkan rasio tugas selesai dan jam kerja
        efficiency = self.task_completed / (self.hours_worked + 1)  # Hindari pembagian dengan nol
        if efficiency > 1.5:
            return "High Performance"
        elif efficiency > 0.75:
            return "Medium Performance"
        else:
            return "Low Performance"

# Kelas turunan dengan metode kerja spesifik
class SoftwareEngineer(Employee):
    def work(self):
        return f"{self.name} (Software Engineer) is coding."

class DataScientist(Employee):
    def work(self):
        return f"{self.name} (Data Scientist) is analyzing data."

class ProductManager(Employee):
    def work(self):
        return f"{self.name} (Product Manager) is managing the product roadmap."

# Contoh penggunaan dengan beberapa karyawan
employees = [
    SoftwareEngineer("Alice", "Software Engineer", 40, 70),
    DataScientist("Bob", "Data Scientist", 50, 60),
    ProductManager("Charlie", "Product Manager", 45, 50),
    SoftwareEngineer("David", "Software Engineer", 50, 30)
]

# Loop untuk menampilkan pekerjaan dan evaluasi performa masing-masing karyawan
for emp in employees:
    print(emp.work())
    print(f"Performance Rating: {emp.evaluate_performance()}\n")
