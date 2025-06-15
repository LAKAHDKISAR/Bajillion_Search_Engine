# Bajillion Search Engine

## Overview
Bajillion Search Engine is a simple web app that allows users to search for news articles from two major sources, The New York Times and The Guardian, using their public APIs. It provides article headlines and summaries in a clean, user-friendly interface built with Streamlit.

## Table of Contents
- [Overview](#Overview)
- [About This Project](#About_This_Project)
- 
- [Dataset Used](#Dataset_Used)
- [Features](#Features)
- [Screenshot](#Screenshot)
- [Usage](#Usage)
- [Requirements](#Requirements)
- [License](#License)

## About_This_Project
This Bajillion Search Engine was developed as my Final Project for Stanford University’s Code in Place course. The goal was to create a meaningful, functional application using the skills I learned during the course.
Currently, the project runs as a Streamlit-based GUI application, allowing users to search news articles from multiple sources (New York Times and The Guardian) in a simple and interactive interface.
In the future, I plan to extend and enhance this project by developing a full web application version with richer features, improved UI/UX, and additional data sources.

## Dataset_Used
This project fetches live data from:
- The New York Times Article Search API
- The Guardian Content API
- No local dataset is stored; all data is fetched dynamically based on user input.

## Screenshot


## Features

- Search articles by keyword from NYTimes and The Guardian simultaneously.
- Display headlines and summaries with clickable links.
- Expandable article details for better reading experience.
- Clean and minimal UI built with Streamlit.

## Usage

1. Clone this repository.
2. Install dependencies.
3. Create a .env file with your API keys for NYTimes and The Guardian.
4. Run the app with Streamlit:
- streamlit run searchmain.py
5. Enter your search term and explore the results from both news sources.

Requirements
- Python 3.7+
- Streamlit
- requests
- python-dotenv

Install dependencies via:
- pip install streamlit requests python-dotenv

## License
This project is licensed under the MIT License.

