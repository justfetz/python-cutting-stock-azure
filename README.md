# Cutting Stock Problem

## Project Description
This project involves implementing the Cutting Stock Problem using Python and dynamic programming. The Cutting Stock Problem is a classic optimization problem where the goal is to minimize the waste produced when cutting raw materials into smaller pieces to meet demand. This implementation uses the Django framework to provide a web-based interface for inputting data and viewing results.

## Approach
The approach used to solve the Cutting Stock Problem in this project is dynamic programming. The dynamic programming algorithm efficiently determines the optimal way to cut the raw materials to minimize waste.

## Features
- Input raw material dimensions and required pieces through a web interface.
- Dynamic programming algorithm to calculate the optimal cutting pattern.
- Display results, including the optimal cutting pattern and waste produced.
- Django framework for a robust and scalable web application.

## Prerequisites
- Python 3.x
- Django 3.x
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/python-cutting-stock-operations-research.git
    cd python-cutting-stock-operations-research
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage
1. **Input Data:**
    - Enter the dimensions of the raw materials.
    - Enter the required dimensions and quantities of the pieces needed.

2. **Calculate Optimal Cutting Pattern:**
    - Click on the "Calculate" button to run the dynamic programming algorithm.
    - View the optimal cutting pattern and the amount of waste produced.

## Project Structure
- `.github/workflows/`: GitHub Actions workflows.
- `cutting_app/`: Django application directory containing the main logic.
  - `migrations/`: Database migration files.
  - `templates/`: HTML templates for the web interface.
  - `views.py`: Contains the view functions for handling requests and rendering templates.
  - `models.py`: Defines the database models.
  - `dynamic_programming.py`: Implementation of the dynamic programming algorithm for the Cutting Stock Problem.
  - `generate_patterns.py`: Functions to generate cutting patterns.
- `cutting_project/`: Django project directory.
- `.gitignore`: Git ignore file.
- `README.md`: This README file.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: List of Python dependencies.

## Dynamic Programming Algorithm
The dynamic programming algorithm used in this project follows these steps:
1. Define the state and subproblems.
2. Establish the recurrence relation.
3. Use a table to store the solutions to subproblems.
4. Build the solution to the original problem from the solutions to subproblems.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/)
- [Dynamic Programming Algorithms](https://en.wikipedia.org/wiki/Dynamic_programming)

## Contact
For questions or comments, please contact [yourname@domain.com](mailto:jasonfetzer@protonmail.com).
