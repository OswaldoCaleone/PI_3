from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.messages import constants

from plataforma.models import Alunos, Escolas, Responsaveis, Transportadores


@login_required(login_url='/auth/logar/')
def plataforma(request):
    return render(request, 'plataforma.html')


@login_required(login_url='/auth/logar/')
def escolas(request):
    if request.method == "GET":
        return render(request, 'escolas.html')
    elif request.method == "POST": 
        nome_escola = request.POST.get('nome_escola')
        cnpj_escola = request.POST.get('cnpj_escola')
        end_escola = request.POST.get('end_escola')
        tel_escola = request.POST.get('tel_escola')
        email = request.POST.get('email')
        resp_escola = request.POST.get('resp_escola')
       
        if len(nome_escola.strip()) == 0 or len(cnpj_escola.strip()) == 0 or len(end_escola.strip()) == 0 or len(tel_escola.strip()) == 0 or len(email.strip()) == 0 or len(resp_escola.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/escolas')

        username = User.objects.filter(cnpj_escola=cnpj_escola).exclude(id=request.user.id)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse CNPJ')
            return redirect('/escolas')
        
        try:
            user = User.objects.create_user(nome_escola=nome_escola, cnpj_escola=cnpj_escola, end_escola=end_escola, tel_escola=tel_escola, email=email, resp_escola=resp_escola)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Escola adicionada com sucesso!')

            return redirect('/escolas')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/escolas')

        return HttpResponse(Recebido)
    return render(request, '/plataforma.html')


@login_required(login_url='/auth/logar/')
def responsaveis(request):
    if request.method == "GET":
        return render(request, 'responsaveis.html')
    elif request.method == "POST": 
        nome_resp = request.POST.get('nome_resp')
        cpf_resp = request.POST.get('cpf_resp')
        email = request.POST.get('email')
        end_resp = request.POST.get('end_resp')
        tel_resp = request.POST.get('tel_resp')
       
        if len(nome_resp.strip()) == 0 or len(cpf_resp.strip()) == 0 or len(email.strip()) == 0 or len(end_resp.strip()) == 0 or len(tel_resp.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/responsavel')

        username = User.objects.filter(username=username).exclude(id=request.user.id)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse CPF')
            return redirect('/responsaveis')
        
        try:
            user = User.objects.create_user(nome_resp=nome_resp, cpf_resp=cpf_resp, email=email, end_resp=end_resp, tel_resp=tel_resp)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Responsável adicionado com sucesso!')

            return redirect('/alunos')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/responsaveis')

        return HttpResponse(Recebido)

    return render(request, 'alunos.html')


@login_required(login_url='/auth/logar/')
def transportadores(request):
    if request.method == "GET":
        return render(request, 'transportadores.html')
    elif request.method == "POST": 
        primeiro_nome_transp = request.POST.get('primeiro_nome_transp')
        ultimo_nome_transp = request.POST.get('ultimo_nome_transp')
        cpf_transp = request.POST.get('cpf_transp')
        email = request.POST.get('email')
        end_transp = request.POST.get('end_transp')
        tel_transp = request.POST.get('tel_transp')
       
        if len(primeiro_nome_transp.strip()) == 0 or len(ultimo_nome_transp.strip()) == 0 or len(cpf_transp.strip()) == 0 or len(email.strip()) == 0 or len(end_transp.strip()) == 0 or len(tel_transp.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/transportadores')

        transportadores = Transportadores.objects.filter(email=email).exclude(id=request.user.id)

        if transportadores.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse CPF')
            return redirect('transportadores')
        
        try:
            user = User.objects.create_user(primeiro_nome_transp=primeiro_nome_transp, ultimo_nome_transp=ultimo_nome_transp, cpf_transp=cpf_transp, email=email, end_transp=end_transp, tel_transp=tel_transp)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'transportador adicionado com sucesso!')

            return redirect('/plataforma')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/transportadores')

        return HttpResponse(Recebido)

    return render(request, 'plataforma.html')

@login_required(login_url='/auth/logar/')
def alunos(request, id):
    aluno = get_object_or_404(Responsaveis, id==id)
    if not aluno.responsaveis == request.user:
        messages.add_message(request, constants.ERROR, 'Este aluno não é seu')
        return redirect('/aluno/')

    if request.method == "GET":
        alunos = alunos.objects.filter(responsaveis=request.user)
        return render(request, 'alunos.html', {'alunos': alunos})
    
    elif request.method == "POST":
        nome_aluno = request.POST.get('nome_aluno')
        end_aluno = request.POST.get('end_aluno')
        escola = request.POST.get('escola')
        end_escola = request.POST.get('end_escola')

        aluno = Alunos(nome_aluno=nome_aluno,
                        end_aluno=end_aluno,
                        escola=escola,
                        end_escola=end_escola)
        
        aluno.save()

        messages.add_message(request, constants.SUCCESS,'Aluno cadastrado com sucesso')


@login_required(login_url='/auth/logar/')
def localizacao(request):
    #if request.method == "GET":
        return render(request, 'localizacao.html')
    

@login_required(login_url='/auth/logar/')
def escolas_parceiras(request):
    #if request.method == "GET":
        return render(request, 'escolas_parceiras.html')
    

@login_required(login_url='/auth/logar/')
def consultar_transportadores(request):
    #if request.method == "GET":
        return render(request, 'consultar_transportadores.html')