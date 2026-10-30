import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_and_plot():
    
    df = pd.read_csv('student_data.csv')
    
    
    avg_hours = np.mean(df['Study_Hours'])
    print(f"--- Data Analysis ---")
    print(f"Average Study Hours: {avg_hours:.2f} hours\n")
    
    
    plt.figure(figsize=(5, 4))
    plt.scatter(df['Study_Hours'], df['Attendance'], c=df['Passed'], cmap='bwr')
    plt.xlabel('Study Hours')
    plt.ylabel('Attendance %')
    plt.title('Study vs Attendance (Red=Fail, Blue=Pass)')
    plt.savefig('student_plot.png')
    plt.close()
    
    return df
