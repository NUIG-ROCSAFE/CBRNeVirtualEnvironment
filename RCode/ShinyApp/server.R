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

#set the working directory to the top level
#working_dir = getwd()
working_dir <<- paste(getwd(), "/../..", sep = "")
setwd(working_dir)

print(getwd())

#move all of this to a config file
java_bin_loc <<- "/usr/bin/"
blog_bin_loc <<- "/usr/bin/"

blog_code_loc <<- paste(working_dir, "/BlogScripts/", sep ="")
blog_prog_name <<- "/ChemicalProbablisticReasoning.blog"
java_code_loc <<- paste(working_dir, "/JavaCode/", sep = "")
java_prog_name <<- "generateCoordinatesRevised.jar"
python_code_loc <<- paste(working_dir, "/SOPRanking/RocsafeCode/Demo-IR/", sep = "")
python_prog_name <<- "elasticMain.py"


end_of_file <- readtext(paste(blog_code_loc, "/ChemProbReasoningSecondHalf.txt", sep = ""))$text 

odors <- c("smell_fruity",
           "smell_odourless",
           "smell_camphor",
           "smell_wood",
           "smell_chlorine",
           "smell_mustard_radish_garlic",
           "smell_unpleasant",
           "smell_fish",
           "smell_herring",
           "smell_soap",
           "smell_geranium",
           "smell_bitter_almonds",
           "smell_sour",
           "smell_pungent",
           "smell_apple_blossom",
           "smell_sweet")

agents <-c("agent_nerve",
           "agent_choking",
           "agent_blister",
           "agent_blood",
           "agent_vomiting",
           "agent_tear",
           "agent_incapacitating_depressant_hallucinogen")

dispersion_methods <- c("dispersion_liquid",
                        "dispersion_gas",
                        "dispersion_vapours",
                        "dispersion_aerosol")

clickedLocs <<- data.frame(lat=numeric(),lng=numeric())
names(clickedLocs) <- c("lat", "long")
rav_positions <- data.frame("lat" = c(53.28, 53.286, 53.2798), 
                            "long" = c(-9.07, -9.0588, -9.0565),
                            "text" = c("RAV1", "RAV2", "RAV3"))

#bottom right, top right,  top left, bottom left
bounding_rect <- data.frame("lat" =c(53.27959959,53.2805257315, 53.2801009832, 53.2791748417),
                            "long" = c(-9.0617270785, -9.0621271428, -9.0648776011, -9.0644775368))



agent_route_analysis <<- ""

RAVIcon <- makeIcon(
  iconUrl = paste(getwd(), "/RCode/ShinyApp/www/RAVIcon.png", sep = ""),
  iconWidth = 30, iconHeight = 30,
  iconAnchorX = 0, iconAnchorY = 0
  #shadowUrl = "http://leafletjs.com/examples/custom-icons/leaf-shadow.png",
  #shadowWidth = 50, shadowHeight = 64,
  #shadowAnchorX = 4, shadowAnchorY = 62
)

f_snapshot_old <<- fileSnapshot("./RCode/ShinyApp/www/", md5sum = TRUE)

