import pandas as pd
import matplotlib.pyplot as plt

def showMeanPlot(df):
    df = df.groupby("Year").head(8).groupby("Year")["Results"].mean().reset_index()
    plot(df)
    
def showFurthestPlot(df):
    df = df.groupby("Year")["Results"].max().reset_index()
    plot(df)

def plot(df):
    plt.plot(df["Year"], df["Results"], marker = "o")
    plt.xlabel("Year")
    plt.ylabel("Distance (meters)")
    plt.grid(True)
    plt.show()


def main():
    df = pd.read_csv("longjumpData.csv")
    showFurthestPlot(df)
    #showMeanPlot(df)
    
    
    

if __name__ == "__main__":
    main()
