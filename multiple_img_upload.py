import requests

def schedule_posts_with_unpublished_photos(page_id, page_access_token, message, photo_urls):
    # Step 1: Upload photos with published state set to false
    photo_ids = []
    for photo_url in photo_urls:
        upload_url = f'https://graph.facebook.com/v13.0/{page_id}/photos'
        params = {
            'access_token': page_access_token,
            'published': 'false',
            'url': photo_url,
        }

        try:
            response = requests.post(upload_url, params=params)
            result = response.json()

            if 'id' in result:
                photo_ids.append(result['id'])
            else:
                print(f"Error uploading photo: {result}")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    # Step 2: Use the IDs of unpublished photos to schedule a post
    url = f'https://graph.facebook.com/v13.0/me/feed'
    params = {
        'access_token': page_access_token,
        'message': message,
    }

    for photo_id in photo_ids:
        params[f'attached_media[{photo_id}]'] = f'{{"media_fbid":"{photo_id}"}}'

    try:
        response = requests.post(url, params=params)
        result = response.json()

        if 'id' in result:
            print(f"Post scheduled successfully. Post ID: {result['id']}")
        else:
            print(f"Error scheduling post: {result}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Replace with your actual values

page_id = 'YOUR_PAGE_ID'
page_access_token = 'YOUR_ACCESS_TOKEN'
message = 'Your message goes here'
photo_urls = [
    'https://example.com/photo1.jpg',
    'https://example.com/photo2.jpg',
]

schedule_posts_with_unpublished_photos(page_id, page_access_token, message, photo_urls)