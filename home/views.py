from django.shortcuts import render
from django.views import View
# Create your views here.
class Index(View):
      template_name='home.html'
      def get(self,*args,**kwargs):
        return  render(self.request,self.template_name)