from src import Extract, Load

def main():
    """Main function to run the ETL pipeline."""
    try:
        extractor = Extract()
        loader = Load()

        countries = ["Brazil", "Portugal"]
        
        for country in countries:
            print(f"Extracting data for {country}...")
            data = extractor.extract_country(country)
            
            loader.create_sqlite_table(
                data, 
                "universities_db", 
                f"universities_{country.lower()}"
            )
            print(f"Success: {country} data loaded.")

    except Exception as e:
        print(f"An error occurred during the process: {e}")

if __name__ == "__main__":
    main()