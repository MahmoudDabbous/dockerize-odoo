FROM odoo:latest

# Copy the custom addons
COPY ./addons /mnt/extra-addons

# Workdir
WORKDIR /mnt/extra-addons
