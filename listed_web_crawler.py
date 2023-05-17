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

    
    if parsed_url.path == '/channel/' or parsed_url.path == '/user/':
        return youtube_link
    
    if 'v' in query_params:
        video_id = query_params['v'][0]
        channel_url = f'https://www.youtube.com/channel/{video_id}'
        #print(channel_url)
        return channel_url
    else:
        return "None"
    
base_url = "https://www.google.com/search?q=site%3Ayoutube.com+openinapp.co&start={}"

# The number of search results per page
results_per_page = 10

num_pages=1000

urls = []

#print(type(num_pages))
#print(num_pages)
for i in range(num_pages):
    # print("first loop")
    start = i * results_per_page
    
    url = base_url.format(start)
    
    response = requests.get(url)
    #print(response)
    
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    #print("hello world")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith("/url?q="):
            url = href.replace("/url?q=", "").split("&")[0]
            urls.append(url)
            
            # Stop the loop 
            if len(urls) == 10000:
                break
            
    # Stop the loop if we have reached the desired number of search results
    if len(urls) == 10000:
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

# converting list into json format

json_data = json.dumps(channel_list,indent=4)
print("############################# Channel Link ##################")
print(json_data)
print("##############################################################")