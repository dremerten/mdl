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

# Testing POST and GET coordinates to/from mdl

`mdl` has a small script in `bin/tools` to test both `infoset` POST and `mdl` POST

Tests getting data from infoset

```bash
  $ ./bin/tools/test_installation.py infoset --get
```

Tests getting data from mdl

```bash
  $ ./bin/tools/test_installation.py mdl --get
```

Run `./bin/tools/test_installation mdl -h` for more information.