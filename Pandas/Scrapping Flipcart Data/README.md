# Flipkart Mobile Data Scraping (Python)

## Overview
This project demonstrates how Python libraries are used to scrape mobile phone data from Flipkart for learning and data analysis purposes. The scraped data can be further used for analysis, visualization, or machine learning tasks.

## Libraries Used

- **requests**  
  Used to send HTTP requests and fetch HTML content from Flipkart search result pages.

- **BeautifulSoup (bs4)**  
  Used to parse HTML content and extract product names, descriptions, and reviews using tags and class names.

- **pandas**  
  Used to store scraped data in a structured tabular format and export it to a CSV file for further analysis.

## How It Works

- The script iterates through multiple pages of Flipkart search results.
- HTML content is fetched using the `requests` library.
- The fetched HTML is parsed using `BeautifulSoup`.
- Required data is extracted using `find()` and `find_all()`.
- Extracted data is stored in Python lists.
- The lists are converted into a pandas DataFrame.
- The final dataset is saved as a CSV file.

## Important Note

Flipkart frequently changes its HTML structure and CSS class names.  
Before running the script, always inspect the Flipkart webpage and verify the class names used in the code.  
If class names change, update them in the script to avoid errors such as `NoneType` or `find_all()` issues.

## Output

- **flipkartdata.csv**
  - Product Name
  - Description
  - Reviews / Ratings

## Use Cases

- Data analysis
- Data visualization
- Practice with pandas and NumPy
- Machine learning projects

## Disclaimer

This project is created for educational purposes only.  
Always follow Flipkart’s terms and conditions while scraping data.
