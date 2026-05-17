import pandas as pd


def clean_data():
    file_path = 'data/raw/upi_transactions_2024.csv'

    df = pd.read_csv(file_path)

    print(df.head())

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove null values
    df.dropna(inplace=True)

    # Convert timestamp column
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Create extra columns
    df['Month'] = df['Timestamp'].dt.month
    df['Hour'] = df['Timestamp'].dt.hour

    # Save cleaned data
    output_path = 'data/processed/cleaned_upi_data.csv'
    df.to_csv(output_path, index=False)

    print("Data cleaned successfully.")

    return df