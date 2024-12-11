## Project Description  
This project is a web application that stores and provides information about historical military battles and conflicts. Users can search, browse, and add information about various battles, as well as visualize data through graphs and maps.  

## Key Features  
### User Registration and Authentication  
- Users can register and log into the system.  
- Administrators have special rights to manage the content.  

### Battle Management  
- **Add New Battles**: A form to input information like date, location, participating countries, outcome, and description.  
- **Edit and Delete Battles**: Administrators can edit and delete records.  
- **Search and Filter**: Users can search battles by various criteria such as date, location, and participating countries.  

### Data Visualization  
- **Graphs**: Visualization of statistical data such as the number of battles over the years, losses, and victories of different countries.  
- **Maps**: Interactive maps displaying the locations of battles.  

### Comments and Ratings  
- Users can leave comments and ratings for each battle.  
- Administrators can moderate comments.  

### Historical Context  
- Articles and analyses providing context for various battles and conflicts.  
- Ability to add multimedia content like images and videos.  

## Technologies and Tools  
- **Django**: The main framework for developing the web application.    
- **PostgreSQL**: Database for storing the information.  
- **JavaScript and D3.js**: For data visualization and interactive maps.  
- **HTML/CSS**: For building the user interface.  

## Implementation Steps  
### Planning and Design  
- Define key functionalities and create wireframes for the user interface.  
- Select technologies and tools.  

### Project Setup  
- Create a Django project and set up the database.  
- Install necessary libraries and packages.  

### Development of Core Modules  
- User registration and authentication.  
- Battle management (CRUD operations).  
- Data visualization.  

### Testing and Debugging  
- Test functionalities and debug issues.  
- Conduct user testing to improve the interface.  

### Deployment  
- Set up a server and deploy the application.  

## Getting Started  
To get a local copy up and running follow these simple steps: 
1. Clone the repository:
    git clone https://github.com/hanvap/battleBGarmy.git

2. Navigate to the project directory

3. Install dependencies:
    pip install -r requirements.txt

4. Run migrations:
    python manage.py migrate

5. Start the development server:
    python manage.py runserver

6. Run tests:
    python manage.py test


Deployment LINK https://battlebg-fgg9cxh5e3fbb3fj.italynorth-01.azurewebsites.net/
