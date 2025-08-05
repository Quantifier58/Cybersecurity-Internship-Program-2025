"""
Demo script showing homoglyph detection in action
"""
from homoglyph_detector import HomoglyphDetector

def main():
    detector = HomoglyphDetector()
    
    # Test domains - mix of legitimate and suspicious
    test_domains = [
        'google.com',           # Legitimate
        'ɡοοɡlе.com',          # Homoglyph attack (mixed Greek/Latin)
        'аmazon.com',          # Cyrillic 'а' instead of Latin 'a'  
        'payрal.com',          # Cyrillic 'р' instead of Latin 'p'
        'facebοοk.com',        # Greek 'ο' instead of Latin 'o'
        'micrοsoft.com',       # Greek 'ο' instead of Latin 'o'
        'github.com',          # Legitimate
        'gοοgle.com'           # Greek 'ο' instead of Latin 'o'
    ]
    
    print("Homoglyph Domain Detector Demo")
    print("=" * 50)
    
    for domain in test_domains:
        print(f"\n Analyzing: {domain}")
        result = detector.detect_homoglyphs(domain)
        
        # Show results
        if result['is_suspicious']:
            print(" SUSPICIOUS DOMAIN DETECTED")
        else:
            print(" Domain appears legitimate")
        
        # Show punycode if different
        if result['punycode'] != domain:
            print(f"Punycode: {result['punycode']}")
        
        # Show homoglyphs found
        if result['homoglyphs_found']:
            print("  Homoglyphs detected:")
            for homoglyph in result['homoglyphs_found']:
                print(f"   Position {homoglyph['position']}: '{homoglyph['character']}' "
                      f"({homoglyph['unicode_code']}) looks like '{homoglyph['looks_like']}'")
        
        # Show if similar to popular domain
        if result['similar_to']:
            print(f" Similar to popular domain: {result['similar_to']}")
            safe_version = detector.create_safe_version(domain)
            print(f" Safe version would be: {safe_version}")

if __name__ == "__main__":
    main()
