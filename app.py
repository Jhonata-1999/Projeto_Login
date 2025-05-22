import customtkinter as ctk

# Criação das funções de funcionalidade

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuario é jhonata e a senha 123456

    if usuario == 'jhonata' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!',
        text_color='green')
    else:
        resultado_login.configure(text='Login incorreto.',
        text_color='red')

# Configuração aparência

ctk.set_appearance_mode('dark')

# Criação da janela principal

app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criação dos campos
# Label

label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)

# Entry

campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

# Label

label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)

# Entry

campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha',show='*')
campo_senha.pack(pady=10)

# Button

botao_login = ctk.CTkButton(app,text='Login',command=validar_login)
botao_login.pack(pady=10)

# Feedback de login

resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

# Inicia o loop da aplicação
app.mainloop()