run_blog <- function(odors_input, nerve_agents_input, dispersion_methods_input){
  blog_file <- readtext(paste(blog_code_loc,"/ChemicalProbablisticReasoning.blog", sep=""))
  if(!is.null(odors_input)){
    odors_selected <- ifelse(!is.na(match(odors, odors_input)), TRUE, FALSE)
  }
  else{
    odors_selected = rep(FALSE, length(odors))
    
  }
  if(!is.null(nerve_agents_input)){
    agents_selected <- ifelse(!is.na(match(agents, nerve_agents_input)), TRUE, FALSE)
  }
  else{
    agents_selected = rep(FALSE, length(agents))
  }
  if(!is.null(dispersion_methods_input)){
    dispersal_methods_selected <- ifelse(!is.na(match(dispersion_methods, dispersion_methods_input)), TRUE, FALSE)
  }
  else{
    dispersal_methods_selected = rep(FALSE, length(dispersion_methods))
  }
  names(odors_selected) = odors
  names(agents_selected) = agents
  names(dispersal_methods_selected) = dispersion_methods
  
  dispersal_str = paste(paste(paste("obs", names(dispersal_methods_selected)), tolower(as.character(dispersal_methods_selected)), sep = "=", collapse = ";\n"),";", sep = "")
  agent_str = paste(paste(paste("obs", names(agents_selected)), tolower(as.character(agents_selected)), sep = "=", collapse = ";\n"), ";", sep = "")
  odor_str = paste(paste(paste("obs", names(odors_selected)), tolower(as.character(odors_selected)), sep = "=", collapse = ";\n"), ";", sep = "")
  
  #paste all of the selected observations to create the string to write to the blog file
  write_string = paste(odor_str, agent_str, dispersal_str, sep = "\n\n")
  write_string <- paste(write_string, end_of_file, collapse = "\n")
  writeLines(write_string, file(paste(blog_code_loc,"/ChemicalProbablisticReasoning.blog", sep="")))
  

  setwd(blog_bin_loc)
  blog_code_output <- system2("blog", args=c (paste(blog_code_loc,"/ChemicalProbablisticReasoning.blog",sep="")), stdout= TRUE, wait= TRUE)
  setwd(working_dir)
  #write the result of the blog program
  writeLines(blog_code_output, paste(blog_code_loc,"/output.txt", sep=""))
}

run_java <- function(no_ravs, locs, lat_spacing, lng_spacing){
  setwd(java_bin_loc)
  
  #add jar and code location
  argsString <- paste("-jar", java_code_loc)
  #pass in the working directory to the java code
  argsString <- paste(argsString, java_prog_name, sep="")
  argsString <- paste(argsString, working_dir)
  argsString <- paste(argsString, no_ravs)
  
  argsString <- paste(argsString, lat_spacing)
  argsString <- paste(argsString, lng_spacing)
  
  #dat$lat <- c(53.28323, 53.28215, 53.27884, 53.27887, 53.28164)
  #dat$long <- c(-9.062691,-9.055781,-9.057240,-9.065051,-9.067411)
  
  argsString = paste(argsString, paste(locs$lat, locs$long, sep = " ", collapse = " "))
  print("argsString: ")
  print(argsString)
  print("calling")
  agent_route_analysis <<- system2("java", args = c(argsString), stdout = TRUE, wait = TRUE)
  setwd(working_dir)
  print(agent_route_analysis)
  return(agent_route_analysis)
}

run_elasticMain <- function(search_terms){
  print("search terms:")
  print(search_terms)
  #build up args to send to python
  argString <- paste(search_terms, collapse = " ")
  argString <- paste(python_prog_name, argString, collapse = " ")
  print(paste("Calling python with arguments: ", argString))
  #run elastic main
  setwd(python_code_loc)
  result <- system2("python", args = argString)
  print(result)
}

#routes <<- ""

#Here's one we prepared earlier!
# dat$lat <- c(53.28323, 53.28215, 53.27884, 53.27887, 53.28164)
# dat$long <- c(-9.062691,-9.055781,-9.057240,-9.065051,-9.067411)

