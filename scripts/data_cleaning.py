import pandas as pd


def clean_data():

    file_path = 'data/raw/upi_transactions_2024.csv'

    df = pd.read_csv(file_path)

    print("\nDATASET COLUMNS:")
    print(df.columns)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove null values
    df.dropna(inplace=True)

    # Convert timestamp column
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Create new columns
    df['month'] = df['timestamp'].dt.month

    df['hour'] = df['timestamp'].dt.hour

    # Rename important columns for easier analysis
    df.rename(columns={
        'amount (inr)': 'amount',
        'sender_state': 'state',
        'transaction_status': 'status'
    }, inplace=True)

    # Save cleaned data
    output_path = 'data/processed/cleaned_upi_data.csv'

    df.to_csv(output_path, index=False)

    print("\nData cleaned successfully.")

    return df