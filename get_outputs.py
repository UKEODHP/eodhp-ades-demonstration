import requests

workspace = ''
ades_job_id = ''
workspace_token = ''
path_to_file = f'processing-results/cat_{ades_job_id}.json'
ades_output_url = f"https://{workspace}.workspaces.test.eodhp.eco-ke-staging.com/files/eodhp-test-workspaces1/{path_to_file}"
user_block_store_url = f'https://{workspace}.workspaces.test.eodhp.eco-ke-staging.com/files/workspaces/{path_to_file}'


def get_outputs_token(url: str, token: str):
    """Send a request with token in Authorization header."""
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.headers)
    print("--------------------")
    print(response.text)

def get_outputs_range(url: str, token: str):
    """Send a request with token in Authorization header and Range header."""
    headers = {
        'Authorization': f'Bearer {token}',
        'Range': 'bytes=4-8'  # Request specific bytes of the file
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.headers)
    print("--------------------")
    print(response.content)

def get_outputs_cookie(url: str, token: str):
    """Send a request with token in a cookie."""
    cookies = {'session': token}
    response = requests.get(url, cookies=cookies)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    get_outputs_token(ades_output_url, workspace_token)
