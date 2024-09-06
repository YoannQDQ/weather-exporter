FROM golang:1.21-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o weather-exporter .



FROM alpine:latest
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app

COPY --from=builder /app/weather-exporter .

EXPOSE 8080
USER app
CMD ["./weather-exporter"]
