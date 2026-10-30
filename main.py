import data_helper
import ml_helper

def main():
    print("=== STUDENT PROGRESS APP ===\n")
    
   
    dataframe = data_helper.analyze_and_plot()
    my_model = ml_helper.train_student_model(dataframe)
    
    print("\n--- Predict Student Status ---")
    
    student_name = input("Enter Student Name: ")
    hours = float(input("Enter Daily Study Hours (1-10): "))
    attendance = float(input("Enter Attendance % (0-100): "))
    
    
    prediction = my_model.predict([[hours, attendance]])
    
    
    if prediction == 1:
        result_status = "PASSED"
    else:
        result_status = "FAILED"
        
    print(f"\nPrediction for {student_name}: Will likely be {result_status}")
    
    
    with open("results_log.txt", "a") as file:
        file.write(f"Name: {student_name} | Hours: {hours} | Attendance: {attendance}% | Result: {result_status}\n")
    print("Result saved to 'results_log.txt'!")

if __name__ == "__main__":
    main()
