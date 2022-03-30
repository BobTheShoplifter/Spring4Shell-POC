# Spring4Shell-POC
![spring4shell](spring4shell.png)

Spring4Shell Proof Of Concept/Information

Early this morning, multiple sources has informed of a possible RCE exploit in the popular java framework spring.

The naming of this flaw is based on the similarities to the infamous Log4j LOG4Shell. No POC has been shared for the time being

## Details

* https://www.cyberkendra.com/2022/03/springshell-rce-0-day-vulnerability.html
* https://bugalert.org/content/notices/2022-03-29-spring.html
* https://websecured.io/blog/624411cf775ad17d72274d16/spring4shell-poc

## CVE

- No cve assigned yet

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

find . -name spring-beans*.jar



## Poc

```python
```

WIP :=)
