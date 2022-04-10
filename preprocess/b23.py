import re


class B23WTF:
    """
    Convert Bilibili short URLs (b23.tv) to anti-tracking URLs (b23.tf).
    """

    def __init__(self):
        self.regex_pattern = re.compile(r'^(https:\/\/b23\.)tv(\/\w+)$')
        self.suffix = 'tf'
    
    def wtf(self, url: str):
        if self.regex_pattern.match(url):
            return self.regex_pattern.sub(f'\\1{self.suffix}\\2', url)
        return url
