import data_base
import view
import phone_book as pb


def choise_menu(choise):
    match choise:
        case 1:
            view.print_phone_book()
        case 2:
            data_base.load_contact()
        case 3:
            data_base.save_contacts()
        case 4:
            pb.add_contact()
        case 5:
            pb.change_contact()
        case 6:
            pb.remove_contact()
        case 7:
            pb.find_contact()
        case 0:
            return True


while True:
    choise = view.main_menu()
    if choise_menu(choise):
        break
