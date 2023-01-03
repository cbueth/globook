# Globook

Repository for the Globook project holding the source code for the web application and
the Globook API.

## Idea

The idea of this project is a place to track hitchhiking books - books that are
passed from person to person. Knowing where a book has travelled might be motivating
for the reader to keep reading and passing it on.

When a book starts its journey, the donator writes a welcoming message with a short
explanation of Globook into the first page of the book. This will include the unique
identifier and the secret. The donator can also write a short message into the book.
Online, the donator registers the book with general information about the book, like
title and author. The donator can also register a location where the book is currently
located.

Identifications are made using a unique identifier and a secret. The unique identifier
is used to identify the book, the secret is used to make sure only a person who
has the book can register a new location.

## Central functionality

- Overview Map
  - Display all books on a map with current location.
  - Click on a book to display the book view.
- Book View
  - Display all catches for a book.
  - Click on a location to display the catch details.
  - Add a new catch.
- Search
  - Search for books by title, author, or unique identifier.
  - Display the search results on a map.
- Add a new book
  - Register a new book with title, author, unique identifier, and secret.
  - Show an example of a welcome message to be written into the book.
- Location Picker
  - Select a location on a map and radius for security.

## Terminology

- **Book**: A book that is registered with Globook.
  - **Title**: The title of the book.
  - **Author**: The author of the book.
  - **Message**: A message written by the donator to be displayed online.
  - **Unique identifier**: A unique identifier for the book.
  - **Secret**: A secret for the book, used as a password for registering.
- **Donator**: The person who donates a book to Globook.
- **Reader**: The person who reads a book and passes it on to another person.
- **User**: Either a donator or a reader. Collect IP addresses and other information
  about the user? No registration wanted.
- **Catch**: A catch is the act of registering a new location for a book.
  - **Location**: The location of the catch
  - **Radius**: The radius of the location. No exact location wanted.
  - **Message**: A message written by the reader.
  - **Date**: The date of the catch.
- **Logbook**: Database table holding all catches for all books.

## Web application

The application is a one-page web application with Flask and Vue that allows a user to
register a location of a physical object, especially a book, by clicking on a leaflet
map and entering the unique identifier and secret.

## Globook API

The Globook API is a RESTful API that provides access to the Globook database. The API
is written in Python using the Flask framework.


### Further ideas

- Don't show all books on the overview map. 
  - Closest books to the user's location.
  - Books that have been caught recently.
  - Books that have been caught far away.
  - Books that have travelled a long distance.
  - Random books.

### Not TODO list

Feel free to implement any of these ideas.

- [ ] Registration of users.
- [ ] Email notification system for new catches of a book.
- [ ] Add a QR code to the book, linking to the book's page on Globook. Who would 
  want to glue a QR code into a book? Certainly not me.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE
file for more information.