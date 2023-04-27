# Student Organiztions for the CSXL

## Overview

Our feature focuses on displaying UNC organizations, displaying events associated with an organization, and in the next sprint, displaying members of an organization to those authorized to view those specific details.


### Our contributions are intended to primary serve a *student* of the University of North Carolina at Chapel Hill.

A student should be able to:

1. View organiztaions/ organiztion details associated with the University.
2. Have the ability to join or request to join a given organization.
3. View events/ event details associated with an organization.
4. Have the ability to go to events.
5. Sign into a session using their Onyen.
6. View their user profile.
7. Update their user profile.
8. Sign out of their session if they so desire.

A student should *not* be able to:

1. View other user profiles.
2. Edit organiztion detials.
4. Delete organizations.
5. Create organizaitons.
6. Edit event details.
7. Delete events.
8. Create events.


### Uses for an *ambassador*

An ambassador should be able to:

1. Do everything a student is able to do.
2. Search for users.
2. Checkin a user to the CSXL.
4. Edit organization detials.
5. Edit event details.


An ambassador should *not* be able to:

1. Edit an organizaiton's name.
2. Edit an event's name.
3. Change a user's role.
4. Delete an organization,
5. Delete an event.
6. Create an organization.
7. Create an event for an organizaiton.


### Uses for a *manager*

A manager should be able to:

1. Do everything an ambassador is able to do.
2. Edit an organization's name.
3. Edit an event's name.
4. Delete an organization.
5. Delete an event.

A manager should *not* be able to:

1. Access developer mode.


### Uses for an *admin*

An admin should be able to:

1. Do everything a manager is able to do.
2. Access developer mode to peer into the inner workings of the applicaiton.

An admin should *not* be able to do:

1. Nothing.  They should be able to do anything possible within the applicaiton.


## Implementation Notes

Our application includes entities for:

1. Events,
2. Organizations,
3. Permissions,
4. Users,
5. User roles,
6. The relationship between a user and an organizaiton,
7. The relationship between an organization and its events

### A further elaboration on the entities that we created and modified

An event entity is composed of fields representing:

1. An event id,
2. An event name,
3. An event desctiption,
4. An event time and date,
5. An event location,
6. An event image,
7. And an organiztion id relating it to an existing organiztion

An organization entity is composed of fields representing:

1. An organization id,
2. An organization name,
3. An organization overview,
4. An organization description,
5. An organization image,
6. And a list of users


### Interesting design choices we made

We chose to make event and organization names unique as we figured this would encourage creative organization/ event names and make it easier to find a specific organization/ event.  

We chose to order organization events in the order of soonest occuring first in order to make it easier for students to view upcoming events and be able to adjust and plan accordingly.  We think this is a more convienient choice rather than ordering alphabetically as it is more intuitive to the end user.


## Development Concerns

#### If a new developer wanted to start working on your feature, what kind of guidance or overview would you give them to get them started?
##### We would advise them to look over this very markdown file.

#### What files would you point them at?
##### We would point them to the test files, the api folder, and the services folder to grasp a primary understanding of the backend and the organization-create TS file in the frontend src folder to understand how the frontend communicates with the backend through the use of calling its service methods.

#### Is there anything special they would need to do to get started?
##### They would need to set up a development enviorment to work on and contribute to our feature.


## Future Work

With more time, our feature could be slightly expanded.  One idea is to add a way to filter and or sort organizations.