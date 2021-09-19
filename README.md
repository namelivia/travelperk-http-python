# travelperk-http-python [![tag](https://img.shields.io/github/tag/namelivia/travelperk-http-python.svg)](https://github.com/namelivia/travelperk-http-python/releases) [![build](https://github.com/namelivia/travelperk-http-python/actions/workflows/build.yml/badge.svg)](https://github.com/namelivia/travelperk-http-python/actions/workflows/build.yml) [![codecov](https://codecov.io/gh/namelivia/travelperk-http-python/branch/main/graph/badge.svg?token=ncBKtvoHR5)](https://codecov.io/gh/namelivia/travelperk-http-python) [![Lint](https://github.com/namelivia/travelperk-http-python/actions/workflows/black.yml/badge.svg)](https://github.com/namelivia/travelperk-http-python/actions/workflows/black.yml)

<p align="center">
  <img src="https://user-images.githubusercontent.com/1571416/118358121-b78de000-b57d-11eb-9987-f750ed530d83.png" alt="TravelPerk Python SDK" />
</p>

## About

This is an unofficial package for acessing the [TravelPerk official Web API](https://developers.travelperk.com) from your Python language project. It is designed so you can easily query and retrieve all data hold on their platform and accessible through the API.

## Installation

This package is hosted on [PyPi](https://pypi.org/project/travelperk-http-python), you can install it using any python package manager. 

```bash
$ pip install travelperk-http-python
```

## Getting started

Before getting started retrieving querying information from the TravelPerk Web API you first need to [get an API Key](https://developers.travelperk.com/reference#authentication).

### Getting a TravelPerk instance

For querying the data you need to get a TravelPerk instance, here are two ways to get a TravelPerk API instance depending on how you authenticate with their API.

At TravelPerk there are [two ways to authenticate](https://developers.travelperk.com/reference#authentication), using an API Key or OAuth2.

#### For API Key Authentication

If you have an [API Key](https://developers.travelperk.com/reference#api-keys-1) for authenticating you need to call the Service Provider's `build` method passing your api key, and a boolean indicating if you will be using the [sandbox environment](https://developers.travelperk.com/docs/postman-collection#step-2---configure-the-postman-environment) or not like this:

```python
from travelperk_http_python.builder.builder import build
is_sandbox = False
travelperk = build("YOUR_API_KEY", is_sandbox)
```

#### For OAuth Authentication

Due to time constrains the OAuth authentication flow is not fully implemented so is not supported yet, see [this GitHub issue](https://github.com/namelivia/travelperk-http-python/issues/10)

### Retrieving data

Everything is ready, you can start asking for the data.
```python
travelperk.expenses().invoices().all()
```
For further information refer to the documentation linked in the next section.

## Documentation

The full documentation can be found [in the wiki section of this github repository](https://github.com/namelivia/travelperk-http-python/wiki).
Also you can refer to the [official TravelPerk Web API documentation](https://developers.travelperk.com/reference)

## License

[MIT](LICENSE)

## Contributing
Any suggestion, bug reports, prs or any other kind enhacements are welcome. Just [open an issue first](https://github.com/namelivia/travelperk-http-python/issues/new), for creating a PR remember this project has linting checkings and unit tests so any PR should comply with both before beign merged, this checks will be automatically applied when opening or modifying the PRs.

## Local development

This project comes with a `docker-compose.yml` file so if you use Docker and docker-compose you can develop without installing anything on your local environment. Just run `docker-compose up --build` for the first time to setup the container and launch the tests. Pytest is configured as the entrypoint so just run `docker-compose up` everytime you want the tests to execute on the Dockerized Python development container.
