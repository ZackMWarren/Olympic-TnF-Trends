import tkinter as tk
from tkinter import ttk
import os
from ScrapeOly import Scrape_Event
import grapher
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Track Trends")
        self.geometry("400x300")
        self.choice = None
        self.event = None
        
        # Create a container frame to hold all pages
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Dictionary to hold all pages
        self.frames = {}
        
        # Create all pages and add to container
        for PageClass in (StartPage, EventPage, GraphPage):
            frame = PageClass(parent=container, controller=self)
            self.frames[PageClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show the start page initially
        self.show_page("StartPage")
    
    def show_page(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = ttk.Label(self, text="Start Page", font=('Arial', 18))
        label.pack(pady=10)
        
        button1 = ttk.Button(self, text="Mean Finalist Scores Trends",
                            command=lambda: self.data_choice("mean"))
        button1.pack(pady=10)
        
        button1 = ttk.Button(self, text="Top Scorers Trends",
                            command=lambda: self.data_choice("top"))
        button1.pack(pady=10)
        
    def data_choice(self, choice):
        self.controller.choice = choice
        self.controller.show_page("EventPage")

class EventPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        track_events = [
        # Sprints & Hurdles
        "100m", "200m", "400m",
        "110m hurdles", "400m hurdles",
        
        # Middle/Long Distance
        "800m", "1500m", "5000m",
        "10,000m", "3000m steeplechase",
        "marathon",
        
        # Relays
        "4x100m relay", "4x400m relay",
        "4x400m relay mixed",
        
        # Jumps
        "high jump", "pole vault", "long jump", "triple jump",
        
        # Throws
        "shot put", "discus throw", "hammer throw", "javelin throw",
        
        # Multisport
        "decathlon"
        ]
        
        label = ttk.Label(self, text="Select Event", font=('Arial', 18))
        label.pack(pady=20)
        
        self.event_box = ttk.Combobox(self, values=track_events)
        self.event_box.set("100m")
        self.event_box.pack(pady=10)
        
        button_frame = ttk.Frame(self)
        button_frame.pack(side = "bottom", pady = 10, fill = "x")
        
        button1 = ttk.Button(button_frame, text="Graph",
                            command=lambda: self.graph())
        button1.pack(pady=10)
        
        go_to_start = ttk.Button(button_frame, text="Back to Start", command=lambda: controller.show_page("StartPage"))
        go_to_start.pack(pady=10)
        
    def graph(self):
        self.controller.event = self.event_box.get()
        self.getData()
        self.controller.show_page("GraphPage")
        self.controller.frames["GraphPage"].ShowPlot()
    
    def getData(self):
        if not os.path.isfile(f"{self.controller.event}{self.controller.choice}Data.csv"):
            data = Scrape_Event(self.controller.event)
            df = pd.DataFrame(data)
            df.to_csv(f"{self.controller.event}{self.controller.choice}Data.csv", index=False)
            

class GraphPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="pg3", font=('Arial', 18))
        label.pack(pady=10)
        
        self.graph_container = ttk.Frame(self)
        self.graph_container.pack(fill="both", expand=True)

        button1 = ttk.Button(self, text="Start Page", command = lambda: self.controller.show_page("StartPage"))
        button1.pack(pady=10)
    

    def ShowPlot(self):
        for widget in self.graph_container.winfo_children():
            widget.destroy()
        
        df = pd.read_csv(f"{self.controller.event}{self.controller.choice}Data.csv")
        
        if self.controller.choice == "mean":
            fig = grapher.Grapher.showMeanPlot(df)
        else:
            fig = grapher.Grapher.showFurthestPlot(df)
            
        canvas = FigureCanvasTkAgg(fig, master=self.graph_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
        
        
    
            
        
        
        
        
   
if __name__ == "__main__":
    app = App()
    app.mainloop()

''''''
