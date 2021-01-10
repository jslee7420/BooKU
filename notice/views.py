from django.shortcuts import render, get_object_or_404
from .models import Notice
from django.core.paginator import Paginator

# Create your views here.
def notice_list(request):
    """
    공지사항 목록
    """
    page = request.GET.get('page','1')
    notice_list = Notice.objects.order_by('-create_date')
    paginator = Paginator(notice_list, 10)
    page_obj = paginator.get_page(page)
    context = {'notice_list': page_obj}
    return render(request, 'notice/notice_list.html', context)


def notice_detail(request, notice_id):
    """
    공지사항 내용 출력
    """
    notice = get_object_or_404(Notice, pk = notice_id)
    context = {'notice': notice}
    return render(request, 'notice/notice_detail.html', context)