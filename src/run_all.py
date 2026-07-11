from generators import (
    generate_hdfc_transactions,
    generate_icici_transactions,
    generate_zerodha_transactions,
)

def main():

    print("=" * 50)
    print("Trade Data Generator")
    print("=" * 50)

    print("\nGenerating HDFC...")
    generate_hdfc_transactions()

    print("\nGenerating ICICI...")
    generate_icici_transactions()

    print("\nGenerating Zerodha...")
    generate_zerodha_transactions()

    print("\nAll files generated successfully!")


if __name__ == "__main__":
    main()