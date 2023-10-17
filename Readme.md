
# Web Scraping with Python: The Infatuation Scraper

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the **Web Scraping with Python: The Infatuation Scraper** project. This repository contains a Python web scraping script that extracts data from the website [www.theinfatuation.com](https://www.theinfatuation.com) using popular libraries like Beautiful Soup (bs4) and Scrapy. The Infatuation is known for its restaurant reviews and recommendations, and this script allows you to extract valuable information for various purposes.

![The Infatuation](https://github.com/adil6572/Infatuation-Web-Scraper/blob/main/The-Infatuation.png)


## Output 

- **review_url**: The URL of the review on 'www.theinfatuation.com'.
- **restaurant_name**: The restaurant's name 
- **restaurant_cuisine**: The type of cuisine served at the restaurant.
- **restaurant_location**: The restaurant's location.
- **restaurant_cost**: An indicator of the cost range, set as "$$."
- **review_date**: The date when the review was published, in the format as "YYYY-MM-DD."
- **review_rating**: The rating given to the restaurant.
- **food_rundown**: A dictionary describing various food items and their descriptions available at the restaurant.
- **review_text**: An array containing different paragraphs describing the restaurant and dining experience.

## Installation

Follow these steps to get started with the Infatuation Scraper:

### Prerequisites

- Python 3.9
- Pip (Python Package Installer)

### Instructions

1. Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/adil6572/Infatuation-Web-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Infatuation-Web-Scraper
   ```

3. Install the required Python packages:
   ```bash
   pip install beautifulsoup4 scrapy
   ```

## Usage

To use the Infatuation Scraper, follow these steps:

1. Run the scraper:

   ```bash
   scrapy crawl Review
   ```

2. The scraped data will be saved in a JSON file named `Reviews.json` in the project directory.

You can now use this data for various purposes, such as analysis, building your restaurant recommendation system, or any other creative project you have in mind.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository to your own GitHub account.

2. Clone the forked repository to your local machine.

3. Create a new branch with a descriptive name for your feature or bug fix.

4. Make your changes and commit them.

5. Push your branch to your GitHub repository.

6. Create a pull request to the main repository, explaining your changes and improvements.

We welcome your contributions and ideas to make this project even better!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using the Infatuation Scraper! Happy web scraping and data analysis! If you have any questions or need assistance, feel free to open an issue or contact the maintainers.
