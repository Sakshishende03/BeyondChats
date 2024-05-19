# citation_finder/utils.py
import requests

# citation_finder/utils.py

import requests

# def fetch_data_from_api():
#     url = "https://devapi.beyondchats.com/api/get_message_with_sources"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         print("API Response:", data)  # Debugging line
#         return data.get('data', {}).get('data', [])  # Adjusted to match the actual data structure
#     else:
#         print("Failed to fetch data from API, status code:", response.status_code)  # Debugging line
#         return None

# citation_finder/utils.py

import requests

def fetch_data_from_api():
    try:
        response = requests.get('https://devapi.beyondchats.com/api/get_message_with_sources')
        response.raise_for_status()  # Ensure we notice bad responses
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


# citation_finder/utils.py

# def identify_citations(api_response):
#     citations = []
#     for obj in api_response:
#         print("Processing object:", obj)  # Debugging line
#         response_text = obj.get('response', '')
#         sources = obj.get('source', [])
#         for source in sources:
#             context = source.get('context', '')
#             if context in response_text:
#                 citations.append({'id': source['id'], 'link': source.get('link', '')})
#     return citations


# citation_finder/utils.py

def identify_citations(api_response):
    try:
        citations_data = api_response['data']['data']
        citations = []
        for item in citations_data:
            citation = {
                'id': item['id'],
                'response': item['response'],
                'source': item['source']
            }
            citations.append(citation)
        return citations
    except KeyError as e:
        print(f"KeyError: {e}")
        return []




