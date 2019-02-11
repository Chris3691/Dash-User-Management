# Dash-Flask-Users

A template Dash App with basic user authentication, user permissions (admin & non-admin), and user management (create new user & update password).

The template has the following views:

`login.py` - User login page, displayed it a user tries to access any page and is not currently logged in
`page1.py` - Empty template page for your own Dash layout
`page2.py` - Another empty template page
`profile.py` - For users to update their own password
`user_admin.py` - A page for admin users only, with ability to create new users and view existing users
`404.py` - Simple 404 error message to catch requests for non-existent pages





# Database Setup

Default database setup is MySQL and the required table can be setup using the table_create_statement in /db.

The database username, password, and table name need be entered in `con` paramenter of `config.txt`.

Other databases can be used - refer to SQLAlchemy for required connection statement and update the `con` parameter of `config.txt`.
