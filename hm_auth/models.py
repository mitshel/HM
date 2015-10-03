from django.db import models
from django.contrib.auth.models import User

LIST_DIVIDER = ','

class UserProfile(models.Model):
    uid = models.OneToOneField(User)
    select_list = models.TextField(null=True, blank=True)

    def add_selected(self, id):
        selected = self.select_list.split(LIST_DIVIDER)
        s_id=str(id)
        if s_id in selected:
            return 0
        else:
            selected.append(s_id)
            self.select_list = LIST_DIVIDER.join(selected)
            self.save()
            return id

    def del_selected(self,id):
        selected = self.select_list.split(LIST_DIVIDER)
        s_id=str(id)
        if s_id in selected:
            selected.remove(s_id)
            self.select_list = LIST_DIVIDER.join(selected)
            self.save()
            return id
        else:
            return 0

    def clear_selected(self):
        selected=[]
        self.save()

    def __str__(self):
        return self.uid.username

    class Meta:
        verbose_name_plural=u'User profiles'