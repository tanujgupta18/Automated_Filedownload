import requests
import pandas as pd
import streamlit as st

def download_file(url, filename):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)

        st.success(f"File processed successfully as {filename}")
        return True

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return False

def process_file(filename):
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(filename)

        # Display the first few rows of the DataFrame
        st.write("First few rows of the DataFrame:")
        st.write(df.head())

        # Perform additional data processing or analysis as needed

        return True

    except Exception as e:
        st.error(f"Error processing file: {e}")
        return False

def main():
    st.title("WPI File Downloader App")

    # Hardcoded download URL and file name
    download_url = 'https://eaindustry.nic.in/indx_download_1112/monthly_index_202311.xls'
    file_name = 'monthly_index_file.xls'

    # Download button
    if st.button("Process File"):
        if download_file(download_url, file_name):
            st.write("File processing started.")
            if process_file(file_name):
                st.success("File processing completed.")
            else:
                st.error("Failed to process the file.")
        else:
            st.error("Failed to download the file.")

if __name__ == "__main__":
    main()
