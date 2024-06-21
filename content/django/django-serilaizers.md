Title: Serializers no Django Rest Framework
Date: 2024-03-01 10:20
Modified: 2024-06-10 19:30
Category: Django
Tags: drf, serializer, django, python
Slug: django-serializer
Author: Priscyla Santos
Lang: pt
Status: published
Summary: Serializers são elementos fundamentais no Django Rest Framework (DRF). Eles desempenham um papel crucial na comunicação entre a API e

<style>body {text-align: justify}</style>

Serializers são elementos fundamentais no Django Rest Framework (DRF). Eles desempenham um papel crucial na comunicação entre a API e o cliente, formatando dados de modelos Django para JSON, XML ou outros formatos serializados e vice-versa.

Este texto aprofundado, com base na documentação oficial do DRF, oferece uma compreensão abrangente dos serializers, explorando seus recursos e funcionalidades em detalhes.

### Funcionalidades Essenciais
Um serializer no DRF é uma classe que lida com a conversão entre objetos de modelo complexos e tipos de dados Python primitivos, que podem ser facilmente renderizados em JSON, XML ou outros tipos de conteúdo. Os serializers do DRF permitem:

- **Serialização:** converte objetos Python em representações serializadas em formatos como JSON, XML ou HTML.
- **Desserialização:** converte dados de requisições HTTP em objetos Python que podem ser manipulados pelo Django.
- **Validação:** garante que os dados recebidos nas requisições sejam válidos e consistentes com o modelo de dados do Django.

A criação de serializers envolve a definição de uma classe que herda de `serializers.Serializer` ou  de outros tipos de serializers como `serializers.ModelSerializer`. A classe define os campos a serem serializados, seus tipos de dados e outras opções de serialização. 

Abaixo temos um exemplo de como criar um serializer:

```python
from datetime import datetime
from rest_framework import serializers

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

#### Transformando Modelos em JSON
O processo de serialização converte objetos de modelo em representações JSON. O DRF fornece métodos convenientes para serializar objetos únicos ou conjuntos de objetos.

```python
serializer = CommentSerializer(comment)
serializer.data
{'email': 'leila@example.com', 'content': 'foo bar', 'created': '2016-01-27T15:17:10.375877'}
```

#### Reconstruindo Modelos a partir de JSON

A desserialização converte dados JSON em objetos de modelo. O DRF permite a criação de novos objetos ou a atualização de objetos existentes através da desserialização.

```python
data = {'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.now()}
serializer = CommentSerializer(data=data)
serializer.is_valid()
True
serializer.validated_data
```

#### Protegendo sua API contra dados inválidos
A validação é crucial para garantir a integridade dos dados. Os serializers do DRF oferecem várias formas de validar dados, incluindo validações a nível de campo e a nível de objeto. 

* **Validadores de campo:** garantem que cada campo individual atenda aos requisitos específicos.
* **Validadores de serializer:** permitem validações complexas que envolvem vários campos.

```python
serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})
serializer.is_valid()
False
serializer.errors
{'email': ['Enter a valid e-mail address.'], 'created': ['This field is required.']}
```

#### Criando e Atualizando Instâncias
Os serializers também lidam com a criação e atualização de instâncias de modelos. 
Serializers fornecem acesso aos dados iniciais recebidos da requisição e à instância do modelo que está sendo serializada ou desserializada. 
Isso permite a implementação de funcionalidades avançadas.

```python
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Comment(**validated_data)
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
```

```python
# Cria um nova instância (create)
serializer = CommentSerializer(data=data)

# Atualiza uma instância já exixtente (update)
serializer = CommentSerializer(comment, data=data)
```

### Práticas Recomendadas
- **Uso de ModelSerializer**: Quando possível, use `ModelSerializer` para aproveitar a geração automática de campos e métodos de criação/atualização, o que reduz o código necessário.
- **Validação**: Aproveite as capacidades de validação do DRF para manter a integridade dos dados. Isso inclui validações a nível de campo, a nível de objeto e validadores personalizados.

```python
from django.db import models
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100)
    style = models.CharField(default='friendly', max_length=100)
    
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```

- **Campos Somente Leitura**: Use o atributo read_only=True em campos que não devem ser alterados diretamente pelos usuários através da API.
- **Nested Serializers**: Para relações complexas, você pode usar serializers aninhados para representar relações de um para muitos ou muitos para muitos.

```python
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField(read_only=True )
```

### Conclusão
Este texto abordou os conceitos básicos e algumas práticas recomendadas para trabalhar com serializers no Django REST Framework. Para um aprofundamento, é altamente recomendável consultar a documentação oficial do DRF, que fornece informações detalhadas e exemplos específicos para diferentes casos de uso.

Serializers são ferramentas poderosas que facilitam a criação de APIs RESTful robustas e eficientes. Ao dominar os conceitos e funcionalidades dos serializers, você estará pronto para construir APIs que atendem às necessidades específicas do seu projeto.

**Referências**

* Documentação oficial do Django Rest Framework: [https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)
* Tutorial sobre Serializers no Django Rest Framework: [https://www.django-rest-framework.org/tutorial/1-serialization/](https://www.django-rest-framework.org/tutorial/1-serialization/)
