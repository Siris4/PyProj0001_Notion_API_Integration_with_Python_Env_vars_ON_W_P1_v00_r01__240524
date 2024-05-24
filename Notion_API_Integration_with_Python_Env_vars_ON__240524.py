import os
from notion_client import Client

# Read Notion API key and page ID from environment variables
notion_api_key = os.environ.get('NOTION_API_KEY_My_Selenium_Notion_Integration')
notion_page_id = os.environ.get('NOTION_PAGE_ID_My_Selenium_Notion_Integration')

# # Debug prints to check if environment variables are being retrieved correctly
print("Notion API Key:", notion_api_key)
print("Notion Page ID:", notion_page_id)

if not notion_api_key or not notion_page_id:
    raise ValueError("Environment variables NOTION_API_KEY and NOTION_PAGE_ID must be set")

# Initialize Notion client
notion = Client(auth=notion_api_key)


def test_integration_access():
    try:
        # Fetch the page
        page = notion.pages.retrieve(page_id=notion_page_id)
        print(f"Integration access confirmed. \n Page data:", page)

        # Check if the page has a title
        if 'properties' in page and 'title' in page['properties']:
            title_property = page['properties']['title']
            if title_property['type'] == 'title' and title_property['title']:
                print("Page title:", title_property['title'][0]['text']['content'])
            else:
                print("Page has no title or title format is unexpected")
        else:
            print("Page properties do not include a title")
    except Exception as e:
        print("Failed to access page:", e)


test_integration_access()
