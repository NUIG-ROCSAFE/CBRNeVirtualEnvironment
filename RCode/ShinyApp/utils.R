################### Put this in config ###################

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

working_dir <<- paste(getwd(), '/../..', sep = '')
blog_code_loc <<- paste(working_dir, "/BlogCode", sep ='')
end_of_file <- readtext(paste(blog_code_loc, "/ChemProbReasoningSecondHalf.txt", sep = ''))$text 

################### Put this in config ###################

concat_paths <- function(arg1,...){
  inargs <- paste(arg1, ..., sep = "/")
  inargs <- str_replace_all(string = inargs, pattern = "\\\\", replacement = "/")
  inargs <- str_replace_all(string = inargs, pattern = "///", replacement = "/")
  inargs <- str_replace_all(string = inargs, pattern = "//", replacement = "/")
  return(inargs)
}

display_err <- function(err_title, err_msg) {
  shinyalert(err_title, err_msg, type = "error")
}

RAVIcon <- makeIcon(
  iconUrl = concat_paths(getwd(), "/www/RAVIcon.png"),
  iconWidth = 35, iconHeight = 35,
  iconAnchorX = 0, iconAnchorY = 0
)

check_dir_exists <- function(path, err_type, msg) {
  if(isFALSE(dir.exists(path))){
    display_err(err_type, msg)
  }
}

check_file_exists <- function(filepath, err_type, msg) {
  if(isFALSE(file.exists(filepath))){
    display_err(err_type, msg)
  }
}

check_config <- function(working_dir, config) {
  err_type <- ""
  
  # [JAVA]
  err_type <- "Java Error"
  if(config$JAVA$JavaBinLoc == ""){
    x <- system("java -h")
    if(x == 127){
      display_err(err_type, "Could not find 'java' in PATH environment variable. Please fix PATH or enter java bin destination Config/config.ini [JAVA] JavaBinLoc.")
    }
  }
  else {
    check_file_exists(concat_paths(config$JAVA$JavaBinLoc, "java"), err_type, "Please fix [JAVA] JavaBinLoc in Config/config.ini.")
  }
  check_file_exists(concat_paths(working_dir, config$JAVA$JavaCodeLoc, config$JAVA$JavaMissionDesignerJar), err_type, "Please fix [JAVA] JavaCodeLoc/JavaMissionDesignerJar in Config/config.ini.")
  
  # [BLOG]
  err_type <- "Blog Error"
  if(config$BLOG$BlogBinLoc  == ""){
    x <- system("blog -h")
    if(x == 127){
      display_err(err_type, "Could not find 'blog' in PATH environment variable. Please fix PATH or enter blog bin destination Config/config.ini [BLOG] BlogBinLoc.")
    }
  }
  else {
    check_file_exists(concat_paths(config$BLOG$BlogBinLoc, "blog"), err_type, "Please fix [BLOG] BlogBinLoc in Config/config.ini.")
  }
  check_file_exists(concat_paths(working_dir, config$BLOG$BlogCodeLoc, config$BLOG$BlogProgName), err_type, "BlogCodeLoc/BlogProgName doesn't exist, please fix [BLOG] BlogCodeLoc/BlogProgName in Config/config.ini.")

  # [PYTHON]
  err_type <- "Python Error"
  x <- system(paste(config$PYTHON$PythonExe, " -V", sep = ""))
  if(x == 127){
    display_err(err_type, sprintf("Could not find '%s' in PATH environment variable. Please fix PATH or change PythonExe in Config/config.ini.", config$PYTHON$PythonExe))
  }
  check_dir_exists(concat_paths(working_dir, config$PYTHON$PythonDocRetrievalCodeLoc), err_type, "PythonDocRetrievalCodeLoc doesn't exist, please fix [PYTHON] PythonDocRetrievalCodeLoc  in Config/config.ini.")
  check_file_exists(concat_paths(working_dir, config$PYTHON$PythonDocRetrievalCodeLoc, config$PYTHON$PythonElasticMain ), err_type, "PythonElasticMain doesn't exist, please fix [PYTHON] PythonElasticMain in Config/config.ini.")
  
  check_dir_exists(concat_paths(working_dir, config$PYTHON$PythonRAVRouteExecutionDir), err_type, "PythonRAVRouteExecutionDir doesn't exist, please fix [PYTHON] PythonRAVRouteExecutionDir  in Config/config.ini.")
  check_dir_exists(concat_paths(working_dir, config$PYTHON$PythonGenerateRouteDir), err_type, "PythonGenerateRouteDir doesn't exist, please fix [PYTHON] PythonGenerateRouteDir in Config/config.ini.")
  check_file_exists(concat_paths(working_dir, config$PYTHON$PythonGenerateRouteDir, config$PYTHON$PythonGenerateRoutesFileLoc), err_type, "PythonGenerateRouteDir/PythonGenerateRoutesFileLoc doesn't exist, please fix [PYTHON] PythonGenerateRoutesFileLoc in Config/config.ini.")
  
  # [BATCHSCRIPTS]
  err_type <- "BatchScripts Error"
  check_dir_exists(concat_paths(working_dir, config$BATCHSCRIPTS$BatchScriptsLoc), err_type, sprintf("%s doesn't exist, please fix [BATCHSCRIPTS] BatchScriptsLoc in Config/config.ini.", concat_paths(working_dir, config$BATCHSCRIPTS$BatchScriptsLoc)))
  
  # [DATA]
  err_type <- "Data Error"
  check_dir_exists(concat_paths(working_dir, config$DATA$RAVGPSRoutesDir), err_type, sprintf("%s doesn't exist, please fix [DATA] RAVGPSRoutesDir in Config/config.ini.", concat_paths(working_dir, config$DATA$RAVGPSRoutesDir)))
  check_dir_exists(concat_paths(working_dir, config$DATA$CollectedPNGImagesDir), err_type, sprintf("%s doesn't exist, please fix [DATA] CollectedPNGImagesDir in Config/config.ini.", concat_paths(working_dir, config$DATA$CollectedPNGImagesDir)))
  check_dir_exists(concat_paths(working_dir, config$DATA$RAVRecordedGPSWaypoints), err_type, sprintf("%s doesn't exist, please fix [DATA] RAVRecordedGPSWaypoints in Config/config.ini.", concat_paths(working_dir, config$DATA$RAVRecordedGPSWaypoints )))
  check_dir_exists(concat_paths(working_dir, config$DATA$UIImagesDir), err_type, sprintf("%s doesn't exist, please fix [DATA] UIImagesDir  in Config/config.ini.", concat_paths(working_dir, config$DATA$UIImagesDir  )))
  check_dir_exists(concat_paths(working_dir, config$DATA$GPSPlannedAgentRoutesDir), err_type, sprintf("%s doesn't exist, please fix [DATA] GPSPlannedAgentRoutesDir  in Config/config.ini.", concat_paths(working_dir, config$DATA$GPSPlannedAgentRoutesDir  )))
  
}


