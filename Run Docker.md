sudo docker run -it --rm \
-u root \
-e GUACD_HOSTNAME=127.0.0.1 \
-e GUACD_PORT=4822 \
-e POSTGRES_DATABASE=guacamole_db \
-e POSTGRES_USER=guacamole_user \
-e POSTGRES_PASSWORD=ChooseYourOwnPasswordHere1234 \
-e POSTGRES_HOSTNAME=127.0.0.1 \
-e POSTGRES_PORT=5432 \
-p 8080:8080 -v $(pwd)/guacamole/target/guacamole-1.5.0.war:/root/tomcat/webapps/guacamole.war guacamole-client-build
