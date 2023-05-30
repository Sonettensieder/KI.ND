KI.ND Sprechpartner:in

Autor: Samuel Mager
Lizenz: CC BY 4.0 (für Details siehe https://creativecommons.org/licenses/by/4.0/)

___________________________________________

ERKLÄRUNG IN DEUTSCH
(ENGLISH BELOW) 
___________________________________________


Die Software wandelt Spracheingabe in Text, sendet diesen an ChatGPT und gibt die Antwort per synthetischer Sprachausgabe wieder aus. Ein Chatbot im akkustischen Sinn. Es gibt zwei Skripte: "GPT3.5" nutzt die neuere KI und wird daher empfohlen. "GPT3" neigt zu einsilbigeren Antworten.

Du brauchst:

1) Einen (zunächst kostenlosen) Account bei OpenAi
2) Einen API-Key für OpenAIs ChatGPT API und OpenAIs Whisper, welchen Du hier generieren kannst: https://platform.openai.com/account/api-keys
3) Ein Zahlungsmittel, welches Du ebenfalls in deinem OpenAI-Account angibst. Leider ist die Nutzung durch API-Nutzung von ChatGPT und Whisper NICHT kostenlos. Entsprechende FOSS-Alternativen sind qualitativ nicht ansatzweise nutzbar. Allerdings werden Anfragen als Tokens abgerechnet, sodass sich die Kosten in niedrigen Bereichen bewegen. Für einen Probeprozess mit mehreren Aufführungen dürften die Kosten wenige Euro nicht überschreiten. Das Abomodell, welches OpenAI anbietet, ist NICHT nötig.
4) Eine Internetverbindung mit akzeptablem Upload. Die aufgenommene Wave-Datei ist zwischen 1,5 und 3 MB groß, eine Konvertierung in Mp3 würde noch länger dauern. Die Wave muss für Whisper hochgeladen werden, damit das Transkript an ChatGPT weitergegeben werden kann. Bei richtig gutem Upload beträgt die Wartezeit etwa 5 Sekunden per Prompt, bei schlechterem Upload kann es bis zu 20 Sekunden dauern.

So benutzt Du KI.ND:

1) Starte das Programm: Wenn Du einen Python 3.X-Interpreter installiert hast, kannst Du das direkt vom Skript aus tun. Wenn Du das nicht hast oder nicht weißt, was das ist, müsstest Du kurz danach recherchieren, wie ein Python-Skript in eine ausführbare Datei umgewandelt werden kann (im Fall von Windows endet diese auf .exe). Ich möchte Das "fertige" Programm nicht anbieten, weil grundsätlich NIEMAND im Internet eine EXE-Datei irgendwo herunterladen und ausführen sollte, das ist der schnellste Weg zu einem vervirten Rechner. Dieses Skript ist sicher, keine Sorge, aber bitte kompiliert Dateien selbst. Keine Sorge, es ist ganz simpel ;)

2) Beim sich öffnenden Fenster gibst Du Deinen API-Key (siehe oben) ein und drückst auf "Speichern". Dann drückst Du auf "Aufnahme" und sprichst Deine Eingabe. Nach einer kurzen (siehe oben) Wartezeit erfolgt die Ausgabe.

3) Die Software speichert die erstellte Audioaufnahme im Verzeichnis, in dem das Programm ausgeführt wird, als Wave ab. Wird eine neue Eingabe getätigt, wird die alte Wave überschrieben. Insofern entsteht kein Datenmüll, unter Umständen kann es aber sinnvoll oder wünschenswert sein, dass die Datei nach der Probe/Vorstellung händisch entfernt wird. Sie wird dann vom Programm einfach neu erstellt, so oder so.

Du kannst verschiedene Dinge anpassen:

