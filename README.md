# d8night-backend

## Standard URL Guide 

### Register New User
##### URL: https://d8nite-backend.herokuapp.com/d8nite/users/
##### Method: POST
##### JSON Format: 
     {
       "username": "x",
       "password": "x"
     }
     
     
### Log In
##### URL: https://d8nite-backend.herokuapp.com/token-auth/
##### Method: POST
##### JSON Format:
    {
       "username": "x",
       "password": "x"
     }
  
  
### Get Current User
##### URL: https://d8nite-backend.herokuapp.com/d8nite/current_user
##### Method: GET


### Get Breweries By Zip Code (Powered by Open Brewery DB)
##### URL: https://d8nite-backend.herokuapp.com/d8nite/breweries/{ZIP}
##### Method: GET
##### Example JSON Output:
    [
      {
          "id": 13590,
          "obdb_id": "props-brewery-and-grill-fort-walton-beach",
          "name": "Props Brewery and Grill",
          "brewery_type": "brewpub",
          "street": "125 Lovejoy Rd",
          "address_2": null,
          "address_3": null,
          "city": "Fort Walton Beach",
          "state": "Florida",
          "county_province": null,
          "postal_code": "32548",
          "country": "United States",
          "longitude": null,
          "latitude": null,
          "phone": "8505867117",
          "website_url": "http://www.propsbrewery.com",
          "updated_at": "2018-08-11T00:00:00.000Z",
          "created_at": "2018-07-24T00:00:00.000Z"
      }
    ]
   
   
### Get Restaurants By Zip Code (Powered by Yelp API)
##### URL: https://d8nite-backend.herokuapp.com/d8nite/restaurants/{ZIP}
##### Method: GET
##### (JSON is too long to add here, though the best bet to use this URL is to step through the "businesses" array provided in the JSON text)


### Get Weather By Zip Code (Powered by OpenWeatherMap API)
##### URL:https://d8nite-backend.herokuapp.com/d8nite/weather/{ZIP}
##### Method: GET
##### Example JSON Output:
    {
      "coord": {
          "lon": -86.6286,
          "lat": 30.4206
      },
      "weather": [
          {
              "id": 802,
              "main": "Clouds",
              "description": "scattered clouds",
              "icon": "03d"
          }
      ],
      "base": "stations",
      "main": {
          "temp": 80.64,
          "feels_like": 85.28,
          "temp_min": 79,
          "temp_max": 82.4,
          "pressure": 1011,
          "humidity": 78
      },
      "visibility": 10000,
      "wind": {
          "speed": 14.97,
          "deg": 170
      },
      "clouds": {
          "all": 40
      },
      "dt": 1620071576,
      "sys": {
          "type": 1,
          "id": 4421,
          "country": "US",
          "sunrise": 1620039657,
          "sunset": 1620087938
      },
      "timezone": -18000,
      "id": 0,
      "name": "Fort Walton Beach",
      "cod": 200
    }


### Get Google Maps Result For Zip Code
##### URL: https://d8nite-backend.herokuapp.com/maps/{ZIP}
##### Method: GET
##### Returns HTTP Repsonse as an HTML Page, NOT JSON
         


### Get Google Places Result For Keyword In Zip Code
##### URL: https://d8nite-backend.herokuapp.com/maps/{ZIP}/{KEYWORD}
##### Method: GET
##### Returns HTTP Repsonse as an HTML Page, NOT JSON

