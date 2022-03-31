# Spring4Shell-POC (CVE-2022-22965)
![spring4shell](spring4shell.png)

Spring4Shell (CVE-2022-22965) Proof Of Concept/Information

Early this morning, multiple sources has informed of a possible RCE exploit in the popular java framework spring.

The naming of this flaw is based on the similarities to the infamous Log4j LOG4Shell. 
## Details

* [https://www.cyberkendra.com/2022/03/springshell-rce-0-day-vulnerability.html](https://www.cyberkendra.com/2022/03/springshell-rce-0-day-vulnerability.html)
* [https://bugalert.org/content/notices/2022-03-29-spring.html](https://bugalert.org/content/notices/2022-03-29-spring.html)
* [https://websecured.io/blog/624411cf775ad17d72274d16/spring4shell-poc](https://websecured.io/blog/624411cf775ad17d72274d16/spring4shell-poc)
* [https://www.springcloud.io/post/2022-03/spring-0day-vulnerability](https://www.springcloud.io/post/2022-03/spring-0day-vulnerability)
* [https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement)

## CVE

- CVE-2022-22965

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

Do a global search after "spring-beans-*.jar" and "spring*.jar"

```sh
find . -name spring-beans*.jar
```



## Poc

Found intresting poc here : https://github.com/craig/SpringCore0day/blob/main/exp.py [^1]. & https://twitter.com/vxunderground/status/1509170582469943303

* clone sample repo from https://spring.io/guides/gs/handling-form-submission/
* you can skip right to the gs-handling-form-submission/complete directory, no need to follow the tutorial
* modify it so that you can build a war file (https://www.baeldung.com/spring-boot-war-tomcat-deploy). build war file :)
* install tomcat9 + java 11 (i did it on ubuntu 20.04 via apt-get)
* deploy the war file
* update the PoC (https://share.vx-underground.org/) to write the tomcatwar.jsp file to webapps/handling-form-submission instead of webapps/ROOT
* run PoC (ignore the URL it gives you for the webshell): python3 exp.py --url http://your.ip.here:8080/handling-form-submission-complete/greeting
* you should see the "tomcatwar.jsp" file now in webapps/handling-form-submission
* hit http://your.ip.here:8080/handling-form-submission/tomcatwar.jsp?pwd=j&cmd=id to see the results

WIP :=)

[^1]: POC, translated fron this repository.
