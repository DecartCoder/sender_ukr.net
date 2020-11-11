inlist = []
all_mail = []


def get_all_email():
    with open('listmail.txt') as lm:
        inlist.append(lm.readlines())

    getlen = len(inlist[0])

    for i in range(getlen):
        lines = str(inlist[0][i]).strip()
        all_mail.append(lines)
        i += 1

def get_len_list():
    lenlist = len(all_mail)
    return lenlist