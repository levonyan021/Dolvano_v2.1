from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from itsdangerous import URLSafeTimedSerializer
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail


def home(request):
    return render(request, 'main/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            tokenizer = URLSafeTimedSerializer(settings.SECRET_KEY)

            serialized_token = tokenizer.dumps(
                {
                    "email": user.email,
                    "username": user.username
                }
            )

            verify_url = f'{settings.BASE_URL}/acc/activate?token={serialized_token}'
            current_site = get_current_site(request)
            send_mail(
                'Activate your blog account.',
                message=render_to_string('main/account/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                }),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                html_message=f'<a href={verify_url}>Click Here!</a>'
            )

            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'main/account/signup.html', {'form': form})


def activate(request):
    mail_token = request.GET.get('token')
    print(mail_token)

    if not mail_token:
        return HttpResponse('Verification failed')

    tokenizer = URLSafeTimedSerializer(settings.SECRET_KEY)
    print(tokenizer)

    try:
        data = tokenizer.loads(mail_token, max_age=settings.VERIFICATION_TIME_IN_SECONDS)
        print(data)
    except Exception:
        return HttpResponse("Verification failed, data expired")

    try:
        user = User.objects.get(username=data["username"], email=data["email"])
    except Exception:
        return HttpResponse(
            dict(message="Verification Failed: someting bad happened")
        )

    user.is_active = True
    user.save()

    return home(request)
