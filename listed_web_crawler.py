import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, parse_qs, unquote

#print("First Block")
def get_channel_url(youtube_link):
    decoded_link = unquote(youtube_link)
    decoded_link = unquote(youtube_link)
    parsed_url = urlparse(decoded_link)
    query_params = parse_qs(parsed_url.query)
    # print(parsed_url)
    # query_params = parse_qs(parsed_url.query)
    # print(query_params)
    #print("inside function")
    if parsed_url.path == '/channel/' or parsed_url.path == '/user/':
        return youtube_link  # Already a channel URL
    
    if 'v' in query_params:
        video_id = query_params['v'][0]
        channel_url = f'https://www.youtube.com/channel/{video_id}'
        #print(channel_url)
        return channel_url
    else:
        return "None"
    
# The base URL for the Google search results page
base_url = "https://www.google.com/search?q=site%3Ayoutube.com+openinapp.co&start={}"

# The number of search results to scrape per page
results_per_page = 10

# The total number of pages to scrape (we want to scrape the first 1000 results)
num_pages=10

# A list to store the URLs of the scraped search results
urls = []

# Loop through each page of search results and scrape the URLs
#rint(type(num_pages))
#print(num_pages)
for i in range(num_pages):
    print("first loop")
    # Calculate the start index for the current page of search results
    start = i * results_per_page
    
    # Construct the URL for the current page of search results
    url = base_url.format(start)
    
    # Send a GET request to the URL and get the response
    response = requests.get(url)
    #print(response)
    # Use Beautiful Soup to parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    #print("hello world")
    # Find all the search result links on the page and add them to the list of URLs
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith("/url?q="):
            url = href.replace("/url?q=", "").split("&")[0]
            urls.append(url)
            
            # Stop the loop if we have reached the desired number of search results
            if len(urls) == 100:
                break
            
    # Stop the loop if we have reached the desired number of search results
    if len(urls) == 100:
        break
print("############################# Youtube Link ##################")
print(urls)
print("##############################################################")



#urls = ['https://www.youtube.com/c/OpeninApp', 'https://www.youtube.com/hashtag/openinapp', 'https://www.youtube.com/watch%3Fv%3DO6lup3SN4Bw', 'https://www.youtube.com/watch%3Fv%3DO6lup3SN4Bw', 'https://www.youtube.com/watch%3Fv%3D-GvsoRszRt4', 'https://www.youtube.com/watch%3Fv%3D-GvsoRszRt4', 'https://www.youtube.com/watch%3Fv%3DNjo_GPYbTvY', 'https://www.youtube.com/watch%3Fv%3DNjo_GPYbTvY', 'https://www.youtube.com/post/UgkxkNMzcb3UCWm4sfl1TtmpUE9eRv_qGnSj']
channel_list = []
for i in range(0,len(urls)):
  channel_url = get_channel_url(urls[i])
  if (channel_url == "None"):
     channel_list.append(urls[i])
  else: 
    channel_list.append(channel_url)

# if channel_url == youtube_link:
#     print('The provided URL is already a channel link.')
# else:
#     print('The channel URL:', channel_url)
#print(channel_list)


json_data = json.dumps(channel_list,indent=4)
print("############################# Channel Link ##################")
print(json_data)
print("##############################################################")