# Use ubuntu:20.04 as the base image
FROM ubuntu:20.04

# Provide the maintainer's information
LABEL maintainer="xianglong lin <s4579143@student.uq.edu.au>"

# Set the timezone and PHP version variables
ENV PHPVER=8.2
ENV TZ=Asia/Shanghai

# Install required packages like nginx, php, and php-fpm
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y nginx php${PHPVER}-fpm && \
    apt-get clean

# Copy Nginx configuration file
COPY src/nginx.ini /etc/nginx/sites-available/default

# Copy test page
COPY . /var/www/html/

# Set the working directory and exposed ports
WORKDIR /var/www/html
EXPOSE 80



# Set the entry point to start nginx and php-fpm
ENTRYPOINT ["sh", "-c", "service php${PHPVER}-fpm start && nginx -g 'daemon off;'"]

