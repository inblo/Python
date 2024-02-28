phone_book = {}
path = '/Users/Augur/Documents/Python/PhoneBook/phones.txt'
SEPARATOR = ';'

def open_phone_book():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for u_id, contact in enumerate(data, 1):
        phone_book[u_id] = contact.strip().split(SEPARATOR)

def save_phone_book():
    global phone_book
    data = []
    for contacts in phone_book.values():
        data.append(SEPARATOR.join(contacts))
    data = '\n'.join(data)
    with open(path, 'w', encoding=U'TF-8') as file:
        file.write(data)

def _next_id():
    global phone_book
    return max(phone_book) + 1 if phone_book else 1

def add_new_contact(new_contact: list[str]):
    global phone_book
    phone_book[_next_id()] = new_contact

def find_contact(serch_word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if serch_word.lower() in ' '.join(contact).lower():
            result[u_id] = contact
    return result

def edit_contact(u_id: int, edit_contact: list[str]):
    global phone_book
    current_contact = phone_book[u_id]
    for i in range(len(current_contact)):
        current_contact = edited_contact[i] if edited_contact[i] else current_contact[i]
        phone_book[u_id] = current_contact
        return current_contact[0]

def delete_contact(u_id: int) -> str:
    global phone_book
    return phone_book.pop(u_id)[0 ]




