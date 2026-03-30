class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for email in emails:
            _email, domain = email.split("@")
            cleaned_email = _email.replace(".", "")
            cleaned_email = cleaned_email.split("+")[0]
            uniques.add(cleaned_email + "@" + domain)
        
        return len(uniques)