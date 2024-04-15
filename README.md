# Django Bookstore Project

This Django project serves as a simple bookstore API with endpoints to list books and retrieve detailed book information. It also includes a welcome page to showcase available books with pagination, book detail links, and filtering functionality by author and category.


## Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/inavellevani/Django-beginning.git```

2. **Navigate to the project directory**:
    
    ```cd Django-market```
   
3. **Install Django (if not already installed)**:

    ```pip install django```
  
4. **Apply migrations to create the database schema**:
  
    ```python manage.py migrate```

5. **Create a superuser to access the admin panel**:

    ```python manage.py createsuperuser```

6. **Start the development server**:

   ```python manage.py createsuperuser```

7. **Acceess the Django admin panel at http://127.0.0.1:8000/admin/ to add books.**

<br />

## Configuration
• **Database:** SQLite is used as the default database.

• **Media Files:** Uploaded book images are stored in the media directory.

• **Django Settings:** The project's Django settings are located in djangoProject/settings.py. Key settings include:

• **SECRET_KEY:** Django secret key used for cryptographic signing.

• **DEBUG:** Debug mode enabled for development.

• **ALLOWED_HOSTS:** List of allowed hosts for the project.

• **INSTALLED_APPS:** List of installed Django apps, including the market app.

• **DATABASES:** Database configuration using SQLite.

• **MEDIA_ROOT and MEDIA_URL:** Configuration for serving media files (uploaded images).

<br />

### API Endpoints
• **List Books:** GET/api/books/
    <br>&nbsp;&nbsp;Retrieves a list of all available in the bookstore.

• **Get Book Details:** GET /api/books/<book_id>/
    <br>&nbsp;&nbsp;Retrieves detailed information about a specific book identified by <book_id>.

<br />

### Views
• **book_list:** View to list all books in JSON format. Also handles HTML rendering for the welcome page with pagination and filtering.

• **book_detail:** View to retrieve detailed information about a specific book in JSON format and render the book detail page.

• **welcome:** View to handle the book listing functionality, including pagination.

<br />

### Templates
• **welcome.html:** Template for the welcome page, displaying paginated book listings with links to book details and filtering functionality by author and category.

• **book_detail.html:** Template for displaying detailed information about a specific book, including its categories.

### Admin Panel

Access the Django admin panel at http://127.0.0.1:8000/admin/ to manage books.

<br />

### API Usage

Use the provided API endpoints to integrate book data into your applications. Ensure proper authentication and authorization mechanisms are implemented for production use.

<br />

### Additional Notes
• Ensure proper media file configuration (MEDIA_ROOT and MEDIA_URL) for serving uploaded book images.

• Customize and extend the project based on your needs and requirements.

• For more information on Django, refer to the official Django documentation.
