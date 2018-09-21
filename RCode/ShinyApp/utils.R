RAVIcon <- makeIcon(
  iconUrl = paste(getwd(), "./RCode/ShinyApp/www/RAVIcon.png", sep = ''),
  iconWidth = 30, iconHeight = 30,
  iconAnchorX = 0, iconAnchorY = 0
  #shadowUrl = "http://leafletjs.com/examples/custom-icons/leaf-shadow.png",
  #shadowWidth = 50, shadowHeight = 64,
  #shadowAnchorX = 4, shadowAnchorY = 62
)

f_snapshot_old <<- fileSnapshot("./RCode/ShinyApp/Data/Images/", md5sum = TRUE)

run_blog <- function(odors_input, nerve_agents_input, dispersion_methods_input){
  blog_file <- readtext(paste(blog_code_loc,"/ChemicalProbablisticReasoning.blog", sep=''))
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
  
  dispersal_str = paste(paste(paste("obs", names(dispersal_methods_selected)), tolower(as.character(dispersal_methods_selected)), sep = '=', collapse = ';\n'),';', sep = '')
  agent_str = paste(paste(paste("obs", names(agents_selected)), tolower(as.character(agents_selected)), sep = '=', collapse = ';\n'), ';', sep = '')
  odor_str = paste(paste(paste("obs", names(odors_selected)), tolower(as.character(odors_selected)), sep = '=', collapse = ';\n'), ';', sep = '')
  
  #paste all of the selected observations to create the string to write to the blog file
  write_string = paste(odor_str, agent_str, dispersal_str, sep = '\n\n')
  write_string <- paste(write_string, end_of_file, collapse = '\n')
  writeLines(write_string, file(paste(blog_code_loc,"/ChemicalProbablisticReasoning.blog", sep='')))
  
  
  setwd(blog_bin_loc)
  blog_code_output <- system2('blog', args=c (paste(blog_code_loc,'/ChemicalProbablisticReasoning.blog',sep='')), stdout= TRUE, wait= TRUE)
  setwd(working_dir)
  #write the result of the blog program
  writeLines(blog_code_output, paste(blog_code_loc,"/output.txt", sep=''))
}

run_java <- function(no_ravs, locs, lat_spacing, lng_spacing){
  setwd(java_bin_loc)
  
  #add jar and code location
  argsString <- paste("-jar", str_replace(java_code_loc, '/', '\\\\'))
  #pass in the working directory to the java code
  argsString <- paste(argsString, java_prog_name, sep='')
  argsString <- paste(argsString, working_dir)
  argsString <- paste(argsString, no_ravs)
  
  argsString <- paste(argsString, lat_spacing)
  argsString <- paste(argsString, lng_spacing)
  
  #dat$lat <- c(53.28323, 53.28215, 53.27884, 53.27887, 53.28164)
  #dat$long <- c(-9.062691,-9.055781,-9.057240,-9.065051,-9.067411)
  
  argsString = paste(argsString, paste(locs$lat, locs$long, sep = ' ', collapse = ' '))
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
  argString <- paste(search_terms, collapse = ' ')
  argString <- paste(python_prog_name, argString, collapse = ' ')
  print(paste("Calling python with arguments: ", argString))
  #run elastic main
  setwd(python_code_loc)
  result <- system2("python", args = argString)
  print(result)
}