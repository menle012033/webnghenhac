from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
import requests
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    chudes = Chude.objects.all()  # Lấy danh sách các chủ đề
    baihats = Baihat.objects.all()  # Lấy danh sách tất cả các bài hát
    # Gắn danh sách các bài hát vào mỗi chủ đề sử dụng annotate
    for chude in chudes:
        chude.baihats = Baihat.objects.filter(theloai__name=chude.name)
    # Lấy danh sách các thể loại
    theloais = Theloai.objects.all()
    # Lấy danh sách các album
    albums = Album.objects.all()
    # Lấy danh sách các playlist
    playlists = Playlist.objects.all()
    # Lấy danh sách các playlist
    quangcaos = Quangcao.objects.all()
    # Kiểm tra người dùng đã đăng nhập hay chưa để hiển thị phần tương ứng trên giao diện
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    # Truyền danh sách chủ đề, bài hát, thể loại, album, playlist vào context
    context = {
        'chudes': chudes,
        'baihats': baihats,
        'theloais': theloais,
        'albums': albums,
        'playlists': playlists,
        'quangcaos': quangcaos,
        'user_not_dangnhap': user_not_dangnhap,
        'user_dangnhap': user_dangnhap
    }
    return render(request, 'app/home.html', context)
def hoso(request):
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    context={'user_not_dangnhap':user_not_dangnhap,'user_dangnhap':user_dangnhap}
    return render(request,'app/hoso.html',context)
def checkout(request):
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    context={'user_not_dangnhap':user_not_dangnhap,'user_dangnhap':user_dangnhap}
    return render(request,'app/checkout.html',context)
#top100
def Top100(request):
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    context={'user_not_dangnhap':user_not_dangnhap,'user_dangnhap':user_dangnhap}
    return render(request,'app/Top100.html',context)
#nghe
def nghe(request):
    theloai_id = request.GET.get('theloai')  # Lấy thể loại từ tham số URL
    chude_id = request.GET.get('chude')  # Lấy chủ đề từ tham số URL
    if theloai_id:
        baihats = Baihat.objects.filter(theloai__id=theloai_id)  # Lọc bài hát theo id thể loại
    elif chude_id:
        baihats = Baihat.objects.filter(theloai__chude__id=chude_id)  # Lọc bài hát theo id chủ đề
    else:
        baihats = Baihat.objects.all()  # Nếu không có thể loại hoặc chủ đề được chọn, lấy tất cả bài hát
    # Xử lý trạng thái đăng nhập của người dùng
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    # Truyền danh sách bài hát, trạng thái đăng nhập và thể loại đã chọn vào context
    context = {
        'baihats': baihats,
        'user_not_dangnhap': user_not_dangnhap,
        'user_dangnhap': user_dangnhap,
        'theloai': Theloai.objects.all(),  # Truyền danh sách thể loại để sử dụng trong template nếu cần
        'chude': Chude.objects.all(),  # Truyền danh sách chủ đề để sử dụng trong template nếu cần
        'theloai_id': theloai_id,  # Truyền id thể loại để sử dụng trong template nếu cần
        'chude_id': chude_id,  # Truyền id chủ đề để sử dụng trong template nếu cần
    }
    return render(request, 'app/nghe.html', context)
#khampha
def khampha(request):
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    context={'user_not_dangnhap':user_not_dangnhap,'user_dangnhap':user_dangnhap}
    return render(request,'app/khampha.html',context)
