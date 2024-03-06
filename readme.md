**Thesis Project**

This is a Django project developed as part of the Application Development Course. The project allows users to view a list of theses and interact with them by leaving comments.

**Features**
- Display a list of theses.
- Users can view details of each thesis.
- Users can leave comments on the theses.

**Installation**
1. Clone the repository:
    ```bash
    git clone https://github.com/TooIneptNeedToLearn/Django-Thesis
    ```

2. Navigate to the project directory:
    ```bash
    cd Django-Thesis
    ```

3. Install the dependencies:
    
    ```bash
    create a text file named "requirement.txt" and it would contain this dependencies:
    asgiref==3.7.2
    Django==4.0.1
    sqlparse==0.4.4
    typing-extensions==4.9.0
    tzdata==2024.1
    
    Then:
    pip install -r requirements.txt
    ```
    

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the application at [http://localhost:8000](http://localhost:8000) in your web browser.
