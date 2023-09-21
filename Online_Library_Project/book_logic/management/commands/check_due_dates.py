from django.core.management.base import BaseCommand
from book_logic.models import BookRental
from django.utils import timezone
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Check due dates and send notifications'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        two_days_from_now = now + timezone.timedelta(days=2)
        
        rentals_due_soon = BookRental.objects.filter(due_date__lte=two_days_from_now, returned=False)
        
        for rental in rentals_due_soon:
            # Send notification to rental.user
            subject = 'Book Due Date Reminder'
            message = f'Your rental for {rental.book.title} is due in 2 days. Please return it on time.'
            from_email = 'noreply@example.com'
            recipient_list = [rental.user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            # You can also implement the logic for allowing extensions or automatically marking books as returned
