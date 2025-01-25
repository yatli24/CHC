library(conflicted)
library(rvest)
library(polite)
library(xml2)
library(xfun)

url <- c("https://data.chc.ucsb.edu/people/laura/DSCapstone_2025/Data/NMME/COLA-RSMAS-CESM1/prec/")

html <- read_html(url)

links <- html %>% 
  html_elements("a") %>% 
  html_attr('href')

links <- links[6:407]

for (i in 1:1){
  new_url = paste(url, links[i], sep="")
  download_file(new_url, output = paste('/data/', links[i], sep=''))
}