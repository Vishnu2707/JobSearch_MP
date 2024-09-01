import requests
import pandas as pd
import os
from dotenv import load_dotenv
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font
from openpyxl.worksheet.hyperlink import Hyperlink

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("RAPIDAPI_KEY")

# Define API URL and query parameters
url = "https://jsearch.p.rapidapi.com/search"
querystring = {"query": "Site Engineer in United Kingdom", "num_pages": "20", "date_posted": "all"}

# Define headers for the API request
headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

# Make the API request and get the JSON response
response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Extract job data from the JSON response
jobs = data['data']  

# Create a list to store the extracted job data
job_list = []

# Loop through each job and extract the relevant information
for job in jobs:
    job_info = {
        'Job Title': job.get('job_title', ''),
        'Employer Name': job.get('employer_name', ''),
        'Location': f"{job.get('job_city', '')}, {job.get('job_state', '')}, {job.get('job_country', '')}",
        'Job Description': job.get('job_description', ''),
        'Application Link': job.get('job_apply_link', ''),
        'Employment Type': job.get('job_employment_type', ''),
        'Date Posted': job.get('job_posted_at_datetime_utc', ''),
        'Job Publisher': job.get('job_publisher', '')
    }
    job_list.append(job_info)

# Convert the list of jobs to a DataFrame
df = pd.DataFrame(job_list)

# Create a new workbook and sheet using openpyxl
wb = Workbook()
ws = wb.active
ws.title = "Job Listings"

# Append the DataFrame to the Excel sheet
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

# Make "Application Link" column clickable as a hyperlink
for cell in ws["E"]:  # Column E is the "Application Link" column
    if cell.row == 1:
        continue  # Skip the header row
    if cell.value:
        # Create a hyperlink
        cell.hyperlink = Hyperlink(ref=cell.coordinate, target=cell.value, display=cell.value)
        cell.font = Font(color="0000FF", underline="single")

# Define the path to save the Excel file
downloads_path = os.path.join(os.path.expanduser("~"), "/Users/vishnuajith/Desktop/Job", "All_of_them.xlsx")

# Save the workbook to the specified path
wb.save(downloads_path)

print(f"Excel file 'All_of_them.xlsx' created successfully in the Job folder with clickable links.")