1) Die Dauer, welche die Aufnahme läuft (Zeile 10 im Skript in Sekunden). 
2) Bei GPT3.5: Die "Identität" der KI in Zeile 35. Dieser Wert wird frei interpretiert, da kann also alles Mögliche stehen. Von "Du bist eine Gottheit" über "Du bist Shakespeare" bis hin zu "Du bist ein Instagram-Influencer" (Im Übrigen kann ich nicht gut einschätzen, wie gut die KI mit gendergerechter Sprache umgehen kann, das musst Du ausprobieren...) ist alles und noch viel mehr denkbar. Dies bestimmt auch die Ausgabesprache. Die KI wird in der Sprache antworten, die Du für die Zuweisung einer Rolle wählst.
3) Bei GPT3: Hier wird diese Rolle nicht frei zugeordnet. Stattdessen lässt sich in Zeile 32 die "Temperatur" einstellen auf einer Skala von 0 bis 1. 0 bedeutet technisch, analytisch, sachlich, 0.5 ist der Standardwert, 1 ist "crazy", wobei mein Eindruck ist, dass eine hohe Temperatur vor allem viel Blog-Spam à la "like and subscribe!" hervorbringt. Auch hier müsstest Du rumprobieren.

Viel Erfolg!

___________________________________________

SAME STUFF IN ENGLISH
___________________________________________

The software converts voice input into text, sends it to ChatGPT, and plays back the response via synthetic voice output. A chatbot in the acoustic sense. There are two scripts: "GPT3.5" uses the newer AI and is therefore recommended. "GPT3" tends to give more monosyllabic answers.

You need:

1) A (initially free) account with OpenAi.
2) An API key for OpenAi's ChatGPT API and OpenAi's Whisper, which you can generate here: https://platform.openai.com/account/api-keys
3) A payment method, which you also specify in your OpenAI account. Unfortunately, the API usage of ChatGPT and Whisper is NOT free. Corresponding FOSS alternatives are not qualitatively usable. However, requests are tokenized, so costs are in low ranges. For a trial process with several performances, the costs should not exceed a few euros. The subscription model that OpenAI offers is NOT necessary.
4) An internet connection with acceptable upload. The recorded Wave file is between 1.5 and 3 MB, conversion to Mp3 would take even longer. The Wave must be uploaded for Whisper to pass the transcript to ChatGPT. If the upload is really good, the waiting time is about 5 seconds per prompt, if the upload is worse, it can take up to 20 seconds.

How to use KI.ND:

1) Start the program: if you have a Python 3.X interpreter installed, you can do this directly from the script. If you don't have that or don't know what it is, you would have to research shortly after how to convert a Python script into an executable (in the case of Windows, this ends in .exe). I don't want to offer the "ready made" program, because basically NOBODY should download an EXE file anywhere on the internet and run it, that's the fastest way to get a virus infected computer. This script is safe, don't worry, but please compile files yourself. Don't worry, it's quite simple ;)

2) When the window opens, enter your API key (see above) and press "Save". Then press "Record" and speak your input. After a short (see above) waiting time the output takes place.

3) The software saves the created audio recording as a wave in the directory where the program is executed. If a new input is made, the old wave is overwritten. In this respect, there is no data garbage, but under certain circumstances it may be useful or desirable to manually remove the file after the rehearsal/performance. It will then simply be recreated by the program, one way or another.

You can adjust several things:

1) The duration the recording runs (line 10 in the scripts, measured in seconds). 
2) For GPT3.5: The "identity" of the AI in line 35. This value is interpreted freely, so it can be anything. From "You are a deity" to "You are Shakespeare" to "You are an Instagram influencer" anything and much more is conceivable. This determines output language as well, the AI will answer in the language you use to assign a role.
3) For GPT3: Here this role is not freely assigned. Instead, in line 32 you can set the "temperature" on a scale from 0 to 1. 0 means technical, analytical, factual, 0.5 is the default value, 1 is "crazy", whereas my impression is that a high temperature mainly produces a lot of blog spam à la "like and subscribe!". Again, you'd have to try it out.

Good luck!