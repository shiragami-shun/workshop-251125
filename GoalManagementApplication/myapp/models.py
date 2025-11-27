from django.db import models

class Goal(models.Model):
    CATEGORY_CHOICES = [
        ('study', '勉強'),
        ('health', '健康'),
        ('work', '仕事'),
        ('hobby', '趣味'),
        ('other', 'その他'),
    ]
    
    STATUS_CHOICES = [
        ('active', '進行中'),
        ('completed', '完了'),
        ('cancelled', 'キャンセル'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='study')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    target_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
