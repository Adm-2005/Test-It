from flask import url_for
from typing import Dict, Any

def pagination_links(endpoint: str, total_count: int, page: int, per_page: int) -> Dict[str, Any]:
    """
    Creates a dictionary containing paginated links.

    Args:
        endpoint: name of the endpoint function.
        total_count: total number of documents received from query.
        page: current page.
        per_page: number of items per page.

    Returns:
        [Dict[str, Any]]: links dictionary.
    """
    links = {
        'self': { 'href': url_for(endpoint, page=page, _external=True) },
        'last': { 'href': url_for(endpoint, page=(total_count // per_page) + 1, _external=True) }
    }

    if page > 1: 
        links['prev'] = {
            'href': url_for(endpoint, page=page - 1, _external=True)
        }
    if page - 1 < total_count // per_page:
        links['next'] = {
            'href': url_for(endpoint, page=page + 1, _external=True)
        }

    return links