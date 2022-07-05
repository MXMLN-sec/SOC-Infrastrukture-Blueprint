# Getting Started

# Voraussetzung 
JDK 1.8 und MAVEN 3.6 (alternativ kann auch Wrapper-Skript mvnw.cmd oder mvnw (LINUX)) sind installiert und im PATH und es besteht eine Netzverbindung (`proxy.materna.de` korrekt gesetzt) zu einem MAVEN-Repository.

Aktuell wird Apache Maven: 3.6.3 verwendet.
Der Wrapper kann mit mvn -N io.takari:maven:0.7.7:wrapper
akrualisiert werden.
Die Maven-Version kann in jse-demo\.mvn\wrapper\maven-wrapper.properties auf 3.8.2 hochgesetzt werden


Um ein funktionsfaehige Beispielprojektstruktur zu erzeugen, gibt es mehrere Möglichkeiten
Am einfachsten geht das fuer Java-Projekte und dem Build-Werkzeug MAVEN mit einem Archetype
`mvn archetype:generate`
	`-DgroupId={project-packaging}`
	`-DartifactId={project-name}`
	`-DarchetypeArtifactId={maven-template}`

Bsp. für ein einfaches JAVA SE 8 Projekt mit einem Junit4 Test
https://maven.apache.org/archetypes/maven-archetype-quickstart/

Beim Aufruf von

`mvn archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-quickstart`  
wird man nach den weiteren Parametern gefragt, die ihr für euer Projekt anpassen müsst
archetypeVersion=1.4
groupId: de.materna
artifactId: jse-demo
version: 1.0-SNAPSHOT
package: de.materna.jse

Danach könnt ihr mit folgenden Befehlen testen, ob eure Einstellungen und Umgebung korrekt funktioniert
`cd jse-demo`
`mvn package`


Alternativ könnt ihr auch die generierte Beispielstruktur in diesem DEMO-Projekt löschen und mit
 `mvn archetype:generate` euch einen anderen Projekttyp auswaehlen und erstellen lassen.
 Bsp. Spring Boot Tomcat Sample

 `mvn archetype:generate -DarchetypeGroupId=org.springframework.boot -DarchetypeArtifactId=spring-boot-sample-tomcat-archetype`

Weitere Infromationen zum Einstieg und Arbeiten mit MAVEN finden sich unter

https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

## MAVEN Standard Goals
Die wichtigsten Standardphasen für MAVEN sind:

    validate: validate the project is correct and all necessary information is available
    compile: compile the source code of the project
    test: test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed
    package: take the compiled code and package it in its distributable format, such as a JAR.
    integration-test: process and deploy the package if necessary into an environment where integration tests can be run
    verify: run any checks to verify the package is valid and meets quality criteria
    install: install the package into the local repository, for use as a dependency in other projects locally
    deploy: done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects
    clean: cleans up artifacts created by prior builds
    site: generates site documentation for this project
Bsp. `mvn test` ruft compile und dann test auf

Fuer Spring Boot kann man sich alternativ noch komfortabler ueber die Webseite https://start.spring.io/ ein Beispielprojekt erstellen lassen.
Gleiches gilt fuer JavaEE8 oder JakartaEE9 Microprofile-Projekte ueber https://start.microprofile.io/

## MAVEN advanced Goals
Folgende Befehle sollten im Projekt regelmaessig ausgefuehrt und dessen Ausgabe auf Massnahmen kontrolliert werden
Mit `mvn dependency:analyze` pruefen Sie ob unnoetige Abhaengigkeiten definiert sind
Mit `mvn versions:display-dependency-updates` werden zu den definierten Abhaengigkeiten neuere Versionen angezeigt, wenn moeglich sollten diese dann verwendet werden. Achtung manchmal gibt es Falschmeldungen!
Mit `mvn versions:display-plugin-updates` hier werden neuere Versionen der verwendeten Plugins angezeigt
Mit `mvn license:license-list` können Sie eine Liste der von Ihnen genutzten Lizenzen erstellen lassen
Mit `mvn org.owasp:dependency-check-maven:check` koennen Sie die benutzten Abhaengigkeiten auf bekannte Sicherheitsluecken (CVE, NIST) testen und sich hierfuer einen Bericht
`mvn org.owasp:dependency-check-maven:aggregate` erstellen lassen
Mit `mvn enforcer:display-info`  kann die eingesetzen Java und Maven-Versionen angezeigt werden
Mit `mvn depgraph:graph` und anschließenden
`dot -Tpng target\dependency-graph.dot > dependency-graph.png` kann man sich auch ein grphisches Bild seiner verwendeten Module erstellen lassen.
Über ein eigenes `mvn depgraph:graph -DcustomStyleConfiguration=custom-style.json` können Farben für eigene oder fremde Module vergeben werden. https://github.com/ferstl/depgraph-maven-plugin/wiki/Styling 
Alternativ geht mit dem integrierten Plugin `mvn dependency:tree  -Doutput=dependency-graph.dot` ein einfacher Abhängigkeitsgraph erstellt werden
Mit `mvn modernizer:modernizer` pruefen Sie, ob älteres Java oder abhängige Bibiliotheken APIs für die Nutzung mit der Java-Zielversion 11 Probleme machen


