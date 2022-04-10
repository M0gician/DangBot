import regex


class B23WTF:
    """
    Convert Bilibili short URLs (b23.tv) to anti-tracking URLs (b23.tf).
    """

    def __init__(self):
        self.full_share_pattern = regex.compile(r'^([\p{Han}\P{Han}]*)(https:\/\/b23\.)tv(\/\w+)$')
        self.url_only_pattern = regex.compile(r'^(https:\/\/b23\.)tv(\/\w+)$')
        self.suffix = 'tf'
    
    def valid(self, url) -> bool:
        return (self.url_only_pattern.match(url) is not None) or (self.full_share_pattern.match(url) is not None)

    def wtf(self, url: str):
        url = url.strip()
        if self.url_only_pattern.match(url):
            return self.url_only_pattern.sub(f'\\1{self.suffix}\\2', url)
        elif self.full_share_pattern.match(url):
            return self.full_share_pattern.sub(f'\\1\\2{self.suffix}\\3', url)
        return url
