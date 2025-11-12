import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("Attendees must be a list of dictionaries")
    for attendee in attendees:
        if not isinstance(attendee, dict):
            raise TypeError("Each attendee must be a dictionary")
    if not template:
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated")
        return
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        invitation = invitation.replace("{name}", str(attendee.get("name", "N/A")))
        invitation = invitation.replace("{event_title}", str(attendee.get("event_title", "N/A")))
        invitation = invitation.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        invitation = invitation.replace("{event_location}", str(attendee.get("event_location", "N/A")))
        filename = f"output_{index}.txt"
        if os.path.exists(filename):
            print(f"File {filename} already exists.")
            continue
        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
    