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