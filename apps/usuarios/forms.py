from django import forms

class LoginForm(forms.Form):
    nome_registro = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Lucas Vieira',
        })
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
          attrs={
              "class": "form-control",
              "placeholder": "Digite a sua senha",
          }
        )
    )

class CadastroForms(forms.Form):
    nome_registro = forms.CharField(
        label='Nome Completo',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Lucas Vieira',
            }
        )
    )

    email_registro = forms.EmailField(
        label='E-mail',
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: lucasvieira@gmail.com',
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha",
            }
        )
    )

    senha2 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme a sua senha",
            }
        )
    )

    def clean_nome_registro(self):
        nome = self.cleaned_data.get('nome_registro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo")
            else:
                return nome

    def clean_senha2(self):

        senha1 = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha')

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("Suas senhas não estão iguais")
            else:
                return senha2