class Contact:
   def __init__(self, name, phone_number, email):
      self.name = name
      self.phone_number = phone_number
      self.email = email
      self.favorite = False

def view_options():
   print('[1]. View contacts')
   print('[2]. Add contact')
   print('[3]. Edit contact')
   print('[4]. Mark contact as a favorite')
   print('[5]. View favorite contacts')
   print('[6]. Delete contact')
   print('[7]. Exit')
   
def view_contacts(contacts):
   if not contacts:
         print('No contacts')
   else:
      print('Contacts:')
      for index, contact in enumerate(contacts):
         print(f'[{index + 1}]. Name: {contact.name}')
         print(f'Phone number: {contact.phone_number}')
         print(f'Email: {contact.email}')
         print(f'Favorite: {contact.favorite}')
         print('-------------------')

contacts = []
option = -1
while option != 7:
   view_options()
   choice = int(input('Enter an option: '))
   
   match choice:
      case 1:
         view_contacts(contacts)
            
      case 2:
         name = input('Enter name: ')
         phone_number = input('Enter phone number: ')
         email = input('Enter email: ')
         contact = Contact(name, phone_number, email)
         contacts.append(contact)
         print('Contact added!')
      
      case 3:
         print('Edit contact')   

      case 4:
         print('Mark contact as a favorite')
      
      case 5:
         print('View favorite contacts')
      
      case 6:
         print('Delete contact')
      
      case 7:
         print('Goodbye!')
      
      case _:
         print('Invalid option')