### Reference Documentation
For further reference, please consider the following sections:

* [Official Apache Maven documentation](https://maven.apache.org/guides/index.html)
* [Spring Boot Reference Documentation](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/)
* to use more error prone bug patterns see [https://errorprone.info/bugpatterns] eg 
    <arg>-Xplugin:ErrorProne
                -XepDisableWarningsInGeneratedCode
                -XepAllDisabledChecksAsWarnings
                -Xep:AndroidJdkLibsChecker:OFF
                -Xep:Java7ApiChecker:OFF
            </arg>
* to skip owasp checks ande downloading CVE-database  use `mvn clean install site:site -Ddependency-check.skip=true`
BITTE nicht vergessen .gitignore und pom.xml an eure aktuellen Anforderungen anzupassen.


### GRADLE BUILD ALTERNATIVE
Statt MAVEN kann auch GRADLE eingesetzt werden, was dazu unter https://gradle.org/releases/ heruntergeladen und im `set GRADLE_HOME=C:\gradle-6.1 und set PATH=%GRADLE_HOME%\bin;%PATH%` Pfad aufgenommen werden muss.
Alternativ können wie Wrapper-Skripte gradlew.bat (WINDOWS) oder gradlew (LINUX) verwendet werden
Informationen zu den einzelnen Tasks erhalten Sie mit `gradle tasks`
Mit `gradle init --type java-application`  kann eine intiale Projektstruktur erstellt werden oder eine build.gradle aus einer pom.xml erstellt werden
https://guides.gradle.org/creating-new-gradle-builds/
Ob die Abhaengigkeiten korrekt sind kann mit folgenden Gradle-Befehlen ueberprueft werden
https://docs.gradle.org/current/userguide/inspecting_dependencies.html
`gradle -q dependencies`
`gradle dependencies --configuration runtime`
`gradle dependencies --configuration compile`
`gradle help --scan` and view the deprecations view of the generated build scan.

### Conventional Commits verwenden (OPTIONAL)
Commit Nachrichten sollten aussagekräftig sein. Wer hierzu einen Standard verwenden möchte kann die Datei `.git\hooks\commit-msg.sample` in `commit-msg` umbenennen
https://www.conventionalcommits.org/en/v1.0.0/#specification 
Dazu muss `python` oder `pip` installiert sein
https://www.python.org/downloads/windows/ 
Test mit `pip --version`

### CHANGELOG.md erstellen (OPTIONAL)
Mit  https://github.com/conventional-changelog/standard-version kann aus den Commits ein CHANGELOG erstellt werden.
Einmalig Skript $ `npm i -g standard-version` installieren (node.js Installation benötigt)
$`standard-version --first-release` initales `CHANGELOG.md` erstellen oder einfach `standard-version`
Alternativ kann man auch das standard-version Skript in seinen npm Build einbauen oder diesen in MAVEN oder GRADLE automatisch anstossen lassen. 
Dazu `npm run script` zu `package.json` hinzufügen

`{
  "scripts": {
    "release": "standard-version"
  }
}` 

Now you can use `npm run release` in place of `npm version` or `standard-version`.

### vulnerabilities audit
JavaScript

Mit `npm audit` kann man zu seiner `package.json` bekannte Sicherheitslücken anzeigen lassen oder mit `npm audit fix` sogar korrigieren lassen
Alternativ geht das
`npm install -g auditjs`
`auditjs ossi`

JAVA

https://owasp.org/www-project-dependency-check/
oder
OWASP Find Security Bugs
Find Security Bugs is the SpotBugs plugin for security audits of Java web applications.
Website : http://find-sec-bugs.github.io/

### Testen (OPTIONAL)
Für Spring Boot Test gibt es einen fertigen Spring Boot Starter Test
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
Dieser enthält die aktuellen Versionen der beliebten Testwerkzeuge JUnit5, Mockito, Hamcrest, AssertJ, JSONassert und JsonPath
Es ist aber möglich deren Version z.B. für die Verwendung von Junit4 statt JUnit5 zu überschreiben
https://rieckpil.de/guide-to-testing-with-spring-boot-starter-test/

Ergänzungen oder Änderungen sind gerne willkommen und können an Frank.Pientka@materna.de geschickt werden


