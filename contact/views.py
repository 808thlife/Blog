from django.core.mail import send_mail
from django.http import JsonResponse
# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        email = request.POST["email"]
        send_mail(subject, message, from_email= email, recipient_list= ["khqyop@gmail.com"])
        return JsonResponse({"message":"Thanks for contacting me! Will Answer As Soon As Possible"}, status = 200)
    return JsonResponse({"error":"Invalid request method."}, status = 400)