import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    st.title('Data Visualization Dashboard')

    # Menampilkan pilihan menu
    menu = ["Top 10 Products", "Top 10 Cities by Number of Customers", "Number of Customers by State", "Top 10 Sellers"]
    choice = st.sidebar.selectbox("Select Visualization", menu)

    # Memanggil fungsi berdasarkan pilihan pengguna
    if choice == "Top 10 Products":
        plot_top_10_products()
    elif choice == "Top 10 Cities by Number of Customers":
        plot_top_10_cities()
    elif choice == "Number of Customers by State":
        plot_customers_by_state()
    elif choice == "Top 10 Sellers":
        plot_top_10_sellers()

def plot_top_10_products():
    # Data 1
    product_orders = pd.DataFrame({
        'product_id_shorten': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'count': [100, 80, 70, 60, 50, 40, 30, 20, 10, 5]
    })

    plt.figure(figsize=(10, 6))
    sns.barplot(x='product_id_shorten',
                y='count',
                data=product_orders,
                palette='autumn',
                order=product_orders['product_id_shorten'].head(10))
    plt.xlabel('Product')
    plt.ylabel('Count')
    plt.title('Top 10 Products')
    st.pyplot()

def plot_top_10_cities():
    # Data 2
    customers_df = pd.DataFrame({
        'customer_city': ['City1', 'City2', 'City3', 'City4', 'City5'],
        'count': [100, 80, 70, 60, 50]
    })

    plt.figure(figsize=(8, 6))
    sns.barplot(x='count',
                y='customer_city',
                data=customers_df.nlargest(10, 'count'),
                palette='viridis')
    plt.xlabel('Number of Customers')
    plt.ylabel('City')
    plt.title('Top 10 Cities by Number of Customers')
    st.pyplot()

def plot_customers_by_state():
    # Data 3
    bystate_df = pd.DataFrame({
        'customer_state': ['CA', 'NY', 'TX', 'FL', 'IL'],
        'customer_count': [100, 80, 70, 60, 50]
    })

    plt.figure(figsize=(10, 6))
    sns.barplot(x='customer_state',
                y='customer_count',
                data=bystate_df,
                palette='Set2',
                edgecolor='black',
                linewidth=1.5,
                alpha=0.8)
    plt.xlabel('State')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.title('Number of Customers by State')
    st.pyplot()

def plot_top_10_sellers():
    # Data 4
    seller_products = pd.DataFrame({
        'seller_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'count': [20, 15, 10, 8, 5]
    })

    plt.figure(figsize=(5, 10))
    seller_products['seller_id'].value_counts()[:10].plot.pie(autopct='%1.1f%%',
                                                             shadow=True, startangle=90, cmap='coolwarm')
    plt.title("Top 10 Sellers", size=17, weight='bold')
    st.pyplot()

if __name__ == '__main__':
    main()
