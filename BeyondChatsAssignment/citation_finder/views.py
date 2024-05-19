from django.shortcuts import render

# Create your views here.
# citation_finder/views.py

# citation_finder/views.py

# citation_finder/views.py

# from django.shortcuts import render
# from .utils import fetch_data_from_api, identify_citations
#
#
# def citations(request):
#     api_response = fetch_data_from_api()
#     if api_response is not None:
#         citations = identify_citations(api_response)
#     else:
#         citations = []
#
#     print("Citations:", citations)  # Ensure data is correct
#     return render(request, 'testapp/citations.html', {'citations': citations})

# citation_finder/views.py

from django.shortcuts import render
from .utils import fetch_data_from_api, identify_citations

def citations(request):
    api_response = fetch_data_from_api()
    print("API Response:", api_response)  # Debugging statement

    if api_response is not None:
        citations = identify_citations(api_response)
    else:
        citations = []

    print("Citations:", citations)  # Debugging statement
    return render(request, 'testapp/citations.html', {'citations': citations})
