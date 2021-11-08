class Solution:
    def numUniqueEmails(self, emails) -> int:
        output=set()
        for i in emails:
            local_name,domain_name=i.split("@")      
            local_name = local_name.split('+')[0].replace(".","")
            output.add(local_name+"@"+domain_name)
        return len(output)