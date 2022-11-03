-- task 9
-- cities by state
SELECT cities.id, cities.name, states.id FROM cities
INNER JOIN states AS st
ON cities.state_id = st.id;