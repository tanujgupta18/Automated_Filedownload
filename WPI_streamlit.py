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

        st.success(f"File downloaded successfully as {filename}")
        return True

    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error ({e.response.status_code}): {e.response.reason}")
        return False

    except requests.exceptions.RequestException as e:
        st.error(f"Error downloading file: {e}")
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

    try:
        if st.button("Download and Process File"):
            if download_file(download_url, file_name):
                st.write("File processing started.")
                if process_file(file_name):
                    st.success("File processing completed.")
                    
                    # Display a download button
                    with open(file_name, 'rb') as file:
                        file_content = file.read()
                    st.download_button(
                        label=f'Download File - {file_name}', 
                        key='download_button',
                        data=file_content,
                        file_name=file_name
                    )
                else:
                    st.error("Failed to process the file.")
            else:
                st.error("Failed to download the file. The file may not be available on the site.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
