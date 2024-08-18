import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ethpm import contract

from dctbapp.models import *
from file_ipfs import *
# Create your views here.
def loginn(request):
    return render(request,"index.html")
def login_post(request):
    un=request.POST['textfield']
    pas=request.POST['textfield2']
    res=login.objects.filter(username=un,password=pas)
    if res.exists():
        if res[0].usertype=='admin':
            request.session['lid'] = res[0].id
            request.session['lg']="lin"
            return HttpResponse("<script>alert('Successfully Login');window.location='/homepage'</script>")

        if res[0].usertype=='user':
            request.session['lg'] = "lin"
            request.session['lid'] = res[0].id
            return HttpResponse("<script>alert('Successfully Login');window.location='/user_homepage'</script>")
 #           return redirect('/user_homepage')
        else:
            return HttpResponse("invalid")
    else:
        return HttpResponse("invalid user")


def complaintt(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")

    res=complaint.objects.all()
    return render(request,"admin/complaintnew.html",{'data':res})

def reply(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request,"admin/reply.html",{"id":id})

def reply_post(request,id):
    res = request.POST['textarea']
    complaint.objects.filter(id=id).update(reply=res,r_date=datetime.datetime.now().strftime("%Y-%m-%d"))
    return HttpResponse("<script>alert('Success');window.location='/complaintt#contact'</script>")

def viewfeedback(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    res = feedback.objects.all()
    return render(request,"admin/viewfeedback.html",{'data':res})

def viewuser(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")

    res = user.objects.all()
    return render(request,"admin/viewuser.html",{'data':res})

def changepswd(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request,"admin/changepas.html")

def changepswd_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    old=request.POST['textfield']
    new=request.POST['textfield2']
    re=request.POST['textfield3']
    res=login.objects.filter(id=request.session['lid'], password=old)
    if res.exists():
        if new==re:
            login.objects.filter(id=request.session['lid']).update(password=new)
            return HttpResponse("<script>alert('Successfully Changed');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('Password Missmatch!!');window.location='/changepswd'</script>")
    else:
        return HttpResponse("<script>alert('Invalid old Password');window.location='/changepswd'</script>")



def homepage(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request,"admin/admin_index.html")
# ===========================================USER MODULE===============================================================

def user_register(request):
    # if request.session['lg']!="lin":
    #     return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request,'REGISTER.html')

def user_register_post(request):
    photo = request.FILES['fileField']
    name = request.POST['textfield']
    phone = request.POST['textfield2']
    email = request.POST['textfield3']
    d=datetime.datetime.now().strftime("%d%m%Y-%H%M%S")
    password = request.POST['textfield4']
    fs=FileSystemStorage()
    fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\"+d+'.jpg',photo)
    path="/static/img/"+d+'.jpg'
    qry=login.objects.filter(username=email)
    if qry.exists():
        return HttpResponse("<script>alert('Email Already exists!!');window.location='/'</script>")

    log=login()
    log.username=email
    log.password=password
    log.usertype='user'
    log.save()


    obj=user()
    obj.username=name
    obj.photo=path
    obj.email=email
    obj.contacts=phone
    obj.LOGIN=log
    obj.save()

    return HttpResponse("<script>alert('Registration Successfull');window.location='/'</script>")

def view_request(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    data = []
    for i in range(blocknumber, 0, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            if str(decoded_input[1]['uid']) == str(request.session['lid']):

                try:
                    print(i,"block number")
                    qry = Request.objects.filter(FILES__blocknumber=i)
                    if qry.exists():
                        for ij in qry:
                            f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])
                            f2 = files.objects.get(blocknumber=decoded_input[1]['bid'])
                            data.append(
                                {
                                    "bid": decoded_input[1]['bid'],
                                    "uid": user.objects.get(id = ij.USER.id),
                                    "f": decoded_input[1]['f'],
                                    "d": decoded_input[1]['d'],
                                    "ft": f.type,
                                    "fp": f2.price,
                                    "status": ij.status,
                                    "id": ij.id
                                }
                            )
                except Exception as e:
                    print("eeeeee",e)
                    qry = Request.objects.filter(FILES__blocknumber=i)
                    if qry.exists():
                        for ij in qry:
                            f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])

                            # f2 = file.objects.filter(blocknumber=)

                            data.append(
                                {
                                    "bid": decoded_input[1]['bid'],
                                    "uid": user.objects.get(id = ij.USER.id),
                                    "f": decoded_input[1]['f'],
                                    "d": decoded_input[1]['d'],
                                    "ft": f.type,
                                    "fp": "Update Amount",
                                    "status": ij.status,
                                    "id":ij.id

                                }
                            )

        except Exception as e:
            print(e)
            pass
    print(data, "data")
    return render(request,'user/request.html',{"data":data})

def send_comp(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request, 'user/send_comp.html')

def send_comp_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    con = request.POST['textarea']
    obj = complaint()
    obj.complaint= con
    obj.c_date= datetime.datetime.now().strftime("%Y-%m-%d")
    obj.USER = user.objects.get(LOGIN=request.session['lid'])
    obj.reply = 'pending'
    obj.save()
    return HttpResponse("<script>alert('Success');window.location='/send_comp'</script>")

def sendfeedback(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request, 'user/sendfeedback.html')

def sendfeedback_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    content = request.POST['textarea']
    obj = feedback()
    obj.feedback = content
    obj.date = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    obj.USER = user.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Send Successfully');window.location='/sendfeedback'</script>")

def sendreq(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    res = files.objects.all()
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    data = []
    for i in range(blocknumber, 0, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("dddddddddd", decoded_input[1]['uid'])
            print("lidddddd", request.session['lid'])
            if str(decoded_input[1]['uid']) != str(request.session['lid']):
                print("aaaaaaaa")
                try:
                    # print("jiii")
                    f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])
                    f2 = files.objects.get(blocknumber=decoded_input[1]['bid'])
                    f23 = Request.objects.filter(FILES=f2,USER__LOGIN=request.session['lid'])
                    if f23.exists():
                        if f23[0].status == 'pending':
                            data.append(
                                {
                                    "bid": decoded_input[1]['bid'],
                                    "uid": user.objects.get(LOGIN=decoded_input[1]['uid']),
                                    "f": decoded_input[1]['f'],
                                    "d": decoded_input[1]['d'],
                                    "ft": f.type,
                                    "fp": f2.price,
                                    "status": "1"

                                }
                            )
                        # if f[0].status == 'paid':
                        #     pass
                    else:
                        #
                        data.append(
                            {
                                "bid": decoded_input[1]['bid'],
                                "uid": user.objects.get(LOGIN=decoded_input[1]['uid']),
                                "f": decoded_input[1]['f'],
                                "d": decoded_input[1]['d'],
                                "ft": f.type,
                                "fp": f2.price,
                                "status":"0"

                            }
                        )
                except Exception as e:
                    print("eeeeeeeeeeee",e)
                    f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])

                    # f2 = file.objects.filter(blocknumber=)

                    data.append(
                        {
                            "bid": decoded_input[1]['bid'],
                            "uid": user.objects.get(LOGIN=decoded_input[1]['uid']),
                            "f": decoded_input[1]['f'],
                            "d": decoded_input[1]['d'],
                            "ft": f.type,
                            "fp": "Update Amount",
                            "status":"3"

                        }
                    )

        except Exception as e:
            print(e)
            pass
    print(data, "data")
    return render(request, 'user/sendreq.html',{"data":data})




