# Spring4Shell-POC (CVE-2022-22965)

![Spring4Shell](spring4shell.png)

![Docker Build](https://github.com/BobTheShoplifter/Spring4Shell-POC/actions/workflows/docker-publish.yml/badge.svg) ![Docker App Build](https://github.com/BobTheShoplifter/Spring4Shell-POC/actions/workflows/app-docker-publish.yml/badge.svg) ![Stars](https://img.shields.io/github/stars/BobTheShoplifter/Spring4Shell-POC?style=social) ![Docker Run](https://img.shields.io/github/followers/BobTheShoplifter?label=Follow&style=social)

Spring4Shell (CVE-2022-22965) Proof Of Concept/Information + [A vulnerable Tomcat server with a vulnerable spring4shell application.](vulnerable-tomcat/)

Early this morning, multiple sources has informed of a possible RCE exploit in the popular java framework spring.

The naming of this flaw is based on the similarities to the infamous Log4j LOG4Shell.

## Details about this vulnerability

- [https://websecured.io/blog/624411cf775ad17d72274d16/spring4shell-poc](https://websecured.io/blog/624411cf775ad17d72274d16/spring4shell-poc)
- [https://www.springcloud.io/post/2022-03/spring-0day-vulnerability](https://www.springcloud.io/post/2022-03/spring-0day-vulnerability)
- [https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement)

## POC Usage

The usage is simple! You can either run the docker image, or just run the python script!

Please see vulnerable-tomcat for inscructions on setting up your own spring4shell vulnerable application [here!](vulnerable-tomcat/)

### Requirements

- Python3 or [Docker](https://hub.docker.com/r/bobtheshoplifter/spring4shell-poc)

### Python

```python
pip install -r requirements.txt
poc.py --help
```

![image](https://user-images.githubusercontent.com/22559547/161398549-05d279b2-51d6-49fb-9245-018747606321.png)

### Docker

```sh
## Dockerhub
docker pull bobtheshoplifter/spring4shell-poc:latest
docker run bobtheshoplifter/spring4shell-poc:latest --url https://example.io/
## Github docker repository
docker pull ghcr.io/bobtheshoplifter/spring4shell-poc:main
docker run ghcr.io/bobtheshoplifter/spring4shell-poc:main --url https://example.io/
```

![image](https://user-images.githubusercontent.com/22559547/161400099-fb6c4f02-9d48-457a-8c91-041a9a8438b7.png)

## Vulnerable Tomcat server

I have now made a docker image for this, which includes a vulnerable spring + tomcat application.

The application should be enough to test this vulnerability.

[Please see (vulnerable-tomcat/README.md)](vulnerable-tomcat/README.md)

## Mitigations

!!(The following mitigations are only theoretical as nothing has been confirmed)!!

### JDK Version under 9

Cyberkendra informed that JDK versions lower than JDK 9

You can easily check this by running

```sh
java -version
```

That will display something similar to this

```sh
openjdk version "17.0.2" 2022-01-18
OpenJDK Runtime Environment (build 17.0.2+8-Ubuntu-120.04)
OpenJDK 64-Bit Server VM (build 17.0.2+8-Ubuntu-120.04, mixed mode, sharing)
```

If your JDK version is under 8, you might be safe, but nothing is confirmed yet

The following article will be updated

### Check if you are using the spring framework

Do a global search after `spring-beans*.jar` and `spring*.jar`

```sh
find . -name spring-beans*.jar
```

[^1]: POC, translated fron this repository.

POC, translated fron this repository: https://github.com/craig/SpringCore0day/blob/main/exp.py