run_blog <- function(blog_code_loc, blog_prog_name, blog_bin_loc, working_dir, odors_input, nerve_agents_input, dispersion_methods_input){
  print("blog_code_loc")
  print(concat_paths(blog_code_loc, blog_prog_name))
  blog_file <- readtext(concat_paths(blog_code_loc, blog_prog_name))
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
  
  print('blog_bin_log')
  print(blog_bin_loc)
  if(blog_bin_loc != ""){
    setwd(blog_bin_loc)
  }
  blog_code_output <- system2('blog', args=c (paste(blog_code_loc,'/ChemicalProbablisticReasoning.blog',sep='')), stdout= TRUE, wait= TRUE)
  setwd(working_dir)
  #write the result of the blog program
  writeLines(blog_code_output, paste(blog_code_loc,"/output.txt", sep=''))
}

run_java <- function(java_bin_loc, java_code_loc, java_prog_name, working_dir, write_dir, no_ravs, locs, lat_spacing, lng_spacing){
  print("java_bin_loc: ")
  print(java_bin_loc)
  if(java_bin_loc != ""){
    setwd(java_bin_loc)
  }
  
  #add jar and code location
  #argsString <- paste("-jar", str_replace(java_code_loc, '/', '\\\\'))
  argsString <- paste("-jar", java_code_loc)
  
  
  #pass in the working directory to the java code
  print(java_prog_name)
  argsString <- paste(argsString, java_prog_name, sep='')
  argsString <- paste(argsString, working_dir)
  argsString <- paste(argsString, write_dir)
  argsString <- paste(argsString, no_ravs)
  
  argsString <- paste(argsString, lat_spacing)
  argsString <- paste(argsString, lng_spacing)
  
  #dat$lat <- c(53.28323, 53.28215, 53.27884, 53.27887, 53.28164)
  #dat$long <- c(-9.062691,-9.055781,-9.057240,-9.065051,-9.067411)
  
  argsString = paste(argsString, paste(locs$lat, locs$long, sep = ' ', collapse = ' '))
  print(paste("Calling java", argsString))
  agent_route_analysis <<- system2("java", args = c(argsString), stdout = TRUE, wait = TRUE)
  
  print(agent_route_analysis)
  if(length(agent_route_analysis) == 4) {
    display_err("Java Error", "Cannot create a polygon with less than 3 vertices.")
  }
  setwd(working_dir)
  return(agent_route_analysis)
}

gen_airsim <- function(python_exe, python_code_loc) {
  argString <- concat_paths(python_code_loc, "gen_airsim.py")
  argString <- paste(python_exe, argString, concat_paths(working_dir, "Config/settings.json"), sep=" ")
  print(argString)
  system(argString)
}

run_elasticMain <- function(python_exe, python_code_loc, script_name, search_terms){
  err_type <- "Elastic Search Error."
  print(search_terms)
  if(is.null(search_terms)){
    display_err(err_type, "Please select a search item.")
    return()
  }
  print("search terms:")
  print(search_terms)
  #build up args to send to python
  argString <- paste(search_terms, collapse = ' ')
  argString <- paste(concat_paths(python_code_loc, script_name), argString, collapse = ' ')
  print(paste("Calling python with arguments: ", argString))
  #run elastic main
  result <- system2(python_exe, args = argString)
  print(result)
  if(result == 1) {
    display_err(err_type, "Elastic search is not running correctly, make sure elastic search is running on port 9200.")
  }
}