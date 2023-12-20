import os
import requests
import streamlit as st

def download_file(url, filename):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)

        st.success(f"File Fetched successfully as {filename}")
        return True

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return False

def create_download_link(filename, label='Download File'):
    """Create a download link to the file."""
    download_link = f'<a href="/downloads/{filename}" download="{filename}" target="_blank">{label}</a>'
    return download_link

def main():
    st.title("WPI File Downloader App")

    download_url = 'https://eaindustry.nic.in/indx_download_1112/monthly_index_202311.xls'
    file_name = 'monthly_index_file.xls'

    if st.button("Fetch File"):
        if download_file(download_url, file_name):
            st.write("File processing completed.")
            
            app_path = os.path.dirname(os.path.abspath(__file__))

            file_path = os.path.join(app_path, file_name)

            st.markdown(create_download_link(file_name), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
