# Pattern Jobs
Pattern Jobs is an intuitive platform designed to change the job value tool. The main goal of Pattern is to provide a user-friendly and efficient platform where users can set what kind of job they are looking for, search for roles based on personalized profiles, and watch their job application history. Pattern Jobs by the use of strong APIs, Pattern Jobs, is the one that takes the job-hunting process the farthest, making it simple both for users looking for new opportunities and for those who are just passively browsing.

Live site can be found [Here](https://deploma4-9a881a09cb04.herokuapp.com/)

## **Table of Content**
glossary

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

![Colour palette used in website: black, dark grey, white, jungle green and yellow](/README_assets/doc_image_1.png)
- Black and white for background to text contrast.
- Dark gray for container backgrounds, like the dashbaord, to distinguish itself from the background but still be seamless.
- Jungle green and yellow as accent colours to provide unique style, and to distimguish different elements from eachother.


## **Features Walkthrough**
Below is a showcase of the website in its features, design process and screen resonsiveness.
### **Home Page**
#### General
![snippet of home page](/README_assets/doc_image_2.png)
- Home constists of a Nav bar, hero segment, info segment and a footer
- Nav bar and footer are only 2 elements which are present and the same on all pages of this site.

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
def get_profile_history(profile_id):
    """
    Retrieve the job search history for a specific profile.

    :param profile_id: ID of the Profile
    :return: Queryset of JobSearchHistory entries, ordered from newest to oldest
    """
    profile = Profile.objects.get(id=profile_id)
    return profile.history.all().order_by("-id")
```

This function will return all History job results for a given profile in reverse order.


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


#### Adzuna API

This app does not hold a model, but has a utils.py to handle all API processes. An example of a function in utils:

```python
```





