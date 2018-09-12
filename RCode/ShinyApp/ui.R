#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

# install.packages("shiny")
# install.packages("readtext")
# install.packages("stringr")
# install.packages("DT")
# install.packages("shinycssloaders")
# install.packages("shinydashboard")
# install.packages("shinyWidgets")
# install.packages("leaflet")
# install.packages("ggmap")

library(shiny)
library(readtext)
library(stringr)
library(DT)
library(shinycssloaders)
library(shinydashboard)
library(shinyWidgets)
library(leaflet)
library(ggmap)


SOPRetrievalTerms = c('ammonia', 'eye irritation', 'pulmonary agent', 'coughing', 'dead insects', 
                      'americium', 'headache', 'Cs137', 'cobalt', 'plume', 'fever', 'breathing problems',
                      'nose irritation', 'phosgene', 'dead birds', 'Co60', 'chlorine', 'yellow cloud',
                      'dead insects', 'gamma', 'green cloud', 'throat irritation',
                      'Am241', 'cesium', 'nausea', 'apnea')# Define UI for application that draws a histogram

header <- dashboardHeader(tags$li(class = "dropdown",
                                          tags$style(".main-header {max-height: 100px}"),
                                          tags$style(".main-header .logo {height: 100px}")),
                          title =  tags$a(href='http://rocsafe.eu',
                          tags$img(src='ROCSAFE-Logo.png')), titleWidth = 450)


sidebar <- dashboardSidebar(
    sidebarMenu(
      tags$style(".left-side, .main-sidebar {padding-top: 100px}"),
      menuItem("Bayesian Reasoning Analysis", tabName = "BayesianAnalysis", icon = icon("cogs")),
      menuItem("Document Retrieval", tabName = "SOPRetrieval", icon = icon("database")),
      menuItem("RAV Mission Planner", tabName = "RAVMissionPlanner", icon = icon("globe")),
      menuItem("Image Analysis", tabName = "ImageAnalysis", icon = icon("image"))
    )
)
  
body <- dashboardBody(
  tags$style('background-image: url("www/ROCSAFE-logo-final.png"'),
  tags$style(type = "text/css", "#map {height: calc(100vh - 80px) !important;}"),
    tabItems(
      tabItem(tabName = "BayesianAnalysis",
              tags$style('background-image: url("ROCSAFE-logo-final.png")'),
              sidebarLayout(
                sidebarPanel(
                  checkboxGroupInput("odors", "Check the following odours if they are suspected/confirmed to be present:",
                                     c("Fruity" = "smell_fruity",
                                       "Odourless"= "smell_odourless", 
                                       "Camphor" = "smell_camphor", 
                                       "Wood" = "smell_wood",
                                       "Chlorine" = "smell_chlorine",
                                       "Mustard Radish Garlic"= "smell_mustard_radish_garlic",
                                       "Unpleasant" = "smell_unpleasant",
                                       "Fish" = "smell_fish",
                                       "Herring" = "smell_herring",
                                       "Soap" = "smell_soap",
                                       "Geranium"="smell_geranium",
                                       "Bitter_almonds"="smell_bitter_almonds",
                                       "Sour"="smell_sour",
                                       "Pungent" ="smell_pungent",
                                       "Apple_blossom" ="smell_apple_blossom",
                                       "Sweet" = "smell_sweet"
                                     )),
                  checkboxGroupInput("nerve_agents", "Check the following nerve agents if they are suspected/confirmed to be present:",
                                     c("Nerve"="agent_nerve",
                                       "Choking"="agent_choking",
                                       "Blister"="agent_blister",
                                       "Blood"="agent_blood",
                                       "Vomiting"="agent_vomiting",
                                       "Tear"="agent_tear",
                                       "Incapacitating Depressant Hallucinogen"="agent_incapacitating_depressant_hallucinogen"
                                     )),
                  checkboxGroupInput("dispersion_methods", "Check the following dispersion methods if they are suspected/confirmed to be present:",
                                     c("Liquid"="dispersion_liquid",
                                       "Gas"="dispersion_gas",
                                       "Vapours"="dispersion_vapours",
                                       "Aerosol"="dispersion_aerosol")),
                  actionButton('do_analysis','Show results of analysis')
                ),
      mainPanel(
        setBackgroundImage(src = "www/ROCSAFE-logo-final.png"),
        DT::dataTableOutput("distPlot")%>% withSpinner(color="#0dc5c1", size=3)
        #htmlOutput("frame")
      )
      )
      ),
      
      tabItem(tabName = "SOPRetrieval", 
              fluidRow(column(width = 3,
              selectizeInput("SOPRetrievalInput",width = '1000px', label = "Choose search terms", choices = SOPRetrievalTerms, multiple = TRUE), offset = 4),
              column(width = 2, actionButton("RankTerms", label = "Rank terms", style='padding-top:5px; padding-bottom: 5px; margin-top: 26px'), offset = 0)),
              br(),
              br(),
              column(width = 8,htmlOutput("frame")%>% withSpinner(color="#0dc5c1", size=3), offset = 1)
              ),
      
      tabItem(tabName = "RAVMissionPlanner",
              
              leafletOutput("map") %>% withSpinner(color="#0dc5c1", size=3),
              
              fluidRow(
              column(width = 2,
                actionButton('map_region','Show agent routes', width = "175px"),
              offset = 3),
              
              column(width = 2,
                actionButton('plot_grid_points', 'Show planned waypoints', width = "175px"),
              offset = 0),
              
              column(width = 2,
                actionButton("clear_region", 'Clear', width = "175px"),
              offset = 0)),
              br(),
              fluidRow(
              column(width = 2,
                selectInput("no_ravs", label="Choose number of RAVs to be used", choices = c("1", "2", "3")),
                selectInput("lat_spacing", label = "Choose the latitude spacing", choices = c(20,25,30,40,50,100)),
                selectInput("lng_spacing", label = "Choose the longitude spacing", choices = c(20,25,30,40,50,100)),
                selectizeInput("num_cameras", label = "Choose the number of cameras to use", choices = c(1,2,3,4)),
                actionButton("show_analysis", label="Show analysis"),
                actionButton("launch_agents", label = "Execute agent routes"),
              offset = 0),
              
              column(width = 5,
                verbatimTextOutput("mission_report"),
              offset = 2))
              ),
      
      tabItem(tabName = "ImageAnalysis",
              column(width = 5, imageOutput("unprocessed_image")),
              column(width = 5, imageOutput("processed_image"))
      )
      
      
  # Application title
  # Sidebar with a slider input for number of bins 
 
    # Show a plot of the generated distribution
    
  )
)

dashboardPage(header, sidebar, body)