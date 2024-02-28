import view
import model
import text

def find_contacts(message):
    serch_word = view.input_data(message)
    result = model.find_contact(serch_word)
    view.show_contacts(result, text.find_contact_no_result(serch_word))
    return True if result else False 


def start_app():
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1: 
                model.open_phone_book()
                view.show_message(text.phone_book_opened_sucessful)
            case 2 : 
                model.save_phone_book()
                view.show_message(text.phone_book_saved_sucessful)
            case 3: 
                view.show_contacts(model.phone_book, empty_phone_book_error)
            case 4: 
                new_contact = view.input_data(text.input_new_contact) 
                model.add_new_contact(new_contact)
                view.show_message(text.new_contact_added_successfull(new_contact[0]))
            case 5: 
                find_contacts(text.input_serch_word)
            case 6:
                if find_contacts(text.input_serch_word_for_edit):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edit_contact = view.input_data(text.edit_contact)
                    name = model.edit_contact(u_id)
                    view.show_message(text.edit_contact_successfull(name))
            case 7: 
                if find_contacts(text.input_serch_word_for_delete):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    name = model.delete_contact(u_id)
                    view.show_message(texе.delet_contact_successfull(name))
            case 8: 
                pass
                break 