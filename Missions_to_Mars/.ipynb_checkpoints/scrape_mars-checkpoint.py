{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import dependencies\n",
    "# pip install webdriver-manager\n",
    "# pip install splinter\n",
    "\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from splinter import Browser\n",
    "from selenium import webdriver\n",
    "\n",
    "# driver = webdriver.Chrome(ChromeDriverManager().install())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [C:\\Users\\Prueba.000\\.wdm\\drivers\\chromedriver\\win32\\91.0.4472.101\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "# Setup splinter\n",
    "\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Enter url to visit\n",
    "\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating beautiful soup\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title: **NASA's Perseverance Rover Will Look at Mars Through These 'Eyes'**\n",
      "Paragraph: A pair of zoomable cameras will help scientists and rover drivers with high-resolution color images.\n"
     ]
    }
   ],
   "source": [
    "# Scrapping news\n",
    "news_title = soup.find('div',class_='content_title').text\n",
    "news_p = soup.find('div', class_='article_teaser_body').text\n",
    "print(f'Title: **{news_title}**')\n",
    "print(f'Paragraph: {news_p}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL2 https://spaceimages-mars.com/\n",
    "\n",
    "# Enter url to visit\n",
    "\n",
    "url2 = 'https://spaceimages-mars.com/'\n",
    "browser.visit(url2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating beautiful soup\n",
    "\n",
    "# Question: html always has to be called html?\n",
    "\n",
    "html = browser.html\n",
    "soup2 = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://spaceimages-mars.com/image/featured/mars2.jpg\n"
     ]
    }
   ],
   "source": [
    "# Scrap and print featured image\n",
    "\n",
    "url3 = url2 + soup.find('img', class_='headerimage')['src']\n",
    "\n",
    "print(url3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Enter url to visit\n",
    "# URL4: https://galaxyfacts-mars.com/\n",
    "\n",
    "url4 = 'https://galaxyfacts-mars.com/'\n",
    "browser.visit(url4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "0                                   Mars            Earth\n",
       "Mars - Earth Comparison                                  \n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Scrape the table containing facts about the planet including Diameter, Mass, etc.\n",
    "# Use Pandas to convert the data to a HTML table string\n",
    "\n",
    "facts = pd.read_html(url4)\n",
    "mars_df = facts[0]\n",
    "mars_df.columns = mars_df.iloc[0]\n",
    "mars_df = mars_df.drop(0)\n",
    "mars_df = mars_df.set_index(['Mars - Earth Comparison'])\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Enter url to visit\n",
    "# URL5: https://marshemispheres.com/\n",
    "\n",
    "url5 = 'https://marshemispheres.com/'\n",
    "browser.visit(url5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating beautiful soup\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Set empty list\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# Variable with list of hemispheres\n",
    "hemispheres = soup.find_all(\"div\", class_=\"item\")\n",
    "\n",
    "# Loop\n",
    "\n",
    "for hemisphere in hemispheres:\n",
    "    \n",
    "    # Create dictionary\n",
    "    temp_dict = {}\n",
    "    \n",
    "    # Find and store titles\n",
    "    title = hemisphere.find(\"h3\").text\n",
    "    \n",
    "    hemispheres_img = hemisphere.find(\"a\", class_=\"itemLink product-item\")[\"href\"]\n",
    "    \n",
    "    # Visit the link that contains the full image website \n",
    "    browser.visit(url5 + hemispheres_img)\n",
    "    \n",
    "    # HTML Object\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "    \n",
    "    # Create full image url\n",
    "    img_url = url5 + soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "    \n",
    "    # Create temporary dictionary and store temporary info\n",
    "    temp_dict = {'title': title, 'img_url': img_url}\n",
    "    \n",
    "    # Append titles and images to a list\n",
    "    hemisphere_image_urls.append(temp_dict)\n",
    "    \n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
