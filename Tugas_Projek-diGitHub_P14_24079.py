import tkinter as tk
from tkinter import messagebox

class Vehicle:
    def __init__(self, brand, model, color, engine_type, cost):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.cost = cost
        self.status = "Belum selesai"

    def assemble(self):
        self.status = "Sedang dirakit"

    def finish(self):
        self.status = "Selesai"

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Warna: {self.color}, Mesin: {self.engine_type}, Biaya: Rp{self.cost}, Status: {self.status}"

class Factory:
    def __init__(self):
        self.vehicles = []
        self.total_cost = 0

    def produce_vehicle(self, brand, model, color, engine_type, cost):
        vehicle = Vehicle(brand, model, color, engine_type, cost)
        self.vehicles.append(vehicle)
        vehicle.assemble()
        vehicle.finish()
        self.total_cost += cost
        return vehicle

    def list_vehicles(self):
        if not self.vehicles:
            return "Belum ada kendaraan diproduksi."
        return "\n".join([v.display_info() for v in self.vehicles]) + f"\n\nTotal Biaya Produksi: Rp{self.total_cost}"

# GUI dengan Tkinter
class VehicleFactoryApp:
    def __init__(self, root):
        self.factory = Factory()
        self.root = root
        self.root.title("Simulasi Pabrik Kendaraan")
        
        # Input fields
        tk.Label(root, text="Brand:").grid(row=0, column=0)
        self.brand_entry = tk.Entry(root)
        self.brand_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Model:").grid(row=1, column=0)
        self.model_entry = tk.Entry(root)
        self.model_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Warna:").grid(row=2, column=0)
        self.color_entry = tk.Entry(root)
        self.color_entry.grid(row=2, column=1)
        
        tk.Label(root, text="Mesin:").grid(row=3, column=0)
        self.engine_entry = tk.Entry(root)
        self.engine_entry.grid(row=3, column=1)
        
        tk.Label(root, text="Biaya (Rp):").grid(row=4, column=0)
        self.cost_entry = tk.Entry(root)
        self.cost_entry.grid(row=4, column=1)
        
        # Buttons
        tk.Button(root, text="Produksi Kendaraan", command=self.produce).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Lihat Daftar Kendaraan", command=self.show_list).grid(row=6, column=0, columnspan=2)
        
        # Output
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=7, column=0, columnspan=2)

    def produce(self):
        try:
            brand = self.brand_entry.get()
            model = self.model_entry.get()
            color = self.color_entry.get()
            engine = self.engine_entry.get()
            cost = int(self.cost_entry.get())
            
            if not all([brand, model, color, engine]):
                messagebox.showerror("Error", "Semua field harus diisi!")
                return
            
            vehicle = self.factory.produce_vehicle(brand, model, color, engine, cost)
            self.output_text.insert(tk.END, f"Kendaraan {brand} {model} berhasil diproduksi!\n")
            # Clear inputs
            self.brand_entry.delete(0, tk.END)
            self.model_entry.delete(0, tk.END)
            self.color_entry.delete(0, tk.END)
            self.engine_entry.delete(0, tk.END)
            self.cost_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Biaya harus angka!")

    def show_list(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, self.factory.list_vehicles())

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleFactoryApp(root)
    root.mainloop()