#dang ky
def dangky(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dangnhap')
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    context={'form':form,'user_not_dangnhap':user_not_dangnhap,'user_dangnhap':user_dangnhap}
    return render(request,'app/dangky.html',context)
#dang nhap
def dangnhap(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username, password =password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'user or password not correct!')
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    context={'user_not_dangnhap':user_not_dangnhap,'user_dangnhap':user_dangnhap}
    return render(request,'app/dangnhap.html',context)
def dangxuat(request):
    logout(request)
    return redirect('dangnhap')
#timkiem
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()    
        # In ra giá trị của searched để kiểm tra
        print("Searched:", searched)
        baihats = Baihat.objects.filter(
            Q(ten__icontains=searched) | 
            Q(casi__icontains=searched) | 
            Q(album__name__icontains=searched)
        )
        albums = Album.objects.filter(name__icontains=searched)
        theloais = Theloai.objects.filter(name__icontains=searched)
        # In ra các kết quả tìm kiếm để kiểm tra
        print("Baihat results:", baihats)
        print("Album results:", albums)
        print("Theloai results:", theloais)
        # Kiểm tra người dùng đã đăng nhập hay chưa để hiển thị phần tương ứng trên giao diện
        if request.user.is_authenticated:
            user_not_dangnhap = "none"
            user_dangnhap = "block"
        else:
            user_not_dangnhap = "block"
            user_dangnhap = "none"
        context = {
            'searched': searched,
            'baihats': baihats,
            'albums': albums,
            'theloais': theloais,
            'user_not_dangnhap': user_not_dangnhap,
            'user_dangnhap': user_dangnhap
        }
        return render(request, 'app/search.html', context)
    return render(request, 'app/search.html')

#admin
def homeadmin(request):
    return render(request,'app/homeadmin.html')

def baihat(request):  
    theloai_id = request.GET.get('theloai')  # Lấy thể loại từ tham số URL
    chude_id = request.GET.get('chude')  # Lấy chủ đề từ tham số URL
    if theloai_id:
        baihats = Baihat.objects.filter(theloai__id=theloai_id)  # Lọc bài hát theo id thể loại
    elif chude_id:
        baihats = Baihat.objects.filter(theloai__chude__id=chude_id)  # Lọc bài hát theo id chủ đề
    else:
        baihats = Baihat.objects.all()  # Nếu không có thể loại hoặc chủ đề được chọn, lấy tất cả bài hát
    # Xử lý trạng thái đăng nhập của người dùng
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    # Truyền danh sách bài hát, trạng thái đăng nhập và thể loại đã chọn vào context
    context = {
        'baihats': baihats,
        'user_not_dangnhap': user_not_dangnhap,
        'user_dangnhap': user_dangnhap,
        'theloai': Theloai.objects.all(),  # Truyền danh sách thể loại để sử dụng trong template nếu cần
        'chude': Chude.objects.all(),  # Truyền danh sách chủ đề để sử dụng trong template nếu cần
        'theloai_id': theloai_id,  # Truyền id thể loại để sử dụng trong template nếu cần
        'chude_id': chude_id,  # Truyền id chủ đề để sử dụng trong template nếu cần
    }
    return render(request, 'app/baihat.html',context)
def album(request):
    return render(request,'app/album.html')
def playlist(request):
    chudes = Chude.objects.all()  # Lấy danh sách các chủ đề
    baihats = Baihat.objects.all()  # Lấy danh sách tất cả các bài hát
    # Gắn danh sách các bài hát vào mỗi chủ đề sử dụng annotate
    for chude in chudes:
        chude.baihats = Baihat.objects.filter(theloai__name=chude.name)
    # Lấy danh sách các thể loại
    theloais = Theloai.objects.all()
    # Lấy danh sách các album
    albums = Album.objects.all()
    # Lấy danh sách các playlist
    playlists = Playlist.objects.all()
    # Kiểm tra người dùng đã đăng nhập hay chưa để hiển thị phần tương ứng trên giao diện
    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn
    # Truyền danh sách chủ đề, bài hát, thể loại, album, playlist vào context
    context = {
        'chudes': chudes,
        'baihats': baihats,
        'theloais': theloais,
        'albums': albums,
        'playlists': playlists,
        'user_not_dangnhap': user_not_dangnhap,
        'user_dangnhap': user_dangnhap
    }
    return render(request, 'app/playlist.html', context)
def quangcao(request):
    quangcaos = Quangcao.objects.all().select_related('baihat')
    baihats = Baihat.objects.all()  # Lấy danh sách tất cả các bài hát

    if request.user.is_authenticated:
        user_not_dangnhap = "none"  # Ẩn
        user_dangnhap = "block"     # Hiển thị
    else:
        user_not_dangnhap = "block" # Hiển thị
        user_dangnhap = "none"      # Ẩn

    context = {
        'quangcaos': quangcaos,
        'baihats': baihats,
        'user_not_dangnhap': user_not_dangnhap,
        'user_dangnhap': user_dangnhap
    }
    return render(request, 'app/home.html', context)

def chude(request):
    chudes = Playlist.objects.all()
    context = {
        'chudes': chude
    }
    return render(request,'app/chude.html', context)
def theloai(request):
    return render(request,'app/theloai.html')
def nghe1 (request):
    return render(request,'app/nghe1.html')
def user(request):
    return render(request,'app/user.html')
#audio
def upload_audio(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')

        if title and file:
            Baihat.objects.create(title=title, file=file)
            return redirect('audio_list')
    return render(request, 'upload_audio.html')
def audio_list(request):
    audios = Baihat.objects.all()
    return render(request, 'audio_list.html', {'audios': audios})

