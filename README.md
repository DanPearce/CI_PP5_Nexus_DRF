# Nexus DRF API
Developed by, [Dan Pearce](https://danpearce.software/)

[View the live application](https://ci-pp5-nexus-drf-danpearce.herokuapp.com/)

The Nexus DRF API has been built for the purposes of providing data to the Nexus application. The API project has been built using the Django REST Framework.

[View the live Nexus application here](https://ci-pp5-nexus-danpearce.herokuapp.com/)

[View the Nexus GitHub page here](https://github.com/DanPearce/CI_PP5_Nexus)

## Contents
1. [User Stories](#user-stories)
2. [Database and Models](#database-and-models)
3. [Technologies](#technologies)
4. [Validation and Testing](#validation-and-testing)
5. [Credits](#credits)
6. [Acknowlegements](#acknowlegements)

## User Stories
The DRF API has only one user story as the live API is only used for administration purposes.

1. USER STORY 3: User Authentication - Admin Moderation
  - As an Owner, I can log into the admin console, so that I can moderate the content on the site.

## Database & Models
### Database
This project was built using a relational database allowing us to easily link aspects of the site with others.

During development, I used [DB SQLite which](https://www.sqlite.org/) which is the default database to use for Django - and for production [ElephantSQL](https://www.elephantsql.com/) has been used and all data migrated during the deployment.

<details><summary>Diagram</summary>
<img src="docs/nexus_drf/nexus_drf_database.png">
</details>

### Models

#### Users
The User Model comes installed with the Django AllAuth Library and is used to connect with various features of the application
- Has a One to One Relationshop with Profiles; owner field.
- Has a ForeignKey relationship with Followers; owner and followed feilds.
- Has a ForeignKey relationship with Posts; owner field.
- Has a ForeignKey relationship with Comments; owner field.
- Has a ForeignKey relationship with Likes; owner field.

#### Profiles
- Fields (owner, name, about, created_on, updated_on, image)
- Has a One to One relationship with User, id.

#### Posts
- Fields (owner, title, body, created_on, updated_on, image)
- Has a ForeignKey relationship with Comments, post and Like, post.

#### Followers
- Fields (owner, followed, created_on)
- Has a ForeignKey relationship with User, id.

#### Comments
- Fields (owner, post, body, created_on, updated_on)
- Has a ForeignKey relationship with User, id and Posts, id.

#### Likes
- Fields (owner, post, created_on)
- Has a ForeignKey relationship with User, id and Posts, id.

## Technologies
### Languages
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

### Libraries, Frameworks and Other Technologies
- [Django](https://www.djangoproject.com) - This side of the project has been created using django .
- [Cloudinary](https://cloudinary.com/) - Used to host the images used on the site.
- [Git](https://git-scm.com/) - Used to implement version control within the project.
- [GitHub](https://github.com/) Used to host my code.
- [GitPod](https://www.gitpod.io/) Used to build my code online.
- [VS Code](https://code.visualstudio.com) - Used occasionally to build the code offline.
- [Heroku](https://dashboard.heroku.com/) - Used to host the live version of the site.
- [Psycopg2](https://www.psycopg.org/docs/) Used to create the database on the development version of the site.
- [ElephantSQL](https://www.elephantsql.com/) - Used to host the database for the live site.
- [DB Diagram.io](https://dbdiagram.io/) - Used to create the diagrams used for the models.
- [PyCodeStyle](https://pypi.org/project/pycodestyle/) - Used to validate the Python code.
- [Python](https://www.python.org/) - Code written in python.
- [Django REST Framework](https://www.django-rest-framework.org/) used for the creation of the API.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) used for user authenticaion/creation.

## Validation and Testing
### PyCodeStyle Valdidation
All Python Code has been checked using the [PyCodeStyle](https://pypi.org/project/pycodestyle/) library. All code has been returned with no errors.

<details><summary>All .py files</summary>
<img src="docs/nexus_drf/nexus_drf_validation.png">
</details>

### Testing 
#### Manual Testing
As an Owner, I can log into the admin console, so that I can moderate the content on the site.

| **Test** | **User Action** | **Desired Outcome** | **Actual Outcome** |
|------------------|-----------------|---------------------|--------------------|
| User | Create, edit and delete | Admin is able to create, edit and delete a new user (Which makes a user profile). | Works as intended. |
|<details><summary>User Create</summary><img src="docs/testing/testing_user_1.png"></details> <details><summary>User Create</summary><img src="docs/testing/testing_user_2.png"></details> | | | |

| **Test** | **User Action** | **Desired Outcome** | **Actual Outcome** |
|------------------|-----------------|---------------------|--------------------|
| User | Change user permissions | Admin is able to edit permissions for a user. | Works as intended. |
| <details><summary>User Permissions</summary><img src="docs/testing/testing_permissons.png"></details> | | | |

| **Test** | **User Action** | **Desired Outcome** | **Actual Outcome** |
|------------------|-----------------|---------------------|--------------------|
| Profiles | Create and delete | Admin is able to create and delete a Profile. | Works as intended. |
| <details><summary>Profiles Edit</summary><img src="docs/testing/testing_edit_profile.png"></details> <details><summary>Profiles Delete</summary><img src="docs/testing/testing_delete_profile_1.png"></details> <details><summary>Profiles Delete</summary><img src="docs/testing/testing_delete_profile_2.png"></details> <details><summary>Profiles Delete</summary><img src="docs/testing/testing_delete_profile_3.png"></details> | | | |

| **Test** | **User Action** | **Desired Outcome** | **Actual Outcome** |
|------------------|-----------------|---------------------|--------------------|
| Posts | Create, edit and delete | Admin is able to create, edit and delete a post. | Works as intended. |
| <details><summary>Posts Create</summary><img src="docs/testing/testing_add_post.png"></details> <details><summary>Posts Edit</summary><img src="docs/testing/testing_edit_post.png"></details> <details><summary>Posts Delete</summary><img src="docs/testing/testing_deleting_post_1.png"></details> <details><summary>Posts Delete</summary><img src="docs/testing/testing_deleting_post_2.png"></details> <details><summary>Posts Delete</summary><img src="docs/testing/testing_deleting_post_3.png"></details> | | | |

| **Test** | **User Action** | **Desired Outcome** | **Actual Outcome** |
|------------------|-----------------|---------------------|--------------------|
| Comments | Create and delete | Admin is able to create, edit and delete a comment. | Works as intended. |
| <details><summary>Comments Create</summary><img src="docs/testing/testing_add_comment_1.png"></details> <details><summary>Comments Create</summary><img src="docs/testing/testing_add_comment_2.png"></details> <details><summary>Comments Delete</summary><img src="docs/testing/testing_delete_comment_1.png"></details> <details><summary>Comments Delete</summary><img src="docs/testing/testing_delete_comment_2.png"></details> <details><summary>Comments Delete</summary><img src="docs/testing/testing_delete_comment_3.png"></details> | | | |

| **Test** | **User Action** | **Desired Outcome** | **Actual Outcome** |
|------------------|-----------------|---------------------|--------------------|
| Likes | Create and delete | Admin is able to create and delete a like. | Works as intended. |
| <details><summary>Likes Create</summary><img src="docs/testing/testing_add_like_1.png"></details> <details><summary>Likes Create</summary><img src="docs/testing/testing_add_like_2.png"></details> <details><summary>Likes Delete</summary><img src="docs/testing/testing_delete_comment_1.png"></details><details><summary>Likes Delete</summary><img src="docs/testing/testing_delete_comment_2.png"></details><details><summary>Likes Delete</summary><img src="docs/testing/testing_delete_comment_3.png"></details> | | | |

| **Test** | **User Action** | **Desired Outcome** | **Actual Outcome** |
|------------------|-----------------|---------------------|--------------------|
| Followers | Create and delete | Admin is able to create delete a new follower. | Works as intended. |
| <details><summary>Followers Create</summary><img src="docs/testing/testing_add_follower_1.png"></details> <details><summary>Followers Create</summary><img src="docs/testing/testing_add_follower_2.png"></details><details><summary>Followers Delete</summary><img src="docs/testing/testing_delete_follower_1.png"></details> <details><summary>Followers Delete</summary><img src="docs/testing/testing_delete_follower_2.png"></details><details><summary>Followers Delete</summary><img src="docs/testing/testing_delete_follower_3.png"></details> | | | |

## Credits
### Code
I learnt how to create this project using the code from my course with Code Institute. 
[Moments DRF](https://github.com/Code-Institute-Solutions/drf-api)

## Acknowledgements
As always there are some people I would especially like to thank for their continued support throughout my coding journey.
- Thank you to my mentor, Mo Shami, for providing me quality information in the past months.
- Thank you to my partner, Harry for allowing me to have the time to continue my efforts.
- Thank you to you, for taking the time to look at my work!

#### [Back to Top](#contents)