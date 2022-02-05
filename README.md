
# KafkaMongo
Docker-compose starting Kafka, Zookeeper, Mongodb, Producer, Consumer and API server<br>
**Basic Flow**:<br>
Producer -> Kafka -> Consumer -> API Server -> Mongodb

## Installation
1. Clone the repo
   ```sh
   git clone https://github.com/YakirShriker/KafkaMongo.git
   ```
2. use Docker-compose to start all services 
   ```sh
   docker-compose start -d
   ```
3. In order see all application logs
   ```sh
    docker-compose logs --tail=0 --follow
   ```

## Frontend UI
  ```
  http://127.0.0.1:5000/
  ```
  <br>
  1."Buy Now!" will produce object that will later be handled by the consumer and sent to mongodb via API server<br>
  2. Use frontend to query the API server directrly by specifing userid or query all. API server will return data from mongodb.

## Backend API Server
  ```
  http://127.0.0.1:5100/
  ```

   **Post to API Server**<br>
      ```sh
         curl --header "Content-Type: application/json" --request POST  --data '{"username":"xyz","userid":"1","price":"333"}' http://127.0.0.1:5100/buyrequest/
      ```
      
   **Query specific userid from API Server**<br>
      ```sh
      curl -i -X GET http://127.0.0.1:5100/query/1
      ```
      
   **Get all**<br>
    ```
    curl -i -X GET http://127.0.0.1:5100/query
    ```
