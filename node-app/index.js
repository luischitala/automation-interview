require('dotenv').config();
const express = require('express');
const { Sequelize, DataTypes } = require('sequelize');

const app = express();

// Get database credentials from environment variables
const dbHost = process.env.DB_HOST;
const dbPort = process.env.DB_PORT;
const dbName = process.env.DB_NAME;
const dbUser = process.env.DB_USER;
const dbPassword = process.env.DB_PASSWORD;

// PostgreSQL database configuration
const sequelize = new Sequelize(dbName, dbUser, dbPassword, {
  host: dbHost,
  port: dbPort,
  dialect: 'postgres',
});

// Define the Extraction model
const Extraction = sequelize.define('Extraction', {
  name: {
    type: DataTypes.TEXT,
    allowNull: false,
  },
  content: {
    type: DataTypes.JSON,
    allowNull: false,
  },
});

// Function to synchronize the model with the database and start the server
const startServer = async () => {
  try {
    await sequelize.sync({ force: false }); // Create the extractions table if it doesn't exist
    app.listen(3000, () => {
      console.log('Express app listening on port 3000!');
    });
  } catch (err) {
    console.error('Error starting server:', err);
  }
};

// Start the server
startServer();
