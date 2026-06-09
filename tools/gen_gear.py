# -*- coding: utf-8 -*-
"""Generate the 'custom-gear-manufacturing' article in 5 languages by cloning
each language's existing cnc-machining-tolerances article and swapping content.
Also patches blog indexes, capabilities pages and sitemap.xml."""
import os, re

BASE = r'C:\Users\druzh\bibparts'
SLUG = 'custom-gear-manufacturing'
IMG = '/assets/images/powder-metal-1.webp'
DATE = '2026-06-09'

LANGS = {
'en': {
 'title_tag': 'Custom Gear Manufacturing - BIB Parts',
 'desc': 'Custom gear manufacturing to drawing: spur, helical, bevel and worm gears in steel, stainless and bronze. Gear types, processes, accuracy classes and how to order precision gears.',
 'og_title': 'Custom Gear Manufacturing - BIB Parts',
 'headline': 'Custom Gear Manufacturing: Types, Materials and How to Source Precision Gears',
 'crumb': 'Custom Gear Manufacturing',
 'cat': 'Engineering guide', 'date': 'June 2026', 'read': '8 min read', 'tagslabel': 'Tags:',
 'cover_alt': 'Custom precision gears manufactured by BIB Parts',
 'h1': 'Custom Gear Manufacturing: Types, Materials and How to Source Precision Gears',
 'lead': 'Gears sit at the heart of almost every machine that transmits power. This guide covers the gear types we manufacture, the processes and materials behind them, the accuracy classes that matter, and exactly what to send us to get a fast, accurate quote for <strong>custom gears</strong>.',
 'tags': ['Gears', 'Gear manufacturing', 'Engineering guide', 'Precision'],
 'cta_h3': 'Need custom gears manufactured to drawing?',
 'cta_p': 'Send us your gear drawing or specifications and we will review them for manufacturability and quote within one business day.',
 'cta_btn': 'Get a quote &rarr;',
 'card_title': 'Custom Gear Manufacturing: Types, Materials and How to Source Precision Gears',
 'card_excerpt': 'We manufacture custom spur, helical, bevel and worm gears to drawing. A practical guide to gear types, machining and sintering processes, materials, DIN accuracy classes and how to order precision gears.',
 'cap_feature': 'Custom gear cutting - spur, helical, bevel and worm gears, splines and sprockets',
 'body': '''    <h2>Gear types we manufacture</h2>
    <p>We produce <strong>custom gears to drawing</strong> for power transmission, motion control and OEM assemblies - from single prototypes to production series. Our range covers:</p>
    <ul>
      <li><strong>Spur gears</strong> - the most common type, for parallel shafts and straightforward power transmission.</li>
      <li><strong>Helical gears</strong> - quieter and stronger than spur gears, for higher loads and speeds.</li>
      <li><strong>Bevel and crown gears</strong> - for transmitting motion between intersecting shafts.</li>
      <li><strong>Worm gears and worm shafts</strong> - for high reduction ratios in a compact envelope.</li>
      <li><strong>Internal (ring) gears</strong> - for planetary systems and compact drives.</li>
      <li><strong>Gear racks, splined shafts and sprockets</strong> - for linear motion and chain drives.</li>
    </ul>

    <h2>Gear manufacturing processes</h2>
    <p>The right process depends on size, accuracy class and volume. We use <strong>gear hobbing</strong> for external spur and helical gears, <strong>gear shaping</strong> for internal gears and tight-shoulder geometries, and <strong>5-axis CNC milling</strong> for bevel gears and one-off prototypes. For the highest accuracy, teeth are finished by <strong>profile grinding</strong>. For high-volume small gears, <strong>sintered powder-metal gears</strong> offer a near-net-shape, low-waste alternative.</p>

    <h2>Materials and heat treatment</h2>
    <p>Gear performance is set as much by material and heat treatment as by geometry. Common choices:</p>
    <ul>
      <li><strong>Case-hardening steels</strong> (16MnCr5, 18CrNiMo7-6) - a hard, wear-resistant surface over a tough core.</li>
      <li><strong>Through-hardening steel</strong> (42CrMo4) - for highly loaded gears and shafts.</li>
      <li><strong>Stainless steel</strong> - for corrosion resistance and hygienic applications.</li>
      <li><strong>Brass and bronze</strong> - for worm wheels and low-noise, low-load gears.</li>
      <li><strong>Engineering plastics</strong> (POM, PA) - for quiet, lightweight, lubrication-free drives.</li>
    </ul>
    <p>Typical treatments include case hardening, induction hardening, nitriding and quench-and-temper, followed by grinding where final accuracy demands it.</p>

    <h2>Gear accuracy and quality control</h2>
    <p>Gear accuracy is defined by quality classes to <code>DIN 3962</code> / <code>ISO 1328</code> (lower number = higher accuracy). The class you need drives both process and cost:</p>
    <table>
      <thead><tr><th>Process</th><th>Typical accuracy</th><th>Application</th></tr></thead>
      <tbody>
        <tr><td>Profile grinding</td><td>DIN 4-6</td><td>High-speed, low-noise, high-load drives</td></tr>
        <tr><td>Hobbing / shaping</td><td>DIN 7-8</td><td>General industrial gearboxes and drives</td></tr>
        <tr><td>CNC milling</td><td>DIN 9-10</td><td>Prototypes, large or low-speed gears</td></tr>
        <tr><td>PM sintering</td><td>DIN 9-11</td><td>High-volume small gears</td></tr>
      </tbody>
    </table>
    <p>Every gear is inspected on gear-measuring and CMM equipment - profile, lead, pitch and runout - and supplied with a dimensional report on request.</p>

    <h2>How to order custom gears</h2>
    <p>To quote quickly and accurately, send a drawing or simply these parameters:</p>
    <ul>
      <li><strong>Module</strong> (or DP), <strong>number of teeth</strong> and <strong>pressure angle</strong></li>
      <li><strong>Helix angle</strong> and hand (for helical gears)</li>
      <li><strong>Face width</strong>, <strong>bore</strong> and keyway or spline</li>
      <li><strong>Quality class</strong>, <strong>material</strong> and heat treatment</li>
      <li><strong>Quantity</strong> and any reference sample or existing gear</li>
    </ul>
    <blockquote><p>No drawing? Send us a sample or a worn gear. We can reverse-engineer the geometry and reproduce it to the original specification.</p></blockquote>

    <h2>Why source gears from BIB Parts</h2>
    <p>We are a single-source manufacturing partner: gear cutting, heat treatment, grinding and surface finishing backed by in-house engineering and a DFM review on every quote. From a single replacement gear to a production series, you get one supplier, one point of contact and consistent quality. <a href="/en/capabilities/">See all our manufacturing capabilities</a> or <a href="/en/contact/">request a gear quote</a>.</p>''',
},
'de': {
 'title_tag': 'Zahnradfertigung nach Maß - BIB Parts',
 'desc': 'Zahnradfertigung nach Zeichnung: Stirn-, Schräg-, Kegel- und Schneckenräder aus Stahl, Edelstahl und Bronze. Zahnradarten, Verfahren, Genauigkeitsklassen und Bestellung.',
 'og_title': 'Zahnradfertigung nach Maß - BIB Parts',
 'headline': 'Zahnradfertigung nach Maß: Arten, Werkstoffe und Beschaffung von Präzisionszahnrädern',
 'crumb': 'Zahnradfertigung nach Maß',
 'cat': 'Engineering-Leitfaden', 'date': 'Juni 2026', 'read': '8 Min. Lesezeit', 'tagslabel': 'Tags:',
 'cover_alt': 'Präzisionszahnräder nach Maß, gefertigt von BIB Parts',
 'h1': 'Zahnradfertigung nach Maß: Arten, Werkstoffe und Beschaffung von Präzisionszahnrädern',
 'lead': 'Zahnräder sind das Herzstück nahezu jeder Maschine, die Leistung überträgt. Dieser Leitfaden behandelt die Zahnradarten, die wir fertigen, die Verfahren und Werkstoffe dahinter, die entscheidenden Genauigkeitsklassen und genau das, was Sie uns für ein schnelles, präzises Angebot für <strong>Zahnräder nach Maß</strong> senden sollten.',
 'tags': ['Zahnräder', 'Zahnradfertigung', 'Engineering-Leitfaden', 'Präzision'],
 'cta_h3': 'Zahnräder nach Zeichnung benötigt?',
 'cta_p': 'Senden Sie uns Ihre Zahnradzeichnung oder Spezifikation - wir prüfen die Fertigbarkeit und erstellen innerhalb eines Werktags ein Angebot.',
 'cta_btn': 'Angebot anfordern &rarr;',
 'card_title': 'Zahnradfertigung nach Maß: Arten, Werkstoffe und Beschaffung von Präzisionszahnrädern',
 'card_excerpt': 'Wir fertigen Stirn-, Schräg-, Kegel- und Schneckenräder nach Zeichnung. Ein praktischer Leitfaden zu Zahnradarten, Fertigungs- und Sinterverfahren, Werkstoffen, DIN-Genauigkeitsklassen und zur Bestellung.',
 'cap_feature': 'Zahnradfertigung nach Maß - Stirn-, Schräg-, Kegel- und Schneckenräder, Verzahnungen und Kettenräder',
 'body': '''    <h2>Zahnradarten, die wir fertigen</h2>
    <p>Wir fertigen <strong>Zahnräder nach Zeichnung</strong> für Antriebstechnik, Bewegungssteuerung und OEM-Baugruppen - vom Einzelprototyp bis zur Serie. Unser Spektrum umfasst:</p>
    <ul>
      <li><strong>Stirnräder</strong> - die häufigste Bauart, für parallele Wellen und einfache Leistungsübertragung.</li>
      <li><strong>Schrägverzahnte Räder</strong> - leiser und tragfähiger als Stirnräder, für höhere Lasten und Drehzahlen.</li>
      <li><strong>Kegel- und Kronenräder</strong> - zur Übertragung zwischen sich schneidenden Wellen.</li>
      <li><strong>Schneckenräder und Schneckenwellen</strong> - für hohe Übersetzungen auf engem Bauraum.</li>
      <li><strong>Innen- (Hohl-)Räder</strong> - für Planetensysteme und kompakte Antriebe.</li>
      <li><strong>Zahnstangen, Keilwellen und Kettenräder</strong> - für Linearbewegung und Kettenantriebe.</li>
    </ul>

    <h2>Fertigungsverfahren für Zahnräder</h2>
    <p>Das richtige Verfahren hängt von Größe, Genauigkeitsklasse und Stückzahl ab. Wir setzen <strong>Wälzfräsen</strong> für außenverzahnte Stirn- und Schrägräder ein, <strong>Wälzstoßen</strong> für Innenverzahnungen und enge Geometrien sowie <strong>5-Achs-CNC-Fräsen</strong> für Kegelräder und Einzelprototypen. Für höchste Genauigkeit werden die Zähne durch <strong>Profilschleifen</strong> endbearbeitet. Für kleine Zahnräder in großen Stückzahlen bieten <strong>gesinterte Pulvermetall-Zahnräder</strong> eine endkonturnahe, abfallarme Alternative.</p>

    <h2>Werkstoffe und Wärmebehandlung</h2>
    <p>Die Leistung eines Zahnrads wird ebenso von Werkstoff und Wärmebehandlung wie von der Geometrie bestimmt. Übliche Optionen:</p>
    <ul>
      <li><strong>Einsatzstähle</strong> (16MnCr5, 18CrNiMo7-6) - harte, verschleißfeste Oberfläche über zähem Kern.</li>
      <li><strong>Vergütungsstahl</strong> (42CrMo4) - für hochbelastete Zahnräder und Wellen.</li>
      <li><strong>Edelstahl</strong> - für Korrosionsbeständigkeit und hygienische Anwendungen.</li>
      <li><strong>Messing und Bronze</strong> - für Schneckenräder sowie geräuscharme, gering belastete Räder.</li>
      <li><strong>Technische Kunststoffe</strong> (POM, PA) - für leise, leichte und schmierungsfreie Antriebe.</li>
    </ul>
    <p>Typische Verfahren sind Einsatzhärten, Induktionshärten, Nitrieren und Vergüten, bei Bedarf gefolgt von Schleifen für die Endgenauigkeit.</p>

    <h2>Genauigkeit und Qualitätssicherung</h2>
    <p>Die Verzahnungsqualität wird über Qualitätsklassen nach <code>DIN 3962</code> / <code>ISO 1328</code> definiert (kleinere Zahl = höhere Genauigkeit). Die benötigte Klasse bestimmt Verfahren und Kosten:</p>
    <table>
      <thead><tr><th>Verfahren</th><th>Typische Genauigkeit</th><th>Anwendung</th></tr></thead>
      <tbody>
        <tr><td>Profilschleifen</td><td>DIN 4-6</td><td>Schnelllaufende, geräuscharme, hochbelastete Antriebe</td></tr>
        <tr><td>Wälzfräsen / -stoßen</td><td>DIN 7-8</td><td>Allgemeine Industriegetriebe und Antriebe</td></tr>
        <tr><td>CNC-Fräsen</td><td>DIN 9-10</td><td>Prototypen, große oder langsam laufende Räder</td></tr>
        <tr><td>PM-Sintern</td><td>DIN 9-11</td><td>Kleine Zahnräder in großen Stückzahlen</td></tr>
      </tbody>
    </table>
    <p>Jedes Zahnrad wird auf Verzahnungsmess- und KMG-Technik geprüft - Profil, Flankenlinie, Teilung und Rundlauf - und auf Wunsch mit Messprotokoll geliefert.</p>

    <h2>So bestellen Sie Zahnräder nach Maß</h2>
    <p>Für ein schnelles, präzises Angebot senden Sie uns eine Zeichnung oder einfach diese Parameter:</p>
    <ul>
      <li><strong>Modul</strong> (oder DP), <strong>Zähnezahl</strong> und <strong>Eingriffswinkel</strong></li>
      <li><strong>Schrägungswinkel</strong> und Richtung (bei Schrägverzahnung)</li>
      <li><strong>Zahnbreite</strong>, <strong>Bohrung</strong> sowie Passfeder oder Verzahnung</li>
      <li><strong>Qualitätsklasse</strong>, <strong>Werkstoff</strong> und Wärmebehandlung</li>
      <li><strong>Stückzahl</strong> und ein Muster oder vorhandenes Zahnrad</li>
    </ul>
    <blockquote><p>Keine Zeichnung? Senden Sie uns ein Muster oder ein verschlissenes Zahnrad. Wir ermitteln die Geometrie per Reverse Engineering und reproduzieren es nach Originalspezifikation.</p></blockquote>

    <h2>Warum Zahnräder von BIB Parts</h2>
    <p>Wir sind Ihr Fertigungspartner aus einer Hand: Verzahnen, Wärmebehandlung, Schleifen und Oberflächenbearbeitung - gestützt auf eigene Konstruktion und eine DFM-Prüfung bei jedem Angebot. Vom einzelnen Ersatzrad bis zur Serie erhalten Sie einen Lieferanten, einen Ansprechpartner und gleichbleibende Qualität. <a href="/de/capabilities/">Alle Fertigungskompetenzen ansehen</a> oder <a href="/de/contact/">Zahnrad-Angebot anfordern</a>.</p>''',
},
'es': {
 'title_tag': 'Fabricación de engranajes a medida - BIB Parts',
 'desc': 'Fabricación de engranajes a medida según plano: rectos, helicoidales, cónicos y sinfín en acero, inox y bronce. Tipos, procesos, clases de precisión y cómo pedir.',
 'og_title': 'Fabricación de engranajes a medida - BIB Parts',
 'headline': 'Fabricación de engranajes a medida: tipos, materiales y cómo solicitar engranajes de precisión',
 'crumb': 'Fabricación de engranajes',
 'cat': 'Guía de ingeniería', 'date': 'Junio 2026', 'read': '8 min de lectura', 'tagslabel': 'Etiquetas:',
 'cover_alt': 'Engranajes de precisión a medida fabricados por BIB Parts',
 'h1': 'Fabricación de engranajes a medida: tipos, materiales y cómo solicitar engranajes de precisión',
 'lead': 'Los engranajes están en el corazón de casi toda máquina que transmite potencia. Esta guía cubre los tipos de engranajes que fabricamos, los procesos y materiales que los respaldan, las clases de precisión que importan y exactamente qué enviarnos para obtener un presupuesto rápido y preciso de <strong>engranajes a medida</strong>.',
 'tags': ['Engranajes', 'Fabricación de engranajes', 'Guía de ingeniería', 'Precisión'],
 'cta_h3': '¿Necesita engranajes fabricados según plano?',
 'cta_p': 'Envíenos el plano o las especificaciones de su engranaje; revisaremos su fabricabilidad y le daremos presupuesto en un día laborable.',
 'cta_btn': 'Pedir presupuesto &rarr;',
 'card_title': 'Fabricación de engranajes a medida: tipos, materiales y cómo solicitar engranajes de precisión',
 'card_excerpt': 'Fabricamos engranajes rectos, helicoidales, cónicos y sinfín según plano. Una guía práctica de tipos de engranajes, procesos de mecanizado y sinterizado, materiales, clases de precisión DIN y cómo pedirlos.',
 'cap_feature': 'Tallado de engranajes a medida - rectos, helicoidales, cónicos y sinfín, estriados y piñones',
 'body': '''    <h2>Tipos de engranajes que fabricamos</h2>
    <p>Fabricamos <strong>engranajes a medida según plano</strong> para transmisión de potencia, control de movimiento y conjuntos OEM, desde prototipos unitarios hasta series de producción. Nuestra gama incluye:</p>
    <ul>
      <li><strong>Engranajes rectos</strong> - el tipo más común, para ejes paralelos y transmisión directa.</li>
      <li><strong>Engranajes helicoidales</strong> - más silenciosos y resistentes que los rectos, para mayores cargas y velocidades.</li>
      <li><strong>Engranajes cónicos y de corona</strong> - para transmitir entre ejes que se cruzan.</li>
      <li><strong>Engranajes sinfín y tornillos sinfín</strong> - para grandes reducciones en poco espacio.</li>
      <li><strong>Engranajes internos (corona)</strong> - para sistemas planetarios y accionamientos compactos.</li>
      <li><strong>Cremalleras, ejes estriados y piñones</strong> - para movimiento lineal y transmisiones por cadena.</li>
    </ul>

    <h2>Procesos de fabricación de engranajes</h2>
    <p>El proceso adecuado depende del tamaño, la clase de precisión y el volumen. Usamos <strong>fresado por generación (hobbing)</strong> para engranajes rectos y helicoidales exteriores, <strong>mortajado</strong> para engranajes internos y geometrías ajustadas, y <strong>fresado CNC de 5 ejes</strong> para engranajes cónicos y prototipos. Para la máxima precisión, los dientes se acaban por <strong>rectificado de perfil</strong>. Para engranajes pequeños de gran volumen, los <strong>engranajes sinterizados de metal en polvo</strong> ofrecen una alternativa de forma casi neta y bajo desperdicio.</p>

    <h2>Materiales y tratamiento térmico</h2>
    <p>El rendimiento de un engranaje depende tanto del material y el tratamiento térmico como de la geometría. Opciones habituales:</p>
    <ul>
      <li><strong>Aceros de cementación</strong> (16MnCr5, 18CrNiMo7-6) - superficie dura y resistente al desgaste sobre núcleo tenaz.</li>
      <li><strong>Acero de temple total</strong> (42CrMo4) - para engranajes y ejes muy cargados.</li>
      <li><strong>Acero inoxidable</strong> - para resistencia a la corrosión y aplicaciones higiénicas.</li>
      <li><strong>Latón y bronce</strong> - para coronas sinfín y engranajes silenciosos de baja carga.</li>
      <li><strong>Plásticos técnicos</strong> (POM, PA) - para accionamientos silenciosos, ligeros y sin lubricación.</li>
    </ul>
    <p>Los tratamientos típicos incluyen cementación, temple por inducción, nitruración y temple y revenido, seguidos de rectificado cuando la precisión final lo exige.</p>

    <h2>Precisión y control de calidad</h2>
    <p>La precisión del engranaje se define por clases de calidad según <code>DIN 3962</code> / <code>ISO 1328</code> (número menor = mayor precisión). La clase necesaria determina proceso y coste:</p>
    <table>
      <thead><tr><th>Proceso</th><th>Precisión típica</th><th>Aplicación</th></tr></thead>
      <tbody>
        <tr><td>Rectificado de perfil</td><td>DIN 4-6</td><td>Accionamientos rápidos, silenciosos y muy cargados</td></tr>
        <tr><td>Hobbing / mortajado</td><td>DIN 7-8</td><td>Reductores y accionamientos industriales generales</td></tr>
        <tr><td>Fresado CNC</td><td>DIN 9-10</td><td>Prototipos, engranajes grandes o de baja velocidad</td></tr>
        <tr><td>Sinterizado PM</td><td>DIN 9-11</td><td>Engranajes pequeños de gran volumen</td></tr>
      </tbody>
    </table>
    <p>Cada engranaje se inspecciona en equipos de medición de engranajes y MMC - perfil, hélice, paso y excentricidad - y se entrega con informe dimensional bajo petición.</p>

    <h2>Cómo pedir engranajes a medida</h2>
    <p>Para presupuestar de forma rápida y precisa, envíe un plano o simplemente estos parámetros:</p>
    <ul>
      <li><strong>Módulo</strong> (o DP), <strong>número de dientes</strong> y <strong>ángulo de presión</strong></li>
      <li><strong>Ángulo de hélice</strong> y sentido (en helicoidales)</li>
      <li><strong>Ancho de cara</strong>, <strong>agujero</strong> y chavetero o estriado</li>
      <li><strong>Clase de calidad</strong>, <strong>material</strong> y tratamiento térmico</li>
      <li><strong>Cantidad</strong> y cualquier muestra o engranaje existente de referencia</li>
    </ul>
    <blockquote><p>¿Sin plano? Envíenos una muestra o un engranaje desgastado. Podemos hacer ingeniería inversa de la geometría y reproducirlo según la especificación original.</p></blockquote>

    <h2>Por qué fabricar engranajes con BIB Parts</h2>
    <p>Somos un socio de fabricación integral: tallado, tratamiento térmico, rectificado y acabado superficial, respaldados por ingeniería propia y revisión DFM en cada presupuesto. Desde un engranaje de recambio hasta una serie, obtiene un proveedor, un interlocutor y calidad constante. <a href="/es/capabilities/">Vea todas nuestras capacidades</a> o <a href="/es/contact/">solicite presupuesto de engranajes</a>.</p>''',
},
'fr': {
 'title_tag': "Fabrication d'engrenages sur mesure - BIB Parts",
 'desc': "Fabrication d'engrenages sur mesure selon plan : droits, hélicoïdaux, coniques et à vis sans fin en acier, inox et bronze. Types, procédés, classes de précision et commande.",
 'og_title': "Fabrication d'engrenages sur mesure - BIB Parts",
 'headline': "Fabrication d'engrenages sur mesure : types, matériaux et comment commander des engrenages de précision",
 'crumb': "Fabrication d'engrenages",
 'cat': "Guide d'ingénierie", 'date': 'Juin 2026', 'read': '8 min de lecture', 'tagslabel': 'Tags :',
 'cover_alt': 'Engrenages de précision sur mesure fabriqués par BIB Parts',
 'h1': "Fabrication d'engrenages sur mesure : types, matériaux et comment commander des engrenages de précision",
 'lead': "Les engrenages sont au cœur de presque toutes les machines qui transmettent de la puissance. Ce guide présente les types d'engrenages que nous fabriquons, les procédés et matériaux associés, les classes de précision qui comptent et exactement ce qu'il faut nous envoyer pour obtenir rapidement un devis précis pour des <strong>engrenages sur mesure</strong>.",
 'tags': ['Engrenages', "Fabrication d'engrenages", "Guide d'ingénierie", 'Précision'],
 'cta_h3': "Besoin d'engrenages fabriqués selon plan ?",
 'cta_p': "Envoyez-nous le plan ou les spécifications de votre engrenage : nous en vérifions la fabricabilité et vous devisons sous un jour ouvré.",
 'cta_btn': 'Demander un devis &rarr;',
 'card_title': "Fabrication d'engrenages sur mesure : types, matériaux et comment commander des engrenages de précision",
 'card_excerpt': "Nous fabriquons des engrenages droits, hélicoïdaux, coniques et à vis sans fin selon plan. Un guide pratique des types d'engrenages, des procédés d'usinage et de frittage, des matériaux, des classes de précision DIN et de la commande.",
 'cap_feature': "Taillage d'engrenages sur mesure - droits, hélicoïdaux, coniques et à vis sans fin, cannelures et pignons",
 'body': '''    <h2>Types d'engrenages que nous fabriquons</h2>
    <p>Nous fabriquons des <strong>engrenages sur mesure selon plan</strong> pour la transmission de puissance, le contrôle de mouvement et les ensembles OEM, du prototype unitaire à la série. Notre gamme couvre :</p>
    <ul>
      <li><strong>Engrenages droits</strong> - le type le plus courant, pour arbres parallèles et transmission directe.</li>
      <li><strong>Engrenages hélicoïdaux</strong> - plus silencieux et résistants que les droits, pour charges et vitesses élevées.</li>
      <li><strong>Engrenages coniques et à couronne</strong> - pour transmettre entre arbres concourants.</li>
      <li><strong>Roues et vis sans fin</strong> - pour de forts rapports de réduction dans un faible encombrement.</li>
      <li><strong>Engrenages intérieurs (couronnes)</strong> - pour trains planétaires et entraînements compacts.</li>
      <li><strong>Crémaillères, arbres cannelés et pignons</strong> - pour le mouvement linéaire et les transmissions par chaîne.</li>
    </ul>

    <h2>Procédés de fabrication des engrenages</h2>
    <p>Le bon procédé dépend de la taille, de la classe de précision et du volume. Nous utilisons le <strong>taillage à la fraise-mère</strong> pour les engrenages droits et hélicoïdaux extérieurs, le <strong>mortaisage</strong> pour les engrenages intérieurs et géométries serrées, et le <strong>fraisage CNC 5 axes</strong> pour les engrenages coniques et les prototypes. Pour la plus haute précision, les dents sont finies par <strong>rectification de profil</strong>. Pour les petits engrenages en grande série, les <strong>engrenages frittés en métal-poudre</strong> offrent une alternative quasi-finie et peu coûteuse en matière.</p>

    <h2>Matériaux et traitement thermique</h2>
    <p>La performance d'un engrenage dépend autant du matériau et du traitement thermique que de la géométrie. Choix courants :</p>
    <ul>
      <li><strong>Aciers de cémentation</strong> (16MnCr5, 18CrNiMo7-6) - surface dure et résistante à l'usure sur cœur tenace.</li>
      <li><strong>Acier trempé à cœur</strong> (42CrMo4) - pour engrenages et arbres fortement chargés.</li>
      <li><strong>Acier inoxydable</strong> - pour la résistance à la corrosion et les applications hygiéniques.</li>
      <li><strong>Laiton et bronze</strong> - pour roues de vis sans fin et engrenages silencieux peu chargés.</li>
      <li><strong>Plastiques techniques</strong> (POM, PA) - pour des entraînements silencieux, légers et sans lubrification.</li>
    </ul>
    <p>Les traitements typiques incluent cémentation, trempe par induction, nitruration et trempe-revenu, suivis de rectification lorsque la précision finale l'exige.</p>

    <h2>Précision et contrôle qualité</h2>
    <p>La précision d'un engrenage est définie par des classes de qualité selon <code>DIN 3962</code> / <code>ISO 1328</code> (numéro plus bas = précision plus élevée). La classe requise détermine le procédé et le coût :</p>
    <table>
      <thead><tr><th>Procédé</th><th>Précision typique</th><th>Application</th></tr></thead>
      <tbody>
        <tr><td>Rectification de profil</td><td>DIN 4-6</td><td>Entraînements rapides, silencieux et très chargés</td></tr>
        <tr><td>Taillage / mortaisage</td><td>DIN 7-8</td><td>Réducteurs et entraînements industriels courants</td></tr>
        <tr><td>Fraisage CNC</td><td>DIN 9-10</td><td>Prototypes, engrenages grands ou lents</td></tr>
        <tr><td>Frittage PM</td><td>DIN 9-11</td><td>Petits engrenages en grande série</td></tr>
      </tbody>
    </table>
    <p>Chaque engrenage est contrôlé sur équipements de mesure d'engrenages et MMT - profil, hélice, pas et faux-rond - et livré avec rapport dimensionnel sur demande.</p>

    <h2>Comment commander des engrenages sur mesure</h2>
    <p>Pour un devis rapide et précis, envoyez un plan ou simplement ces paramètres :</p>
    <ul>
      <li><strong>Module</strong> (ou DP), <strong>nombre de dents</strong> et <strong>angle de pression</strong></li>
      <li><strong>Angle d'hélice</strong> et sens (pour les hélicoïdaux)</li>
      <li><strong>Largeur de denture</strong>, <strong>alésage</strong> et clavette ou cannelure</li>
      <li><strong>Classe de qualité</strong>, <strong>matériau</strong> et traitement thermique</li>
      <li><strong>Quantité</strong> et tout échantillon ou engrenage existant de référence</li>
    </ul>
    <blockquote><p>Pas de plan ? Envoyez-nous un échantillon ou un engrenage usé. Nous relevons la géométrie par rétro-ingénierie et le reproduisons selon la spécification d'origine.</p></blockquote>

    <h2>Pourquoi fabriquer vos engrenages chez BIB Parts</h2>
    <p>Nous sommes un partenaire de fabrication unique : taillage, traitement thermique, rectification et finition de surface, soutenus par un bureau d'études interne et une revue DFM sur chaque devis. D'un engrenage de rechange à une série, vous avez un fournisseur, un interlocuteur et une qualité constante. <a href="/fr/capabilities/">Voir toutes nos capacités</a> ou <a href="/fr/contact/">demander un devis d'engrenage</a>.</p>''',
},
'pl': {
 'title_tag': 'Produkcja kół zębatych na zamówienie - BIB Parts',
 'desc': 'Produkcja kół zębatych wg rysunku: walcowe, skośne, stożkowe i ślimakowe ze stali, nierdzewki i brązu. Rodzaje, procesy, klasy dokładności i jak zamówić.',
 'og_title': 'Produkcja kół zębatych na zamówienie - BIB Parts',
 'headline': 'Produkcja kół zębatych na zamówienie: rodzaje, materiały i jak zamówić koła precyzyjne',
 'crumb': 'Produkcja kół zębatych',
 'cat': 'Poradnik inżynieryjny', 'date': 'Czerwiec 2026', 'read': '8 min czytania', 'tagslabel': 'Tagi:',
 'cover_alt': 'Precyzyjne koła zębate na zamówienie produkowane przez BIB Parts',
 'h1': 'Produkcja kół zębatych na zamówienie: rodzaje, materiały i jak zamówić koła precyzyjne',
 'lead': 'Koła zębate są sercem niemal każdej maszyny przenoszącej moc. Ten poradnik omawia rodzaje kół, które produkujemy, procesy i materiały, istotne klasy dokładności oraz dokładnie to, co należy nam przesłać, aby szybko otrzymać precyzyjną wycenę <strong>kół zębatych na zamówienie</strong>.',
 'tags': ['Koła zębate', 'Produkcja kół zębatych', 'Poradnik inżynieryjny', 'Precyzja'],
 'cta_h3': 'Potrzebujesz kół zębatych wykonanych wg rysunku?',
 'cta_p': 'Prześlij rysunek lub specyfikację koła - sprawdzimy wykonalność i wycenimy w ciągu jednego dnia roboczego.',
 'cta_btn': 'Poproś o wycenę &rarr;',
 'card_title': 'Produkcja kół zębatych na zamówienie: rodzaje, materiały i jak zamówić koła precyzyjne',
 'card_excerpt': 'Produkujemy walcowe, skośne, stożkowe i ślimakowe koła zębate wg rysunku. Praktyczny poradnik o rodzajach kół, procesach obróbki i spiekania, materiałach, klasach dokładności DIN i sposobie zamawiania.',
 'cap_feature': 'Obróbka kół zębatych na zamówienie - walcowe, skośne, stożkowe i ślimakowe, wielowypusty i koła łańcuchowe',
 'body': '''    <h2>Rodzaje kół zębatych, które produkujemy</h2>
    <p>Produkujemy <strong>koła zębate na zamówienie wg rysunku</strong> do napędów, sterowania ruchem i zespołów OEM - od pojedynczych prototypów po serie produkcyjne. Nasza oferta obejmuje:</p>
    <ul>
      <li><strong>Koła walcowe (proste)</strong> - najczęstszy typ, do wałów równoległych i prostego przeniesienia napędu.</li>
      <li><strong>Koła skośne</strong> - cichsze i wytrzymalsze od prostych, do większych obciążeń i prędkości.</li>
      <li><strong>Koła stożkowe i koronowe</strong> - do przeniesienia napędu między wałami przecinającymi się.</li>
      <li><strong>Ślimaki i ślimacznice</strong> - do dużych przełożeń w małej zabudowie.</li>
      <li><strong>Koła wewnętrzne (wieńce)</strong> - do układów planetarnych i kompaktowych napędów.</li>
      <li><strong>Zębatki, wały wielowypustowe i koła łańcuchowe</strong> - do ruchu liniowego i napędów łańcuchowych.</li>
    </ul>

    <h2>Procesy produkcji kół zębatych</h2>
    <p>Właściwy proces zależy od wielkości, klasy dokładności i wielkości serii. Stosujemy <strong>obwiedniowe frezowanie (hobbing)</strong> do zewnętrznych kół walcowych i skośnych, <strong>dłutowanie</strong> do uzębień wewnętrznych i ciasnych geometrii oraz <strong>frezowanie CNC 5-osiowe</strong> do kół stożkowych i prototypów. Dla najwyższej dokładności zęby są wykańczane przez <strong>szlifowanie profilowe</strong>. Dla małych kół w dużych seriach <strong>spiekane koła z metalu proszkowego</strong> stanowią niemal gotową, niskoodpadową alternatywę.</p>

    <h2>Materiały i obróbka cieplna</h2>
    <p>Osiągi koła zależą tak samo od materiału i obróbki cieplnej, jak od geometrii. Typowe wybory:</p>
    <ul>
      <li><strong>Stale do nawęglania</strong> (16MnCr5, 18CrNiMo7-6) - twarda, odporna na zużycie powierzchnia na ciągliwym rdzeniu.</li>
      <li><strong>Stal ulepszana cieplnie</strong> (42CrMo4) - do mocno obciążonych kół i wałów.</li>
      <li><strong>Stal nierdzewna</strong> - do odporności na korozję i zastosowań higienicznych.</li>
      <li><strong>Mosiądz i brąz</strong> - do ślimacznic oraz cichych, lekko obciążonych kół.</li>
      <li><strong>Tworzywa konstrukcyjne</strong> (POM, PA) - do cichych, lekkich i bezsmarowych napędów.</li>
    </ul>
    <p>Typowe zabiegi to nawęglanie, hartowanie indukcyjne, azotowanie oraz ulepszanie cieplne, a w razie potrzeby szlifowanie dla końcowej dokładności.</p>

    <h2>Dokładność i kontrola jakości</h2>
    <p>Dokładność uzębienia określają klasy jakości wg <code>DIN 3962</code> / <code>ISO 1328</code> (niższa liczba = wyższa dokładność). Wymagana klasa decyduje o procesie i koszcie:</p>
    <table>
      <thead><tr><th>Proces</th><th>Typowa dokładność</th><th>Zastosowanie</th></tr></thead>
      <tbody>
        <tr><td>Szlifowanie profilowe</td><td>DIN 4-6</td><td>Szybkoobrotowe, ciche, mocno obciążone napędy</td></tr>
        <tr><td>Hobbing / dłutowanie</td><td>DIN 7-8</td><td>Ogólne przekładnie i napędy przemysłowe</td></tr>
        <tr><td>Frezowanie CNC</td><td>DIN 9-10</td><td>Prototypy, koła duże lub wolnoobrotowe</td></tr>
        <tr><td>Spiekanie PM</td><td>DIN 9-11</td><td>Małe koła w dużych seriach</td></tr>
      </tbody>
    </table>
    <p>Każde koło jest kontrolowane na urządzeniach do pomiaru uzębień i CMM - zarys, linia zęba, podziałka i bicie - oraz dostarczane z raportem wymiarowym na życzenie.</p>

    <h2>Jak zamówić koła zębate na zamówienie</h2>
    <p>Aby szybko i dokładnie wycenić, prześlij rysunek lub po prostu te parametry:</p>
    <ul>
      <li><strong>Moduł</strong> (lub DP), <strong>liczba zębów</strong> i <strong>kąt przyporu</strong></li>
      <li><strong>Kąt pochylenia linii zęba</strong> i kierunek (dla kół skośnych)</li>
      <li><strong>Szerokość wieńca</strong>, <strong>otwór</strong> oraz rowek wpustowy lub wielowypust</li>
      <li><strong>Klasa dokładności</strong>, <strong>materiał</strong> i obróbka cieplna</li>
      <li><strong>Ilość</strong> oraz wzór lub istniejące koło referencyjne</li>
    </ul>
    <blockquote><p>Brak rysunku? Prześlij wzór lub zużyte koło. Odtworzymy geometrię metodą inżynierii odwrotnej i wykonamy je zgodnie z oryginalną specyfikacją.</p></blockquote>

    <h2>Dlaczego koła zębate od BIB Parts</h2>
    <p>Jesteśmy partnerem produkcyjnym z jednego źródła: obróbka uzębień, obróbka cieplna, szlifowanie i wykończenie powierzchni, wsparte własnym biurem konstrukcyjnym i przeglądem DFM przy każdej wycenie. Od pojedynczego koła na wymianę po serię - jeden dostawca, jeden kontakt i stała jakość. <a href="/pl/capabilities/">Zobacz wszystkie nasze możliwości</a> lub <a href="/pl/contact/">poproś o wycenę kół zębatych</a>.</p>''',
},
}

