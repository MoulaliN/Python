import pandas as pd 

def convert_excel_to_csv(input_excel_path, output_csv_path):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(input_excel_path)

        # Write the DataFrame to a CSV file
        df.to_csv(output_csv_path, index= True)

        print(f"Conversion successful. CSV file saved at {output_csv_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_excel_path = 'C:/Users/0025T7744/Downloads/convert_test.xls'
output_csv_path = 'C:/Users/0025T7744/Downloads/convert_test.csv'

convert_excel_to_csv(input_excel_path, output_csv_path)