#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

# install.packages("shiny")
# install.packages("readtext")


library(shiny)
library(readtext)
library(ini)

source("utils.R")

#set the working directory to the top level
#working_dir = getwd()
working_dir <<- paste(getwd(), '/../..', sep = '')
setwd(working_dir)

print(paste("Working directory: ",getwd()))

#move all of this to a config file

config <<- read.ini("Config/config.ini")




clickedLocs <<- data.frame(lat=numeric(),lng=numeric())
names(clickedLocs) <- c("lat", "long")
rav_positions <- data.frame("lat" = c(53.28, 53.286, 53.2798), 
                            "long" = c(-9.07, -9.0588, -9.0565),
                            "text" = c("RAV1", "RAV2", "RAV3"))

#bottom right, top right,  top left, bottom left
bounding_rect <- data.frame("lat" =c(53.27959959,53.2805257315, 53.2801009832, 53.2791748417),
                            "long" = c(-9.0617270785, -9.0621271428, -9.0648776011, -9.0644775368))



agent_route_analysis <<- ""
f_snapshot_old <<- fileSnapshot(concat_paths(working_dir, config$DATA$UIImagesDir), md5sum = TRUE)



#routes <<- ""

#Here's one we prepared earlier :P!
# dat$lat <- c(53.28323, 53.28215, 53.27884, 53.27887, 53.28164)
# dat$long <- c(-9.062691,-9.055781,-9.057240,-9.065051,-9.067411)

