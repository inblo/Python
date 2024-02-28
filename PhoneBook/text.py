main_menu = ['Главное меню', 'Открыть телефонную книгу', 
'Сохранить телефонную книгу', 'Показать контакты', 
'Создать контакт', 'Найти контакт', 'Изменить контакт', 
'Удалить контакт', 'Выход']

choice_main_menu = f'Выберете пункт меню ({1} - {len(main_menu)-1}):'
choice_main_menu_error = f'Нужно ввести число от 1 до {len(main_menu)-1}!'

phone_book_opened_sucessful  =  'Телефонная книга успешно открыта!'
phone_book_saved_sucessful  =  'Телефонная книга успешно сохранена!'

empty_phone_book_error = 'Телефонная книга пуста или не открыта!'

input_new_contact = ['Введите имя контакта:', 'Введите номер контакта', 'Введите комментарий для контакта']

input_serch_word = 'Введите слово для поиска: '

input_serch_word_for_edit = 'Введите слово для поиска контакта, которое хотите изменить: '

input_serch_word_for_delete = 'Введите слово для поиска контакта, которое хотите удалить: '

input_id_for_edit =  'Введите ID контакта, который хотите изменить: '

input_id_for_delete =  'Введите ID контакта, который хотите удалить: '

no_changes = 'Введите ENTERчтобы оставить без изменений!'

edit_contact = [f'Введите новое имя ({no_changes}): ', 
               f'Введите новый номер контакта ({no_changes}): ',
               f'Введите новый комментарий ({no_changes}): ']

def new_contact_added_successfull(name: str) -> str:
     return f'Контакт "{name}" успешно добавлен!'

def find_contact_no_result(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'

def edit_contact_successfull(name) -> str:
     return f'Контакт "{name}" успешно изменен!'

def delete_contact_successfull(name) -> str:
     return f'Контакт "{name}" успешно удален!'