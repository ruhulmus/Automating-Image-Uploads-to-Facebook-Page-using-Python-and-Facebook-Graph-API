import requests

def post_single_photo(page_id, page_access_token, message, photo_url):
    url = f"https://graph.facebook.com/v13.0/{page_id}/photos"
    params = {
        'access_token': page_access_token,
        'message': message,
        'url': photo_url,
    }

    try:
        response = requests.post(url, params=params)
        result = response.json()

        if 'id' in result:
            print(f"Photo posted successfully. Post ID: {result['id']}")
        else:
            print(f"Error posting photo: {result}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Replace with your actual values

page_id = 'YOUR_PAGE_ID'
page_access_token = 'YOUR_ACCESS_TOKEN'
message = 'Your message goes here'
photo_url = 'https://example.com/your-photo.jpg'

post_single_photo(page_id, page_access_token, message, photo_url)