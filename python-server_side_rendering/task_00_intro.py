#!/usr/bin/python3
""" Create invitations based on a template and a list of attendees. """


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Each attendee must be a dictionary")
            return
    if not template or template.strip() == "":
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        name = attendee.get("name")
        invitation = invitation.replace(
          "{name}", str(name) if name is not None else "N/A")

        title = attendee.get("event_title")
        invitation = invitation.replace(
          "{event_title}", str(title) if title is not None else "N/A")

        date = attendee.get("event_date")
        invitation = invitation.replace(
          "{event_date}", str(date) if date is not None else "N/A")

        location = attendee.get("event_location")
        invitation = invitation.replace(
          "{event_location}", str(location) if location is not None else "N/A")

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
