from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import (LoginForm,MyPasswordChangeForm,MyPasswordResetForm, MySetPasswordForm)

urlpatterns = [
    # path('', views.home), 
    path('', views.ProductView.as_view(),name='home'),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    path('add-to-cart/', views.add_to_cart,   name='add-to-cart'),
    
    path('cart/', views.show_cart, name='showcart'),

    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdata/',views.payment_done,name='paymentdone'),
    
    path('buy/', views.buy_now, name='buy-now'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    path('address/', views.address, name='address'),
    
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('mobile/', views.mobile, name='mobile'),

    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),

    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

    # path('login/', views.login, name='login'),
    path('accounts/login/', views.CustomLoginView.as_view(template_name='app/login.html',
    authentication_form=LoginForm), name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    # path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),

    path('passwordchange/',views.MyPasswordChangeView.as_view(),name='passwordchange'),

    path('passwordchangedone/',views.MyPasswordChangeDoneView.as_view()),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),

    path('current-time/', views.current_time_view, name='current_time'),

] + static(settings.MEDIA_URL,document_root = settings
.MEDIA_ROOT)


urlpatterns+=[
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    # path('verify/<str:uidb64>/<str:token>/', views.verify, name='verify'),
    path('verify/<str:data>/', views.verify, name='verify'),
    # /<str:data>/'
]