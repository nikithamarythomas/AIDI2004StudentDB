# Student Management System

## Accessing the Website
You can access the live application through the following URL:

[https://aidi2004studentdb.onrender.com](https://aidi2004studentdb.onrender.com)


## Overview
AIDI2004StudentDB is a project repository for managing a student database using Flask and MySQL. The project demonstrates CRUD operations through a RESTful API. The repository includes necessary scripts and files to set up and run the application.

## Features
- **CRUD Operations:** Create, Read, Update, and Delete student records.
- **Flask Framework:** Utilizes Flask for creating the web application.
- **MySQL Database:** Manages student data using MySQL.

## Project Structure
- **app.py:** Main application file to run the Flask server.
- **create_students_table.py:** Script to create the students table in the database.
- **instance/:** Contains configuration settings.
- **static/:** Stores static files like CSS.
- **templates/:** HTML templates for rendering web pages.
- **requirements.txt:** Lists required Python packages.

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/nikithamarythomas/AIDI2004StudentDB
   ```
2. Navigate to the project directory:
```sh
cd AIDI2004StudentDB
```
3. Install the required packages
```sh
pip install -r requirements.txt
```
4. Create the database and table:
```sh
python create_students_table.py
```
5. Run the application:
```sh
python app.py
```
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




