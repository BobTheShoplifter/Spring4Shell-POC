# Spring4Shell-POC (CVE-2022-22965)

![spring4shell](spring4shell.png)

Spring4Shell (CVE-2022-22965) Proof Of Concept/Information + A vulnerable Tomcat server with a vulnerable spring4shell application.

Early this morning, multiple sources has informed of a possible RCE exploit in the popular java framework spring.

The naming of this flaw is based on the similarities to the infamous Log4j LOG4Shell.

## Details about this vulnerability

- [https://www.cyberkendra.com/2022/03/springshell-rce-0-day-vulnerability.html](https://www.cyberkendra.com/2022/03/springshell-rce-0-day-vulnerability.html)
- [https://bugalert.org/content/notices/2022-03-29-spring.html](https://bugalert.org/content/notices/2022-03-29-spring.html)
- [https://websecured.io/blog/624411cf775ad17d72274d16/spring4shell-poc](https://websecured.io/blog/624411cf775ad17d72274d16/spring4shell-poc)
- [https://www.springcloud.io/post/2022-03/spring-0day-vulnerability](https://www.springcloud.io/post/2022-03/spring-0day-vulnerability)
- [https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement)

## Vulnerable Tomcat server

I have now made a docker image for this, which includes a vulnerable spring + tomcat application.

The application should be enough to test this vulnerability.

[Please see (vulnerable-tomcat/README.md)](vulnerable-tomcat/README.md)

## Requirements

- Python3 Or Docker

## Usage

```python
pip install -r requirements.txt
poc.py --help
```

![image](https://user-images.githubusercontent.com/22559547/161398549-05d279b2-51d6-49fb-9245-018747606321.png)

```sh
docker pull ghcr.io/bobtheshoplifter/spring4shell-poc:main
docker run ghcr.io/bobtheshoplifter/spring4shell-poc:main --url https://example.io/
```

![image](https://user-images.githubusercontent.com/22559547/161400099-fb6c4f02-9d48-457a-8c91-041a9a8438b7.png)

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

Do a global search after "spring-beans-_.jar" and "spring_.jar"

```sh
find . -name spring-beans*.jar
```

[^1]: POC, translated fron this repository.
