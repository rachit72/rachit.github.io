# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import webbrowser

class Movie():
    def __init__(self, title, description, image, trailer_url):
        self.title = title
        self.storyline = description
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    def show_image(self):
        webbrowser.open(self.poster_image_url)