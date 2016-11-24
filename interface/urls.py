from django.conf.urls import url
from interface import views


urlpatterns = [
    # o-m c6-ne api/v1/
    url(r'^v1/vnfs$',
        views.vnfs, name='vnf_instantiate_or_query '),
    url(r'^v1/vnfs/(?P<vnfInstanceID>[0-9a-zA-Z\-_]+)$',
        views.vnf_detail, name='vnf_delete_or_query'),
    url(r'^v1/jobs/(?P<jobId>[0-9a-zA-Z\-_]+)$',
        views.job_status, name='job_status'),
    # m-o ->c6
    url(r'^api/v1/m_nbi_i/(?P<nfvoid>[0-9a-zA-Z\-_]+)/api/v1/nf_o_i/resource/grant$',
        views.vnf_grant_lcm, name='vnf_grant_lcm'),
    url(r'^api/v1/m_nbi_i/(?P<nfvoid>[0-9a-zA-Z\-_]+)/api/v1/nf_o_i/nfs/lcmnotification$',
        views.nf_notification, name='nf_notification'),]
