import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def PlotPopulations():
    data = pd.read_csv("./Data/data.csv")
    data = data.values
    plt.style.use("Solarize_Light2")
    prey, = plt.plot(data[:,0],data[:,1], c="blue", label="Prey")
    pred, = plt.plot(data[:,0],data[:,2], c="red", label="Predators")
    food, = plt.plot(data[:,0],data[:,3], c="green", label="Food")
    plt.xlabel("Iterations")
    plt.ylabel("Populations")
    plt.legend(handles = [prey,pred,food])
    # plt.show()
    plt.savefig("./Data/Population.png")

def PlotRelativeRatio():
    data = pd.read_csv("./Data/data.csv")
    data = data.values
    plt.style.use("Solarize_Light2")
    ratio, = plt.plot(data[:,0],data[:,4], c="orange", label="Ratio")
    plt.xlabel("Iterations")
    plt.ylabel("Ratio")
    plt.legend(handles = [ratio])
    # plt.show()
    plt.savefig("./Data/Ratio.png")

PlotPopulations()
# PlotRelativeRatio()