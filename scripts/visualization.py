import matplotlib.pyplot as plt


def create_visualizations(df):

    # State-wise transaction chart
    top_states = (
        df.groupby('State')['Amount']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    top_states.plot(kind='bar')

    plt.title('Top States by UPI Transaction Amount')

    plt.xlabel('State')

    plt.ylabel('Amount')

    plt.tight_layout()

    plt.savefig('screenshots/top_states.png')

    print("Visualization saved.")