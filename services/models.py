from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("edit_service", "Can edit service details"),  # Chỉ giữ quyền tùy chỉnh khác nếu cần
        ]

    def __str__(self):
        return self.name