def sendimgreq(request, id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    print(id,"ki")
    res=Request.objects.filter(FILES = files.objects.get(blocknumber=id), USER = user.objects.get(LOGIN=request.session['lid']), status = 'pending')
    if res.exists():
        return HttpResponse(
            "<script>alert('Already requested');window.location='/sendreq#contact'</script>")
    else:
        obj = Request()
        obj.FILES = files.objects.get(blocknumber=id)
        obj.USER = user.objects.get(LOGIN=request.session['lid'])
        obj.status = 'pending'
        obj.date = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        obj.save()
        return HttpResponse("<script>alert('Successfully Sent..Wait for Approval');window.location='/sendreq#contact'</script>")

def approvereq(request, id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    Request.objects.filter(id=id).update(status='approved')
    return HttpResponse("<script>alert('Approved');window.location='/view_request'</script>")

def rejectreq(request, id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    Request.objects.filter(id=id).update(status='rejected')
    return HttpResponse("<script>alert('Rejected');window.location='/view_request'</script>")

def uploadimage(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request, 'user/uploadimage.html')

# def uploadimage_post(request):
#     if request.session['lg']!="lin":
#         return HttpResponse("<script>alert('please login');window.location='/'</script>")
#     fil = request.FILES['fileField']
#     pric = request.POST['textfield']
#     print(fil.name)
#     t = fil.name.split('.')[-1]
#     print("type....",t)
#     typ = t
#     print("tyyyyy",typ)
#     # type = ''
#     # path =''
#
#     if typ == 'png' or 'jpeg' or 'PNG' or 'JPEG' or 'jpg' or 'JPG':
#         print("aaaaaaaaa")
#         dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
#         fs = FileSystemStorage()
#         fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', fil)
#         path = "/static/img/" + dt + 'post.jpg'
#         type = 'image'
#         res = file()
#         res.USER = user.objects.get(LOGIN=request.session['lid'])
#         res.image = path
#         res.type = type
#         res.price = pric
#         res.date = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
#         res.save()
#         return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
#     elif typ == 'MP4' or 'mp4':
#         print("bbbbbbbbbbbbbbb")
#         dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
#         fs = FileSystemStorage()
#         fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\video\\" + dt + 'post.mp4', fil)
#         path = "/static/video/" + dt + 'post.mp4'
#         type = 'video'
#     # print("ty....",type+"\n"+"pth........",path)
#
#         res = file()
#         res.USER = user.objects.get(LOGIN=request.session['lid'])
#         res.image = path
#         res.type = type
#         res.price = pric
#         res.date = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
#         res.save()
#         return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
#
#     else:
#         return HttpResponse("<script>alert('Please upload image/video');window.location='/uploadimage'</script>")


def uploadimage_post(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    fil = request.FILES['fileField']
    # pric = request.POST['textfield']
    print(fil.name)
    t = fil.name.split('.')[-1]
    print("type....",t)
    typ = t
    print("tyyyyy",typ)
    # type = ''
    # path =''
    from file_ipfs import hello_world
    if typ == 'png':
        print("aaaaaaaaa")
        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        type = 'image'

        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', fil)
        url=hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")

        path = "/static/img/" + dt + 'post.jpg'
        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber = blocknumber)
        if fle.exists():
            fle.update(type = "image")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "image"
            f.save()

        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price=request.POST['textfield']
            f.save()

        return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
    if typ == 'PNG':
        type = 'image'

        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', fil)
        path = "/static/img/" + dt + 'post.jpg'
        url = hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg',
                          request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")


        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(type="image")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "image"
            f.save()

        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price = request.POST['textfield']
            f.save()

        return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
    if typ == 'jpeg':
        type = 'image'
        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', fil)
        path = "/static/img/" + dt + 'post.jpg'
        url = hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg',
                          request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")



        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(type="image")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "image"
            f.save()
        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price = request.POST['textfield']
            f.save()

        return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")

    if typ == 'JPEG':
        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        type = 'image'
        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg',fil)
        path = "/static/img/" + dt + 'post.jpg'
        url = hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg',
                          request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(type="image")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "image"
            f.save()
        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price = request.POST['textfield']
            f.save()

        return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
    if typ == 'jpg' :
        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        type = 'image'
        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', fil)
        path = "/static/img/" + dt + 'post.jpg'
        url = hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg',
                          request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(type="image")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "image"
            f.save()
        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price = request.POST['textfield']
            f.save()

        return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
    if typ == 'JPG' :
        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        type ="image"
        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', fil)
        path = "/static/img/" + dt + 'post.jpg'
        type = 'image'
        url = hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg',request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(type="image")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "image"
            f.save()
        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price = request.POST['textfield']
            f.save()

        return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
    if typ == 'mp4':
        print("bbbbbbbbbbbbbbb")
        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        type = 'video'
        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\video\\" + dt + 'post.mp4', fil)
        path = "/static/video/" + dt + 'post.mp4'

        url = hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\video\\" + dt + 'post.mp4',
                          request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(type="video")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "video"
            f.save()
        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price = request.POST['textfield']
            f.save()

        return HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
    if typ == 'MP4':
        dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        fs = FileSystemStorage()
        type = 'video'
        fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\video\\" + dt + 'post.MP4', fil)
        url = hello_world(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\video\\" + dt + 'post.MP4',
                          request.session['lid'])

        if str(url) == "no":
            return HttpResponse("<script>alert('File is uploaded by someone');window.location='/uploadimage'</script>")

        if str(url) == "you":
            return HttpResponse("<script>alert('Check your file list');window.location='/uploadimage'</script>")

        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        fle = filetype.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(type="video")
        else:
            f = filetype()
            f.blocknumber = blocknumber
            f.type = "video"
            f.save()
        fle = files.objects.filter(blocknumber=blocknumber)
        if fle.exists():
            fle.update(price=request.POST['textfield'])
        else:
            f = files()
            f.blocknumber = blocknumber
            f.price = request.POST['textfield']
            f.save()

        HttpResponse("<script>alert('File uploaded');window.location='/uploadimage'</script>")
    else:
        return HttpResponse("<script>alert('Please upload image/video');window.location='/uploadimage'</script>")


def view_reply(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    res = complaint.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request, 'user/view_reply.html',{"data":res})

def view_req_status(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    data = []
    res = Request.objects.filter(USER__LOGIN=request.session['lid'])
    for i in res:
        a = web3.eth.get_transaction_by_block(int(i.FILES.blocknumber), 0)
        decoded_input = contract.decode_function_input(a['input'])
        data.append(
            {
                'id' : i.id,
                "USER" : user.objects.get(LOGIN=decoded_input[1]['uid']),
                "f" : decoded_input[1]['f'],
                "date" : decoded_input[1]['d'],
                "ft" : filetype.objects.get(blocknumber=i.FILES.blocknumber).type,
                "price" : i.FILES.price,
                "status" : i.status,
            }
        )


    return render(request, 'user/view_req_status.html',{"data":data})


def paymentupdate(request):
    Request.objects.filter(id = request.session['rid']).update(status='paid')
    return HttpResponse("<script>alert('Paid successfully');window.location='/view_req_status#contact'</script>")

def viewimage(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    #res = file.objects.filter(USER__LOGIN=request.session['lid'])

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    data = []
    for i in range(blocknumber, 0, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("dddddddddd",decoded_input[1]['uid'])
            print("lidddddd",request.session['lid'])
            if str(decoded_input[1]['uid']) == str(request.session['lid']):
                print("aaaaaaaa")
                try:
                    f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])
                    f2 = files.objects.get(blocknumber=decoded_input[1]['bid'])
                    print("hhhhhhhh", f)

                    # f2 = file.objects.filter(blocknumber=)

                    data.append(
                        {
                            "bid": decoded_input[1]['bid'],
                            "uid": decoded_input[1]['uid'],
                            "f": decoded_input[1]['f'],
                            "d": decoded_input[1]['d'],
                            "ft": f.type,
                            "fp": f2.price,

                        }
                    )
                except:
                    f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])


                    # f2 = file.objects.filter(blocknumber=)

                    data.append(
                        {
                            "bid": decoded_input[1]['bid'],
                            "uid": decoded_input[1]['uid'],
                            "f": decoded_input[1]['f'],
                            "d": decoded_input[1]['d'],
                            "ft": f.type,
                            "fp": "Update Amount",

                        }
                    )

        except Exception as e:
            print(e)
            pass
    print(data,"data")
    return render(request, 'user/viewimage.html',{"data":data})

def updateimage(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    try:
        res = files.objects.get(blocknumber=id)
        return render(request, 'user/updateimage.html',{"data":res.price,"id":id})
    except:
        return render(request, 'user/updateimage.html',{"id":id})

def updateimage_post(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")

    pric = request.POST['textfield']

    # if 'fileField' in request.FILES:
    #     fil = request.FILES['fileField']
    #     print(fil.name)
    #     t = fil.name.split('.')[-1]
    #     print(t)
    #     typ = t
    #     type = ''
    #     path = ''
    #     if typ == 'png' and 'jpeg' and 'PNG' and 'JPEG' and 'jpg' and 'JPG' :
    #         type = 'image'
    #         dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    #         fs = FileSystemStorage()
    #         fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\\" + dt + 'post.jpg', fil)
    #         path = "/static/img/" + dt + 'post.jpg'
    #     if typ == 'MP4' and 'mp4':
    #         type = 'video'
    #         dt = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    #         fs = FileSystemStorage()
    #         fs.save(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\video\\" + dt + 'post.mp4', fil)
    #         path = "/static/video/" + dt + 'post.mp4'
    #     files.objects.filter(id=id).update(image=path,date=datetime.datetime.now(),type=type,price=pric)
    # else:
    f = files.objects.filter(blocknumber=id)
    if f.exists():
        print("jiii")
        f.update(price=pric)
    else:
        fil = files()
        fil.blocknumber = id
        fil.price = pric
        fil.save()
    return HttpResponse("<script>alert('Updated successfully');window.location='/viewimage'</script>")

def deleteimg(request,id):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    files.objects.get(blocknumber=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/viewimage#contact'</script>")

def logout(request):
     request.session['lg']=""
     return HttpResponse("<script>alert('Logout');window.location='/'</script>")

def viewprofile(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    res=user.objects.get(LOGIN=request.session['lid'])
    return render(request, 'user/viewprofile.html',{"data":res})

def userhomepage(request):
    if request.session['lg']!="lin":
        return HttpResponse("<script>alert('please login');window.location='/'</script>")
    return render(request,'user/user_index.html')


def viewothersimage(request):
    uid=user.objects.get(LOGIN_id=request.session['lid'])
    # res=files.objects.filter(~Q(blocknumber=uid))

    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    data = []
    for i in range(blocknumber, 0, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("dddddddddd", decoded_input[1]['uid'])
            print("lidddddd", request.session['lid'])
            if str(decoded_input[1]['uid']) != str(request.session['lid']):
                print("aaaaaaaa")
                try:
                    f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])
                    f2 = files.objects.get(blocknumber=decoded_input[1]['bid'])
                    print("hhhhhhhh", f)

                    # f2 = file.objects.filter(blocknumber=)

                    data.append(
                        {
                            "bid": decoded_input[1]['bid'],
                            "uid": user.objects.get(LOGIN=decoded_input[1]['uid']),
                            "f": decoded_input[1]['f'],
                            "d": decoded_input[1]['d'],
                            "ft": f.type,
                            "fp": f2.price,

                        }
                    )
                except:
                    f = filetype.objects.get(blocknumber=decoded_input[1]['bid'])

                    # f2 = file.objects.filter(blocknumber=)

                    data.append(
                        {
                            "bid": decoded_input[1]['bid'],
                            "uid": user.objects.get(LOGIN=decoded_input[1]['uid']),
                            "f": decoded_input[1]['f'],
                            "d": decoded_input[1]['d'],
                            "ft": f.type,
                            "fp": "Update Amount",

                        }
                    )

        except Exception as e:
            print(e)
            pass
    print(data, "data")
    return render(request,'user/viewothersimage.html',{"data":data})


def payment(request,amount,id):
    request.session['rid']= id
    print(amount)
    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount = int(amount)*100
    # amount = float(amount)

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'user/payment.html',{'razorpay_api_key': razorpay_api_key,
                                            'amount': order_data['amount'],
                                            'currency': order_data['currency'],
                                            'order_id': order['id']})


from django.http import HttpResponseRedirect
import requests
from django.http import HttpResponse

def download_file_from_ipfs(request, ipfs_hash):
    # IPFS API endpoint
    ipfs_url = "http://127.0.0.1:8080/ipfs/{}".format(ipfs_hash)

    # Send a GET request to IPFS API
    response = requests.get(ipfs_url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Set the appropriate content type for the response
        content_type = response.headers.get('Content-Type', 'image/jpeg')

        # Set the filename for the response (you can use the IPFS hash as filename)
        filename = "{}.jpg".format(ipfs_hash)

        # Create the response with the downloaded file content
        http_response = HttpResponse(response.iter_content(chunk_size=4096), content_type=content_type)
        http_response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        return http_response
    else:
        return HttpResponse("Error downloading file from IPFS: {}".format(response.status_code), status=response.status_code)



def download_file_from_ipfs_video(request, ipfs_hash):
    # IPFS API endpoint
    ipfs_url = "http://127.0.0.1:8080/ipfs/{}".format(ipfs_hash)

    # Send a GET request to IPFS API
    response = requests.get(ipfs_url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Set the appropriate content type for the response
        content_type = response.headers.get('Content-Type', 'video/mp4')

        # Set the filename for the response (you can use the IPFS hash as filename)
        filename = "{}.mp4".format(ipfs_hash)

        # Create the response with the downloaded file content
        http_response = HttpResponse(response.iter_content(chunk_size=4096), content_type=content_type)
        http_response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        return http_response
    else:
        return HttpResponse("Error downloading file from IPFS: {}".format(response.status_code), status=response.status_code)
