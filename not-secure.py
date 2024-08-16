import requests
import json

# Define the JWT token and other parameters
JWT = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1NTBlZjUxLTA5NGEtNGE0MS05Zjc0LTVmZWY1ZGUxZjE4MiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkX3YyIjoiMDFIRjU0VFE0NVdDUTMzUDJRS1JRMUVNQ1oiLCJhY2NvdW50X25hbWUiOiJDdXN0b21lciIsImFjY291bnRfc2x1ZyI6ImN1c3RvbWVyIiwiYWNjb3VudF90eXBlIjoiRU5URVJQUklTRSIsImF0dHJpYnV0ZXMiOnt9LCJhdWQiOlsiZGY4ZTk3YTItMzc1NS00MWYwLWE5YmUtMmZiYTMzZmQzZTYyIl0sImF6cCI6IjYyNDk1MDE0LTg3MzMtNDE4My1hZjlhLWI1OWY1ODBhYTY0OSIsImNsaWVudElkIjoiZGY4ZTk3YTItMzc1NS00MWYwLWE5YmUtMmZiYTMzZmQzZTYyIiwiY2xpZW50X2lkIjoiZGY4ZTk3YTItMzc1NS00MWYwLWE5YmUtMmZiYTMzZmQzZTYyIiwiZW1haWwiOiJsdWNhcy52aWNlbnpvdHRvQHNhbGVzLnVzLnN0YWNrc3BvdC5jb20iLCJleHAiOjE3MjI2MjI3NjksImZhbWlseV9uYW1lIjoiVmljZW56b3R0byIsImdpdmVuX25hbWUiOiJMdWNhcyIsImlhdCI6MTcyMjYyMTU2OSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnN0YWNrc3BvdC5jb20vY3VzdG9tZXIvb2lkYyIsImp0aSI6Inh2UFB3RTB3VzIxMHk3WWE4QUlwSFFmYnhKSmFBMjNsYm50Q2JlZDRjSmY5TGFGZ3g2aHVvYVdZWnlMMFR3Y2ciLCJtYXhfYWdlIjoxNzIyNjUwMzY5LCJuYW1lIjoiTHVjYXMgVmljZW56b3R0byIsIm5iZiI6MTcyMjYyMTU2OSwicHJlZmVycmVkX3VzZXJuYW1lIjoibHVjYXMudmljZW56b3R0b0BzYWxlcy51cy5zdGFja3Nwb3QuY29tIiwicmVhbG0iOiJjdXN0b21lciIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJjcmVhdG9yIiwiYWNjb3VudF9hZG1pbiIsImFpX2RldmVsb3BlciIsImRldmVsb3BlciIsImFpX2FkbWluIiwiYWNjb3VudF9ob2xkZXIiXX0sInJvbGVzIjpbImNyZWF0b3IiLCJhY2NvdW50X2FkbWluIiwiYWlfZGV2ZWxvcGVyIiwiZGV2ZWxvcGVyIiwiYWlfYWRtaW4iLCJhY2NvdW50X2hvbGRlciJdLCJzY29wZSI6InJvbGVzIGF0dHJpYnV0ZXMgcHJvZmlsZSBlbWFpbCIsInN1YiI6ImRmOGU5N2EyLTM3NTUtNDFmMC1hOWJlLTJmYmEzM2ZkM2U2MiIsInRlbmFudCI6ImN1c3RvbWVyIiwidG9rZW5UeXBlIjoiQ0xJRU5UX1NFUlZJQ0VfQUNDT1VOVCIsInRva2VuX3R5cGUiOiJDTElFTlRfUEVSU09OQUwiLCJ1c2VybmFtZSI6Imx1Y2FzLnZpY2Vuem90dG9Ac2FsZXMudXMuc3RhY2tzcG90LmNvbSJ9.JtCTjgQsIC76hrazYjc2ZQdzn5eoKL3TOXc6OzHy7IDLa_O8JfcDGU0u_dBRVomuSF9E6bQi5BmtJPbhrjS9Tk0qlb_ZWPcyAgk4Xf0GI9di_zkBdDtEQfXUaMD16V_T7bXCMs-AXR9nfYn2y7rq9Lw3UfBONE9EZDihwGWwXI1GA5myenJBqTzpbx4LP41PjmA4FIkpItHlfXQDP3aBMC3ym8_b6RG6xPZ88bPBvfXSB835wOmkqNlW8aGCee3dSh7rb_yUBO1hx3ZPbqU0GoSXeW_Z6k3IQ49uWd3z87-cJZug8v5fzoRjgOprq5kNRvqHU0MSk0DL8_wyIV05k7YW2wKV4miCZouwK94jgwM4dDXNSmFHvjPNLk8A7bckyP5gIshCOnsXavgI2-7cPgWRf3ZgW1xcodjb65QCVgB1IL9FlF3J-7MzJQKmO7EICla3ybYdEQBTYW563iWVkla9UhkotXCs02whUM1M4IBdIhAlKD1kwhTBrHxVLgUtE7u8l5E01rq8weZ3T_13srHeRXULbnUkyIzYlf2i9UcJWGemdcsCH-RZum1tUILwMFOyWkOAu5uax-fKUlrnUBBjcPFjItmGZtTBB9A9BgrBllWWe9kdaxtzXV8g8T9CRpurCWtnfhMe0wgz-BQFhIJdE2p9pcBtuMsNojZ8SQk"
file_name = "weather-api"
target_id = "weather-api"
target_type = "KNOWLEDGE_SOURCE"
expiration = 600
file_path = "/Users/lucas/Desktop/projects/demos/weather-dot-gov-api.json"

# Step 01: Get the upload data
url = 'https://genai-code-buddy-api.stackspot.com/v1/file-upload/form'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {JWT}'
}
data = {
    "file_name": file_name,
    "target_id": target_id,
    "target_type": target_type,
    "expiration": expiration
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response)
print(response.json)
upload_data = response.json()

# Print the file upload iddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
print(f"file upload id = {upload_data['id']}")

# Step 2: Upload the file
upload_url = upload_data['url']
form_data = upload_data['form']

files = {
    'file': open(file_path, 'rb')
}
form_fields = {
    'key': form_data['key'],
    'x-amz-algorithm': form_data['x-amz-algorithm'],
    'x-amz-credential': form_data['x-amz-credential'],
    'x-amz-date': form_data['x-amz-date'],
    'x-amz-security-token': form_data['x-amz-security-token'],
    'policy': form_data['policy'],
    'x-amz-signature': form_data['x-amz-signature']
}

response = requests.post(upload_url, files=files, data=form_fields)
print(response)
# Step 2.5 Check if the file upload was successful
if response.status_code == 204:
    print("File uploaded successfully.")
else:
    print(f"Failed to upload file. Status code: {response.status_code}")

# Step 3: Check the upload status
file_upload_id = upload_data['id']
print(file_upload_id)
status_url = f'https://genai-code-buddy-api.stackspot.com/v1/file-upload/@{file_upload_id}'
status_headers = {
    'Authorization': f'Bearer {JWT}'
}

status_response = requests.get(status_url, headers=status_headers)
print(f'Upload Status: {status_response}')
print(status_response.json())

# Check if the status check was successful
if status_response.status_code == 200:
    print("Upload status checked successfully.")
    print(status_response.json())
else:
    print(f"Failed to check upload status. Status code: {status_response.status_code}")
