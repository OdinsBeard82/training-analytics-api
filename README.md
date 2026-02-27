1️⃣ Project Overview

# Inventory API

A Node.js/Express/Sequelize API for managing inventory, categories, and users.  
Uses PostgreSQL for data storage and includes JWT-based authentication for protected routes.

2️⃣ Current Progress

## Current Progress

### Database

- PostgreSQL database `inventory_api_dev` set up.
- Tables created via Sequelize migrations:
  - `Categories`
  - `Items`
  - `Users` (migration in progress)
  
### Users Migration Status

- Step 1: `id` column with UUID primary key ✅
- Step 2: `username` column (NOT NULL, UNIQUE) ✅
- Step 3: `password_hash` column (NOT NULL) ✅
- Step 4: `createdAt` and `updatedAt` timestamps ✅

3️⃣ Next Steps

## Next Steps

- Run the Users migration to create the table in PostgreSQL
- Implement `/api/users/register` endpoint
- Implement `/api/users/login` endpoint with JWT authentication
- Implement CRUD routes for `Items` and `Categories`

  4️⃣ Optional Notes

## Notes

- Following a **section-by-section commit strategy** to demonstrate incremental understanding of migrations and database design.
- All columns and constraints carefully planned for data integrity and real-world best practices.
