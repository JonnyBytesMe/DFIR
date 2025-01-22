import pandas as pd
import matplotlib.pyplot as plt

def analyze_csv(file_path):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
        
        # Display general information about the dataset
        print("Dataset Information:")
        print(data.info())

        # Display statistical summary
        print("\nStatistical Summary:")
        print(data.describe())

        # Check for missing values
        print("\nMissing Values:")
        print(data.isnull().sum())

        # Visualize the data
        for column in data.select_dtypes(include=['number']).columns:
            plt.figure(figsize=(8, 4))
            data[column].hist(bins=20, color='skyblue', edgecolor='black')
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.grid(axis='y')
            plt.savefig(f'{column}_distribution.png')  # Save the plot as an image
            plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the CSV Data Analyzer!")
    csv_file = input("Enter the path to your CSV file: ")
    analyze_csv(csv_file)
