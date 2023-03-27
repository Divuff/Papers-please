while get_image_color(DAY_TEST_POSITION) == DAY_COLOR:

    if detect_person():
        if not detect_person_leaving():
            if detect_textbox:
                time.sleep(1.5)

                if not detect_passport():
                    drag_and_drop(PASSPORT_POSITION, PASSPORT_SLOT_POSITION)
                    print("Passport detected")
                else:
                    print("No passport!")
                    handle_no_passport()
            else:
                print("Textbox not detected")
        else:
            print("Person has left")
    else:
        print("No person detected")

    if detect_country() == ARSTOTZKA_COLOR:
        handle_accepted_person()
        print("Arstotzkan detected")
    elif detect_country() != DESK_COLOR:
        handle_rejected_person()
        print("Foreign scum")
    else:
        print("No passport")

print("Day is over")