shinyServer(function(input, output, session) {
  
  autoInvalidate <- reactiveTimer(10000)
  update_images <- reactiveVal(value = 0)
  update_sops <- reactiveVal(value = 0)
  agent_route_analysis_flag <- reactiveVal(value = 0)
  
  blog_chem_likelihood_output <- eventReactive(input$do_blog_analysis,{
    run_blog(isolate(input$odors), isolate(input$nerve_agents), isolate(input$dispersion_methods))
    file = readtext(paste(blog_code_loc,"/output.txt", sep=""))$text
    #relevant_data = strsplit(file, "Query Results")
    x <- str_split(file, "Query Results", 2, TRUE)
    
    #31 chemicals
    chems <- lapply(str_split(x[2], "Distribution", 32, TRUE), function(x) substr(str_extract(x,"for ([a-z].*)"),5, nchar(str_extract(x,"for ([a-z].*)"))))
    values_false <- lapply(str_split(x[2], "Distribution", 32, TRUE), function(x) substr(str_extract(x,"false\t[0-9].[0-9].*"),7, nchar(str_extract(x,"false\t[0-9].[0-9].*"))))
    values_true <- lapply(str_split(x[2], "Distribution", 32, TRUE), function(x) substr(str_extract(x,"true\t[0-9].[0-9].*"),6, nchar(str_extract(x,"true\t[0-9].[0-9].*"))))
    
    df <- data.frame("Chemical Name"=unlist(chems), "Probability not present" = unlist(as.numeric(values_false)), "Probability present" = unlist(as.numeric(values_true)))
    df <- df[-c(1),]
    rownames(df) <- seq(length = nrow(df))
    brks <- quantile(df$Probability.present, probs = seq(0, 1, .05), na.rm = TRUE)
    clrs <- round(seq(255, 40, length.out = length(brks) + 1), 0) %>%
    {paste0("rgb(255,", ., ",", ., ")")}
    df <- df[order(df$Probability.not.present, decreasing = FALSE),]
    datatable(df) %>% formatStyle("Probability.present", backgroundColor = styleInterval(brks, clrs))
  })
  
  #Renders the data table for BLOG calculated threat likelihood
  output$distPlot <- DT::renderDataTable({
    #input$do_analysis
    blog_chem_likelihood_output()
  })
  
  #Displays Brett's document retrieval procedure
  output$frame <- renderUI({
    update_sops()
    my_test <- tags$iframe(src="http://127.0.0.1:5000/", height=400, width=1400, frameBorder = 0)
    my_test
  })
  
  observeEvent(input$plot_grid_points,{
    #hard code in data collection region
    if(input$DataColletionMode){
      showNotification(paste("Using pre-defined rectangle to gather images: ", clickedLocs))
      clickedLocs <<- data.frame("lat" = c(53.2780931659, 53.2804041456, 53.281325917, 53.2790149872),
                                 "long" = c( -9.0648465368, -9.0661543305, -9.0615979824, -9.0602901886)) 
    }
    print(clickedLocs)
    run_java(isolate(input$no_ravs), clickedLocs, isolate(input$lat_spacing), isolate(input$lng_spacing))
    print("found analysis")
    agent_route_analysis_flag(agent_route_analysis_flag() + 1) 
    print(agent_route_analysis)
    grid_points <- read.csv("./RCode/ShinyApp/Data/gridPoints.csv", header = TRUE)
    leafletProxy("map") %>% addPolygons(lng = clickedLocs$long, lat = clickedLocs$lat) %>% addCircles(lng = grid_points$long, lat = grid_points$lat, weight=1, radius=7, color="black", fillColor="orange", popup = paste(grid_points$lat, grid_points$long))
  })
  
  output$mission_report <- renderText({
    input$show_analysis
    paste(agent_route_analysis, sep = "", collapse = "\n")
  })
  
  
  output$map <- renderLeaflet({
    leaflet() %>%
      setView(lng = -9.0615, lat = 53.2770, zoom = 12) %>%
      addTiles(options = providerTileOptions(noWrap = TRUE)) %>%
      addMarkers(lng = rav_positions$long, lat = rav_positions$lat, icon = RAVIcon) %>%
      addPolygons(lng = bounding_rect$long, lat = bounding_rect$lat, opacity = 0.2, color = "#ff0000")
  })
  
  observeEvent(input$clear_region, {
    clickedLocs<<-clickedLocs[0,]
    leafletProxy("map") %>% clearShapes() %>% clearMarkers() %>% 
      addMarkers(lng = rav_positions$long, lat = rav_positions$lat, icon = RAVIcon) %>%
      addPolygons(lng = bounding_rect$long, lat = bounding_rect$lat, opacity = 0.2, color = "#ff0000")
  })
  
  observeEvent(input$map_region, {
    print("request issued to map region")
    ##add the last row to complete the polygon
    rbind(clickedLocs, clickedLocs[1,])
    #draw the polygon
    leafletProxy("map") %>% addPolygons(lng = clickedLocs$long, lat = clickedLocs$lat) %>%
      addMarkers(lng = rav_positions$long, lat = rav_positions$lat, icon = RAVIcon)
    
    #hard code in data collection region
    if(input$DataColletionMode){
      showNotification(paste("Using pre-defined rectangle to gather images: ", clickedLocs))
      clickedLocs <<- data.frame("lat" = c(53.2780931659, 53.2804041456, 53.281325917, 53.2790149872),
                                                                 "long" = c( -9.0648465368, -9.0661543305, -9.0615979824, -9.0602901886)) 
    }
    
    #get the java script to generate the routes for each rav
    agent_routes <- run_java(isolate(input$no_ravs), clickedLocs, isolate(input$lat_spacing), isolate(input$lng_spacing))
    
    # 
    # #read the csvs that contain the routes for each agent
    points1 <-read.csv("./RCode/ShinyApp/Data/Agent1.csv", header = TRUE)
    leafletProxy("map") %>% addCircles(lng = points1$long, lat = points1$lat, weight=1, radius=7, color="black", fillColor="blue", popup = paste("RAV1",paste(points1$lat, points1$long))) %>% addPolylines(lng = points1$long, lat = points1$lat, weight=1, color="blue", fillColor="blue")
    if(isolate(input$no_ravs > 1)){
      points2 <- read.csv("./RCode/ShinyApp/Data/Agent2.csv")
      leafletProxy("map") %>% addCircles(lng = points2$long, lat = points2$lat, weight=1, radius=7, color="black", fillColor="green", popup = paste("RAV2",paste(points2$lat, points2$long))) %>% addPolylines(lng = points2$long, lat = points2$lat, weight=1, color="green", fillColor="green")
    }
    if(isolate(input$no_ravs > 2)){
      points3 <- read.csv("./RCode/ShinyApp/Data/Agent3.csv")
      leafletProxy("map") %>% addCircles(lng = points3$long, lat = points3$lat, weight=1, radius=7, color="black", fillColor="red", popup = paste("RAV3",paste(points3$lat, points3$long))) %>% addPolylines(lng = points3$long, lat = points3$lat, weight=1,color="red", fillColor="red")
    }
  })

  observeEvent(input$launch_agents,{
    # input = list()
    # input$no_ravs = 4
    # input$num_cameras = 4
    # input$rav_veloctiy = 20.4
    # input$rav_altitude = 37
    #run generate_routes.py in order to generate routes for agents
    setwd(paste(working_dir,"/PythonCode/PythonGridMapping/RoutePlotting", sep="", collapse=""))
    #generateUnrealPlotRoutes  -   no_ravs, no_cameras, rav_route_write_dir, saved_images_dir, gps_coords_write_dir
    gen_route_command <- paste(paste0(getwd(),("/generateUnrealPlotRoutes.py")), isolate(input$no_ravs), isolate(input$num_cameras), isolate(input$rav_veloctiy), isolate(input$rav_altitude), collapse="")
  
    print(paste("running python command", gen_route_command))
    system2("python", args = c(gen_route_command))
    
    showNotification("Agents ready to execute planned routes", duration = 10, type = "message")
    setwd(paste(working_dir, "/BatchScripts", collapse="", sep=""))
    noDrones = ifelse(isolate(input$no_ravs) == 1, "one", ifelse(isolate(input$no_ravs)==2, "two", "three"))
    system2(paste(noDrones,"_drone.bat", sep="", collapse=""))
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
    ## then do something like hide all the circles with hideGroup("circles")
    returnMap <- leafletProxy("map") %>% # use the proxy to save computation
      addCircles(lng=clng, lat=clat, group="circles",
                 weight=1, radius=8, color="black", fillColor="orange",
                 popup=address, fillOpacity=0.5, opacity=1)
    
    if(nrow(clickedLocs)>0){
      returnMap %>%addPolylines(data = clickedLocs, lng = ~long, lat = ~lat, weight = 2)
    }
    returnMap
  })
  
  output$processed_image <- renderImage({
    update_images()
    list(src = paste(getwd(), "/RCode/ShinyApp/www/mostRecentImageProcessed.jpg", sep=""),
         contentType = "image/png",
         width = 750,
         height = 750,
         alt = "No collected images to show")
  }, deleteFile = FALSE)
  
  output$unprocessed_image <- renderImage({
    update_images()
    list(src = paste(getwd(), "/RCode/ShinyApp/www/mostRecentImageRaw.jpg", sep=""),
         contentType = "image/png",
         width = 600,
         height = 600,
         alt = "No collected images to show")
  }, deleteFile = FALSE)
  
  observe({
    autoInvalidate()
    print("autoInvalidating")
    print(Sys.time())
    f_snapshot_new <<- fileSnapshot(paste(working_dir,"/RCode/ShinyApp/www/", sep="", collapse=""), md5sum = TRUE)
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
