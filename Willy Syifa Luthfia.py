#Agriculture: Smart Farming System

#Nama: Willy Syifa Luthfia
#NIM : 123140071

from abc import ABC, abstractmethod

#Kelas abstrak untuk tanaman.
class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name
        self.water_needs = water_needs
        self.fertilizer_needs = fertilizer_needs
        self.adjusted_water = water_needs
        self.adjusted_fertilizer = fertilizer_needs

    #Metode abstrak untuk pertumbuhan tanaman
    @abstractmethod
    def grow(self):
        """Metode abstrak untuk pertumbuhan tanaman."""
        pass

    def calculate_needs(self, rainfall, soil_moisture):
        #Menyesuaikan kebutuhan air dan pupuk berdasarkan kondisi cuaca
        if rainfall > 5:  #Contoh logika: jika hujan lebih dari 5 mm, kurangi kebutuhan air
            self.adjusted_water = max(0, self.water_needs - rainfall)
        else:
            self.adjusted_water = self.water_needs

        #logika penyesuaian pupuk.
        if soil_moisture < 50:
            self.adjusted_fertilizer = self.fertilizer_needs
        else:
            self.adjusted_fertilizer = self.fertilizer_needs

    def show_needs(self, rainfall, soil_moisture):
        #Menampilkan kebutuhan tanaman yang disesuaikan
        print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
        if rainfall > 5:
            print(f"Adjusted Water Needs: {self.adjusted_water} liters (reduced due to rain)")
        else:
            print(f"Adjusted Water Needs: {self.adjusted_water} liters")
        print(f"Adjusted Fertilizer Needs: {round(self.adjusted_fertilizer)} kg")

#Kelas untuk tanaman padi.
class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 25, 4)  #Kebutuhan air dan pupuk standar untuk padi

    def grow(self):
        print("Rice is growing in the paddy field")

#kelas untuk tanaman jagung
class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 18, 7)  #Kebutuhan air dan pupuk standar untuk jagung

    def grow(self):
        print("Corn is growing in the farm")

# Simulasi kondisi cuaca dan pertumbuhan tanaman
rice = RicePlant()
rice.grow()
rice.calculate_needs(10, 75)
rice.show_needs(10, 75)

print()
corn = CornPlant()
corn.grow()
corn.calculate_needs(2, 40)
corn.show_needs(2, 40)
