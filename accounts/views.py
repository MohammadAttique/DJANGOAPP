from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.shortcuts import redirect


def activation(request, uid, token):
    try:
        # Decode the user ID and check if it's a valid user
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check if the user exists and the token is valid
    if user is not None and default_token_generator.check_token(user, token):
        # Activate the user account
        user.is_active = True
        user.save()

        # Optionally, you can log the user in automatically after activation
        # from django.contrib.auth import login
        # login(request, user)

        messages.success(request, 'Your account has been activated successfully. You can now log in.')
        return redirect('login')  # Replace 'login' with the actual URL name for your login view
    else:
        messages.error(request, 'Invalid activation link. Please try again.')
        return render(request,
                      'activation_failed.html')  # Create an activation_failed.html template for displaying an error message


def send_email_view(request):
    subject = 'Subject of the email'
    message = 'Message body of the email.'
    sender_email = 'anambi456@gmail.com'  # Replace with your email
    recipient_email = 'za@gmail.com'  # Replace with recipient's email

    send_mail(
        subject,
        message,
        sender_email,
        [recipient_email],
        fail_silently=False,
    )

    return HttpResponse('Email sent successfully!')