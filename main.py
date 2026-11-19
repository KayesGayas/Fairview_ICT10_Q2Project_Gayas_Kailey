
from pyscript import document


# Member Checker - Seatwork 1

volleyball_members = {
    "kailey gayas",
    "johanna ramos",
    "julienne miranda",
    "hope benitez",
}


def verify_candidate(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    result = document.getElementById("result")

    if first_name == "" or last_name == "":
        result.innerHTML = "Please enter both your first and last name."

    else:
        full_name = (first_name + " " + last_name).lower()

        if full_name in volleyball_members:
            result.innerHTML = (
                "Congratulations, " + first_name.title() +
                "! You are part of the OBFV Volleyball Varsity!"
            )
        else:
            result.innerHTML = (
                "Sorry, " + first_name.title() +
                ". You are not part of the OBFV Volleyball Varsity."
            )


# Element Checker - Skills Test

elements = {
    "H": {
        "name": "Hydrogen",
        "number": 1,
        "mass": 1.008
    },
    "C": {
        "name": "Carbon",
        "number": 6,
        "mass": 12.011
    },
    "N": {
        "name": "Nitrogen",
        "number": 7,
        "mass": 14.007
    },
    "O": {
        "name": "Oxygen",
        "number": 8,
        "mass": 15.999
    },
    "P": {
        "name": "Phosphorus",
        "number": 15,
        "mass": 30.974
    },
    "S": {
        "name": "Sulfur",
        "number": 16,
        "mass": 32.06
    },
    "Se": {
        "name": "Selenium",
        "number": 34,
        "mass": 78.971
    }
}


def search_element(event):
    element_input = document.getElementById("element1").value.strip()

    symbol_output = document.getElementById("symbol")
    name_output = document.getElementById("name")
    number_output = document.getElementById("number")
    mass_output = document.getElementById("mass")

    symbol = element_input.title()

    if symbol == "":
        symbol_output.innerHTML = "---"
        name_output.innerHTML = "Please enter an element symbol."
        number_output.innerHTML = "---"
        mass_output.innerHTML = "---"

    elif symbol in elements:
        symbol_output.innerHTML = symbol
        name_output.innerHTML = elements[symbol]["name"]
        number_output.innerHTML = str(elements[symbol]["number"])
        mass_output.innerHTML = str(elements[symbol]["mass"])

    else:
        symbol_output.innerHTML = "---"
        name_output.innerHTML = "Element not found."
        number_output.innerHTML = "---"
        mass_output.innerHTML = "---"

# CLUB MEMBERS - DRILL 2

club_members = {
    "Grade 7": {
        "Jane Smith",
        "Kendra Well",
        "Tom Holland",
        "Bobby Trap",
        "Kyrie Irving"
    },

    "Grade 8": {
        "Jordan Lim",
        "Sofia Viologa",
        "Brad Bill",
        "Simon Says",
        "Achiles Muscle"
    },

    "Grade 9": {
        "Mariah Pelobello",
        "Kristel Esguerra",
        "Inno Pena",
        "Chloe Adlawan",
        "Lai Lazarte"
    },

    "Grade 10": {
        "Kailey Gayas",
        "Megan Gacita",
        "Cedric Velasco",
        "Vyelle Bunag",
        "Isabella Acosta"
    }
}

additional_members = set()


def display_members():
    result_box = document.getElementById("result-box")
    member_count = document.getElementById("member-count")

    if result_box is None:
        return

    total_members = sum(
        len(members) for members in club_members.values()
    ) + len(additional_members)

    member_count.innerHTML = str(total_members)

    output = ""

    for grade, members in club_members.items():
        output += "<div class='grade-section'>"
        output += "<h3>" + grade + "</h3>"
        output += "<ul>"

        for member in sorted(members):
            output += "<li>" + member + "</li>"

        output += "</ul>"
        output += "</div>"

    if additional_members:
        output += "<div class='grade-section'>"
        output += "<h3>Additional Members</h3>"
        output += "<ul>"

        for member in sorted(additional_members):
            output += "<li>" + member + "</li>"

        output += "</ul>"
        output += "</div>"

    result_box.innerHTML = output


def verify(event):
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()

    message = document.getElementById("message")

    if first_name == "" or last_name == "":
        message.innerHTML = "Please enter both first name and last name."

    else:
        new_member = first_name.title() + " " + last_name.title()

        all_members = set()

        for members in club_members.values():
            all_members.update(members)

        all_members.update(additional_members)

        existing_names = {member.lower() for member in all_members}

        if new_member.lower() in existing_names:
            message.innerHTML = new_member + " is already in the club."

        else:
            additional_members.add(new_member)

            message.innerHTML = (
                new_member + " has been successfully added!"
            )

            document.getElementById("firstname").value = ""
            document.getElementById("lastname").value = ""

            display_members()

if document.getElementById("result-box") is not None:
    display_members()
