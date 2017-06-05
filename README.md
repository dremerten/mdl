# mdl

# Register Driver
To register a driver in the database, send a POST to `http://nylon.palisadoes.org:3000/mdl/api/v1/mobile/post/register/driver` with the following JSON data packet structure.

```javascript
{
  "firstName":"Jordan",
  "lastName": "Jones",
  "email": "sample@email.com",
  "password": "hashedpasswerd",
  "phone": "8765555555",
  "utc_timestamp":"14000000"
  }
```

# Login Driver
To login a driver to application, send a POST to `http://nylon.palisadoes.org:3000/mdl/api/v1/mobile/post/login/driver` with the following JSON data packet structure.

```javascript
{
  "email": "sample@email.com",
  "password": "hashedpasswerd"
  }
```

# Register Rider/Commuter
To register a driver in the database, send a POST to `http://nylon.palisadoes.org:3000/mdl/api/v1/mobile/post/register/rider` with the following JSON data packet structure.

```javascript
{
  "firstName":"Jordan",
  "lastName": "Jones",
  "email": "sample@email.com",
  "password": "hashedpasswerd",
  "phone": "8765555555",
  "utc_timestamp":"14000000"
  }
```

# Login Rider/Commuter
To login a driver to application, send a POST to `http://nylon.palisadoes.org:3000/mdl/api/v1/mobile/post/login/driver` with the following JSON data packet structure.

```javascript
{
  "email": "sample@email.com",
  "password": "hashedpasswerd"
  }
```
