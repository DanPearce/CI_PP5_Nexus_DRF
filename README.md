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