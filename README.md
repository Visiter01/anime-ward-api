# 🎌 Anime Ward API

A Flask-based RESTful API for managing your personal anime collection. Keep track of your favorite anime series, add new discoveries, and never forget what to watch next!

## ✨ Features  (check the umesh branch it got all hte files)

- **Random Anime Selection**: Get a random anime from your collection when you can't decide what to watch
- **Add New Anime**: Easily add new anime to your ward with links
- **View All Anime**: Browse your entire collection at once
- **Update Entries**: Modify anime names or links
- **Delete Entries**: Remove anime from your collection
- **MySQL Database**: Persistent storage for your anime collection

## 🚀 Prerequisites

Before running the Anime Ward API, make sure you have the following installed:

- **Python 3.7+**
- **Flask**
- **MySQL Server**
- **MySQL Connector for Python**

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Visiter01/anime-ward-api
   cd anime-ward-api
   ```

2. **Install required packages**
   ```bash
   pip install flask
   pip install mysql-connector-python
   ```

3. **Set up MySQL Database**
   - Create a new MySQL database
   - Update database connection settings in your Flask app
   - Create the anime table (schema provided below)

## 🗄️ Database Schema

Create the following table in your MySQL database:

```sql
CREATE TABLE anime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    link VARCHAR(500),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔧 Configuration

Update your Flask application with your MySQL database credentials:

```python
# Database configuration
DB_HOST = 'localhost'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'animeward'
```

## 🎯 API Endpoints

### 1. Get Random Anime
- **Endpoint**: `/get`
- **Method**: `GET`
- **Description**: Retrieves a random anime from your ward
- **Response**: JSON object with anime details

### 2. Add New Anime
- **Endpoint**: `/add`
- **Method**: `POST`
- **Description**: Adds a new anime to your collection
- **Required Parameters**:
  - `name`: Anime title
  - `link`: URL to anime (optional)
- **Response**: Success confirmation

### 3. Get All Anime
- **Endpoint**: `/getall`
- **Method**: `GET`
- **Description**: Retrieves all anime from your collection
- **Response**: JSON array of all anime entries

### 4. Delete Anime
- **Endpoint**: `/delete`
- **Method**: `DELETE`
- **Description**: Removes an anime from your ward
- **Required Parameters**:
  - `id`: Anime ID to delete
- **Response**: Deletion confirmation

### 5. Update Anime
- **Endpoint**: `/update`
- **Method**: `PUT`
- **Description**: Updates anime name or link
- **Required Parameters**:
  - `id`: Anime ID to update
  - `name`: New anime name (optional)
  - `link`: New anime link (optional)
- **Response**: Update confirmation

## 🚀 Running the Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Access the API**
   - Default URL: `http://localhost:5000`
   - Test endpoints using tools like Postman or curl

## 📝 Example Usage

### Adding a new anime:
```bash
curl -X POST http://localhost:5000/add \
  -H "Content-Type: application/json" \
  -d '{"name": "Attack on Titan", "link": "https://example.com/aot"}'
```

### Getting a random anime:
```bash
curl http://localhost:5000/get
```

### Getting all anime:
```bash
curl http://localhost:5000/getall
```

### Updating an anime:
```bash
curl -X PUT http://localhost:5000/update \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Shingeki no Kyojin", "link": "https://newlink.com"}'
```

### Deleting an anime:
```bash
curl -X DELETE http://localhost:5000/delete \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

## 🛠️ Troubleshooting

### Common Issues:

1. **MySQL Connection Error**
   - Verify MySQL server is running
   - Check database credentials
   - Ensure MySQL connector is installed

2. **Table Not Found**
   - Create the anime table using the provided schema
   - Verify database name is correct

3. **Port Already in Use**
   - Change the Flask port in your application
   - Kill the process using the port

## 📚 Dependencies

```txt
Flask==2.3.3
mysql-connector-python==8.1.0
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Anime Watching! 🎌✨**

*Keep your anime collection organized and never run out of great shows to watch!*