def lit(s):
    """return a function for re.sub that inserts literal replacement"""
    return lambda m: s

def build_article(lang, d):
    src = os.path.join(BASE, lang, 'blog', 'cnc-machining-tolerances', 'index.html')
    with open(src, encoding='utf-8') as f:
        s = f.read()
    # 1. slug everywhere (paths, canonical, hreflang, og:url, switcher, JSON-LD urls)
    s = s.replace('cnc-machining-tolerances', SLUG)
    # 2. image (cover + og:image) -> existing asset
    s = s.replace('/assets/images/' + SLUG + '.webp', IMG)
    # 3. head meta
    s = re.sub(r'<title>.*?</title>', lit('<title>' + d['title_tag'] + '</title>'), s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*"', lit('<meta name="description" content="' + d['desc'] + '"'), s, count=1)
    s = re.sub(r'(<meta property="og:title" content=)"[^"]*"', lit('<meta property="og:title" content="' + d['og_title'] + '"'), s, count=1)
    s = re.sub(r'(<meta property="og:description" content=)"[^"]*"', lit('<meta property="og:description" content="' + d['desc'] + '"'), s, count=1)
    s = re.sub(r'(<meta property="article:published_time" content=)"[^"]*"', lit('<meta property="article:published_time" content="' + DATE + '"'), s, count=1)
    # 4. JSON-LD values
    s = re.sub(r'"headline":\s*"[^"]*"', lit('"headline": "' + d['headline'] + '"'), s, count=1)
    s = re.sub(r'"description":\s*"[^"]*"', lit('"description": "' + d['desc'] + '"'), s, count=1)
    s = re.sub(r'"datePublished":\s*"[^"]*"', lit('"datePublished": "' + DATE + '"'), s, count=1)
    s = re.sub(r'("position": 3, "name": )"[^"]*"', lit('"position": 3, "name": "' + d['crumb'] + '"'), s, count=1)
    # 5. breadcrumb visible last span
    s = re.sub(r'(<a href="/' + lang + r'/blog/">[^<]*</a>\s*<span class="breadcrumb-sep">[^<]*</span>\s*<span>).*?(</span>)',
               lambda m: m.group(1) + d['crumb'] + m.group(2), s, count=1, flags=re.S)
    # 6. cover alt
    s = re.sub(r'(<div class="article-cover full-width">\s*<img src="' + re.escape(IMG) + r'" alt=)"[^"]*"',
               lit('<div class="article-cover full-width">\n    <img src="' + IMG + '" alt="' + d['cover_alt'] + '"'), s, count=1, flags=re.S)
    # 7. header block
    header = ('<header class="article-header">\n'
        '    <div class="article-meta">\n'
        '      <span class="article-cat">' + d['cat'] + '</span>\n'
        '      <span class="meta-sep">&middot;</span>\n'
        '      <span class="article-date">' + d['date'] + '</span>\n'
        '      <span class="meta-sep">&middot;</span>\n'
        '      <span class="article-read-time">' + d['read'] + '</span>\n'
        '      <span class="meta-sep">&middot;</span>\n'
        '      <span class="article-author">BIB Parts</span>\n'
        '    </div>\n'
        '    <h1 class="article-title">' + d['h1'] + '</h1>\n'
        '    <p class="article-lead">' + d['lead'] + '</p>\n'
        '  </header>')
    s = re.sub(r'<header class="article-header">.*?</header>', lit(header), s, count=1, flags=re.S)
    # 8. body
    body = '<article class="article-body">\n' + d['body'] + '\n\n  </article>'
    s = re.sub(r'<article class="article-body">.*?</article>', lit(body), s, count=1, flags=re.S)
    # 9. tags
    tags = '<div class="article-tags">\n      <span class="tag-label">' + d['tagslabel'] + '</span>\n'
    for t in d['tags']:
        tags += '      <span class="tag">' + t + '</span>\n'
    tags += '    </div>'
    s = re.sub(r'<div class="article-tags">.*?</div>', lit(tags), s, count=1, flags=re.S)
    # 10. cta
    cta = ('<div class="article-cta">\n'
        '      <div class="article-cta-text">\n'
        '        <h3>' + d['cta_h3'] + '</h3>\n'
        '        <p>' + d['cta_p'] + '</p>\n'
        '      </div>\n'
        '      <a href="/' + lang + '/contact/" class="article-cta-btn">' + d['cta_btn'] + '</a>\n'
        '    </div>')
    s = re.sub(r'<div class="article-cta">.*?</a>\s*</div>', lit(cta), s, count=1, flags=re.S)
    # write
    outdir = os.path.join(BASE, lang, 'blog', SLUG)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(s)
    return s

def patch_blog_index(lang, d):
    p = os.path.join(BASE, lang, 'blog', 'index.html')
    with open(p, encoding='utf-8') as f:
        s = f.read()
    card = ('      <!-- POST: custom-gear-manufacturing -->\n'
        '      <a href="/' + lang + '/blog/' + SLUG + '/" class="post-row" data-cat="engineering">\n'
        '        <div class="post-row-img">\n'
        '          <img loading="lazy" src="' + IMG + '" alt="' + d['cover_alt'] + '">\n'
        '        </div>\n'
        '        <div class="post-row-body">\n'
        '          <div class="post-meta">\n'
        '            <span class="post-cat">' + d['cat'] + '</span>\n'
        '            <span class="post-sep">&middot;</span>\n'
        '            <span class="post-date">' + d['date'] + '</span>\n'
        '          </div>\n'
        '          <div class="post-row-title">' + d['card_title'] + '</div>\n'
        '          <div class="post-row-excerpt">' + d['card_excerpt'] + '</div>\n'
        '        </div>\n'
        '      </a>\n\n')
    anchor = '<a href="/' + lang + '/blog/aluminium-alloy-selection-cnc-machining/" class="post-row"'
    idx = s.find(anchor)
    if idx == -1:
        raise RuntimeError('anchor not found in ' + p)
    # back up to the comment line before the anchor if present
    line_start = s.rfind('<!--', 0, idx)
    insert_at = line_start if line_start != -1 and s.count('\n', line_start, idx) <= 2 else idx
    s = s[:insert_at] + card + s[insert_at:]
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)

