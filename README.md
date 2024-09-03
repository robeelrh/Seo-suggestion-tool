## Getting Started

## Prerequisites

Make sure you have the following software installed on your machine:

- Node.js and npm
- PHP (>=7.4)
- Composer
- MySQL or another database supported by Laravel

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/robeelrh/Seo-suggestion-tool.git
cd Seo-suggestion-tool
```

#### 2. Install Vue.js dependencies

Navigate to the `seo-tracker-frontend` directory and run the following command:

```bash
npm install
```

#### 3. Install Laravel dependencies

Navigate to the `laravel-backend` directory and run the following command:

```bash
composer install
```

#### 4. Set up the environment

Copy the `.env.example` file to `.env` in the `backend` directory and update the necessary environment variables:

```bash
cp .env.example .env
```

Generate the application key:

```bash
php artisan key:generate
```

#### 5. Migrate the database

Make sure your database is set up, then run the migrations:

```bash
php artisan migrate
```

#### 6. Serve the application

To start the Laravel development server, run:

```bash
php artisan serve
```

### Running Cron Jobs

To start the queue worker for processing jobs, run the following command:

```bash
php artisan queue:work --timeout=0
```
