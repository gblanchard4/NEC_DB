from django.shortcuts import get_object_or_404,  get_list_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.views import generic

from .models import Patient,Stool,Environment

# # Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'patients/index.html'
#     context_object_name = 'patients_by_id'

#     def get_queryset(self):
#         return Patient.objects.order_by('patientid')

# class PatientView(generic.DetailView):
#     model = Patient
#     template_name = 'patients/patientdetail.html'

# # class StoolView(generic.DetailView)
# #     model = Stool
# #     template_name = 'patients/stooldetail.html'




def index(request):
    patients_by_id = Patient.objects.order_by('patientid')
    template = loader.get_template('patients/index.html')
    context = {'patients_by_id':patients_by_id}
    return render( request, 'patients/index.html', context)

def patient_detail(request, patientid):
    context ={ 'patient':Patient.objects.get(pk=patientid),
                'stool':Stool.objects.filter(patient_id=patientid).order_by('date'),
                'enviro':Environment.objects.filter(patientid=patientid).order_by('date')
            }
    #patient = get_object_or_404(Patient, pk=patientid)
    #return render(request, 'patients/patientdetail.html', {'patient':patient})
    return render(request, 'patients/patientdetail.html', context)

def stool_detail(request, patientid):
    stool = get_list_or_404(Stool.objects.order_by('date'), patient_id=patientid )
    return render(request, 'patients/stooldetail.html', {'stool':stool})

def stool_single(request, stoolid):
    stool = get_list_or_404(Stool.objects.get(id=stoolid))
    return render(request, 'patients/stooldetail.html', {'stool':stool})
