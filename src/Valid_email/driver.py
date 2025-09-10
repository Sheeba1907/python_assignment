from util import filter_mails

def main():
    n = int(input("Enter the number of emails: ").strip())
    emails = []
    for _ in range(n):
        emails.append(input("Enter the email: ").strip())

    valid_sorted_emails = filter_mails(emails)
    print(valid_sorted_emails)

if __name__ == "__main__":
    main()