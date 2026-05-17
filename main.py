from scripts.data_cleaning import clean_data
from scripts.analysis import perform_analysis
from scripts.visualization import create_visualizations


def main():
    print("Starting UPI Analytics Project...")

    df = clean_data()

    perform_analysis(df)

    create_visualizations(df)

    print("Project completed successfully.")


if __name__ == "__main__":
    main()