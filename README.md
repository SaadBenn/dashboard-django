## Your Mission
Hey Full-Stack developer. Welcome. Your mission, should you choose to accept it, is to carve out 2 hours and create a new feature in the single page app provided here.

> Hey this is important! We hope you can spend about two hours on this project. If you can finish faster -- great! If not, limit yourself and don't spend much longer than 2 hours.

## Your Task

Build a new dashboard card showing revenue by sales rep. Users can be sales reps, managers, or directors and the card should display a breakdown for each user based on the sales attributed to all sales reps under them. The database is provided for you and the relevant tables are described in `backend/main/models.py`.

Simplifications:
- each tab in the app is hard coded in `frontend/src/App.jsx` to request a specific user, that's whose "dashboard" is being displayed
- the backend endpoint doesn't take a date so you can just return the data for the current date
- there is no authentication

We've provided a lot of code for you to get up and running fast! This is a feature from our existing codebase, just packaged in a simplified manner, so treat this like a real-world task. You can add other packages/helpers but the ones provided are good enough to get the job done.

## Getting Started
There are three files you need to change to complete this task (although feel free to modify anything else as well):
- `frontend/src/Containers/RevenueGraph.jsx`
- `frontend/src/Components/RevenueGraph.jsx`
- `backend/main/views.py`

The app is dockerized so you can reference the `Dockerfile`s and `docker-compose.yml` for any configuration questions (or just run the app with `docker-compose up --build`).

If you're new to React or Django, here are some resources to help bring you up to speed:
- Django ORM: [Models](https://docs.djangoproject.com/en/3.0/topics/db/models/) and [QuerySets](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)
- [Getting Started with React](https://reactjs.org/docs/hello-world.html) and [Presentational vs Container components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)

Please don't hesitate to reach out if you have any questions whatsoever.

## Example

![design spec](example.png)
