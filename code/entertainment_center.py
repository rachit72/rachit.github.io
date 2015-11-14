# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:14:47 2015

@author: MESSI
"""

import media
import fresh_tomatoes

ManOfSteel = media.Movie(title = "Man of Steel", description = "A boy is sent from another\
planet to earth because his planet is dying. He has to represent the element of choice\
for their planet on earth", image = "http://www.reesspechtlife.com/wp-content/uploads\
/2013/04/Supeman-Man-of-Steel-Logo-Hi-Res.jpg",\
trailer_url = "https://www.youtube.com/watch?v=T6DJcgm3wNY")


cinderella_man = media.Movie(title = "Cinderella Man", description = "A boxer \
facing the hardships of life during Great Depression becomes an icon for the public", \
image = "http://cinemagogue.com/wp-content/uploads/2012/11/Cinderella-Man-201x300.jpg",\
trailer_url = "https://www.youtube.com/watch?v=DlbHzcH4VJY")

thor = media.Movie(title = "Thor", description = "Thor, the son of Odin is expelled\
from his planet and thrown to earth to gain some maturity and humility",
image = "https://encrypted-tbn0.gstatic.com\
/images?q=tbn:ANd9GcT-37eMJFmhqe0pAJFDM293WK2UZLo_cwA5KK1YOPOsh-iuwN9m",
trailer_url = "https://www.youtube.com/watch?v=JOddp-nlNvQ")
#ManOfSteel.show_trailer()
#ManOfSteel.show_image()
movies = [ManOfSteel, cinderella_man, thor]
fresh_tomatoes.open_movies_page(movies)