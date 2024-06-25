class SameSiteCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        for cookie in response.cookies.values():
            cookie['samesite'] = 'None'
            cookie['secure'] = True
        return response
