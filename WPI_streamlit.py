import os
import requests
import streamlit as st
import pandas as pd

def download_file(url, filename):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)

        st.success(f"File Processed successfully as {filename}")
        return True

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return False

def process_file(filename):
    try:
        df = pd.read_excel(filename)

        st.write("First 10 entries of the DataFrame:")
        st.write(df.head(10))
        return True

    except Exception as e:
        st.error(f"Error processing file: {e}")
        return False

def main():
    st.title("WPI File Downloader App")

    download_url = 'https://eaindustry.nic.in/indx_download_1112/monthly_index_202311.xls'
    file_name = 'monthly-index-file.xls'

    if st.button("Process File"):
        if download_file(download_url, file_name):
            st.write("File processing started.")
            if process_file(file_name):
                st.success("File processing completed.")
                
                file_path = os.path.relpath(file_name)
                
                st.markdown(f'<a href="{file_path}" download="{file_name}">Download File - {file_name}</a>', unsafe_allow_html=True)
            else:
                st.error("Failed to process the file.")
        else:
            st.error("Failed to download the file.")

if __name__ == "__main__":
    main()
