import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class Grapher:
    @staticmethod
    def showMeanPlot(df):
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        df = df.groupby("Year").head(8).groupby("Year")["Results"].mean().reset_index()
        Grapher.plot(df, ax)
        return fig

    @staticmethod    
    def showFurthestPlot(df):
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        df = df.groupby("Year")["Results"].max().reset_index()
        Grapher.plot(df, ax)
        return fig

    @staticmethod
    def plot(df, ax):
        ax.plot(df["Year"], df["Results"], marker = "o")
        ax.set_xlabel("Year")
        ax.set_ylabel("Distance (meters)")
        ax.grid(True)

"""
def main():
    df = pd.read_csv("longjumpData.csv")
    showFurthestPlot(df)
    #showMeanPlot(df)
    
    
    

if __name__ == "__main__":
    main()
"""