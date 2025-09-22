# CineBook
A web-based cinema e-booking system. 


## Project Overview

CineBook is a web-based cinema e-booking system. The application will allow users to browse and search for movies, view detailed movie information, and book tickets and seats online. Registered users will have a profile and the ability to view their order history, while administrators will have full control over movie information, ticket prices, and user management. The system is being developed using an incremental hybrid model, combining aspects of both waterfall and agile methodologies to ensure an early working version of the system.

## High-Level System Requirements

### For Web Users & Customers
* **Registration and Profile Management:** Users can register and manage their profile and password, although their email address cannot be changed. Registration is verified by a system-generated code sent to the user's email.
* **Movie Browsing and Search:** Users can browse "Now playing" and "Coming soon" movies, and search by category, title, or show date.
* **Online Booking:** The system provides a booking facility for all users. Users can select a movie, show date, show time, and the number of tickets by age category (Child, Adult, Senior). They can also select their seats from a graphical view of the hall.
* **Secure Payment:** The system must provide a secure checkout facility and allow customers to use promotion codes. The total price is the sum of ticket prices, sales tax, and online fees.
* **Order History:** Customers must be able to view their order history.
* **Ticket Cancellation:** Users can return tickets and receive a refund if they cancel up to 60 minutes before the show time.

### For System Administrators
* **Movie and Pricing Management:** Administrators can add, update, and delete movie information, including movie title, category, cast, director, synopsis, and show dates and times. They can also update ticket prices, online booking fees, and promotions.
* **User Management:** Administrators can add, delete, or update member information, and suspend member accounts. They can also send email promotions to subscribed users.
* **Real-Time Statistics:** The system will allow administrators to view real-time statistics on bookings, sales, running movies, and registered users.

## Technology Stack

* **Backend:** Django (Python)
* **Frontend:** Next.js
* **Database:** PostgreSQL
* **Containerization:** Docker