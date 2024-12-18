
# LLM-text-generation

**Installation
Prerequisites
To run this project, you need to have the following software installed:**

Python 3.x (for the backend)
Node.js (for the frontend)
Django (for backend development)
Angular CLI (for frontend development)

**1- Clone the Repository:**
git clone https://github.com/your-username/llm-text-generation.git
cd llm-text-generation

**2- Set Up Virtual Environment**
python -m venv venv
source venv/bin/activate  

**3- Install Required Python Libraries**
pip install -r requirements.txt

**These libraries include:**

Django: The web framework for the backend.
Django Rest Framework: For creating the REST API endpoint.
transformers: For working with Hugging Face models like GPT-2.
torch: PyTorch backend for running the GPT-2 model.
django-cors-headers: For handling cross-origin resource sharing (CORS) issues.

**4- Set Up the Django Database: Run the migrations to set up the database:**
python manage.py migrate

**5- Run the Django Development Server: Start the Django server:**
python manage.py runserver
Your backend will be running at http://localhost:8000/.

**Frontend Setup (Angular)
1- Install Angular CLI: If you don’t have Angular CLI installed, you can install it globally:**
npm install -g @angular/cli

**2- Install Frontend Dependencies: Navigate to the frontend folder and install the dependencies:**
cd frontend
npm install

**3- Run the Angular Development Server: Start the Angular development server:**
ng serve

Your frontend will be running at http://localhost:4200/

**Usage**
Navigate to the Frontend: Open your browser and go to http://localhost:4200/.

Enter a Prompt: Type a prompt (e.g., "Once upon a time") in the input box.

Generate Text: Click the "Generate Text" button to send the prompt to the backend for processing.

View Results: The backend will generate text based on the input prompt using the GPT-2 model, and the generated text will be displayed on the page

![LLM Directory Structure](https://github.com/user-attachments/assets/90d3b810-e7b3-4af0-bb8d-513bee9c0053)
