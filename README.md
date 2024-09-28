# Sword Health - Book Management Application 📚

## 📖 Overview

This application is a full-stack web application designed to manage a collection of book records. It consists of a backend built with Django and a frontend developed using React. The application provides features for searching and viewing book details, as well as administering books.

## 🗂️ Project Structure

The project is organized into two main folders:

- **BE_SWORD**: Contains the backend implementation using Django, handling API requests and database interactions.
- **FE_SWORD**: Contains the frontend implementation using React, providing a user interface for interacting with the backend.

## 🏛️ Architecture

### Backend (BE_SWORD)

The main files of the application structure are detailed below:

```text
be_sword
├── be_sword
│   └── settings.py
├── book
│   ├── admin.py
│   ├── filters.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── scripts
├── tests
├── .env
├── pyproject.toml
```

The **be_sword** folder contains the core Django configurations for the application. It includes the **settings.py** file, which defines essential settings and configurations for the project. When using Docker, these settings are loaded from environment variables specified in the **.env** file.

The **book** folder is dedicated to managing book records and includes the following files:

- **models.py**: Represents the structure of the database tables.
- **urls.py**: Maps URLs to their corresponding views.
- **views.py**: Contains view functions for handling requests and returning responses.
- **filters.py**: Defines custom filters for querying book records.
- **serializers.py**: Transforms complex data into JSON format and handles JSON inputs.
- **admin.py**: Configures the Django admin interface, enabling the management of book records.
- **forms.py**: Contains forms used for uploading files.
- **utils.py**: Includes helper methods to support various functionalities.

The **scripts** folder is designed to prepare the application for deployment on Docker.

The **tests** folder contains unit and integration tests to ensure the reliability of the application.

Lastly, **pyproject.toml** is utilized to specify the project's dependencies.

### Frontend (FE_SWORD)

The main files of the application structure are detailed below:

```text
fe_sword
├── src
|   ├── components
|   ├── pages
|   |   ├── HomePage.js
|   |   ├── BookDetail.js
│   └── App.js
├── .env
├── package.json
```

The project consists of two main **pages**: the **HomePage.js**, which displays a collection of books, and the **BookDetail.js** page, which provides detailed information about a specific book.

All components necessary for creating these pages are developed in the **components** folder.

The primary entry point of the application, **App.js**, is responsible for routing between pages based on the current URL.

The **.env** file contains the environment variables used throughout the application, while **package.json** lists the dependencies and packages required for the project.

## 🛠️ Design choices

- Django was selected for its simplicity and effectiveness in building RESTful APIs. It facilitates the creation of an admin interface, views, serializers, and filters with remarkable ease, utilizing its robust and well-established functionalities.

- The entire project is designed to run in Docker, utilizing PostgreSQL as the database and MailHog as a mock email server. For development purposes, it also supports running without Docker, using basic configurations.

- MailHog was selected for its simplicity in tracking sent emails. The backend allows for the configuration of a real email server by supplying the appropriate credentials through environment variables.

- The frontend was designed to be user-friendly, displaying all loaded books along with a search bar and pagination features.

## 💭 Assumptions

- The book ingestion process was developed using a provided file containing 10,000 records. By treating this file as a standard, the algorithm was optimized to perform efficiently.

## ⚙️ Setup instructions

### Pre-requisites to execute the app

To run the application, ensure you have the following installed:

- **Git**: Required for version control and managing the source code.

   [Git installation](https://git-scm.com/downloads)

- **Docker**: Necessary for running the application in a containerized environment.

   [Docker installation](https://docs.docker.com/engine/install/ubuntu/)

### Pre-requisites to run locally

To work with the application locally, you will need:

- **Python**: Needed to run backend application.

   [Python installation](https://www.python.org/downloads/)

- **Node.js**: Required for running the frontend application.

   [Node.js installation](https://nodejs.org/en/download/)

## 🚀 Running the application

1. **Setup**:
   - Build and start all Docker containers by running the following command:

     ```bash
     docker-compose up --build
     ```

2. **Access the administration**:
   - Open your web browser and navigate to `http://localhost:8000/admin` to access the administration page. Use the default admin credentials:

     ```text
     username: admin
     password: admin
     ```

3. **Access the application**:
   - In your web browser, go to `http://localhost:3000` to access the frontend of the application.

4. **Open e-mail server**
   - To monitor emails sent by the backend, open `http://localhost:8025/` to access the mock email inbox.

5. **Connect to database**
   - If necessary, connect to the PostgreSQL database using the following credentials:

   ```text
   Host: localhost
   Port: 5432
   Database: postgres
   Username: postgres
   Password: postgres
   ```

## 💻 Working locally

### Backend setup

1. **Navigate to the project directory:**

   Change to the `be_sword` directory.

   ```bash
   cd be_sword
   ```

2. **Set up a virtual environment:**

   It is recommended to use a virtual environment to manage dependencies effectively. You can choose your preferred installer.
   For example, if you’re using Miniconda, run the following commands:

   ```bash
   conda create -n sword python=3.12
   conda activate sword
   ```

3. **Install Poetry:**

   Install Poetry for dependency management:

   ```bash
   pip install poetry
   ```

4. **Install Dependencies:**

   Use Poetry to install all required packages:

   ```bash
   poetry install
   ```

5. **Database and e-mail:**

   For local development, the application is initially configured to use a local SQLite database and the console as the email target. These settings are optimized for smooth operation.

   If you prefer to use Docker for the database and email, you can set the following environment variables:

   ```bash
   export DB_LOCAL=False
   export EMAIL_MOCK=False
   export EMAIL_HOST=localhost
   ```

   Additionally, you can specify other database and email server configurations by setting their credentials accordingly.

6. **Run the application**:

   To start the application, use the following command:

   ```bash
   python manage.py runserver
   ```

**Frontend Setup**:

1. **Navigate to the `fe_sword` directory.**

   ```bash
   cd fe_sword
   ```

2. **Install all required dependencies:**

   ```bash
   npm install
   ```

3. **Start the react application:**

   ```bash
   npm start
   ```

## 🕹️ Operating

- **Ingest books**
In the administration page, select the `Book` model and click on the `Add Multiple Books` button. Then, click on `Choose File` to select a CSV file for importing books.

## ✅ Conclusion

The Sword Book Application was designed to be simple, user-friendly, and performant, while meeting the requirements outlined in the technical challenge. It is also built for easy expansion and maintenance.
