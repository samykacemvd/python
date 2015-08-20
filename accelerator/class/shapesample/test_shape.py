#!/usr/bin/python

from class_shape import Shape


#exec
rectangle = Shape(100, 45)
print "Area"
print rectangle.area()

#making the rectangle 50% smaller
print "New area"
rectangle.scaleSize(0.5)
print rectangle.area()

print rectangle.description
print rectangle.author

rectangle.describe('This is a new description')
rectangle.authorName('John Do')

print rectangle.description
print rectangle.author
