from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_view(email):
    subject = 'Your appointment is received'
    message = "Hi, Sir/Ma'am your appointment for conserned lawyerbhas saved in our database. Please wait for the lawyer appointment"
    from_email = 'pnishant030@gmail.com'  #must match default_from_email
    recipient_list = [email] #email address of the recipient
    
    # render html email from template
    html_message = render_to_string('appointment_email_template.html')
    # create plain text version by stripping html tags
    plain_message = strip_tags(html_message)

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False
        )
        return HttpResponse("Email sent successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred while sending the email: {str(e)}")