def patch_capabilities(lang, d):
    p = os.path.join(BASE, lang, 'capabilities', 'index.html')
    with open(p, encoding='utf-8') as f:
        s = f.read()
    if d['cap_feature'] in s:
        return
    s = re.sub(r'(<ul class="cap-features">)',
               lit('<ul class="cap-features">\n          <li>' + d['cap_feature'] + '</li>'),
               s, count=1)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)

def patch_sitemap():
    p = os.path.join(BASE, 'sitemap.xml')
    with open(p, encoding='utf-8') as f:
        s = f.read()
    if SLUG in s:
        return
    entries = '\n  <!-- custom-gear-manufacturing -->\n'
    for L in ['en', 'de', 'es', 'fr', 'pl']:
        entries += '  <url>\n'
        entries += '    <loc>https://bibparts.com/' + L + '/blog/' + SLUG + '/</loc>\n'
        for h in ['en', 'de', 'es', 'fr', 'pl']:
            entries += '    <xhtml:link rel="alternate" hreflang="' + h + '" href="https://bibparts.com/' + h + '/blog/' + SLUG + '/"/>\n'
        entries += '    <xhtml:link rel="alternate" hreflang="x-default" href="https://bibparts.com/en/blog/' + SLUG + '/"/>\n'
        entries += '    <lastmod>' + DATE + '</lastmod>\n'
        entries += '    <changefreq>monthly</changefreq>\n'
        entries += '    <priority>0.7</priority>\n'
        entries += '  </url>\n'
    s = s.replace('</urlset>', entries + '\n</urlset>')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)

for lang, d in LANGS.items():
    build_article(lang, d)
    patch_blog_index(lang, d)
    patch_capabilities(lang, d)
    print('done', lang)
patch_sitemap()
print('sitemap patched')
