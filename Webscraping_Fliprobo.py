#!/usr/bin/env python
# coding: utf-8

# # WebScraping Assignment of Flip Robo

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


import pandas as pd


# In[4]:


from bs4 import BeautifulSoup


# In[5]:


import requests


# In[159]:


wikepedia_page= requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[160]:


wikepedia_page


# #  1. Page Header content

# In[161]:


soup= BeautifulSoup(wikepedia_page.content)


# In[162]:


soup


# In[169]:


header = []
for i in bs.find_all(['h1', 'h2','h3','h4','h5','h6']):
    header.append(i.text)
    print(i.text)


# In[171]:


header


# In[174]:


Header_df = pd.DataFrame({'Headers title': header})


# In[175]:


Header_df


# # 2. President Webscraping 

# In[178]:


President_page= requests.get('https://presidentofindia.nic.in')


# In[179]:


President_page


# In[180]:


Soup = BeautifulSoup(President_page.content)
Soup


# In[185]:


President_name =  []
for i in Soup.find_all(['h3']):
    President_name.append(i.text)
    print(i.text)


# In[186]:


President_df = pd.DataFrame({'Former President Name': President_name})


# In[187]:


President_df


# # 3. Scrape Cricket Ranking

# In[189]:


Cricket_page= requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[191]:


SoupCricket = BeautifulSoup(Cricket_page.content)
SoupCricket


# In[199]:


Cricket_ODI_team =  []
for i in SoupCricket.find_all('span', class_="u-hide-phablet"):
    Cricket_ODI_team.append(i.text)
    print(i.text)


# In[230]:


Cricket_team_Matches_point =  []
Ind_point= SoupCricket.find('td', class_="rankings-block__banner--points")
Cricket_team_Matches_point.append(Ind_point.text)
Cricket_team_Matches_point


# In[231]:


k=1
for i in SoupCricket.find_all('td', class_="table-body__cell u-center-text"):
    if (k%2==0):
        print(i.text)
        Cricket_team_Matches_point.append(i.text)
        
    k=k+1


# In[232]:


Cricket_team_Matches_point


# In[236]:


Cricket_team_Matches_matches =  []
Ind_Matches= SoupCricket.find('td', class_="rankings-block__banner--matches")
Cricket_team_Matches_matches.append(Ind_Matches.text)
Cricket_team_Matches_matches


# In[237]:


l=1
for i in SoupCricket.find_all('td', class_="table-body__cell u-center-text"):
    if (l%2!=0):
        print(i.text)
        Cricket_team_Matches_matches.append(i.text)
        
    l=l+1


# In[238]:


Cricket_team_Matches_matches


# In[249]:


Cricket_team_Matches_Ratings =  []
Ind_Ratings= SoupCricket.find('td', class_="rankings-block__banner--rating u-text-right")
Ind_Ratings.text.strip()
Cricket_team_Matches_Ratings.append(Ind_Ratings.text.strip())
print(Ind_Ratings)
Cricket_team_Matches_Ratings


# In[321]:


for i in SoupCricket.find_all('td', class_="table-body__cell u-text-right rating"):
    print(i.text)
    Cricket_team_Matches_Ratings.append(i.text)

Cricket_team_Matches_Ratings


# In[253]:


Cricket_df= pd.DataFrame({'Team Name':Cricket_ODI_team, 'Matches':Cricket_team_Matches_matches,'Points':Cricket_team_Matches_point,'Ratings':Cricket_team_Matches_Ratings})


# In[254]:


Cricket_df


# In[258]:


Cricket_df=Cricket_df.head(10)


# ###### Top 10 teams

# In[259]:


Cricket_df


# ### Batsman Player rating

# In[322]:


MPlayer_cricket= requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')

Mplayer_soup = BeautifulSoup(response.content, "html.parser")
batsman_data = []
table = Mplayer_soup.find("table", class_="table rankings-table")
rows = table.find_all("tr")

for row in rows[1:11]:
  cells = row.find_all("td")
  batsman = cells[1].text.strip()
  team = cells[2].text.strip()
  rating = cells[3].text.strip()
  batsman_data.append([batsman, team, rating])

df = pd.DataFrame(batsman_data, columns=["Batsman", "Team", "Rating"])
print(df)


# #### Bowlers Rating
# 

# In[8]:


Bowlers_url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
Bowler_response = requests.get(Bowlers_url)
Bowler_soup = BeautifulSoup(Bowler_response.content, "html.parser")

bowler_data = []
table = Bowler_soup.find("table", class_="table")
rows = table.find_all("tr")

for row in rows[1:11]:
  cells = row.find_all("td")
  bowler = cells[1].text.strip()
  team = cells[2].text.strip()
  rating = cells[3].text.strip()
  bowler_data.append([bowler, team, rating])

df = pd.DataFrame(bowler_data, columns=["Bowler", "Team", "Rating"])
print(df)


