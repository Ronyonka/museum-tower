# Museum Tower

Welcome to the **Museum Tower** project repository! This project is a Flask application that manages tenant data and transactions for the Museum Tower property. Follow the instructions below to set up and run the application.

## Prerequisites

Before getting started, ensure you have the following prerequisites installed:

- Python (version 3.6 or higher)
- PostgreSQL

## Installation

1. Clone the repository by running the following command:

```bash
 git clone https://github.com/Ronyonka/museum-tower.git
```
2. Change into the project directory:
```bash
cd museum-tower
```
3. Create a virtual environment file:
```bash
python3 -m venv venv
```
4. Activate the virtual environment:

For macOS/Linux:

```bash
source venv/bin/activate
```
For Windows:

```bash
venv\Scripts\activate
```
5. Install the required packages from the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Configuration
1. Create a .env file in the project root directory.

2. Add the following environment variables to the `.env` file:
```
DB_USERNAME=<your_database_username>
DB_PASSWORD=<your_database_password>
DB_NAME=<your_database_name>
DB_HOST=<your_database_host>
```
Replace `<your_database_username>`, `<your_database_password>`, `<your_database_name>`, and `<your_database_host>` with the appropriate values for your PostgreSQL configuration.

Make sure to create a postgresql database and add the name of your database.

## Migrations

Apply the database migrations to create the necessary tables. Run the following command:

```bash
flask db upgrade
```

## Running the Application

Ensure you have activated the virtual environment.

In the project root directory, run the following command:

```bash
python main.py
```
This will run the script in your terminal and normalize the excel data, adding it to your database

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)