shinyServer(function(input, output, session) {
  
  #check for new images every 10 seconds
  autoInvalidate <- reactiveTimer(10000)
  update_images <- reactiveVal(value = 0)
  update_sops <- reactiveVal(value = 0)
  agent_route_analysis_flag <- reactiveVal(value = 0)
  
  blog_chem_likelihood_output <- eventReactive(input$do_blog_analysis,{
    showNotification("Calculating likelihoods of threat", duration = 8, type = "message")
    run_blog(concat_paths(working_dir,config$BLOG$BlogCodeLoc), config$BLOG$BlogProgName, config$BLOG$BlogBinLoc, working_dir, isolate(input$odors), isolate(input$nerve_agents), isolate(input$dispersion_methods))
    file = readtext(concat_paths(working_dir, config$BLOG$BlogCodeLoc,"/output.txt"))$text
    #relevant_data = strsplit(file, 'Query Results')
    x <- str_split(file, "Query Results", 2, TRUE)
    
    #31 chemicals
    chems <- lapply(str_split(x[2], "Distribution", 32, TRUE), function(x) substr(str_extract(x,"for ([a-z].*)"),5, nchar(str_extract(x,"for ([a-z].*)"))))
    values_false <- lapply(str_split(x[2], "Distribution", 32, TRUE), function(x) substr(str_extract(x,"false\t[0-9].[0-9].*"),7, nchar(str_extract(x,"false\t[0-9].[0-9].*"))))
    values_true <- lapply(str_split(x[2], "Distribution", 32, TRUE), function(x) substr(str_extract(x,"true\t[0-9].[0-9].*"),6, nchar(str_extract(x,"true\t[0-9].[0-9].*"))))
    
    df <- data.frame('Chemical Name'=unlist(chems), 'Probability not present' = unlist(as.numeric(values_false)), 'Probability present' = unlist(as.numeric(values_true)))
    df <- df[-c(1),]
    rownames(df) <- seq(length = nrow(df))
    brks <- quantile(df$Probability.present, probs = seq(0, 1, .05), na.rm = TRUE)
    clrs <- round(seq(255, 40, length.out = length(brks) + 1), 0) %>%
    {paste0("rgb(255,", ., ",", ., ")")}
    df <- df[order(df$Probability.not.present, decreasing = FALSE),]
    datatable(df) %>% formatStyle('Probability.present', backgroundColor = styleInterval(brks, clrs))
  })
  
  #Renders the data table for BLOG calculated threat likelihood
  output$distPlot <- DT::renderDataTable({
    #input$do_analysis
    blog_chem_likelihood_output()
  })
  
  #Displays Brett's document retrieval procedure
  output$frame <- renderUI({
    update_sops()
    tags$iframe(src="http://127.0.0.1:5000/", height=400, width=1400, frameBorder = 0)
    #my_test <- tags$iframe(src="http://127.0.0.1:5000/", height=400, width=1400, frameBorder = 0)
    #my_test
  })
  
  observeEvent(input$plot_grid_points,{
    #hard code in data collection region
    if(input$DataColletionMode){
      showNotification(paste("Using pre-defined rectangle to gather images: ", clickedLocs))
      clickedLocs <<- data.frame("lat" = c(53.2780931659, 53.2804041456, 53.281325917, 53.2790149872),
                                 "long" = c( -9.0648465368, -9.0661543305, -9.0615979824, -9.0602901886)) 
    }
  
    run_java(concat_paths(working_dir, config$JAVA$JavaBinLoc), concat_paths(working_dir, config$JAVA$JavaCodeLoc), config$JAVA$JavaMissionDesignerJar, working_dir, config$DATA$PlannedAgentRoutesDir, isolate(input$no_ravs), clickedLocs, isolate(input$lat_spacing), isolate(input$lng_spacing))
    print("found analysis")
    agent_route_analysis_flag(agent_route_analysis_flag() + 1) 
    print(agent_route_analysis)
    #grid_points <- read.csv("./RCode/ShinyApp/Data/gridPoints.csv", header = TRUE)
    grid_points <- read.csv(concat_paths(working_dir, config$DATA$PlannedAgentRoutesDir, config$DATA$RAVPlannedWaypointsFile), header = TRUE)
    leafletProxy('map') %>% addPolygons(lng = clickedLocs$long, lat = clickedLocs$lat) %>% addCircles(lng = grid_points$long, lat = grid_points$lat, weight=1, radius=7, color='black', fillColor='orange', popup = paste(grid_points$lat, grid_points$long))
  })
  
  output$mission_report <- renderText({
    input$show_analysis
    paste(agent_route_analysis, sep = '', collapse = '\n')
  })
  
  
  output$map <- renderLeaflet({
    leaflet() %>%
      setView(lng = -9.0615, lat = 53.2770, zoom = 12) %>%
      addTiles(options = providerTileOptions(noWrap = TRUE)) %>%
      addMarkers(lng = rav_positions$long, lat = rav_positions$lat, icon = RAVIcon) %>%
      addPolygons(lng = bounding_rect$long, lat = bounding_rect$lat, opacity = 0.2, color = '#ff0000')
  })
  
  observeEvent(input$clear_region, {
    clickedLocs<<-clickedLocs[0,]
    leafletProxy('map') %>% clearShapes() %>% clearMarkers() %>% 
      addMarkers(lng = rav_positions$long, lat = rav_positions$lat, icon = RAVIcon) %>%
      addPolygons(lng = bounding_rect$long, lat = bounding_rect$lat, opacity = 0.2, color = '#ff0000')
  })
  
  observeEvent(input$map_region, {
    print("request issued to map region")
    ##add the last row to complete the polygon
    rbind(clickedLocs, clickedLocs[1,])
    #draw the polygon
    leafletProxy('map') %>% addPolygons(lng = clickedLocs$long, lat = clickedLocs$lat) %>%
      addMarkers(lng = rav_positions$long, lat = rav_positions$lat, icon = RAVIcon)
    
    #hard code in data collection region
    if(input$DataColletionMode){
      showNotification(paste("Using pre-defined rectangle to gather images: ", clickedLocs))
      clickedLocs <<- data.frame("lat" = c(53.2780931659, 53.2804041456, 53.281325917, 53.2790149872),
                                                                 "long" = c( -9.0648465368, -9.0661543305, -9.0615979824, -9.0602901886)) 
    }
    
    if(is.null(config$JAVA$JavaBinLoc)){
      #assume that correct java version is installed
      config$JAVA$JavaBinLoc = "java"
    }
    #get the java script to generate the routes for each rav
    #java_bin_loc, java_code_loc, java_prog_name, working_dir, no_ravs, locs, lat_spacing, lng_spacing
    cat(paste0(concat_paths(working_dir, config$JAVA$JavaBinLoc), concat_paths(working_dir, config$JAVA$JavaCodeLoc), config$JAVA$JavaMissionDesignerJar, working_dir, isolate(input$no_ravs), clickedLocs, isolate(input$lat_spacing), isolate(input$lng_spacing)))
    print(concat_paths(working_dir, config$JAVA$JavaBinLoc))
    agent_routes <- run_java(concat_paths(config$JAVA$JavaBinLoc), concat_paths(working_dir, config$JAVA$JavaCodeLoc), config$JAVA$JavaMissionDesignerJar, working_dir, config$DATA$PlannedAgentRoutesDir, isolate(input$no_ravs), clickedLocs, isolate(input$lat_spacing), isolate(input$lng_spacing))
    
    # 
    # #read the csvs that contain the routes for each agent
    #points1 <-read.csv("./RCode/ShinyApp/Data/Agent1.csv", header = TRUE)
    points1 <- read.csv(concat_paths(working_dir, config$DATA$PlannedAgentRoutesDir, "Agent1.csv"))
    
    leafletProxy('map') %>% addCircles(lng = points1$long, lat = points1$lat, weight=1, radius=7, color='black', fillColor='blue', popup = paste("RAV1",paste(points1$lat, points1$long))) %>% addPolylines(lng = points1$long, lat = points1$lat, weight=1, color='blue', fillColor='blue')
    if(isolate(input$no_ravs > 1)){
      #points2 <- read.csv("./RCode/ShinyApp/Data/Agent2.csv")
      points2 <- read.csv(concat_paths(working_dir, config$DATA$PlannedAgentRoutesDir, "Agent2.csv"))
      leafletProxy('map') %>% addCircles(lng = points2$long, lat = points2$lat, weight=1, radius=7, color='black', fillColor='green', popup = paste("RAV2",paste(points2$lat, points2$long))) %>% addPolylines(lng = points2$long, lat = points2$lat, weight=1, color='green', fillColor='green')
    }
    if(isolate(input$no_ravs > 2)){
      #points3 <- read.csv("./RCode/ShinyApp/Data/Agent3.csv")
      points3 <- read.csv(concat_paths(working_dir, config$DATA$PlannedAgentRoutesDir, "Agent3.csv"))
      leafletProxy('map') %>% addCircles(lng = points3$long, lat = points3$lat, weight=1, radius=7, color='black', fillColor='red', popup = paste("RAV3",paste(points3$lat, points3$long))) %>% addPolylines(lng = points3$long, lat = points3$lat, weight=1,color='red', fillColor='red')
    }
  })

  observeEvent(input$launch_agents,{
    # input = list()
    # input$no_ravs = 4
    # input$num_cameras = 4
    # input$rav_veloctiy = 20.4
    # input$rav_altitude = 37
    #run generate_routes.py in order to generate routes for agents
    
    ###################### Put all of this into utils.py ######################
    setwd(concat_paths(working_dir, config$PYTHON$PythonRAVRouteExecutionDir))
    #setwd(paste(working_dir,"/PythonCode/PythonGridMapping/RoutePlotting", sep='', collapse=''))
    #generateUnrealPlotRoutes  -   no_ravs, no_cameras, rav_route_write_dir, saved_images_dir, gps_coords_write_dir
    gen_route_command <- paste(concat_paths(working_dir, config$PYTHON$PythonGenerateRouteDir, config$PYTHON$PythonGenerateRoutesFileLoc), isolate(input$no_ravs), isolate(input$num_cameras), isolate(input$rav_veloctiy), isolate(input$rav_altitude), collapse='')
  
    print(paste("running python command", gen_route_command))
    system2(config$PYTHON$PythonExe, args = c(gen_route_command))
    ###################### Put all of this into utils.py ######################
    
    showNotification("Agents ready to execute planned routes", duration = 10, type = "message")
    noDrones = ifelse(isolate(input$no_ravs) == 1, "one", ifelse(isolate(input$no_ravs)==2, "two", "three"))
    setwd(concat_paths(working_dir, config$BATCHSCRIPTS$BatchScriptsLoc))
    if((stringr::str_extract(config$BATCHSCRIPTS$BatchScriptsLoc, "Unix")) == "Unix"){
      drone_ex <<- concat_paths(working_dir, config$BATCHSCRIPTS$BatchScriptsLoc, paste(noDrones, "_drone.sh", sep="", collapse=""))
      system(drone_ex)
    }
    else {
      system2(paste(noDrones,"_drone.bat", sep="", collapse=""))
    }
    setwd(working_dir)
    showNotification("RAVs executing planned routes in games engine")
  })
  
  ## Observe mouse clicks and add circles
 
   observeEvent(input$map_click, {
    ## Get the click info like had been doing
    click <- input$map_click
    clat <- click$lat
    clng <- click$lng
    address <- revgeocode(c(clng,clat))
    clickedLocs <<- rbind(clickedLocs,c(as.numeric(clat), as.numeric(clng)))
    names(clickedLocs) <<- c("lat", "long")
    print("clickedLocs")
    print(clickedLocs)
    ## Add the circle to the map proxy
    ## so you dont need to re-render the whole thing
    ## I also give the circles a group, "circles", so you can
    ## then do something like hide all the circles with hideGroup('circles')
    returnMap <- leafletProxy('map') %>% # use the proxy to save computation
      addCircles(lng=clng, lat=clat, group='circles',
                 weight=1, radius=8, color='black', fillColor='orange',
                 popup=address, fillOpacity=0.5, opacity=1)
    
    if(nrow(clickedLocs)>0){
      returnMap %>%addPolylines(data = clickedLocs, lng = ~long, lat = ~lat, weight = 2)
    }
    returnMap
  })
  
  output$processed_image <- renderImage({
    update_images()
    list(src = concat_paths(working_dir, config$DATA$UIImagesDir,config$DATA$MostRecentProcessImageFileLoc),
         contentType = 'image/png',
         width = 750,
         height = 750,
         alt = "No collected images to show")
  }, deleteFile = FALSE)
  
  output$unprocessed_image <- renderImage({
    update_images()
    list(src = concat_paths(working_dir, config$DATA$UIImagesDir, config$DATA$MostRecentImageRawFileLoc),
         contentType = 'image/png',
         width = 600,
         height = 600,
         alt = "No collected images to show")
  }, deleteFile = FALSE)
  
  observe({
    autoInvalidate()
    print("autoInvalidating")
    print(Sys.time())
    f_snapshot_new <<- fileSnapshot(concat_paths(working_dir, config$DATA$UIImagesDir), md5sum = TRUE)
    #need to check that f_snapshots are not null so changes can be compared
    if(!is.null(dim(f_snapshot_new)) && !is.null(dim(f_snapshot_old))){
      if(TRUE %in% changedFiles(f_snapshot_old, f_snapshot_new)$changes){
        #set flag to update images
        update_images(update_images() + 1)
      }
    }
    f_snapshot_old <<- f_snapshot_new
  })
  
  observeEvent(input$RankTerms, {
    print("Ranking user terms")
    value <- run_elasticMain(isolate(input$SOPRetrievalInput))
    update_sops(update_sops() + 1)
  })
  
  observe({
    print(input$DataColletionMode)
    if(input$DataColletionMode){
      updateSelectInput(session, "no_ravs", label="Choose number of RAVs to be used", choices = c(1:20), selected = 1)
      updateSelectInput(session, "lat_spacing", label = "Choose the latitude spacing (m)", choices = c(1:500)/2, selected = 20)
      updateSelectInput(session, "lng_spacing", label = "Choose the longitude spacing (m)", choices = c(1:500)/2, selected = 20)
      #any more than 10 would definitely cause gpu to crash...
      updateSelectInput(session, "num_cameras", label = "Choose the number of cameras to use", c(0:10), selected = 2)
      updateSelectInput(session, "rav_altitude", label = "Choose the altitude at which RAVs will fly (m)", choices = c(1:400)/2, selected = 30)
      updateSelectInput(session, "rav_veloctiy", label = "Choose the velocity at which RAVs will fly (m/s)", choices = c(1:50)/5, selected = 3)
    }
    else{
      updateSelectInput(session, "no_ravs", label="Choose number of RAVs to be used", choices = c("1", "2", "3"), selected = 1)
      updateSelectInput(session, "lat_spacing", label = "Choose the latitude spacing", choices = c(20,25,30,40,50,100), selected = 20)
      updateSelectInput(session, "lng_spacing", label = "Choose the longitude spacing", choices = c(20,25,30,40,50,100), selected = 25)
      updateSelectInput(session, "num_cameras", label = "Choose the number of cameras to use", choices = c(0,1,2,3,4), selected = 1)
      updateSelectInput(session, "rav_altitude", label = "Choose the altitude at which RAVs will fly (m)", choices =  c(25, 30, 35, 40), selected = 30)
      updateSelectInput(session, "rav_veloctiy", label = "Choose the velocity at which RAVs will fly (m/s)", choices = c(1:8), selected = 3)
      
    }
  })
  
})
