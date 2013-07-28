from tastypie import fields
from tastypie.resources import ModelResource
from .models import Commission, Company


class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()


class CommissionResource(ModelResource):
    firma = fields.ToOneField(CompanyResource, 'firma')

    class Meta:
        queryset = Commission.objects.all()
