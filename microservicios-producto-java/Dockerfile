FROM openjdk:17-jdk-slim
ARG JAR_FILE=target/microservicios-producto-java-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} app_productos.jar
EXPOSE 8081
CMD ["java", "-jar", "app_productos.jar"]
