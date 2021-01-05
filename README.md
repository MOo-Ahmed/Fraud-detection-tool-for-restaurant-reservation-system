# Fraud detection tool for restaurant reservation system
 
This tool is meant to help another system (Restaurant reservation system) to detect the fraudulent reservations
It uses data mining techniques such as classification to judge various reservations as safe or fake
This should help the system identify fraudulent users and ban them according to system policy

How does it judge a reservation ?
The validation of a reservation should have 2 phases (restaurant, user)  & (restaurant, restaurant)
The first phase is concerned with the location of a user and the location of the restaurant where the reservation takes place
The second phase is concerened with the location of
  - The restaurant of the last reservation
  - The restaurant of the current reservation
For phase 1, this is how it works : 
  if the expected time is <= 15 minutes   -> safe	
  if distance >= 800 kilometers	and if actual time / expected time >= 0.7 	-> safe
  if the expected time is <= 120 minutes and if actual time / expected time >= 0.5 	-> safe
  if 300  <= distance < 800 and expected time > 120 minutes and if actual time / standard time >= 0.5   -> safe		
  if the expected time is >= 120 & distance < 300	and if actual time / standard time >= 0.5 	-> safe
  otherwise  -> fake
  
For phase 2, this is how it works : 
  no new reservation take place before one hour from the other 		
  no new reservation take place if expected time between the two places  > 150 minutes		
  Otherwise, this is a fraud		
