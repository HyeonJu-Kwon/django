from django.db import models

# Create your models here.
# 동아리 정보 저장 모델
class Club(models.Model):
    name = models.CharField(max_length=100)  # 동아리명
    description = models.TextField()           # 설명
    registration_date = models.DateField(auto_now_add=True)  # 등록 날짜

    def __str__(self):
        return self.name  # 동아리명 반환

# 회원 정보 관리 모델
class Member(models.Model):
    name = models.CharField(max_length=100)    # 이름
    email = models.EmailField(unique=True)      # 이메일
    password = models.CharField(max_length=128) # 비밀번호
    join_date = models.DateField(auto_now_add=True)  # 가입날짜

    def __str__(self):
        return self.name  # 이름 반환


# 출석 기록 저장 모델
class AttendanceRecord(models.Model):
    ATTENDANCE_CHOICES = [
        ('present', '출석'),
        ('absent', '결석'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)  # 회원 외래 키
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)  # 출석상태
    attendance_date = models.DateField()  # 출석날짜

    def __str__(self):
        return f"{self.member.name} - {self.status} on {self.attendance_date}"  # 출석기록 반환

# 활동내역 모델 설계 중
#class ActivityLog(models.Model):
  #  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  #  activity_name = models.CharField(max_length=100)
   # timestamp = models.DateTimeField(auto_now_add=True)
  #  duration = models.DecimalField(max_digits=5, decimal_places=2)