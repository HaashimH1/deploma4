# Pattern Jobs
Pattern Jobs is an intuitive platform designed to change the job value tool. The main goal of Pattern is to provide a user-friendly and efficient platform where users can set what kind of job they are looking for, search for roles based on personalized profiles, and watch their job application history. Pattern Jobs by the use Adzunas Ad Search API. Pattern Jobs, is the one that takes the job-hunting process the farthest, making it simple both for users looking for new opportunities and for those who are just passively browsing.

Live site can be found [Here](https://deploma4-9a881a09cb04.herokuapp.com/)

## **Table of Contents**

1. [Pattern Jobs](#pattern-jobs)
2. [Table of Content](#table-of-content)
3. [User Experience (UX)](#user-experience-ux)
   - [Target Audience](#target-audience)
   - [User Goals](#user-goals)
   - [User Stories](#user-stories)
   - [Intuitive and Consistent Design](#intuitive-and-consistent-design)
   - [Key UX Design Principles](#key-ux-design-principles)
4. [Design](#design)
   - [Interface](#interface)
     - [User Flow](#user-flow)
     - [Mockups](#mockups)
       - [Home Page Mockup](#home-mock)
       - [Login & Register Page Mockup](#login-register-mock)
       - [Dashboard Page Mockup](#dashboard-mock)
     - [Rationale](#rationale)
   - [Features Walkthrough](#features-walkthrough)
     - [Home Page](#home-page)
       - [Nav Bar](#nav-bar)
       - [Hero Segment](#hero-segment)
       - [Info Segment](#info-segment)
       - [Footer](#footer)
     - [Login/Register](#login-register)
       - [General](#general)
       - [Input Fields](#input-fields)
     - [Dashboard](#dashboard)
       - [Profile Content](#profile-content)
       - [Dashboard Content](#dashboard-content)
         - [Jobs Display](#jobs-display)
         - [History Display](#history-display)
       - [General Dashboard Functionality](#general-dashboard-functionality)
5. [Implementation](#implementation)
   - [Overall Structure](#overall-structure)
   - [Models/App](#modelsapp)
     - [Users](#users)
     - [Profiles](#profiles)
     - [JobSearchHistory](#jobsearchhistory)
     - [API](#api)
     - [Templates](#templates)
6. [Technologies Used](#technologies-used)
   - [Languages and Frameworks](#languages-and-frameworks)
   - [Development Tools](#development-tools)
   - [Deployment Tools](#deployment-tools)
7. [Testing](#testing)
   - [Code Validation](#code-validation)
   - [Manual Testing Table](#manual-testing-table)
8. [Deployment](#deployment)
   - [Hosting Platform](#hosting-platform)
   - [Steps to Deploy on Heroku](#steps-to-deploy-on-heroku)
   - [Cloning the Repository Locally](#cloning-the-repository-locally)
   - [PostgreSQL Integration](#postgresql-integration)
   - [Final Verification](#final-verification)
9. [Credits](#credits)



## **User Experience (UX)**

### Target Audience
The app provides a service to those who want to keep the job search process simple and easy. It is perfect for you whether you are onto the next stage of your supporting career or you are still looking for a job actively or setting up a diverse job profile. Besides, employers and recruiters could also derive a great deal of value from the job-seeking functionality which is highly intuitive.

---

### User Goals
Users accessing the platform expect:
- **Seamless Profile Management**: The ability to create, edit, and manage job search profiles effortlessly.
- **Personalised Job Searches**: Tailored job search results based on specific user criteria like location, job title, salary expectations, and employment type.
- **Historical Tracking**: A comprehensive history of past job searches for quick reference and revisits.
- **Intuitive Interface**: A simple, clutter-free design that’s easy to navigate for users of all technical skill levels.
- **Data Integrity**: Confidence that their preferences and history are securely stored and accessible anytime.

---

### User Stories
1. *As a user, I want to create profiles tailored to different job roles, so I can organise my job searches effectively.*
2. *As a user, I want to search for jobs by location and salary range, so I can find the most relevant opportunities.*
3. *As a user, I want to view my search history, so I can track and revisit jobs I’ve explored before.*
4. *As a user, I want to edit my profile details easily, so I can update my preferences as they change.*
5. *As a user, I want to delete profiles I no longer need, so I can keep my dashboard organised.*
6. *As a user, I want an interface that highlights the most important information, so I can use the platform efficiently.*

---

### Intuitive and Consistent Design
The application features a clean and responsive design, making it accessible across devices ranging from mobile phones to desktops. The colour palette uses a blend of neutral tones and accent colours to create a professional yet inviting atmosphere. The interface ensures:
- Consistent typography and spacing for readability.
- Clearly defined sections for profiles, job search results, and history.
- Highlighted interactive elements like buttons and links to guide user actions.

---

### Key UX Design Principles
1. **Ease of Navigation**: 
   - The platform provides a logical and straightforward menu structure, ensuring users can quickly locate the desired functionalities.
   - Profiles, job searches, and history are compartmentalised for clarity.

2. **Accessibility**: 
   - A user-friendly interface ensures individuals with minimal technical knowledge can operate the platform.
   - Efforts have been made to comply with accessibility standards, including high-contrast elements and keyboard navigation.

3. **User Feedback**: 
   - Actions such as saving profiles, performing job searches, and editing details are accompanied by confirmation messages to provide users with real-time feedback.
   - Errors are clearly indicated with helpful instructions on how to resolve them.

4. **Consistency**:
   - The design, layout, and terminology used throughout the application remain consistent, reducing the learning curve for users.

---

By prioritising these UX elements, the platform delivers a robust and user-centric solution for managing job searches effectively.


## **Design**
###  Interface

![Colour palette used in website: black, dark grey, white, jungle green and yellow](/README_assets/doc_image_1.png)
- Black and white for background to text contrast.
- Dark gray for container backgrounds, like the dashbaord, to distinguish itself from the background but still be seamless.
- Jungle green and yellow as accent colours to provide unique style, and to distimguish different elements from eachother.


To ensure an intuitive and well-structured user experience, I designed mockups before implementing the final version of the site. Below is a breakdown of the design process, including the rationale behind the choices made and how these have been carried through to implementation.

#### User flow
Showcase users navigation through the site, ensuring a logical and efficient experience.
- Users start at the Home Page, where they can either register or log in.
- After logging in, they are directed to the Dashboard, where they can:
  - Create, edit, or delete job search profiles.
  - Perform job searches based on their profile criteria.
  - View and manage their search history.
- The system ensures proper authentication, meaning users cannot access restricted features unless logged in.
- If an error occurs (e.g., missing required fields), appropriate feedback is provided.

#### Mockups
##### Home mock
![home page design mockup](/README_assets/doc_wf_1.png)
- A simple hero section that introduces the platform and its functionality.
- A login/register button in the navigation bar for easy access.
- Key features are highlighted to provide an overview of what the platform offers.

##### Login Register Mock
![login page design mockup](/README_assets/doc_wf_2.png) ![register page design mockup](/README_assets/doc_wf_3.png)
- Fields for username, email, password, confirm password.
- Submit button for each form.
- Validation messages to showcase error info.
- Redirected to dashboard after successfull authentication.


##### Dashboard Mock
![dashboard page design mockup](/README_assets/doc_wf_4.png)
- The dashboard is divided into two main sections:
  - Profile Selection (left) → Users can select, edit, or delete job profiles.
  - Main Content (right) → Users can search for jobs or view their search history.
- On smaller screens, sections stack vertically to enhance readability.
- Selected fields (like selected profile) background colour change.


#### Rationale
To create an optimal user experience, I followed UX best practices:

- Simplicity & Minimalism
  - Clean interface with a focus on essential actions.
  - Avoided unnecessary distractions, ensuring users quickly find what they need.
  - Responsiveness & Mobile-First Approach

- Designed for mobile usability first, then expanded to desktop views.
  - Used flexbox & media queries to ensure a smooth experience across all devices.
  - Consistency & Intuitiveness

- Navigation bar and footer remain consistent across all pages.
  - CTA buttons (e.g., search, edit profile) use clear, bold text for better usability.
  - Feedback & Error Handling

- Visual indicators for successful actions (e.g., profile updates).
  - Error messages guide users when something goes wrong (e.g., missing required fields).






## **Features Walkthrough**
Below is a showcase of the website in its features, design process and screen resonsiveness.
### **Home Page**
#### General
![snippet of home page](/README_assets/doc_image_2.png)
- Home constists of a Nav bar, hero segment, info segment and a footer
- Nav bar and footer are only 2 elements which are present and the same on all pages of this site.
- Following the layout from the initial design mockup, fitting its rationale.

#### Nav Bar
![snippet of nav bar](/README_assets/doc_image_3.png)
![snippet of nav bar alternate](/README_assets/doc_image_4.png)

Nav bar is split into 2, left and right:
- Left side is the logo and title, on click takes to home page.
- Right side is 2 buttons for either:
  - `Login` and `Register`
  - `Dashboard` and `Logout`
- Depending if the user is logged or not, eithe will show respectively
- On hover, backgorund changes to highlight to user a clickable element.

#### Hero segment

![snippet of hero](/README_assets/doc_image_5.png)
- Simple, content light hero.
- COlours to highlight certain aspects of content
- Not much responsiveness due to the little amount of content

#### Info Segment

![snipper of info segment on bigger screens](/README_assets/doc_image_6.png)
- Using the gray background container to emphasize the difference of this segment to the hero and footer
- Brief description of features that can grab the attention of new user.
- Bigger screens, every other content container is reversed to improve readability

![snippet of info segment on smaller screens](/README_assets/doc_image_7.png)
- Smaller screens content is stacked vertically for better readability

#### Footer
![snippet of footer](/README_assets/doc_image_8.png)
- Simple, content light footer.
- No responsiveness as content is so little
- Not much colour because not alot of elements to differentiate from

### **Login / Register**
#### General
![snippet of login page](/README_assets/doc_image_9.png)
![snippet of register page](/README_assets/doc_image_10.png)

- Very similluar styled pages due to nature of the content.
- One dark grey container to differnentiate itself from the black backround
- Following the layout from the initial design mockup, fitting its rationale.

#### Input Fields
![snippet of login text fields](/README_assets/doc_image_11.png)
![snippet of register text fields](/README_assets/doc_image_12.png)

- Focused field is highlighted to show the current element user is using.
- Submit button highlighted on hover

![snippet of empty field error message](/README_assets/doc_image_13.png)

- Error message on empty field submit.

![snippet of register inputs error ](/README_assets/doc_image_15.png)
![snippet of login inputs error](/README_assets/doc_image_14.png)

- Error message shown and the nature of the errors.
- User to reneter fields that were invalid prior to submit
- Password fields always removed on error for ease of use to reenter
- On successfull login, user redirected to dashboard.
- On successfull register, user redirected to login page.

### **Dashboard**
#### General
![snippet of dashboard page](/README_assets/doc_image_16.png)

- User can only access this page if they are authenticated (logged in)
- One dark grey container to house all the dashbaord content.
- Following the layout from the initial design mockup, fitting its rationale.

![snippet of dashboard container on bigger screens](/README_assets/doc_image_17.png)
- Container is split into 2:
  - `Profile Selection`: Profile utilitys, and buttons to display either search or history display
  - `Dashboard Content`: Displays either Job search utility, or history of that profiles searches
- Black thin divider so user can visually see the seperation of both containers
- Bigger screens, containers are displayed horizontally for ease of use as everything is in one screen

![snippet of dashboard comtainer on smaller screens](/README_assets/doc_image_18.png)
- Smaller screens, container are displayed vertically for better readabilty, user will have to scroll to view all the content

![snippet of dashboard for new user](/README_assets/doc_image_20.png)
- For a new user with no profiles created, prompt displayed to do so.

#### Profile Content
![snippet of profiles utilitys](/README_assets/doc_image_19.png)
- Displays all profiles user has.
- Selected Profile is always at the bottom of the list, and is styled differently to highlight its current selection 
- Below selected profile, are utilitys:
  - `Edit`: Change selected profiles set parameters
  - `Delete`: Delete selected profile entirely
  - ` + `: Create a whole new profile, this wont appear if user has hit the 5 profile cap.

On click of a profile utility, will display a popup box respectively:

![snippet of create popup](/README_assets/doc_image_23.png)
![snippet of edit popup](/README_assets/doc_image_21.png)
![snippet of delete popup](/README_assets/doc_image_22.png)
![snippet of delete popup with only 1 profile](/README_assets/doc_image_24.png)

- `Create`: Profile parameters consists of:
  - `Job Title`: String
  - `Minimum Salary`: Integer
  - `Full Time`: Boolean
  - `City`: String

  5 Profiles max for each given user.

- `Edit`: Change the already defined set of profiles parameters
- `Delete`: Deletes the profile permanently, cant delete profile if its the only one a user has. After deletion, Selected profile is changed a different one.

![snippet of functions to change dashboard display](/README_assets/doc_image_25.png)

- Buttons to change the display of the content comtainer respectively


#### **Dashboard Content**
### Jobs Display
![snippet of job search display](/README_assets/doc_image_26.png)

- Message to the user to make sure the profiles set parameters are correct and valid, as an invalid search will not return back anything.

![snippet of job search results](/README_assets/doc_image_27.png)

- On search, max of 5 results are received and displayed.

### History Display
![snippet of history display](/README_assets/doc_image_28.png)

- Displays all previous results that the profile has ever searched for from newest to oldest, does not store/show duplicates.

### General

![snippet of comtainer scroll on bigger screens](/README_assets/doc_image_29.png)
![snippet of page scroll on smaller screens](/README_assets/doc_image_30.png)

On both History and Search display:
- For bigger screens, the display container itself is scrollable to view all the jobs, this makes is so the whole dashbaord page is viewable in one display without scrolling the page itself for ease of use.
- For smaller screens, the display conatiner is not scrollable however it is just simply extended to fit all the results, this make is so the whole dashboard page is not viewable in one display, so the user will have to scroll the page itself and not the container within for ease of use and better readability on smaller screens.

![snippet of one job result](/README_assets/doc_image_31.png)

Each Job result is designed like so:
- Black container to contrast the dark grey background, on click will open a new tab with the link to that jobs ad.
- Green coloured Job title to highlight the job position, with the company and location on the same line but plain white.
- Description is slighlty darker than the rest to highlight the importance of the other elements first, as a user would naturally be more inclined to read the basic things like title, company and salary. So the description is much distinct to help the user skim read the results as the description takes up most the space while being the least important to user.
- Salary figures highlighted in yellow to also highlight the importance of this data, however different colour than the job title to signify the difference of the data shown.
- Having the job title at the top with one colour, and the salary figures at the bottom with another colour can further help the user differentiate between different results as those different coloured data that are at the bottom and top of each result act as a wrapper to that result.

## **Implementation**

Since this is a Django based web app, directory structure consists of apps with multiple .py files.

### Overall Structure
| Name     | Type     | Use      |
|----------|----------|----------|
| my_project  | Directory, Django App | Main Django App |
| users  | Directory, Django App | handles all user related processes |
| profiles  | Directory, Django App  | handles all profile related processes|
| api  | Directory, Django App  | handles all API processes  |
| requirements  | Text  | Snapshot of all modules used  |
| staticfiles  | Directory  | holds files such as css, js and images  |
| templates  | Directory  | holds all HTML files  |
| manage  | Python  | holds the main() function, starts the web app  |

Both profiles and api apps have a utility file, instead of thos apps having its own views/pages, the users holds all the views and pages, and it uses the utility functions to handle profile or api use.

### Models / App

Below shows a table of each model, its attributes, keys and features.

#### Users

Uses the Django based User model to handle login, registration, authentication and logout, with its pre defined model and utilitys.

| Attribute | Type |
|----------|----------|
| Username | String  |
| Email  | String  | 
| Password1 | Hash  | 
| Password2  | Hash |


#### Profiles

| Attribute | Type | Settings |
|----------|----------|----------|
| user  | Foreign Key  | FK to User, delon_delete=models.CASCADE |
| job_title  | String  | max_length=100  |
| min_salary | Integer  | null=True, blank=True  |
| is_full_time  | Boolean  | default=True  |
| city  | String  | max_length=100  |
| active  | Boolen  | blank=True  |

`active`: This attribute is to hold which profile is selected, only 1 profile can be active for every user, implementing it like this would make so if the user refreshes or logs out, on return the profile that is selected will be the last used one. This attribute also helps when determining which profile to apply certain thinds like edit, delete, job search etc.. These utilitys will apply to the onlyactive profile

The profiles app holds a utils.py file which holds all functions to interact with the model, For example:

```python
def activate_profile_for_user(user, profile_id):
    """
    Activate a specific profile for a user and deactivate all others.

    :param user: The user who owns the profiles.
    :param profile_id: The ID of the profile to activate.
    :raises Profile.DoesNotExist: If the profile does not exist or does not belong to the user.
    :return: The activated Profile object.
    """
    make_all_profiles_inactive(user)  # Deactivate all other profiles

    profile = Profile.objects.get(id=profile_id, user=user)  # Activate the selected profile
    profile.active = True
    profile.save()
    return profile
```

This function makes a given profile active, whilst making all other profiles inactive (active = false)


#### JobSearchHistory

| Attribute       | Type         | Settings                                    |
|------------------|--------------|--------------------------------------------|
| profile         | Foreign Key  | FK to Profile, on_delete=models.CASCADE, related_name='history' |
| job_title       | String       | max_length=255                             |
| redirect_url    | URLField     | URL to the job posting                     |
| description     | Text         | Description of the job                     |
| company_name    | String       | max_length=255, null=True, blank=True      |
| location        | String       | max_length=255, default="N/A"              |
| salary_min      | Integer      | null=True, blank=True                      |
| salary_max      | Integer      | null=True, blank=True                      |
| created_at      | DateTime     | auto_now_add=True                          |

Holds each job result ever searched for each profile, holds utilitys to make sure there are no duplicates based on the description.


#### API

This app does not hold a model, but has a utils.py to handle all API processes. An example of a function in utils:

```python
def search_jobs(profile):
    """
    Search for jobs using the Adzuna API based on a Profile's attributes.

    :param profile: A Profile instance with fields like job_title, city, min_salary, and is_full_time
    :return: JSON response from the Adzuna API containing job listings
    :raises ValueError: If API credentials are missing
    :raises HTTPError: If the API request fails
    """
    if not ADZUNA_API_KEY or not ADZUNA_APP_ID:
        raise ValueError("API key or App ID is missing. Please set them in env.py.")

    # Construct the request URL
    url = (
        f"https://api.adzuna.com/v1/api/jobs/gb/search/1?"
        f"app_id={ADZUNA_APP_ID}&app_key={ADZUNA_API_KEY}"
        f"&results_per_page={RESULTS_PER_REQUEST}"
        f"&what={profile.job_title.replace(' ', '%20')}"
        f"&where={profile.city}"
        f"&salary_min={profile.min_salary}"
    )

    # Add full-time or part-time preference
    if profile.is_full_time:
        url += "&full_time=1"
    else:
        url += "&part_time=1"

    url += "&content-type=application/json"

    # Make the API request
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP responses

    return response.json()
```

functions does a API request using a given profiles parameters, then return results in JSON form.

#### Templates

Each page is extend of a `base.html` template. This makes it so much easier to make pages with the same features. For example, Nav bar and footer only implemented 1 time in the base, then all other pages get it by extending off it.

Each page can then change the title:

```html
<title>{% block title %}Job Search{% endblock %}</title>
```

And the main for its content:

```html
 <main>
      {% block content %}{% endblock %}
    </main>
```

Exmaple of how `login.html` is extending of base and changing the title:

```html
{% extends 'base.html' %}

{% block title %}Login{% endblock %}
```


## **Technologies Used**
### Languages and Frameworks
- **Python**: Used as the main programming language for backend logic and API integrations.
- **Django**: Framework used for managing views, URLs, models, and template rendering.
- **HTML**: Provides the structure of the web pages.
- **CSS**: Handles the styling and layout of the web pages, including responsiveness.
- **JavaScript JQuery**: Implements client-side interactivity.

### Development Tools
- **GitPod - Visual Studio Code**: IDE for writing, editing, and debugging code.
- **Git**: Version control system to track changes and manage collaboration.
- **GitHub**: Repository hosting platform for storing and sharing the project's codebase.

### Deployment
- **Heroku**: Used to deploy the live version of the project.
- **Gunicorn**: WSGI HTTP server for deploying the Django application on Heroku.

## **Testing**
### Code Validation
All code passed through its respective validators:
- `Python`: PEP8
- `HTML`: W3C
- `CSS`: W3C Jigsaw
- `JavaScript`: JSHint

## Manual Testing Table

| **Feature**                     | **Test Description**                                                                 | **Expected Outcome**                                                                                           | **Result** |
|----------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------|
| **Navigation**                  | Ensure all navigation links (Register, Login, Logout) are functional.               | Each link redirects to the correct page without errors.                                                       | PASS       |
| **Register**                    | Test registration with valid inputs.                                                | User account is created, and the user is redirected to the login page.                                        | PASS       |
|                                  | Test registration with invalid inputs (e.g., missing fields, invalid email).         | Error messages are displayed, and the user cannot proceed until the errors are resolved.                      | PASS       |
| **Login**                       | Test login with valid credentials.                                                  | User is redirected to the dashboard after successful login.                                                   | PASS       |
|                                  | Test login with invalid credentials.                                                | Error message "Invalid Login. Please try again" is displayed, and the user remains on the login page.         | PASS       |
| **Logout**                      | Test logout functionality.                                                          | User is redirected to the homepage, and the session is terminated.                                            | PASS       |
| **Dashboard**                   | Ensure active profiles are displayed correctly.                                     | The active profile is highlighted, and others remain inactive.                                                | PASS       |
|                                  | Test adding a profile.                                                              | New profile appears in the list, and the number of profiles updates accordingly. Cant add profile if 5 profile limit is reached                             | PASS       |
|                                  | Test editing a profile.                                                             | Changes to the profile (e.g., job title, salary) are saved and reflected immediately.                         | PASS       |
|                                  | Test deleting a profile.                                                            | Profile is removed, and the profiles count updates. Error shown if user tries to delete the last profile.     | PASS       |
| **Job Search**                  | Search with valid parameters (e.g., job title, city, salary).                       | Job results are displayed with relevant information (e.g., title, company, salary).                           | PASS       |
|                                  | Search with invalid parameters (e.g., empty fields, non-existent city).             | No results are displayed, and guidance is shown for improving search parameters.                              | PASS       |
| **Job History**                 | Ensure the history of job searches is displayed.                                    | Previously searched jobs appear in reverse chronological order.                                               | PASS       |
| **Popup Modals**                | Test "Add Profile" modal.                                                          | Modal opens and closes correctly, cannot interact with background elements, and new profile data is validated and saved.                                | PASS       |
|                                  | Test "Edit Profile" modal.                                                         | Modal opens and closes correctly, cannot interact with background elements, and edited profile data is saved.                                           | PASS       |
|                                  | Test "Delete Profile" modal.                                                       | Modal opens and prompts for confirmation cannot interact with background elements. Profile is deleted only after confirmation.                         | PASS       |
| **Accessibility**               | Test navigation using only the keyboard (tab, enter).                              | All interactive elements are accessible and can be activated without a mouse.                                 | PASS       |
|                                  | Test site responsiveness on various screen sizes.                                   | Layout adapts correctly for mobile, tablet, and desktop views.                                                | PASS       |
| **Error Handling**              | Test invalid inputs for all forms (e.g., blank fields, invalid formats).           | Error messages are displayed, and the user is unable to proceed until corrections are made.                   | PASS       |
| **Deployment**                  | Ensure the site is live and accessible via the deployed URL.                       | The website is accessible via the Heroku or GitHub-hosted URL.                                                | PASS       |
|                                  | Test all pages for load times and general performance.                              | All pages load within 2-3 seconds on average, with no missing resources.                                      | PASS       |
| **Database Integration**        | Test CRUD operations for profiles and job history.                                 | Profiles and history data are correctly stored, retrieved, updated, and deleted in the database.              | PASS       |
| **Validation**                  | Validate form fields for all scenarios (e.g., email format, required fields).       | Form submissions are only allowed with valid inputs; invalid inputs trigger descriptive error messages.        | PASS       |
| **Session Management**          | Test session expiry by staying idle after logging in.                              | User is logged out after a predefined session expiry time.                                                    | PASS       |
|                                  | Test session persistence by closing and reopening the browser.                      | User remains logged in if session is active; otherwise, the session ends.                            | PASS       |
| **API Integration**             | Test Adzuna API integration by searching for jobs.                                  | Relevant job results are returned from the API and displayed in the dashboard.                                | PASS       |


## Deployment

This section explains how the project was deployed and made accessible online, along with the steps to replicate the deployment process.

---

### **Hosting Platform**
The project is hosted on **Heroku**, which allows deploying Django applications with ease. GitHub was used for version control and as a source repository for the deployment.

---

### **Steps to Deploy on Heroku**

1. **Create a Heroku Account**
   - Visit [Heroku's website](https://www.heroku.com/) and create an account if you don’t already have one.

2. **Install Heroku CLI**
   - Download and install the Heroku Command Line Interface (CLI) from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

3. **Prepare the Django Project**
   - Add the required dependencies to `requirements.txt` by running:
     ```bash
     pip freeze > requirements.txt
     ```
   - Create a `Procfile` in the root directory to specify the application process type:
     ```plaintext
     web: gunicorn my_project.wsgi
     ```
   - Ensure `ALLOWED_HOSTS` in `settings.py` includes the Heroku app domain:
     ```python
     ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com']
     ```

4. **Initialize a New Heroku App**
   - Log in to Heroku using the CLI:
     ```bash
     heroku login -i
     ```
   - Create a new app:
     ```bash
     heroku create your-heroku-app-name
     ```

5. **Configure Heroku Environment Variables**
   - Set up configuration variables for the project using the Heroku dashboard or CLI:
     ```bash
     heroku config:set DEBUG=False
     heroku config:set SECRET_KEY='your-secret-key'
     heroku config:set DATABASE_URL='your-database-url'
     ```
   - Add any other environment variables needed (e.g., API keys).

6. **Connect to GitHub Repository**
   - In the Heroku dashboard:
     1. Go to the "Deploy" tab.
     2. Select "GitHub" as the deployment method.
     3. Search for your repository and connect it.

7. **Deploy the Application**
   - In the "Deploy" tab, enable automatic deploys from the `main` branch, or manually deploy by clicking "Deploy Branch."

8. **Verify Deployment**
   - After deployment, access the live site via the provided Heroku URL:
     ```plaintext
     https://your-heroku-app-name.herokuapp.com
     ```

---

### **Cloning the Repository Locally**

To work on the project locally, follow these steps:

1. **Clone the Repository**
   - Run the following command:
     ```bash
     git clone https://github.com/your-username/your-repository-name.git
     ```

2. **Set Up a Virtual Environment**
   - Navigate into the project directory and create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     # Windows
     venv\Scripts\activate
     
     # macOS/Linux
     source venv/bin/activate
     ```

3. **Install Dependencies**
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application Locally**
   - Apply migrations and start the development server:
     ```bash
     python manage.py migrate
     python manage.py runserver
     ```
   - Open `http://127.0.0.1:8000` in your browser to view the project locally.

---

### **PostgreSQL Integration**
- A PostgreSQL database was used for production. Heroku automatically provisions this database.
- The database URL is added to the `DATABASES` configuration in `settings.py` via an environment variable.

---

### **Final Verification**
Ensure the following are functional after deployment:
- Navigation links work as expected.
- User authentication (registration, login, logout) is seamless.
- Job search and history features retrieve data correctly.
- Responsive design works across all devices.

---

By following these steps, the application can be deployed and tested successfully on Heroku or any similar hosting platform.


## Credits

- All images used were generated from text descriptions with [DALL-E Open-AI](https://openai.com/index/dall-e-3/)
- Font is from [Google Fonts](https://fonts.google.com/)
- Feature Implementation guidance using [Chat GPT](https://openai.com/index/chatgpt/)
- Project setup using rescources at [Code Institute](https://codeinstitute.net/)








