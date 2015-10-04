from django.db import models
from django.contrib.auth.models import User

LIST_DIVIDER = ','

class UserProfile(models.Model):
    uid = models.OneToOneField(User)
    select_list = models.TextField(null=True, blank=True)

    def add_selected(self, s_id=None):
        if self.select_list==None or self.select_list=='':
            selected=[]
        else:
            selected = self.select_list.split(LIST_DIVIDER)
        if s_id in selected:
            return None
        else:
            selected.append(s_id)
            self.select_list = LIST_DIVIDER.join(selected)
            self.save()
            return s_id

    def del_selected(self,s_id):
        if self.select_list==None or self.select_list=='':
            selected=[]
        else:
            selected = self.select_list.split(LIST_DIVIDER)
        if s_id in selected:
            selected.remove(s_id)
            self.select_list = LIST_DIVIDER.join(selected)
            self.save()
            return s_id
        else:
            return None

    def clear_selected(self):
        selected=[]
        self.select_list = LIST_DIVIDER.join(selected)
        self.save()

    def get_selected(self):
        selected = self.select_list.split(LIST_DIVIDER)
        return selected

    def is_checked(self,s_id=None):
        if self.select_list==None or self.select_list=='':
            selected=[]
        else:
            selected = self.select_list.split(LIST_DIVIDER)

        result = s_id in selected
        return result

    def __str__(self):
        return self.uid.username

    class Meta:
        verbose_name_plural=u'User profiles'