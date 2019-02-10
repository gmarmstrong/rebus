#!/usr/bin/env python3

def empty_dict():
	return (
	{
		'answer': "",
		'elements': {
			'textElements': [],
			"shapeElements": {
				"lines": [],
				"rects": [],
				"circles": []
			},
			"imageElements": []
		}
	}
	)

def build_text_element(text,x,y,font,color):
	return (
	{
		"text": text,
		"x": x,
		"y": y,
		"font": font,
		"color": color
	}
	)

def build_line_element(x1,y1,x2,y2,color):
	return (
	{
		"x1": x1,
		"y1": y1,
		"x2": x2,
		"y2": y2,
		"color": color
	}
	)

def build_rect_element(x,y,width,height,color,fill):
	return (
	{
		"x": x,
		"y": y,
		"width": width,
		"height": height,
		"color": color,
		"fill": fill
	}
	)

def build_circle_element(x,y,radius,color,fill):
	return (
	{
		"x": x,
		"y": y,
		"radius": radius,
		"color": color,
		"fill": fill
	}
	)

def build_image_element(src,x,y):
	return (
	{
		"src": src,
		"x": x,
		"y": y
	}
	)
