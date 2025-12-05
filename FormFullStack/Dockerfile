FROM gradle:8.5-jdk21 AS builder

WORKDIR /app

COPY settings.gradle.kts ./
COPY gradlew .
COPY gradle ./gradle
COPY build.gradle.kts ./
COPY src ./src

RUN gradle clean build -x test

FROM amazoncorretto:21-alpine AS runtime

WORKDIR /app
COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 9805
ENTRYPOINT ["java", "-jar", "app.jar"]
