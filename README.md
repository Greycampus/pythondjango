# Installation of Python, Django and PostgreSQL
This tutorial will guide you through the installation of Python , installing Django and setting up PostgreSQL as database for Django.

**complete guide** *go to installation folder*

**only python installation** *go to python folder*

**only django installation** *go to django folder*

**only setting PostgreSQl** *go to postgresql folder*

**only server deployment** *go to server folder*

---
## Table of Contents

---
### Part one : Getting Started
---

  - Introdution to Django
  - The Basics of Python
    - The Introdution and Setup
    - Variables and names
    - Strings and Text
    - Conditions and loops
    - Functions and files
  - The Basics of Dynamic webpages
    - What is Dynamic webpages
    - How dynamic content is generated
    - Client side vs Server side scripting.
    - Case Study : *Instagram*
  - The Basics of PostgreSQL
    - Introduction to PostgreSQL
    - Databases: making new databases,tables and Users
    - Data Control: Altering tables;using spreadsheets and flatfiles for data loading
  - Configuring deployment server and bridge modules
    - choosing the server and bridge modules
    - Configuring Nginx
    - Configuring Gunicorn
  - **Exercise:** About basics
    - A test on python variables, loops, function calls
    - A test on PostgreSQL queries.

---
### Part two : beginning development
---

 - Django Template system
    - Template system basics
    - Built-in backends
    - Custom backends
    - Debug integration for custom backends
 - Interacting with Database : Models
    - Using Django with database:with PostgreSQL,MySQL,sqlite3
    - Using Django without database
    - Lazy Evaluation and Advances Query tools
    - Transactions and Django ORM transaction resources
 - The Django Admin page
    - Overview
    - *ModelAdmin* objects and options
    - the *register* decorator
    - Discovery of Admin files
    - Custom Template options
    - *ModelAdmin* methods and asset definitions
    - *Inline ModelAdmin* objects and options
    - *Many-to-Many* models and *Many-to-Many* intermediate models
    - Overriding vs replacing admin templates
    - AdminSite Objects and methods
    - Adding views and passord reset feature to admin page
 - Form processing
    - HTML forms,GET and POST
    - Django's role in forms
    - forms in django
      - The Django *Form* class
      - Instantiating, processing and rendering forms
    - Building forms
    - More about Django *Form* class
 - **Exercise:** Connect to different databases and making schemas with normalization , make a simple form

---
### Part three : Becoming a Novice developer
---

 - Advanced views and URLconfs
    - Streamlining function imports
    - Using multiple view prefixes
    - Special casing URLs in Debug mode
    - Passing extra options to view functions
    - Using Default view arguments and special casing views
    - Determining What the URLconf Searches Against
 - Generic Views
    - Class based views
    - Built-in class based generic views
    - Subclassing generic views
    - Generic view of objects
    - Viewing subsets of objects
    - Dynamic filtering
 - generating non-HTML Content
    - Views and MIME types
    - Producing CSVs and PDFS
    - The Syndication feed and the Sitemap frameworks
 - Session, Users and Registration
    - Getting and Setting cookies
    - The Django Session framework
      - Enabling sessions
      - using sessions in views
      - Setting Test cookies
      - Other session settings
    - Enabling authentication support
      - Using Users
      - logging in and out
      - limiting access
 - Caching
    - Django's cache framework
    - setting up the cache
      - Memcached
      - Database Caching
      - Filesystem Caching
      - Local-memory Caching
    - Using custom cache backend
    - Cache arguments
    - The per-site cache
    - The per-view cache
    - Template fragment  Caching
    - The low level cache API
    - Cache key prefixing and versioning
    - Cache key tranformation and warnings
    - Downstream Caches
 - **Exercise:** Make a blog with user commenting and login

---
### Part four : The Django Master
---

 - Other Contributed subframeworks(Standard library, usage optimizations)
    - Django Standard library
    - Reusing Data on multiple sites
    - Associating content with single sites
    - CurrentSiteManager
    - Flatpages
    - Redirects
    - CSRF Protection
 - Best practices
    - class based views
    - templates
 - **Exercise:** Build a online shopping platform
