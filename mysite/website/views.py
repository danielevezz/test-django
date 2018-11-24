from django.shortcuts import render

from .models import Event


def index(request):
    event_list = Event.objects.all()
    context = {
        "articles": [
            {
                "title": "The Metamorphosis",
                "summary": "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could se",
                "author": "Franz Kafka",
                "date": "02/04/1915",
                "image": "https://www.sololibri.net/local/cache-vignettes/L740xH340/arton146614-1e8f1.jpg?1538750777",
                "index": 0
            },
            {
                "title": "The Metamorphosis",
                "summary": "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could se",
                "author": "Franz Kafka",
                "date": "02/04/1915",
                "image": "https://www.sololibri.net/local/cache-vignettes/L740xH340/arton146614-1e8f1.jpg?1538750777",
                "index": 1
            },
            {
                "title": "The Metamorphosis",
                "summary": "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could se",
                "author": "Franz Kafka",
                "date": "02/04/1915",
                "image": "https://www.sololibri.net/local/cache-vignettes/L740xH340/arton146614-1e8f1.jpg?1538750777",
                "index": 2
            },
            {
                "title": "The Metamorphosis",
                "summary": "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could se",
                "author": "Franz Kafka",
                "date": "02/04/1915",
                "image": "https://www.sololibri.net/local/cache-vignettes/L740xH340/arton146614-1e8f1.jpg?1538750777",
                "index": 3
            },
            {
                "title": "The Metamorphosis",
                "summary": "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could se",
                "author": "Franz Kafka",
                "date": "02/04/1915",
                "image": "https://www.sololibri.net/local/cache-vignettes/L740xH340/arton146614-1e8f1.jpg?1538750777",
                "index": 4
            }
        ],
        "projects": [
            {
                "name": "ERK - GANN",
                "description": "Progettare una rete neurale in grado di classificare informazioni di carattere generico e gestirne l’evoluzione dei parametri (supervised training) mediante un apposito algoritmo genetico per giungere a un livello di errore al di sotto di una tolleranza data in tempi accettabili.",
                "manager": "Nicola Onofri",
                "creation_date": "18/10/2016",
                "image": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
            },
            {
                "name": "ERK - GANN",
                "description": "Progettare una rete neurale in grado di classificare informazioni di carattere generico e gestirne l’evoluzione dei parametri (supervised training) mediante un apposito algoritmo genetico per giungere a un livello di errore al di sotto di una tolleranza data in tempi accettabili.",
                "manager": "Nicola Onofri",
                "creation_date": "18/10/2016",
                "image": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
            },
            {
                "name": "ERK - GANN",
                "description": "Progettare una rete neurale in grado di classificare informazioni di carattere generico e gestirne l’evoluzione dei parametri (supervised training) mediante un apposito algoritmo genetico per giungere a un livello di errore al di sotto di una tolleranza data in tempi accettabili.",
                "manager": "Nicola Onofri",
                "creation_date": "18/10/2016",
                "image": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
            },
            {
                "name": "ERK - GANN",
                "description": "Progettare una rete neurale in grado di classificare informazioni di carattere generico e gestirne l’evoluzione dei parametri (supervised training) mediante un apposito algoritmo genetico per giungere a un livello di errore al di sotto di una tolleranza data in tempi accettabili.",
                "manager": "Nicola Onofri",
                "creation_date": "18/10/2016",
                "image": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
            }
        ],
        "top_news": [
            {
                "title": "Cisb 2018",
                "date": "02/04/1915"
            },
            {
                "title": "Cisb 2018",
                "date": "02/04/1915"
            },
            {
                "title": "Cisb 2018",
                "date": "02/04/1915"
            },
            {
                "title": "Cisb 2018",
                "date": "02/04/1915"
            },
            {
                "title": "Cisb 2018",
                "date": "02/04/1915"
            }
        ],
        "events": [
            {
                "name": "ERK - GANN",
                "description": "Progettare una rete neurale in grado di classificare informazioni di carattere generico e gestirne l’evoluzione dei parametri (supervised training) mediante un apposito algoritmo genetico per giungere a un livello di errore al di sotto di una tolleranza data in tempi accettabili.",
                "place": "Università degli studi di Brescia",
                "creation_date": "18/10/2016",
                "image": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
            },
            {
                "name": "ERK - GANN",
                "description": "Progettare una rete neurale in grado di classificare informazioni di carattere generico e gestirne l’evoluzione dei parametri (supervised training) mediante un apposito algoritmo genetico per giungere a un livello di errore al di sotto di una tolleranza data in tempi accettabili.",
                "place": "Università degli studi di Brescia",
                "creation_date": "18/10/2016",
                "image": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
            }
        ],
        "team": [
            {
                "name": "Nicola Onofri",
                "role": "Secretary",
                "avatar": "http://ieeesb.unibs.it/images/headers/ERK-logo.png",
                "links": {
                    "github": "http://ieeesb.unibs.it/images/headers/ERK-logo.png",
                    "fb": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
                }
            },
            {
                "name": "Nicola Onofri",
                "role": "Secretary",
                "avatar": "http://ieeesb.unibs.it/images/headers/ERK-logo.png",
                "links": {
                    "github": "http://ieeesb.unibs.it/images/headers/ERK-logo.png",
                    "fb": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
                }
            },
            {
                "name": "Nicola Onofri",
                "role": "Secretary",
                "avatar": "http://ieeesb.unibs.it/images/headers/ERK-logo.png",
                "links": {
                    "github": "http://ieeesb.unibs.it/images/headers/ERK-logo.png",
                    "fb": "http://ieeesb.unibs.it/images/headers/ERK-logo.png"
                }
            }
        ]
    }
    return render(request, "website/main_page/index.html", context)


def detail(request, event_id):
    e = Event.objects.get(id=event_id)
    context = {"event": e}
    return render(request, 'website/detail.html', context)
