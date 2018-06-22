
# Scaleable ToDo Application

## The Outline

As an arbitrairy goal I would like the application to be able to handle close to a million users.

Python was chosen to help focus on structure over code. 

Actors
- Users

Actions
- Login
- CRUD Todo item


Action technical details
- Signup: send to database 
- On Login: load todo items into a cache, referencing session token
- On CUD: update memory and check if update is possible. If update fails... throw error? :(
- After memory update: start timer, if X time passed AND no new update: update disk
- On Logout: update disk