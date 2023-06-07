
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
tech-sheet-app
</h1>
<h3 align="center">📍 Streamline your tech game with Tech-Sheet-App on GitHub</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgresSQL" />
<img src="https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white" alt="SwaggerUI" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [💫 Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The tech-sheet-app is a Flask-based web application with a PostgreSQL database that allows users to create, read, and update app details. The app details include ID, URL, name, description, front-end and back-end technology, database technology, author, and GitHub URL. The project provides a reliable and scalable solution for managing app details and offers value by allowing users to quickly access and update details for their apps in a central location. Additionally, the project includes robust security measures, such as Go-Auth server verification, to ensure app details are only accessible by authorized users.

---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase follows a standard directory structure with scripts for deployment and setups, a Dockerfile for the Flask app, and a separate directory for the PostgreSQL setup. The Flask app directory follows a modular design pattern with separate files for database helper functions, console logging, and the main Flask API code. |
| **📝 Code Documentation** | The code is generally well-documented, with comments explaining the purpose and functionality of most functions and scripts in the codebase. Docstrings are also present in some modules, though not consistently throughout. |
| **🧩 Dependency Management** | Dependencies are handled using a requirements.txt file for the Flask app and a Dockerfile for the PostgreSQL setup, with both listing the necessary packages and versions. |
| **♻️ Modularity and Reusability** | The Flask app is designed with modularity in mind, with separate files for database helper functions, logging, and the main Flask API code. The PostgreSQL setup is similarly separated into its own directory. Helper functions and SQL queries are designed for reusability across the Flask app endpoints. |
| **✔️ Testing and Quality Assurance** | No testing or quality assurance code is present in the repository for the moment. |
| **🔒 Security Measures** | The Flask app includes integration with an authentication server to verify permissions before allowing updates. The database setup includes granting necessary privileges to a user for the app details table. |
| **🔄 Version Control and Collaboration** | The codebase uses Git for version control, with frequent commits and descriptive commit messages. Collaboration is not apparent as there is only one contributor in the repository. |
| **🔌 External Integrations** | The Flask app includes integration with a Go-Auth server for authentication. The Docker containers for the Flask app and the PostgreSQL database may also be integrated with external tools and services. |
| **📈 Scalability and Extensibility** | The modular design of the Flask app and PostgreSQL setup allows for easy extension and modification of app details functionality.

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## 📂 Project Structure


```bash
repo
├── LICENSE
├── README.md
├── flask-app
│   ├── Dockerfile
│   ├── app
│   │   ├── api
│   │   │   ├── api.json
│   │   │   └── api.yaml
│   │   ├── app.py
│   │   ├── console_logger.py
│   │   └── psql_helper.py
│   └── requirements.txt
├── postgresql-db
│   ├── Dockerfile
│   ├── setup.sql
│   └── setup_template.sql
└── scripts
    ├── deploy_api.sh
    ├── deploy_db.sh
    ├── prepare_db_setup.sh
    └── prepare_env.sh

5 directories, 16 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>App</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Module                          |
|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| psql_helper.py    | The code snippet provides functions to establish a connection to a PostgreSQL database, set up keys to be used in CRUD operations, and generate SQL queries for create, read (by ID and count), and update operations on app entries in the database. The app details include ID, URL, name, description, front-end and back-end technology, database technology, author, and GitHub URL. The queries use environment variables to retrieve database connection details and table name. | flask-app/app/psql_helper.py    |
| app.py            | The code is a Flask API for creating, reading, and updating app details stored in a PostgreSQL database. The API endpoints allow GET and POST requests, with GET returning the details of a specified app and POST allowing the creation or updating of the app details. The code also includes connection to a Go-Auth server to verify permissions before allowing updates.                                                                                                           | flask-app/app/app.py            |
| console_logger.py | The code initializes a logger named "APP_DETAILS_API" with a debug level. Then, it creates a console handler with an info level and a formatter for log messages. Finally, the console handler is added to the logger to output log messages to the console.                                                                                                                                                                                                                            | flask-app/app/console_logger.py |

</details>

<details closed><summary>Flask-app</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                 | Module               |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| Dockerfile | The code snippet sets up a Docker container running Python 3.10 with Flask. It installs the necessary requirements, sets environment variables for a PostgreSQL database connection, and exposes port 3500 for the Flask server to run on. Finally, it runs the Flask app with the command "flask run". | flask-app/Dockerfile |

</details>

<details closed><summary>Postgresql-db</summary>

| File               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                               | Module                           |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| setup.sql          | The provided code snippet performs the following tasks in a PostgreSQL database: creates a database if it does not exist, lists all databases, connects to a specific database, creates a user if not already exists, grants necessary privileges to the user, creates a table if it does not exist, and grants necessary privileges to the user for the table. It also provides the command to list all tables and show details of a specific table. | postgresql-db/setup.sql          |
| Dockerfile         | The provided code snippet sets up a Postgres container with environment variables for database initialization and usage. It copies a setup.sql file to the container's entrypoint init directory for database setup. Finally, it exposes the Postgres port 5432.                                                                                                                                                                                      | postgresql-db/Dockerfile         |
| setup_template.sql | The code snippet creates a PostgreSQL database, a table, and a user with the necessary privileges. It also checks if the database, the table, and user exist, and grants necessary privileges to the user. Finally, it lists all databases and tables in the database.                                                                                                                                                                                | postgresql-db/setup_template.sql |

</details>

<details closed><summary>Scripts</summary>

| File                | Summary                                                                                                                                                                                                                                                                                                                                                                                                         | Module                      |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| prepare_db_setup.sh | This code snippet is a bash script that sources another script called "prepare_env.sh" and reads data from a setup_with_vars.sql file. It then replaces environment variable placeholders with their corresponding values and writes the output to a setup.sql file. The purpose appears to be to prepare a PostgreSQL database environment with the necessary configurations.                                  | scripts/prepare_db_setup.sh |
| deploy_api.sh       | The code snippet prepares the environment using a shell script, builds and pushes a Docker image, and deploys it as a Docker container on port 3500 with environment variables set for PostgreSQL database and authentication. The container is named "APPDETAILS-API-LOCAL".                                                                                                                                   | scripts/deploy_api.sh       |
| prepare_env.sh      | The code snippet sets environment variables for a PostgreSQL admin database, app details information, and an auth server. The variables include database credentials, table name, server host and port, and authentication server URL. The purpose is to provide necessary information and credentials for executing queries and accessing resources within a PostgreSQL database and an authentication server. | scripts/prepare_env.sh      |
| deploy_db.sh        | This code snippet is a Bash script that builds and runs a Docker container named "APPDETAILS-PSQL-LOCAL" which hosts a PostgreSQL database locally. The script also sets environment variables required for the database setup. The Docker container is built from a Dockerfile located in the "../postgresql-db" directory.                                                                                    | scripts/deploy_db.sh        |

</details>

---

## 🚀 Getting Started

<!-- ### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - [📌  PREREQUISITE-1]
> - [📌  PREREQUISITE-2]
> - ... -->

### 🖥 Installation

1. Clone the tech-sheet-app repository:
```sh
git clone ../tech-sheet-app
```

2. Change to the project directory:
```sh
cd tech-sheet-app
```

3. Install the dependencies:
```sh
chmod +x main.sh
```

### 🤖 Using tech-sheet-app

```sh
./main.sh
```

### 🧪 Running Tests
```sh
bats *.bats
```

<!-- ---


## 🗺 Roadmap

> - [X] [📌  Task 1: Implement X]
> - [ ] [📌  Task 2: Refactor Y]
> - [ ] [📌  Task 3: Optimize Z]
> - [ ] ... -->


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `Apache-2.0` License. See the [LICENSE](LICENSE) file for additional info.

---

## 👏 Acknowledgments

> - Personal Project

---


## Credits

This awesome documentation was automatically generated using the [README-AI Project](https://github.com/eli64s/README-AI)

---