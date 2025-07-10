# Use the official nginx base image
FROM nginx:alpine

# Remove the default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy your website files to the nginx folder
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx (default CMD works fine)
