from sklearn.linear_model import LogisticRegression

def train_student_model(df):
    
    X = df[['Study_Hours', 'Attendance']]
    y = df['Passed']
    
    
    model = LogisticRegression()
    model.fit(X, y)
    
    print("-> Supervised ML Model Trained successfully!")
    return model
