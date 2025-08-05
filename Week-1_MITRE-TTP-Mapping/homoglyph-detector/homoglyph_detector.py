"""
Simple homoglyph detector for domain names
"""
import unicodedata
from homoglyph_data import HOMOGLYPH_MAP, POPULAR_DOMAINS

class HomoglyphDetector:
    def __init__(self):
        self.homoglyph_map = HOMOGLYPH_MAP
        self.popular_domains = POPULAR_DOMAINS
    
    def detect_homoglyphs(self, domain):
        """
        Detect homoglyphs in a domain name
        Returns dictionary with detection results
        """
        result = {
            'domain': domain,
            'is_suspicious': False,
            'homoglyphs_found': [],
            'normalized_domain': self.normalize_domain(domain),
            'punycode': self.to_punycode(domain),
            'similar_to': None
        }
        
        # Find homoglyph characters
        for i, char in enumerate(domain):
            if char in self.homoglyph_map:
                result['homoglyphs_found'].append({
                    'position': i,
                    'character': char,
                    'looks_like': self.homoglyph_map[char],
                    'unicode_code': f'U+{ord(char):04X}'
                })
        
        # Check if similar to popular domain
        result['similar_to'] = self.find_similar_domain(result['normalized_domain'])
        
        # Mark as suspicious if homoglyphs found or similar to popular domain
        result['is_suspicious'] = len(result['homoglyphs_found']) > 0 or result['similar_to'] is not None
        
        return result
    
    def normalize_domain(self, domain):
        """Normalize domain using Unicode NFKC"""
        try:
            return unicodedata.normalize('NFKC', domain.lower())
        except:
            return domain.lower()
    
    def to_punycode(self, domain):
        """Convert domain to punycode"""
        try:
            return domain.encode('idna').decode('ascii')
        except:
            return domain
    
    def find_similar_domain(self, domain):
        """Find if domain is similar to any popular domain"""
        for popular in self.popular_domains:
            # Simple similarity check - if only 1-2 characters different
            if self.is_similar(domain, popular):
                return popular
        return None
    
    def is_similar(self, domain1, domain2):
        """Check if two domains are suspiciously similar"""
        if len(domain1) != len(domain2):
            return False
        
        differences = sum(1 for a, b in zip(domain1, domain2) if a != b)
        # Consider similar if 1-3 characters are different
        return 1 <= differences <= 3
    
    def create_safe_version(self, domain):
        """Convert homoglyphs to their Latin equivalents"""
        safe_domain = ""
        for char in domain:
            if char in self.homoglyph_map:
                safe_domain += self.homoglyph_map[char]
            else:
                safe_domain += char
        return safe_domain
