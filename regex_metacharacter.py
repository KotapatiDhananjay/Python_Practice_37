import re
meaasge = "The current Python version is 3.13. Other previous versions are 3.12, 3.11, 3.10."

match_obj = re.search("[0-9][0-9]", meaasge)
print(match_obj)

match_obj = re.search("[0-9][0-9]", "House nuumber: 251/A")
print(match_obj)

match_obj = re.search("[0-9].[0-9][0-9]", meaasge)
print(match_obj)

# . matches any character except a new line character

message_1 = "The year is 2026"
match_obj = re.search("[0-9].[0-9][0-9]", message_1)
print(match_obj)
