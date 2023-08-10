# Freelancer Spider
This is a web scraping spider built using the Scrapy framework for Python. The spider is designed to scrape job information from the [Freelancer website](https://www.freelancer.com/jobs/). It navigates through different job listing pages, extracts relevant data from each job listing, and outputs the collected information.

# How It Works

**Spider Configuration:** The spider is named "Freelancer" and is configured to start its crawl from the URL "https://www.freelancer.com/jobs". It is set to obey the domain "www.freelancer.com", ensuring that it only crawls within this domain.

**HTTP Headers:** The spider includes a set of HTTP headers in its requests to simulate a web browser. These headers include various details like user-agent, accept headers, and more.

**Starting Requests:** The spider starts by making a request to the initial job listing page. It extracts the links to individual job listings from this page and sends requests to each job's detail page.

**Parsing Job Listings:** The parse method is responsible for extracting links to individual job listings from the current page. It then sends requests to each job's detail page to collect further information.

**Job Details Extraction:** For each job detail page, the spider extracts relevant information such as job title, description, location, and price using CSS selectors. This data is then yielded as a dictionary containing these attributes.

**Pagination:** After processing the current page, the spider increments the page counter to move to the next job listing page (up to page 199). It continues this process until all desired pages have been crawled.

# Installation
To use the Freelancer Spider, follow these steps:

- Install Scrapy (if not already installed):
  ```bash
  pip install scrapy
  ```
- Clone this repository:
  ```bash
  git clone https://github.com/eniayejudaniel/Freelancer-Job-Listings-Web-Scraper-with-Scrapy.git
  cd Freelancer-Job-Listings-Web-Scraper-with-Scrapy
  ```
# Usage
- Replace the contents of the provided spider file with the code from the repository.

- Run the spider using the following command:
  ```bash
  scrapy crawl Freelancer -o freelancer_output.csv
  ```
  This command starts the spider, collects job data, and saves it to a freelancer_output.csv file.

# Technologies Used

- **Scrapy:** A powerful and extensible framework for web scraping and crawling.

# Customization
Feel free to customize the spider according to your needs. You can adjust the CSS selectors, headers, and other parameters to match any changes in the target website's structure.

# Important Notes
- Respect the website's terms of use and robots.txt before scraping.
- Web scraping may impact the target website's performance. Be mindful of the frequency and volume of requests.
  
# Contributing
Contributions are welcome! If you find any issues or have improvements to suggest, please feel free to open an issue or submit a pull request.

# License
This project is licensed under the [MIT License](License).


