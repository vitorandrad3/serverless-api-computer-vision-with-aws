O projeto tem o objetivo de criar uma API utilizando o serviço de visão computacional da AWS, o Rekognition, para classificar e recuperar labels de imagens e rostos.

## Arquitetura do Projeto



## Como utilizar a aplicação
- Tenha uma conta Postman
- Abra o Postman e escolha uma destas URL's e realize uma requisição POST para testar nos endpoints gerados após o deploy com o serverless

***EXEMPLOS FICTICIOS*** A aplicação pode atender qualquer imagem que esteja em um bucket do s3

- Utilize um destes jsons para testar 
```json
{
    "bucket": "bucketExemple",
    "imagename": "person.jpg"
}
```
```json
{
    "bucket": "bucketExemple",
    "imagename": "people.jpg"
}
```
```json
{
    "bucket": "bucketExemple",
    "imagename": "bird.jpg"
}
```
- retorno esperado v1_vision (bird.jpg):
```json
{
    "url_to_image": "s3LinkExemple.com",
    "created_image": "23-10-2023 12:18:48",
    "labels": [
        {
            "Confidence": 99.99836730957031,
            "Name": "Animal"
        },
        {
            "Confidence": 99.99836730957031,
            "Name": "Bird"
        },
        {
            "Confidence": 99.99836730957031,
            "Name": "Finch"
        },
        {
            "Confidence": 98.55673217773438,
            "Name": "Beak"
        },
        {
            "Confidence": 71.10396575927734,
            "Name": "Cardinal"
        }
    ]
}
```
- retorno esperado v2_vision (person.jpg):
```json
{
    "url_to_image": "s3LinkExemple.com",
    "created_image": "20-10-2023 14:58:34",
    "faces": [
        {
            "positon": {
                "Width": 0.22761882841587067,
                "Height": 0.38853025436401367,
                "Left": 0.3737991452217102,
                "Top": 0.17610755562782288
            },
            "classified_emotion": "SAD",
            "classified_emotion_confidence": 99.99689483642578
        }
    ]
}
```


## Arquitetura de Pasta
```bash
├── aws
│   ├── rekognition
│   │    ├── functions
│   │    │   ├── detect_faces.py
│   │    │   └── detect_labels.py
│   │    └── rekognition_client.py
│   ├── s3
│   │     ├──functions
│   │     │    └──  get_date.py
│   │     └── s3_client.py
│   └── boto_session.py
├── models
│   └── error_model.py
├── services
│   ├── template
│   │      └── handler.py
│   ├── v1_vision
│   │      └── handler.py
│   └── v2_vision
│          └── handler.py
├── utils
│   ├── format_date.py
│   └── get_user_input.py
├── tests
│   ├── ...
│
├── .env.exemple
├── .gitignore
├── package.json
├── README.md
├── requirements.txt
├── serverless.yml
└──test.json
```

## Coverage dos testes:


