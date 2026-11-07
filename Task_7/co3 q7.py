import time

def normalize_phone(phone):
    if not phone:
        return ""

    digits = ''.join(c for c in str(phone) if c.isdigit())

    if len(digits) == 10:
        return "91" + digits

    if len(digits) == 11 and digits.startswith("0"):
        return "91" + digits[1:]

    return digits


def normalize_email(email):
    return email.strip().lower() if email else ""


def merge_contacts(contacts):

    phone_dict = {}
    email_dict = {}
    groups = {}
    parent = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[b] = a
            groups[a]["phones"].update(groups[b]["phones"])
            groups[a]["emails"].update(groups[b]["emails"])
            groups[a]["names"].update(groups[b]["names"])

    for contact in contacts:

        name = contact.get("name", "").strip()
        phones = {
            normalize_phone(p)
            for p in contact.get("phones", [])
            if normalize_phone(p)
        }

        emails = {
            normalize_email(e)
            for e in contact.get("emails", [])
            if normalize_email(e)
        }

        matches = set()

        for p in phones:
            if p in phone_dict:
                matches.add(find(phone_dict[p]))

        for e in emails:
            if e in email_dict:
                matches.add(find(email_dict[e]))

        if not matches:
            group_id = len(parent)
            parent[group_id] = group_id

            groups[group_id] = {
                "names": set(),
                "phones": set(),
                "emails": set()
            }
        else:
            group_id = matches.pop()

            for other in matches:
                union(group_id, other)

            group_id = find(group_id)

        group_id = find(group_id)

        if name:
            groups[group_id]["names"].add(name)

        groups[group_id]["phones"].update(phones)
        groups[group_id]["emails"].update(emails)

        for p in phones:
            phone_dict[p] = group_id

        for e in emails:
            email_dict[e] = group_id

    result = []

    for group_id in groups:
        root = find(group_id)

        if root == group_id:
            result.append(groups[root])

    return result


# Test data
contacts = [
    {
        "name": "Dr. Ravi",
        "phones": ["+91 98400 12345"],
        "emails": ["ravi@gmail.com"]
    },
    {
        "name": "Ravi Kumar",
        "phones": ["9840012345", "9876543210"],
        "emails": ["ravi@gmail.com"]
    },
    {
        "name": "Arun",
        "phones": ["9876500000"],
        "emails": ["arun@gmail.com"]
    }
]

start = time.perf_counter()

result = merge_contacts(contacts)

end = time.perf_counter()

for contact in result:
    print(contact)

print("Execution time:", end - start)