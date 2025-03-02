def city_country(city_name,country_name,city_population=""):
    
    #case where population is included in function calling
    if city_population:
        beauty_naming = (f"{city_name}, {country_name} - {city_population}").title() 
    
    #case where population is not included in function calling
    else:
        beauty_naming = (f"{city_name}, {country_name}").title()
    return beauty_naming


