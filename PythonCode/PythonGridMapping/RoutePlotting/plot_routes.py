import folium
import sys
import time
import os
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

GPSCoordinate = namedtuple("GPSCoordinate", ["lat", "long"])

os.chdir('..\\..')
#gps_coords_loc = 'MissionResolverCode\\work_resolver_runner.txt'
gps_coords_loc = "D:\\IJCAIDemoCode\\CommsHubCode\\work_resolver_runner.txt"
locations = open(gps_coords_loc, 'r')

gps_coordinates = []
file_lines = locations.readlines()
colors = ['blue','green','red', 'yellow', 'black']
marker_sides = [i for i in range(3, 3 + len(colors)+1)]
color_counter = 0
map=folium.Map(location=[53.28174954176364, -9.061292838154545], tiles='Stamen Terrain',zoom_start=15)
points = []
for location in file_lines:
	if location == '\n':
		folium.PolyLine(points, color = colors[color_counter], weight = 3).add_to(map)
		color_counter+=1
		points = []
	elif len(location.split(','))>1:
		print(location)
		location = location.replace('\n','')
		gps_coordinates.append(GPSCoordinate(location.split(',')[0], location.split(',')[1]))
		print('creating location: ', [location.split(',')[0], location.split(',')[1]])
		folium.RegularPolygonMarker(location = [float(location.split(',')[0]), float(location.split(',')[1])],
		fill_color = colors[color_counter], radius = 5, number_of_sides=marker_sides[color_counter]).add_to(map)
		points.append((float(location.split(',')[0]), float(location.split(',')[1])))
		
		
folium.TileLayer('openstreetmap').add_to(map)
map_loc = '\\PythonClientGPSMapping\\rav_route_mapping.html'
#os.chdir('..\\..')
print('current directory: ' + os.getcwd())
map.save(os.getcwd() + map_loc)
browser = webdriver.Chrome()
browser.get(os.getcwd() + map_loc)

def show_path(driver, file_path):
	driver.get('https://www.darrinward.com/lat-long/')
	csv_input = driver.find_element_by_name('csv_file')
	csv_input.send_keys(os.getcwd() + file_path)
	wait = WebDriverWait(driver, 5)
	element = wait.until(EC.element_to_be_clickable((By.ID, 'labels_show')))
	time.sleep(0.5)
	element = driver.find_element_by_id('labels_show')
	if element.is_selected():
		print('clicking labels_show')
		time.sleep(1)
		try:
			element.click()
		except Exception as e:
			print(e)
		print('clicked labels_show')
		
	element = wait.until(EC.element_to_be_clickable((By.ID, 'line_show')))
	time.sleep(0.5)
	element = driver.find_element_by_id('line_show')
	if element.is_selected():
		print('clicking line_show')
		time.sleep(1)
		element.click()
		print('clicked line_show')

	driver.find_element_by_id('submitButton').click()

second_browser = webdriver.Chrome()
show_path(second_browser, '\\MissionResolverCode\\test_work_resolver31_all.csv')

third_browser = webdriver.Chrome()
show_path(third_browser, '\\MissionResolverCode\\test_work_resolver31_one.csv')

fourth_browser = webdriver.Chrome()
show_path(fourth_browser, '\\MissionResolverCode\\test_work_resolver31_two.csv')

fifth_browser = webdriver.Chrome()
show_path(fifth_browser, '\\MissionResolverCode\\test_work_resolver31_three.csv')

import sys
sys.exit(0)

third_browser = webdriver.Chrome()
third_browser.get('https://www.darrinward.com/lat-long/')
csv_input = third_browser.find_element_by_name('csv_file')

csv_input.send_keys(os.getcwd() + '\\MissionResolverCode\\test_work_resolver31_one.csv')

wait = WebDriverWait(third_browser, 5)
element = wait.until(EC.element_to_be_clickable((By.ID, 'labels_show')))
if element.is_selected():
	element.click()
	
element = wait.until(EC.element_to_be_clickable((By.ID, 'line_show')))
if third_browser.find_element_by_id('line_show').is_selected():	
	third_browser.find_element_by_id('line_show').click()
time.sleep(2)
third_browser.find_element_by_id('submitButton').click()

fourth_browser = webdriver.Chrome()
fourth_browser.get('https://www.darrinward.com/lat-long/')
csv_input = fourth_browser.find_element_by_name('csv_file')
csv_input.send_keys(os.getcwd() + '\\MissionResolverCode\\test_work_resolver31_one.csv')
fourth_browser.find_element_by_id('labels_show').click()
fourth_browser.find_element_by_id('line_show').click()
fourth_browser.find_element_by_id('submitButton').click()

fifth_browser = webdriver.Chrome()
fifth_browser.get('https://www.darrinward.com/lat-long/')
csv_input = fifth_browser.find_element_by_name('csv_file')
csv_input.send_keys(os.getcwd() + '\\MissionResolverCode\\test_work_resolver31_one.csv')
fifth_browser.find_element_by_id('labels_show').click()
fifth_browser.find_element_by_id('line_show').click()
fifth_browser.find_element_by_id('submitButton').click()