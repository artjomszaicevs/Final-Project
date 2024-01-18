Projekts Artjoma Zaiceva un Džavida Gubatova

#Nasdaq OMX Nordic tīmekļa skrāpis.

Nasdaq OMX Nordic tīmekļa skrāpis ir Python skripts, kas izstrādāts, lai automatizētu datu ieguvi no Nasdaq OMX Nordic tīmekļa vietnes.

Šis rīks pārlūko tīmekļa vietni, vācot informāciju par akcijām un obligācijām dažādos tirgos; Baltijas valstu tirgū un konkrētās obligāciju kategorijās Dānijā, Zviedrijā, Islandē, Somijā un citur.

Šā projekta izstrādes laikā tiek izmantotas šādas Python bibliotēkas:

Selenium: Izmantots tīmekļa vietnes automatizētai pārlūkošanai un datu izgūšanai.

Time: Izmantots, lai ievietotu aizkavēsanas laiku skripta izpildei, īpaši gadījumos, kad nepieciešams pagaidīt, kamēr tīmekļa lapa ielādējas,lai nolasītu informāciju.

Ideja bija tāda, ka no sākuma mēs dabūsim akciju un obligāciju nosaukumus, kurus mēs saglabāsim atsevišķos teksta dokumentos (informācijas saglabāšana notika decembra beigās, 27 decembrī). Tādi teksta faili ir nosaukti ar ciparu 2 beigās vai "previous_day".

Pēc tam, modificējot kodu, programmai ir jāskrāp tīmekli un katru reizi jātaisa jaunus failus (bez cipara beigās vai "next_day"). 

Beigās, programmai ir divi faili par katru no tirgiem ar akciju vai obligāciju nosaukumiem. Pirmais ir nosaukumi, kurus mēs dabūjām 27 decembrī, un otrais ir nosaukumi, kad kods tiek palaists. Tad jauns fails tiek salīdzināts ar pirmo failu (27 decembra failu) un terminālā programmai ir jāuzraksta izmaiņas, kādas akcijas parādījās vai pazuda tirgū. 

