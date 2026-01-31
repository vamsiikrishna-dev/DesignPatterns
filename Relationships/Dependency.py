# Dependency: "I consume your services temporarily"
# Semantic essence: Service consumer relationship

class EmailService:
    @staticmethod
    def send_email(to, subject, body):
        print(f"📧 Sending email to {to}: {subject}")
        return True

class SMSService:
    @staticmethod
    def send_sms(phone, message):
        print(f"📱 Sending SMS to {phone}: {message}")
        return True

class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# DEPENDENCY: NotificationManager uses services temporarily
class NotificationManager:
    def __init__(self):
        self.notifications_sent = 0
    
    def notify_by_email(self, user, message):
        # Uses EmailService temporarily - no permanent relationship
        success = EmailService.send_email(user.email, "Notification", message)
        if success:
            self.notifications_sent += 1
    
    def notify_by_sms(self, user, message):
        # Uses SMSService temporarily - no permanent relationship
        success = SMSService.send_sms(user.phone, message)
        if success:
            self.notifications_sent += 1

# DEPENDENCY: Calculator uses MathService temporarily
class MathService:
    @staticmethod
    def calculate_tax(amount, rate):
        return amount * (rate / 100)
    
    @staticmethod
    def format_currency(amount):
        return f"${amount:.2f}"

class Invoice:
    def __init__(self, amount):
        self.amount = amount
    
    def calculate_total(self, tax_rate):
        # Uses MathService temporarily - no permanent relationship
        tax = MathService.calculate_tax(self.amount, tax_rate)
        total = self.amount + tax
        return MathService.format_currency(total)

# DEPENDENCY: FileProcessor uses different services based on file type
class FileValidator:
    @staticmethod
    def validate_pdf(file_path):
        return file_path.endswith('.pdf')
    
    @staticmethod
    def validate_image(file_path):
        return file_path.endswith(('.jpg', '.png', '.gif'))

class FileProcessor:
    def process_file(self, file_path, file_type):
        # Uses different services temporarily based on need
        if file_type == 'pdf':
            if FileValidator.validate_pdf(file_path):
                print(f"Processing PDF: {file_path}")
        elif file_type == 'image':
            if FileValidator.validate_image(file_path):
                print(f"Processing Image: {file_path}")
        # No permanent relationships formed

if __name__ == '__main__':
    # Semantic test: Service consumption without permanent relationships
    user = User("Alice", "alice@email.com", "+1234567890")
    notifier = NotificationManager()
    
    # NotificationManager uses services temporarily
    notifier.notify_by_email(user, "Welcome!")
    notifier.notify_by_sms(user, "Account created")
    
    print(f"Notifications sent: {notifier.notifications_sent}")
    
    # Invoice uses MathService temporarily
    invoice = Invoice(100.00)
    total = invoice.calculate_total(8.5)
    print(f"Invoice total: {total}")
    
    # FileProcessor uses validation services temporarily
    processor = FileProcessor()
    processor.process_file("document.pdf", "pdf")
    processor.process_file("photo.jpg", "image")
    
    # Key semantic point: No permanent relationships exist
    # Services can be replaced without affecting consumers