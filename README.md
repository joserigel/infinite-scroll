# Infinite Scroll
This project is done to explore video econding (H246) and also mimic the social media feature of infinite scrolling 
of videos with minimal lag.

### Backend
To run the backend run
```
mvn spring-boot:run
```
within the backend folder.

### Dependencies
This project requires a Redis instance. You can run a local one by running
```
docker run -d -p 6379:6379 redis:latest
```