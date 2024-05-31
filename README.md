# Containerized Odoo App - By Mahmoud Dabbous

## Get Started
  
- ``` docker compose up --build -d ```

## Usage

- Enter the container shell ``` docker compose exec web bash ```
- Direct command ``` docker compose exec web <your-command> ```
  - Note: you are at the /mnt/extra-addons directory
  - example: ``` docker compose exec web odoo scaffold example-module ```
