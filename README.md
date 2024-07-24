# SpyLock
# Roadmap for SpyLock: Anonymous Messenger

## Overview
SpyLock is an anonymous messenger designed to ensure secure, peer-to-server-to-peer encrypted communication leveraging blockchain web3 technology. The application will be divided into two separate projects: the Client Side and the Server Side. Both projects will use PostgreSQL for the database. The application will feature advanced security measures, including RSA key encryption for message security and blockchain integration for data integrity and decentralized features.

## Table of Contents
1. Project Structure
2. Key Features
3. Development Phases
4. Security Features
5. Database Schema
6. Dependencies and Requirements

## 1. Project Structure

### Client Side
- **Project Name:** SpyLockClient
- **Purpose:** Provides a web-based user interface for user interaction, including registration, login, and messaging. Handles message encryption/decryption and storage of keys and dialogues.
- **Technologies:** Django, PostgreSQL, RSA, Web3.py, HTML/CSS, JavaScript

### Server Side
- **Project Name:** SpyLockServer
- **Purpose:** Handles registration, login, user search by nickname, and manages encrypted message transmission between users.
- **Technologies:** Django, PostgreSQL, RSA, Web3.py, REST API

## 2. Key Features
- **User Registration and Login:** Secure registration using username and password. Handled by the server side, but accessible via the client-side web interface.
- **Encrypted P2P Messaging:** Messages are encrypted using RSA before transmission.
- **Blockchain Integration:** Utilize blockchain for secure, decentralized message verification and storage.
- **Database:** PostgreSQL for robust and scalable data management.
- **Web UI:** A user-friendly web interface for registration, login, and messaging.

## 3. Development Phases

### Phase 1: Initial Setup and Basic Functionality
- Set up Django projects for Client and Server sides.
- Configure PostgreSQL databases.
- Implement user registration and login functionality on the server side, accessible via the client side.

### Phase 2: Implement Messaging System
- Develop P2P encrypted messaging system.
- Implement RSA encryption/decryption.
- Integrate Web3 for blockchain functionality.

### Phase 3: Develop Web UI
- Create web interface for user registration, login, and messaging.
- Implement profile settings to update nickname.

### Phase 4: Security Enhancements
- Implement advanced security measures (e.g., RSA key management, data integrity checks).
- Conduct security audits and testing.

### Phase 5: Deployment and Testing
- Deploy the application on a cloud platform.
- Perform extensive testing (unit, integration, and security testing).

## 4. Security Features
- **RSA Encryption:** Use RSA keys for encrypting messages.
- **Blockchain Verification:** Implement blockchain for verifying message integrity.
- **Secure Storage:** Encrypt stored dialogues and keys in the database.
- **Two-Factor Authentication (Optional):** Add an extra layer of security for user accounts.

## 5. Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique)
- `password` (Hashed)
- `nickname` (Unique)

### Messages Table
- `id` (Primary Key)
- `sender_id` (Foreign Key to Users)
- `receiver_id` (Foreign Key to Users)
- `message_content` (Encrypted)
- `timestamp`

### Keys Table
- `id` (Primary Key)
- `user_id` (Foreign Key to Users)
- `public_key`
- `private_key` (Encrypted)

## 6. Dependencies and Requirements
- Python 3.x
- Django
- PostgreSQL
- RSA (PyCryptodome)
- Web3.py
- HTML/CSS
- JavaScript
- Docker (for deployment)
