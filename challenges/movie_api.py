#!/usr/bin/env python3
import requests

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")

    full_url= URL + choice

    movies= requests.get(full_url).json()
    
    for movie in movies["Search"]:
        if movie["Type"] == "movie":
            print(f"{movie['Title']} was released in {movie['Year']}")
    #print(movies)
    #print(full_url)

if __name__ == "__main__":
    main()
