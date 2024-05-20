import pandas as pd

def load(path):
    try:
        # Read the dataset
        df = pd.read_csv(path)
        
        # Get dimensions of the dataset
        dimensions = df.shape
        print(f"Loading dataset of dimensions {dimensions}")
        return df
        
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except pd.errors.EmptyDataError:
        print("Empty file. Please provide a non-empty dataset.")
    except pd.errors.ParserError:
        print("Error parsing the file. Please check the file format.")
    except Exception as e:
        print("An error occurred:", e)
    
    return None