# # 4. Women's Cricket
# 

# ####  Team Ranking

# In[9]:


url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

team_data = []
table = soup.find("table", class_="table")
rows = table.find_all("tr")

for row in rows[1:11]:
  cells = row.find_all("td")
  team = cells[1].text.strip()
  matches = cells[2].text.strip()
  points = cells[3].text.strip()
  rating = cells[4].text.strip()
  team_data.append([team, matches, points, rating])

df = pd.DataFrame(team_data, columns=["Team", "Matches", "Points", "Rating"])
print(df)


# ####  Batsman Ranking of Women team

# In[10]:


url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

batsman_data = []
table = soup.find("table", class_="table")
rows = table.find_all("tr")

for row in rows[1:11]:
  cells = row.find_all("td")
  batsman = cells[1].text.strip()
  team = cells[2].text.strip()
  rating = cells[3].text.strip()
  batsman_data.append([batsman, team, rating])

df = pd.DataFrame(batsman_data, columns=["Batsman", "Team", "Rating"])
print(df)


# ####  Bowler's Rating Women's team

# In[11]:


url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

bowler_data = []
table = soup.find("table", class_="table")
rows = table.find_all("tr")

for row in rows[1:11]:
  cells = row.find_all("td")
  bowler = cells[1].text.strip()
  team = cells[2].text.strip()
  rating = cells[3].text.strip()
  bowler_data.append([bowler, team, rating])

df = pd.DataFrame(bowler_data, columns=["Bowler", "Team", "Rating"])
print(df)


# # 5. News details Scraping

# In[43]:


url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the news articles on the page
articles = soup.find_all("div", class_="Card-titleContainer")

# Initialize empty lists to store the scraped data
headlines = []
times = []
links = []

# Extract Time:
for time_atr  in soup.find_all("span", class_="MarketNews-datePublished"):
    times.append(time_atr.text)
    print(time_atr.text)

# Loop through each article and extract the required information
for article in articles:
  # Extract the headline
  headline = article.find("a").text.strip()
  headlines.append(headline)

  
  # Extract the news link
  link = article.find("a")["href"]
  links.append(link)

# Create a dataframe using the scraped data
data = {
  "Headline": headlines,
#    "Time": times,
  "News Link": links
}
df = pd.DataFrame(data)

# Print the dataframe
print(df)


# #  6. Download AI articles in last 90 days

# In[36]:


url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the container that holds the article details
articles_container = soup.find("div", class_="sc-orwwe2-3 jOMrrY")

# Initialize empty lists to store the scraped data
titles = []
authors = []
dates = []
urls = []

# Iterate over each article in the container
for article in articles_container.find_all("li"):
  # Scrape the title
  title = article.find("h2").text.strip()
  titles.append(title)
  
  # Scrape the authors
  author = article.find("span", class_="sc-1w3fpd7-0 dnCnAO").text.strip()
  authors.append(author)
  
  # Scrape the published date
  date = article.find("span", class_="sc-1thf9ly-2 dvggWt").text.strip()
  dates.append(date)
  
  # Scrape the paper URL
  url = article.find("a")["href"]
  urls.append(url)

# Create a dataframe with the scraped data
data = {
  "Paper Title": titles,
  "Authors": authors,
  "Published Date": dates,
  "Paper URL": urls
}
df = pd.DataFrame(data)

# Print the dataframe
print(df)


# # 7.Dineput Data frame

# In[38]:


url = "https://www.dineout.co.in"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements containing the details you want to scrape
restaurant_names = soup.find_all('h2', class_='restnt-name ellipsis')
cuisines = soup.find_all('span', class_='double-line-ellipsis')
locations = soup.find_all('span', class_='double-line-ellipsis')
ratings = soup.find_all('span', class_='rating-value')
image_urls = soup.find_all('img', class_='img-responsive')

# Create empty lists to store the scraped data
restaurant_list = []
cuisine_list = []
location_list = []
rating_list = []
image_url_list = []

# Extract the data from the elements and append them to the respective lists
for name in restaurant_names:
  restaurant_list.append(name.text.strip())

for cuisine in cuisines:
  cuisine_list.append(cuisine.text.strip())

for location in locations:
  location_list.append(location.text.strip())

for rating in ratings:
  rating_list.append(rating.text.strip())

for image in image_urls:
  image_url_list.append(image['src'])

# Create a dictionary from the lists
data = {
  'Restaurant Name': restaurant_list,
  'Cuisine': cuisine_list,
  'Location': location_list,
  'Ratings': rating_list,
  'Image URL': image_url_list
}

# Create a dataframe from the dictionary
df = pd.DataFrame(data)

# Print the dataframe
print(df)


# ###  Hi Team, code no. 7 is not working coz URL is not working in UK , that's why its not access any of the data. Please find the code above but as URL not working so can't gether any of the data.
