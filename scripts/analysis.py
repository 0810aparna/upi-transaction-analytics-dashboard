def perform_analysis(df):

    print("\n===== UPI ANALYSIS =====")

    total_transactions = len(df)

    total_amount = df['amount'].sum()

    print(f"\nTotal Transactions: {total_transactions}")

    print(f"Total Amount: ₹{total_amount:,.2f}")

    print("\nTop States by Transaction Amount:")

    top_states = (
        df.groupby('state')['amount']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_states)

    print("\nTransaction Status:")

    print(df['status'].value_counts())

    print("\nTop Merchant Categories:")

    print(df['merchant_category'].value_counts().head(10))