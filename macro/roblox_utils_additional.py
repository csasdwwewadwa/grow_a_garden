import urllib.parse

def generate_private_server_login_link(private_server_link):
    # Parse the query parameters from the private_server_link
    parsed_url = urllib.parse.urlparse(private_server_link)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    code = query_params.get("code", [None])[0]
    type_ = query_params.get("type", [None])[0]

    if not code or not type_:
        raise ValueError("Invalid private_server_link. Missing code or type.")

    # Construct the deep link URL
    return_url = (
        f"https://www.roblox.com/share-links?code={code}&type={type_}"
        f"&pid=share&is_retargeting=false"
        f"&deep_link_value=roblox://navigation/share_links?code={code}&type={type_}"
    )

    # URL encode the return_url
    encoded_return_url = urllib.parse.quote(return_url, safe='')

    # Construct the final login link
    login_link = f"https://www.roblox.com/login?returnUrl={encoded_return_url}"

    return login_link