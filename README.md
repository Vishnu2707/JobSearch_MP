# Job Search Automation Script for "Any Roles" according to the "Location"

This Python script automates the process of searching for "Cloud Engineer" jobs in London, United Kingdom, and saves the job details to an Excel file. The data is fetched using the JSearch API, and the results are stored locally for easy access and further processing.

### Features

- Fetches job listings for "Cloud Engineer" roles in London, UK.
- Extracts key information like Job Title, Employer Name, Location, Job Description, Application Link, Employment Type, Date Posted, and Job Publisher.
- Saves the extracted data into an Excel file for easy access and further analysis.

### Installation

To run this script, you need to have Python installed on your system along with the required libraries. Follow the steps below to set up your environment:

1. **Install Python**: Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the required Python libraries:

   ```bash
   pip install requests pandas openpyxl
   ```

### Script Overview

```python
import requests
import pandas as pd
import os

# Define API URL and query parameters
url = "https://jsearch.p.rapidapi.com/search"
querystring = {"query": "Cloud Engineer in London,United Kingdom", "num_pages": "10", "date_posted": "all"}

# Define headers for the API request
headers = {
    "x-rapidapi-key": "Rapid-Key",
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

# Make the API request and get the JSON response
response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Extract job data from the JSON response
jobs = data['data']  # List of job dictionaries

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

# Get the user's home directory and construct the path to the Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "/Users/vishnuajith/Desktop/Job", "All_of_them.xlsx")

# Save the DataFrame to an Excel file in the Downloads folder
df.to_excel(downloads_path, index=False)

print(f"Excel file 'All_of_them.xlsx' created successfully in the Job folder.")
```

### How to Use

1. **Update API Key**: Replace `"Rapid Key"` with your actual RapidAPI key in the `headers` dictionary.

2. **Run the Script**: Open your terminal or command prompt, navigate to the directory where the script is saved, and run:

   ```bash
   python your_script_name.py
   ```

3. **Check the Output**: After running the script, an Excel file named `All_of_them.xlsx` will be created in the specified folder (`/Users/vishnuajith/Desktop/Job`). This file contains all the job listings fetched by the script.

### 📄 Notes

- Ensure you have the correct permissions to access the specified output directory.
- The script is configured to fetch data for "Cloud Engineer" roles in London. You can modify the query parameters in the `querystring` dictionary to fetch jobs for different roles or locations.
- The script can be easily customized for other job searches by changing the `query` parameter.

### Contact

For any questions or feedback, feel free to reach out to me on LinkedIn!
