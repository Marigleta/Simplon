# Marigleta
# 1 
SELECT rental_id, date_format(rental_date,"%W %M %e% %Y") AS 'Date_emprunt'
FROM rental
WHERE rental_date LIKE '2006%';

#2
SELECT datediff(return_date,rental_date) AS duree_location_jours
FROM rental;

#3 

SELECT date_format(rental_date,"%W %M %e% %Y") 
FROM rental 
WHERE rental_date LIKE ‘2005%’;

# 4
SELECT rental_id,  date_format(rental_date,"%W %M %e% %Y") AS rentalDate
FROM rental 
WHERE month(rental_date) < 4 and month(rental_date)< 5
ORDER BY rental_date ASC;

#5
SELECT film_id, title 
FROM film 
WHERE title NOT LIKE "le%"; 

# 6

SELECT title
FROM film 
where rating LIKE "PG-13" OR rating LIKE "NC-17";

# 7

SELECT category_id, name as nom_categorie
FROM category
WHERE name LIKE 'A%' OR name LIKE 'C%';

#8
SELECT LEFT(name,3) AS nom_categorie
FROM category;

#9





# JOINTURES

#1.
SELECT film.title,language.name
FROM film
JOIN language
ON film.language_id=language.language_id
LIMIT 10;

#Question 2

SELECT film.title,actor.first_name,
actor.last_name,film.release_year
FROM film
JOIN film_actor
ON film.film_id=film_actor.film_id
JOIN actor
ON film_actor.actor-id=actor.actor_id
WHERE film.release_year=2006
AND(actor.first_name='JENNIFER' AND
actor.last_name='DAVIS');

#Question 3

SELECT customer.first_name,
customer.last_name
FROM customer
JOIN rental
ON customer.customer_id=rental.customer_id
JOIN inventory
ON rental.inventory_id=inventory.inventory_id
JOIN film
ON film.film_id=inventory.film_id
WHERE film.title='ALABAMA DEVIL'

#QUESTION NR.4

SELECT film.film_id
FROM film
JOIN inventory
ON film.film_id = inventory.film_id
JOIN rental
ON inventory.inventory_id = rental.inventory_id
JOIN customer
ON rental.customer_id = customer.customer_id
JOIN address
ON customer.address_id = address.address_id
JOIN city
ON address.city_id=city.city_id
WHERE city="Woodridge"

# QUESTION NR.5 (à revoir forcement)

SELECT film MIN rental_duration GROUP
BY rental_duration HAVING MAX (rental_duration) < 5;


#6

SELECT film.title
FROM film
JOIN category
ON film.category_id=category.category_id
ORDER BY film.title

#7

SELECT film.title
WHERE rental_duration <=2
 





