# mdl (middleware)

Middleware uses `infosetdb` to store GPS coordinates of devices (mobile) for [one-stop](https://github.com/PalisadoesFoundation/one-stop) and [do-road](https://github.com/PalisadoesFoundation/do-road)

# Routes

All routes are prefixed with `/mdl/api/v1/mobile`. eg `localhost:3000/mdl/api/v1/mobile` + any route below.


| Description                                  |Full Route                |
|----------------------------------------------|--------------------------------------------------------|
| Register Driver                              |`/mdl/api/v1/mobile/post/register/driver`               |
| Login Driver                                 |`/mdl/api/v1/mobile/post/login/driver`                  |
| Register Rider                               |`/mdl/api/v1/mobile/post/register/rider`                |
| Login Rider                                  |`/mdl/api/v1/mobile/post/login/rider`                   |
| Post Driver GPS coordinates                  |`/mdl/api/v1/mobile/post/drivercoordinates`             |
| Post Rider GPS coordinates                   |`/mdl/api/v1/mobile//post/ridercoordinates`             |
| Gets list of last contacted drivers          |`/mdl/api/v1/mobile/get/coordinates/lastcontactdrivers` |
| Gets list of last contacted riders/passengers|`/mdl/api/v1/mobile/get/coordinates/lastcontactdrivers` |


# Register Driver
To register a driver in the database, send a POST to `http://nylon.palisadoes.org:3000/mdl/api/v1/mobile/post/register/driver` with the following JSON data packet structure.

```javascript
{
  "firstName":"Jordan",
  "lastName": "Jones",
  "email": "sample@email.com",
  "password": "hashedpasswerd",
  "phone": "8765555555",
  "utc_timestamp":"14000000",
  "name": "DoRoad"

  }
```

# Login Driver
To login a driver to application, send a POST to `http://nylon.palisadoes.org:3000/mdl/api/v1/mobile/post/login/driver` with the following JSON data packet structure.

```javascript
{
  "email": "sample@email.com",
  "password": "hashedpasswerd",
  "name": "DoRoad"
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
  "utc_timestamp":"14000000",
  "name": "OneStop"
  }
```

# Login Rider/Commuter
To login a driver to application, send a POST to `http://nylon.palisadoes.org:3000/mdl/api/v1/mobile/post/login/driver` with the following JSON data packet structure.

```javascript
{
  "email": "sample@email.com",
  "password": "hashedpasswerd",
  "name": "OneStop"
  }
```
