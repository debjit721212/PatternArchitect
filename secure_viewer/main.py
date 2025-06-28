from document import Document
from user import User
from proxy import AccessProxy

# Simulate users
guest = User("Alice", "guest")
user = User("Charlie", "user")
admin = User("Bob", "admin")

# Create document
doc = Document("Secrets", "Top Secret Data Here...")

# Create proxies
guest_proxy = AccessProxy(doc, guest)
user_proxy = AccessProxy(doc, user)
admin_proxy = AccessProxy(doc, admin)

print("\n--- Guest Tries to Access ---")
print(guest_proxy.display("Secrets"))  # Should be denied

print("\n--- User Tries to Access ---")
print(user_proxy.display("Secrets"))  # Should work

print("\n--- Admin Tries to Access ---")
print(admin_proxy.display("Secrets"))  # Should work

print("\n--- User Adds New Document ---")
user_proxy.add("PublicNotes", "General user notes")

print("\n--- Admin Displays New Document ---")
print(admin_proxy.display("PublicNotes"))

print("\n--- Admin Deletes Document ---")
admin_proxy.delete("Secrets")
print(admin_proxy.display("Secrets"))  # Should return not found

print("\n--- Guest Tries to Delete ---")
print(guest_proxy.delete("PublicNotes"))  # Should be denied

