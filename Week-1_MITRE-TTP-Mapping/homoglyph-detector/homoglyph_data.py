"""
Homoglyph character mappings for detection
"""

# Common homoglyph mappings - characters that look similar but are different Unicode
HOMOGLYPH_MAP = {
    # Cyrillic to Latin
    'а': 'a', 'с': 'c', 'е': 'e', 'о': 'o', 'р': 'p', 'х': 'x', 'у': 'y',
    'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H', 'К': 'K', 'М': 'M', 
    'О': 'O', 'Р': 'P', 'Т': 'T', 'Х': 'X',
    
    # Greek to Latin  
    'ο': 'o', 'α': 'a', 'ν': 'v', 'Α': 'A', 'Β': 'B', 'Ε': 'E', 'Η': 'H',
    'Ι': 'I', 'Κ': 'K', 'Μ': 'M', 'Ν': 'N', 'Ο': 'O', 'Ρ': 'P', 'Τ': 'T',
    'Χ': 'X', 'Υ': 'Y', 'Ζ': 'Z',
    
    # Number look-alikes
    'О': '0', 'l': '1', 'З': '3', 'Ч': '4', 'б': '6',
}

# Simple list of popular domains to check against
POPULAR_DOMAINS = [
    'google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'microsoft.com',
    'apple.com', 'twitter.com', 'instagram.com', 'linkedin.com', 'netflix.com',
    'github.com', 'paypal.com', 'ebay.com', 'wikipedia.org', 'reddit.com'
]
