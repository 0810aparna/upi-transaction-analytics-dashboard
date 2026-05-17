def perform_analysis(df):

    print("\\n===== ANALYSIS =====")

    total_transactions = len(df)

    total_amount = df['Amount'].sum()

    print(f"Total Transactions: {total_transactions}")

    print(f"Total Amount: {total_amount}")

    print("\\nTop States:")

    top_states = (
        df.groupby('State')['Amount']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_states)

    print("\\nTop Merchant Categories:")

    categories = (
        df['Merchant Category']
        .value_counts()
        .head(10)
    )

    print(categories)