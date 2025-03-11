class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        
        email_set = set()

        for email in emails:
            
            email = email.split("@")
            local_name = email[0]
            domain_name = email[1]

            if("+" in local_name):
                local_name = local_name[0 : local_name.index("+")]
            
            if("." in local_name):
                local_name = local_name.replace(".", "")

            email_set.add(local_name + "@" + domain_name)

        return len(email_set)