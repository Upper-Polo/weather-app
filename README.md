# weather-app
Get the current weather by inputting city, country using Open Weather Map

#### Pair programming

- use the same team as last time with the todo list

- Create a new repo in your organization

- Use the OpenWeatherMap API: http://openweathermap.org/api

- Get API key (free, takes 1 min to activate)

- Sample API call: http://api.openweathermap.org/data/2.5/weather?q=Lexington&appid=17aaf89fcf237288f605d1197a3575fc
- User should be able to get the current weather by inputting city,country
- User should see a list of current weather attributes: temperature, description, humidty, etc.
- User should see an appropriate error message if the city is not found. For instance, if the user enters "assdf"
- User should be get the 5 day forecast by inputting city, country
- User should be able to see the weather attributes for each of the 5 days

#### Note:

Don't try to get a location by zipcode with the OpenWeatherMap API. There is currently an issue with free accounts where most cities are not found

#### Bonus:

- User should be able to save a location as a favorite and load the favorites from a file
-Switch to using a different weather API: http://www.programmableweb.com/news/top-10-weather-apis/analysis/2014/11/13#apiu
-Add Comment Collapse
