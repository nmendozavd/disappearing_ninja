# Coding Dojo Bootcamp Assignment  
## Python, Django / Flask / Disappearing Ninja

### Assignment details  
Build a flask application with the below functionality.  

This exercise will help you practice URL routing, using views, and rendering static content.  

These are the routes that you need to set up:  

1. On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
2. When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
3. /ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL)
   1. If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
   2. /ninja/orange - Ninja Turtle Michelangelo.
   3. /ninja/red - Ninja Turtle Raphael
   4. /ninja/purple - Ninja Turtle Donatello
   5. If a user tries to hack into your web app by specifying a color or string combination other than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then display the image notapril.jpg
4. You'll need to remember how to use static files for this assignment. Take a minute to refresh your memory back to the static files section if you need to :)

Click here to download the image files.  