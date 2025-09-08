#!/usr/bin/env python3
import random
import time
import os
import json
from datetime import datetime
from typing import Dict, List, Optional

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class IHKAP2Quiz:
    def __init__(self):
        self.questions = {
            "systemarchitektur": {
                "easy": [
                    {
                        "question": "Was ist eine Service-orientierte Architektur (SOA)?",
                        "options": [
                            "A) Eine Architektur mit vielen Servern",
                            "B) Eine Architektur, die Funktionalitäten als Services bereitstellt",
                            "C) Eine Sicherheitsarchitektur",
                            "D) Eine Netzwerkarchitektur"
                        ],
                        "correct": "B",
                        "explanation": "SOA ist ein Architekturmuster, bei dem Anwendungsfunktionen als Services über ein Netzwerk bereitgestellt werden.",
                        "hint": "Denke an 'Services' als wiederverwendbare Funktionseinheiten."
                    },
                    {
                        "question": "Was ist Microservices-Architektur?",
                        "options": [
                            "A) Sehr kleine Computer",
                            "B) Eine Architektur mit vielen kleinen, unabhängigen Services",
                            "C) Miniaturisierte Software",
                            "D) Kurze Programmcodes"
                        ],
                        "correct": "B",
                        "explanation": "Microservices-Architektur zerlegt Anwendungen in kleine, unabhängige Services, die separat entwickelt und deployed werden können.",
                        "hint": "'Micro' bedeutet klein - kleine, unabhängige Services."
                    },
                    {
                        "question": "Was ist ein Load Balancer?",
                        "options": [
                            "A) Ein Gewichtsmessgerät",
                            "B) Ein System, das eingehende Anfragen auf mehrere Server verteilt",
                            "C) Ein Speichergerät",
                            "D) Ein Sicherheitssystem"
                        ],
                        "correct": "B",
                        "explanation": "Ein Load Balancer verteilt eingehende Netzwerkanfragen gleichmäßig auf mehrere Server, um die Last zu balancieren.",
                        "hint": "'Load' = Last, 'Balance' = ausgleichen."
                    },
                    {
                        "question": "Was ist Horizontal Scaling?",
                        "options": [
                            "A) Server breiter machen",
                            "B) Mehr Server hinzufügen",
                            "C) Server höher stapeln",
                            "D) Server drehen"
                        ],
                        "correct": "B",
                        "explanation": "Horizontal Scaling bedeutet, die Kapazität durch Hinzufügen weiterer Server zu erhöhen, anstatt bestehende Server zu verbessern.",
                        "hint": "Horizontal = in die Breite, also mehr Einheiten."
                    },
                    {
                        "question": "Was ist ein API Gateway?",
                        "options": [
                            "A) Ein Tor für APIs",
                            "B) Ein zentraler Eingangspoint für API-Aufrufe",
                            "C) Eine API-Dokumentation",
                            "D) Ein API-Test-Tool"
                        ],
                        "correct": "B",
                        "explanation": "Ein API Gateway ist ein zentraler Eingangspoint, der API-Aufrufe verwaltet, weiterleitet und oft zusätzliche Funktionen wie Authentifizierung bietet.",
                        "hint": "Gateway = Eingangstor für alle API-Anfragen."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist das CAP-Theorem?",
                        "options": [
                            "A) Consistency, Availability, Partition tolerance - nur 2 von 3 gleichzeitig möglich",
                            "B) Ein Theorem über Computerkappen",
                            "C) Ein Sicherheitstheorem",
                            "D) Ein Netzwerkprotokoll"
                        ],
                        "correct": "A",
                        "explanation": "Das CAP-Theorem besagt, dass in verteilten Systemen nur zwei der drei Eigenschaften Consistency, Availability und Partition tolerance gleichzeitig garantiert werden können.",
                        "hint": "CAP = Consistency, Availability, Partition tolerance."
                    },
                    {
                        "question": "Was ist Event-Driven Architecture?",
                        "options": [
                            "A) Architektur für Veranstaltungen",
                            "B) Architektur, die auf Events und deren Verarbeitung basiert",
                            "C) Architektur für Eventmanagement",
                            "D) Architektur für Kalender-Apps"
                        ],
                        "correct": "B",
                        "explanation": "Event-Driven Architecture ist ein Architekturmuster, bei dem Komponenten durch Events kommunizieren und auf Events reagieren.",
                        "hint": "Events = Ereignisse, die Aktionen auslösen."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist CQRS (Command Query Responsibility Segregation)?",
                        "options": [
                            "A) Ein Datenbanktyp",
                            "B) Trennung von Lese- und Schreiboperationen in separate Modelle",
                            "C) Ein Sicherheitsprotokoll",
                            "D) Ein Netzwerkstandard"
                        ],
                        "correct": "B",
                        "explanation": "CQRS trennt Lese- (Query) und Schreiboperationen (Command) in separate Modelle, um Performance und Skalierbarkeit zu verbessern.",
                        "hint": "Command = Schreiben, Query = Lesen, Segregation = Trennung."
                    }
                ]
            },
            "softwareentwicklung": {
                "easy": [
                    {
                        "question": "Was ist ein Design Pattern?",
                        "options": [
                            "A) Ein Grafikdesign-Muster",
                            "B) Eine bewährte Lösung für wiederkehrende Programmierprobleme",
                            "C) Ein Webseitendesign",
                            "D) Ein Datenbankschema"
                        ],
                        "correct": "B",
                        "explanation": "Design Patterns sind bewährte, wiederverwendbare Lösungen für häufig auftretende Probleme in der Softwareentwicklung.",
                        "hint": "Pattern = Muster für Lösungsansätze."
                    },
                    {
                        "question": "Was ist das Singleton Pattern?",
                        "options": [
                            "A) Ein Pattern für einzelne Personen",
                            "B) Ein Pattern, das sicherstellt, dass nur eine Instanz einer Klasse existiert",
                            "C) Ein Pattern für einfache Objekte",
                            "D) Ein Pattern für Einzeldateien"
                        ],
                        "correct": "B",
                        "explanation": "Das Singleton Pattern stellt sicher, dass von einer Klasse nur eine einzige Instanz existiert und bietet einen globalen Zugriffspunkt darauf.",
                        "hint": "'Single' = einzeln, nur eine Instanz."
                    },
                    {
                        "question": "Was ist Refactoring?",
                        "options": [
                            "A) Code löschen",
                            "B) Code umstrukturieren ohne Funktionalität zu ändern",
                            "C) Neue Features hinzufügen",
                            "D) Code kompilieren"
                        ],
                        "correct": "B",
                        "explanation": "Refactoring ist die Umstrukturierung von Code zur Verbesserung der Lesbarkeit und Wartbarkeit, ohne die externe Funktionalität zu ändern.",
                        "hint": "Re-factoring = neu strukturieren."
                    },
                    {
                        "question": "Was ist Test-Driven Development (TDD)?",
                        "options": [
                            "A) Tests nach der Entwicklung schreiben",
                            "B) Tests vor der Implementierung schreiben",
                            "C) Nur manuelle Tests durchführen",
                            "D) Tests vermeiden"
                        ],
                        "correct": "B",
                        "explanation": "Bei TDD werden zuerst Tests geschrieben, dann wird der Code implementiert, um diese Tests zu erfüllen.",
                        "hint": "Test-Driven = Tests treiben die Entwicklung an."
                    },
                    {
                        "question": "Was ist Continuous Integration (CI)?",
                        "options": [
                            "A) Ständiges Arbeiten ohne Pause",
                            "B) Regelmäßiges Zusammenführen und Testen von Code-Änderungen",
                            "C) Kontinuierliche Meetings",
                            "D) Dauerhafte Internetverbindung"
                        ],
                        "correct": "B",
                        "explanation": "CI ist eine Praxis, bei der Entwickler ihre Code-Änderungen regelmäßig in ein gemeinsames Repository integrieren und automatisch testen lassen.",
                        "hint": "Integration = Zusammenführung von Code-Änderungen."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist das Observer Pattern?",
                        "options": [
                            "A) Ein Pattern für Überwachungskameras",
                            "B) Ein Pattern, bei dem Objekte über Änderungen benachrichtigt werden",
                            "C) Ein Pattern für Beobachtungen",
                            "D) Ein Pattern für Sicherheit"
                        ],
                        "correct": "B",
                        "explanation": "Das Observer Pattern definiert eine Abhängigkeit zwischen Objekten, sodass bei Änderungen alle abhängigen Objekte automatisch benachrichtigt werden.",
                        "hint": "Observer = Beobachter, die über Änderungen informiert werden."
                    },
                    {
                        "question": "Was ist Dependency Injection?",
                        "options": [
                            "A) Abhängigkeiten in Code einbauen",
                            "B) Abhängigkeiten von außen bereitstellen statt intern zu erstellen",
                            "C) Abhängigkeiten entfernen",
                            "D) Abhängigkeiten verstecken"
                        ],
                        "correct": "B",
                        "explanation": "Dependency Injection ist ein Entwurfsmuster, bei dem Abhängigkeiten von außen bereitgestellt werden, anstatt sie intern zu erstellen.",
                        "hint": "Injection = Einspritzen von Abhängigkeiten von außen."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist Domain-Driven Design (DDD)?",
                        "options": [
                            "A) Design für Domains/Websites",
                            "B) Ein Ansatz, der die Geschäftsdomäne in den Mittelpunkt der Softwareentwicklung stellt",
                            "C) Design für Domainnamen",
                            "D) Design für Datenbanken"
                        ],
                        "correct": "B",
                        "explanation": "DDD ist ein Ansatz zur Softwareentwicklung, der die Geschäftsdomäne und deren Logik in den Mittelpunkt stellt und komplexe Designs durch ein Modell der Domäne strukturiert.",
                        "hint": "Domain = Geschäftsbereich, der die Software-Architektur bestimmt."
                    }
                ]
            },
            "netzwerksicherheit": {
                "easy": [
                    {
                        "question": "Was ist eine Firewall?",
                        "options": [
                            "A) Eine Brandmauer",
                            "B) Ein Sicherheitssystem, das Netzwerkverkehr filtert",
                            "C) Eine Antivirensoftware",
                            "D) Ein Backup-System"
                        ],
                        "correct": "B",
                        "explanation": "Eine Firewall ist ein Sicherheitssystem, das den Netzwerkverkehr überwacht und basierend auf Sicherheitsregeln filtert.",
                        "hint": "Fire-wall = Schutzwall gegen unerwünschten Verkehr."
                    },
                    {
                        "question": "Was ist HTTPS?",
                        "options": [
                            "A) Hypertext Transfer Protocol Secure",
                            "B) Hypertext Transfer Protocol Simple",
                            "C) Hypertext Transfer Protocol Standard",
                            "D) Hypertext Transfer Protocol System"
                        ],
                        "correct": "A",
                        "explanation": "HTTPS ist die sichere Version von HTTP, die SSL/TLS-Verschlüsselung für die Datenübertragung verwendet.",
                        "hint": "Das 'S' steht für Secure = sicher."
                    },
                    {
                        "question": "Was ist ein DDoS-Angriff?",
                        "options": [
                            "A) Distributed Denial of Service",
                            "B) Direct Denial of Service",
                            "C) Distributed Data of Service",
                            "D) Direct Data of Service"
                        ],
                        "correct": "A",
                        "explanation": "Ein DDoS-Angriff überlastet einen Service durch koordinierte Anfragen von vielen verschiedenen Quellen.",
                        "hint": "Distributed = verteilt, Denial = Verweigerung."
                    },
                    {
                        "question": "Was ist SSL/TLS?",
                        "options": [
                            "A) Ein Betriebssystem",
                            "B) Verschlüsselungsprotokolle für sichere Kommunikation",
                            "C) Eine Programmiersprache",
                            "D) Ein Dateisystem"
                        ],
                        "correct": "B",
                        "explanation": "SSL (Secure Sockets Layer) und TLS (Transport Layer Security) sind Verschlüsselungsprotokolle für sichere Internetkommunikation.",
                        "hint": "Secure = sicher, für verschlüsselte Verbindungen."
                    },
                    {
                        "question": "Was ist ein Penetrationstest?",
                        "options": [
                            "A) Ein Test der Internetgeschwindigkeit",
                            "B) Ein autorisierter Angriff auf ein System zur Sicherheitsprüfung",
                            "C) Ein Hardwaretest",
                            "D) Ein Softwaretest"
                        ],
                        "correct": "B",
                        "explanation": "Ein Penetrationstest ist ein autorisierter simulierter Angriff auf ein System, um Sicherheitslücken zu identifizieren.",
                        "hint": "Penetration = Eindringen, um Schwachstellen zu finden."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist ein Man-in-the-Middle-Angriff?",
                        "options": [
                            "A) Ein Angriff von der Mitte des Raums",
                            "B) Ein Angriff, bei dem sich der Angreifer zwischen zwei Kommunikationspartner schaltet",
                            "C) Ein Angriff auf mittlere Unternehmen",
                            "D) Ein Angriff zur Mittagszeit"
                        ],
                        "correct": "B",
                        "explanation": "Bei einem Man-in-the-Middle-Angriff schaltet sich ein Angreifer heimlich zwischen zwei Kommunikationspartner und kann deren Kommunikation abhören oder manipulieren.",
                        "hint": "Der Angreifer steht 'in der Mitte' der Kommunikation."
                    },
                    {
                        "question": "Was ist ein Honeypot?",
                        "options": [
                            "A) Ein Honigtopf",
                            "B) Ein Köder-System zur Erkennung von Angriffen",
                            "C) Ein süßes Programm",
                            "D) Ein Backup-System"
                        ],
                        "correct": "B",
                        "explanation": "Ein Honeypot ist ein Köder-System, das Angreifer anlockt, um ihre Methoden zu studieren und Angriffe zu erkennen.",
                        "hint": "Honey = Honig als Köder für Angreifer."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist Perfect Forward Secrecy?",
                        "options": [
                            "A) Perfekte Vorwärtssicherheit",
                            "B) Eine Eigenschaft, bei der vergangene Sitzungsschlüssel sicher bleiben, auch wenn der Hauptschlüssel kompromittiert wird",
                            "C) Ein perfektes Sicherheitssystem",
                            "D) Eine Verschlüsselungsmethode"
                        ],
                        "correct": "B",
                        "explanation": "Perfect Forward Secrecy stellt sicher, dass vergangene Kommunikation sicher bleibt, selbst wenn langfristige Schlüssel kompromittiert werden.",
                        "hint": "Forward = vorwärts, Secrecy = Geheimhaltung für die Zukunft."
                    }
                ]
            },
            "datenbanken": {
                "easy": [
                    {
                        "question": "Was ist Normalisierung in Datenbanken?",
                        "options": [
                            "A) Daten normal machen",
                            "B) Redundanzen reduzieren und Datenintegrität verbessern",
                            "C) Daten sortieren",
                            "D) Daten löschen"
                        ],
                        "correct": "B",
                        "explanation": "Normalisierung ist der Prozess der Strukturierung einer Datenbank, um Redundanzen zu reduzieren und die Datenintegrität zu verbessern.",
                        "hint": "Normal = ohne Redundanzen und Anomalien."
                    },
                    {
                        "question": "Was ist ein Index in einer Datenbank?",
                        "options": [
                            "A) Ein Inhaltsverzeichnis",
                            "B) Eine Datenstruktur zur Beschleunigung von Abfragen",
                            "C) Eine Seitenzahl",
                            "D) Ein Backup"
                        ],
                        "correct": "B",
                        "explanation": "Ein Index ist eine Datenstruktur, die die Geschwindigkeit von Datenbankabfragen verbessert, indem sie schnelle Zugriffspfade zu den Daten bereitstellt.",
                        "hint": "Wie ein Buchindex - schneller Zugriff auf Informationen."
                    },
                    {
                        "question": "Was ist ACID in Datenbanken?",
                        "options": [
                            "A) Eine Säure",
                            "B) Atomicity, Consistency, Isolation, Durability",
                            "C) Ein Datenbanktyp",
                            "D) Ein SQL-Befehl"
                        ],
                        "correct": "B",
                        "explanation": "ACID sind die vier Grundeigenschaften von Datenbanktransaktionen: Atomicity, Consistency, Isolation und Durability.",
                        "hint": "ACID = vier wichtige Eigenschaften für Transaktionen."
                    },
                    {
                        "question": "Was ist ein Stored Procedure?",
                        "options": [
                            "A) Ein gespeichertes Verfahren",
                            "B) Eine vorkompilierte Sammlung von SQL-Anweisungen",
                            "C) Ein Backup-Verfahren",
                            "D) Ein Sicherheitsverfahren"
                        ],
                        "correct": "B",
                        "explanation": "Eine Stored Procedure ist eine vorkompilierte Sammlung von SQL-Anweisungen, die in der Datenbank gespeichert und ausgeführt werden kann.",
                        "hint": "Stored = gespeichert, Procedure = Verfahren/Prozedur."
                    },
                    {
                        "question": "Was ist der Unterschied zwischen INNER JOIN und LEFT JOIN?",
                        "options": [
                            "A) Kein Unterschied",
                            "B) INNER JOIN zeigt nur übereinstimmende Datensätze, LEFT JOIN alle aus der linken Tabelle",
                            "C) LEFT JOIN ist schneller",
                            "D) INNER JOIN ist für interne Daten"
                        ],
                        "correct": "B",
                        "explanation": "INNER JOIN gibt nur Datensätze zurück, die in beiden Tabellen übereinstimmen, während LEFT JOIN alle Datensätze der linken Tabelle zurückgibt.",
                        "hint": "INNER = nur Übereinstimmungen, LEFT = alle von links."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist Database Sharding?",
                        "options": [
                            "A) Datenbank teilen",
                            "B) Horizontale Partitionierung einer Datenbank über mehrere Server",
                            "C) Datenbank sichern",
                            "D) Datenbank verschlüsseln"
                        ],
                        "correct": "B",
                        "explanation": "Sharding ist eine Methode der horizontalen Partitionierung, bei der große Datenbanken in kleinere, verwaltbare Teile (Shards) aufgeteilt werden.",
                        "hint": "Shard = Scherbe, Aufteilung in Teile."
                    },
                    {
                        "question": "Was ist ein Materialized View?",
                        "options": [
                            "A) Eine materielle Ansicht",
                            "B) Eine physisch gespeicherte Sicht mit vorberechneten Ergebnissen",
                            "C) Eine virtuelle Tabelle",
                            "D) Eine Backup-Tabelle"
                        ],
                        "correct": "B",
                        "explanation": "Ein Materialized View ist eine physisch gespeicherte Sicht, die vorberechnete Abfrageergebnisse enthält und regelmäßig aktualisiert wird.",
                        "hint": "Materialized = materialisiert/physisch gespeichert."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist das CAP-Theorem in Bezug auf verteilte Datenbanken?",
                        "options": [
                            "A) Consistency, Availability, Partition tolerance - nur 2 von 3 gleichzeitig erreichbar",
                            "B) Create, Alter, Partition",
                            "C) Cache, Access, Performance",
                            "D) Cluster, Availability, Performance"
                        ],
                        "correct": "A",
                        "explanation": "Das CAP-Theorem besagt, dass verteilte Datenbanksysteme nur zwei der drei Eigenschaften Consistency, Availability und Partition tolerance gleichzeitig garantieren können.",
                        "hint": "CAP = drei Eigenschaften, aber nur zwei gleichzeitig möglich."
                    }
                ]
            },
            "projektmanagement": {
                "easy": [
                    {
                        "question": "Was ist Agile Softwareentwicklung?",
                        "options": [
                            "A) Schnelle Programmierung",
                            "B) Ein iterativer Ansatz mit flexibler Anpassung an Änderungen",
                            "C) Sportliche Programmierung",
                            "D) Automatische Programmierung"
                        ],
                        "correct": "B",
                        "explanation": "Agile Softwareentwicklung ist ein iterativer Ansatz, der Flexibilität, Zusammenarbeit und schnelle Anpassung an Änderungen betont.",
                        "hint": "Agile = beweglich, flexibel auf Änderungen reagieren."
                    },
                    {
                        "question": "Was ist ein Sprint in Scrum?",
                        "options": [
                            "A) Ein schneller Lauf",
                            "B) Ein zeitlich begrenzter Entwicklungszyklus (meist 1-4 Wochen)",
                            "C) Ein Fehler im Code",
                            "D) Ein Meeting"
                        ],
                        "correct": "B",
                        "explanation": "Ein Sprint ist ein zeitlich begrenzter Entwicklungszyklus in Scrum, typischerweise 1-4 Wochen, in dem ein funktionsfähiges Produktinkrement erstellt wird.",
                        "hint": "Sprint = kurzer, intensiver Zeitraum."
                    },
                    {
                        "question": "Was ist ein Product Owner?",
                        "options": [
                            "A) Der Besitzer des Produkts",
                            "B) Die Person, die die Produktanforderungen definiert und priorisiert",
                            "C) Der Projektmanager",
                            "D) Der Hauptentwickler"
                        ],
                        "correct": "B",
                        "explanation": "Der Product Owner ist verantwortlich für die Definition und Priorisierung der Produktanforderungen und vertritt die Stakeholder-Interessen.",
                        "hint": "Owner = Besitzer der Produktvision und -anforderungen."
                    },
                    {
                        "question": "Was ist ein Daily Standup?",
                        "options": [
                            "A) Tägliches Aufstehen",
                            "B) Ein kurzes tägliches Meeting zur Synchronisation des Teams",
                            "C) Eine Übung",
                            "D) Ein Arbeitsplatz"
                        ],
                        "correct": "B",
                        "explanation": "Das Daily Standup ist ein kurzes tägliches Meeting, in dem das Team sich über Fortschritte, Pläne und Hindernisse austauscht.",
                        "hint": "Daily = täglich, Standup = kurzes stehendes Meeting."
                    },
                    {
                        "question": "Was ist eine User Story?",
                        "options": [
                            "A) Eine Geschichte über Benutzer",
                            "B) Eine kurze Beschreibung einer Funktionalität aus Benutzersicht",
                            "C) Ein Benutzerprofil",
                            "D) Eine Anleitung für Benutzer"
                        ],
                        "correct": "B",
                        "explanation": "Eine User Story ist eine kurze, einfache Beschreibung einer Funktionalität, geschrieben aus der Perspektive des Endbenutzers.",
                        "hint": "Story = Geschichte, wie ein Benutzer eine Funktion nutzt."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist Kanban?",
                        "options": [
                            "A) Ein japanisches Gericht",
                            "B) Ein visuelles System zur Arbeitsfluss-Verwaltung",
                            "C) Eine Programmiersprache",
                            "D) Ein Testverfahren"
                        ],
                        "correct": "B",
                        "explanation": "Kanban ist ein visuelles System zur Verwaltung von Arbeitsabläufen, das den Arbeitsfluss sichtbar macht und Engpässe identifiziert.",
                        "hint": "Kanban = japanisch für Signalkarte, visualisiert Arbeit."
                    },
                    {
                        "question": "Was ist Definition of Done?",
                        "options": [
                            "A) Eine Definition von Fertigstellung",
                            "B) Gemeinsame Kriterien, wann eine Aufgabe als abgeschlossen gilt",
                            "C) Das Ende des Projekts",
                            "D) Eine Checkliste"
                        ],
                        "correct": "B",
                        "explanation": "Definition of Done ist eine gemeinsame Vereinbarung des Teams über die Kriterien, die erfüllt sein müssen, damit eine Aufgabe als abgeschlossen gilt.",
                        "hint": "Done = fertig, Definition = klare Kriterien dafür."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist SAFe (Scaled Agile Framework)?",
                        "options": [
                            "A) Ein Sicherheitsframework",
                            "B) Ein Framework für die Skalierung agiler Praktiken in großen Organisationen",
                            "C) Ein sicheres Framework",
                            "D) Ein Framework für kleine Teams"
                        ],
                        "correct": "B",
                        "explanation": "SAFe ist ein Framework, das agile Praktiken und Prinzipien für große Organisationen und komplexe Projekte skaliert.",
                        "hint": "Scaled = skaliert, für große Organisationen."
                    }
                ]
            },
            "qualitaetssicherung": {
                "easy": [
                    {
                        "question": "Was ist ein Unit Test?",
                        "options": [
                            "A) Ein Test einer Einheit",
                            "B) Ein Test der kleinsten testbaren Teile einer Anwendung",
                            "C) Ein Test der gesamten Anwendung",
                            "D) Ein Benutzertest"
                        ],
                        "correct": "B",
                        "explanation": "Ein Unit Test testet die kleinsten testbaren Teile einer Anwendung (meist einzelne Funktionen oder Methoden) isoliert.",
                        "hint": "Unit = Einheit, kleinste testbare Komponente."
                    },
                    {
                        "question": "Was ist der Unterschied zwischen Verifikation und Validierung?",
                        "options": [
                            "A) Kein Unterschied",
                            "B) Verifikation prüft 'richtig gebaut', Validierung prüft 'das Richtige gebaut'",
                            "C) Validierung ist schneller",
                            "D) Verifikation ist wichtiger"
                        ],
                        "correct": "B",
                        "explanation": "Verifikation prüft, ob das Produkt richtig gebaut wurde (Spezifikation erfüllt), Validierung prüft, ob das richtige Produkt gebaut wurde (Kundenbedürfnisse erfüllt).",
                        "hint": "Verifikation = richtig, Validierung = das Richtige."
                    },
                    {
                        "question": "Was ist Regression Testing?",
                        "options": [
                            "A) Rückwärts testen",
                            "B) Testen, ob neue Änderungen bestehende Funktionalitäten beeinträchtigen",
                            "C) Langsames Testen",
                            "D) Wiederholtes Testen"
                        ],
                        "correct": "B",
                        "explanation": "Regression Testing stellt sicher, dass neue Code-Änderungen keine unerwünschten Auswirkungen auf bestehende Funktionalitäten haben.",
                        "hint": "Regression = Rückschritt, prüft ob etwas kaputt gegangen ist."
                    },
                    {
                        "question": "Was ist Black Box Testing?",
                        "options": [
                            "A) Testen in dunklen Räumen",
                            "B) Testen ohne Kenntnis der internen Struktur",
                            "C) Testen schwarzer Software",
                            "D) Testen von Boxen"
                        ],
                        "correct": "B",
                        "explanation": "Black Box Testing testet die Funktionalität einer Software ohne Kenntnis ihrer internen Struktur oder Implementierung.",
                        "hint": "Black Box = undurchsichtig, nur Eingabe und Ausgabe sichtbar."
                    },
                    {
                        "question": "Was ist Code Coverage?",
                        "options": [
                            "A) Wie viel Code geschrieben wurde",
                            "B) Der Anteil des Codes, der durch Tests abgedeckt wird",
                            "C) Wie gut Code dokumentiert ist",
                            "D) Wie schnell Code läuft"
                        ],
                        "correct": "B",
                        "explanation": "Code Coverage misst, welcher Anteil des Quellcodes durch automatisierte Tests ausgeführt wird.",
                        "hint": "Coverage = Abdeckung, wie viel Code getestet wird."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist Mutation Testing?",
                        "options": [
                            "A) Testen von Mutationen",
                            "B) Testen der Testqualität durch Einführung kleiner Code-Änderungen",
                            "C) Testen genetischer Algorithmen",
                            "D) Testen von Veränderungen"
                        ],
                        "correct": "B",
                        "explanation": "Mutation Testing bewertet die Qualität von Tests, indem kleine Änderungen (Mutationen) in den Code eingeführt werden und geprüft wird, ob die Tests diese erkennen.",
                        "hint": "Mutation = Veränderung, testet ob Tests gut genug sind."
                    },
                    {
                        "question": "Was ist Property-Based Testing?",
                        "options": [
                            "A) Testen von Eigenschaften",
                            "B) Testen durch Definition von Eigenschaften, die immer wahr sein sollten",
                            "C) Testen von Immobilien",
                            "D) Testen von Objekteigenschaften"
                        ],
                        "correct": "B",
                        "explanation": "Property-Based Testing definiert Eigenschaften (Properties), die für alle gültigen Eingaben wahr sein sollten, und generiert automatisch Testfälle.",
                        "hint": "Property = Eigenschaft, die immer gelten sollte."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist Chaos Engineering?",
                        "options": [
                            "A) Chaotische Programmierung",
                            "B) Bewusstes Einführen von Fehlern zur Verbesserung der Systemresilienz",
                            "C) Unorganisierte Tests",
                            "D) Zufällige Entwicklung"
                        ],
                        "correct": "B",
                        "explanation": "Chaos Engineering ist die Disziplin des Experimentierens mit verteilten Systemen durch bewusstes Einführen von Fehlern, um Schwachstellen zu identifizieren.",
                        "hint": "Chaos = kontrolliertes Chaos zur Systemverbesserung."
                    }
                ]
            }
        }
        
        self.current_category = "alle"
        self.current_difficulty = "medium"
        self.score = 0
        self.total_questions = 0
        self.wrong_answers = []
        self.stats_file = "ap2_quiz_stats.json"
        self.stats = self.load_stats()
        self.used_questions = set()
        self.start_time = None
        self.hints_used = 0

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_colored(self, text: str, color: str = Colors.END):
        """Print text with color"""
        print(f"{color}{text}{Colors.END}")

    def print_progress_bar(self, current: int, total: int, width: int = 50):
        """Display a progress bar"""
        if total == 0:
            return
        
        progress = current / total
        filled = int(width * progress)
        bar = "█" * filled + "░" * (width - filled)
        percentage = progress * 100
        
        self.print_colored(f"Fortschritt: [{bar}] {percentage:.1f}% ({current}/{total})", Colors.CYAN)

    def display_welcome(self):
        self.clear_screen()
        self.print_colored("=" * 70, Colors.HEADER)
        self.print_colored("🎯 IHK AP2 Prüfungsfragen Quiz - 30 Fragen", Colors.HEADER + Colors.BOLD)
        self.print_colored("=" * 70, Colors.HEADER)
        self.print_colored("Willkommen zum AP2 (Abschlussprüfung Teil 2) Quiz!", Colors.BLUE)
        self.print_colored("✨ 30 fortgeschrittene Fragen zu allen wichtigen AP2-Themen!", Colors.GREEN)
        print()
        self.print_colored("Verfügbare Kategorien:", Colors.YELLOW)
        self.print_colored("• Systemarchitektur (System Architecture)", Colors.CYAN)
        self.print_colored("• Softwareentwicklung (Advanced Software Development)", Colors.CYAN)
        self.print_colored("• Netzwerksicherheit (Network Security)", Colors.CYAN)
        self.print_colored("• Datenbanken (Advanced Databases)", Colors.CYAN)
        self.print_colored("• Projektmanagement (Advanced Project Management)", Colors.CYAN)
        self.print_colored("• Qualitätssicherung (Quality Assurance)", Colors.CYAN)
        self.print_colored("• Alle Kategorien gemischt", Colors.CYAN)
        print()
        self.print_colored("Schwierigkeitsgrade: Easy, Medium, Hard", Colors.YELLOW)
        self.print_colored("Gib 'q' ein, um das Spiel zu beenden.", Colors.RED)
        self.print_colored("Gib 'h' ein, um einen Hint zu erhalten.", Colors.GREEN)
        self.print_colored("=" * 70, Colors.HEADER)

    def select_difficulty(self):
        """Let user select difficulty level"""
        while True:
            self.print_colored("\nSchwierigkeitsgrad wählen:", Colors.YELLOW + Colors.BOLD)
            self.print_colored("1) Easy - Grundlagen und einfache Konzepte", Colors.GREEN)
            self.print_colored("2) Medium - Fortgeschrittene Themen", Colors.YELLOW)
            self.print_colored("3) Hard - Komplexe und spezialisierte Konzepte", Colors.RED)
            
            choice = input("\nDeine Wahl (1-3): ").strip()
            
            if choice == "1":
                self.current_difficulty = "easy"
                self.print_colored("✅ Easy-Modus gewählt!", Colors.GREEN)
                break
            elif choice == "2":
                self.current_difficulty = "medium"
                self.print_colored("✅ Medium-Modus gewählt!", Colors.YELLOW)
                break
            elif choice == "3":
                self.current_difficulty = "hard"
                self.print_colored("✅ Hard-Modus gewählt!", Colors.RED)
                break
            else:
                self.print_colored("❌ Ungültige Eingabe! Bitte 1-3 wählen.", Colors.RED)

    def select_category(self):
        """Let user select question category"""
        while True:
            self.print_colored("\nKategorie wählen:", Colors.YELLOW + Colors.BOLD)
            self.print_colored("1) Systemarchitektur (System Architecture)", Colors.CYAN)
            self.print_colored("2) Softwareentwicklung (Advanced Software Development)", Colors.CYAN)
            self.print_colored("3) Netzwerksicherheit (Network Security)", Colors.CYAN)
            self.print_colored("4) Datenbanken (Advanced Databases)", Colors.CYAN)
            self.print_colored("5) Projektmanagement (Advanced Project Management)", Colors.CYAN)
            self.print_colored("6) Qualitätssicherung (Quality Assurance)", Colors.CYAN)
            self.print_colored("7) Alle Kategorien gemischt", Colors.BLUE)
            
            choice = input("\nDeine Wahl (1-7): ").strip()
            
            categories = {
                "1": "systemarchitektur",
                "2": "softwareentwicklung", 
                "3": "netzwerksicherheit",
                "4": "datenbanken",
                "5": "projektmanagement",
                "6": "qualitaetssicherung",
                "7": "alle"
            }
            
            if choice in categories:
                self.current_category = categories[choice]
                category_names = {
                    "systemarchitektur": "Systemarchitektur",
                    "softwareentwicklung": "Softwareentwicklung",
                    "netzwerksicherheit": "Netzwerksicherheit",
                    "datenbanken": "Datenbanken",
                    "projektmanagement": "Projektmanagement",
                    "qualitaetssicherung": "Qualitätssicherung",
                    "alle": "Alle Kategorien"
                }
                self.print_colored(f"✅ {category_names[self.current_category]} gewählt!", Colors.GREEN)
                break
            else:
                self.print_colored("❌ Ungültige Eingabe! Bitte 1-7 wählen.", Colors.RED)

    def get_questions_for_quiz(self) -> List[Dict]:
        """Get unique questions based on selected category and difficulty"""
        available_questions = []
        
        if self.current_category == "alle":
            # Mix questions from all categories
            for category in self.questions:
                if self.current_difficulty in self.questions[category]:
                    available_questions.extend(self.questions[category][self.current_difficulty])
        else:
            # Get questions from specific category
            if self.current_difficulty in self.questions[self.current_category]:
                available_questions.extend(self.questions[self.current_category][self.current_difficulty])
        
        # Create unique IDs for questions and filter out used ones
        unique_questions = []
        for question in available_questions:
            question_id = f"{question['question'][:50]}_{question['options'][0][:20]}"
            if question_id not in self.used_questions:
                unique_questions.append(question)
                self.used_questions.add(question_id)
        
        random.shuffle(unique_questions)
        
        # Return available unique questions (up to 30)
        return unique_questions[:min(30, len(unique_questions))]

    def ask_question(self, question_data: Dict, question_num: int, total_questions: int) -> bool:
        """Ask a single question and return True if answered correctly"""
        self.clear_screen()
        
        # Show progress
        self.print_progress_bar(question_num - 1, total_questions)
        print()
        
        self.print_colored(f"Frage {question_num}/{total_questions}", Colors.HEADER + Colors.BOLD)
        self.print_colored("-" * 50, Colors.HEADER)
        
        # Display question
        self.print_colored(f"\n{question_data['question']}", Colors.BLUE + Colors.BOLD)
        print()
        
        # Display options
        for option in question_data['options']:
            self.print_colored(option, Colors.CYAN)
        
        print()
        
        # Get user answer
        while True:
            answer = input("Deine Antwort (A/B/C/D, 'h' für Hint, 'q' zum Beenden): ").upper().strip()
            
            if answer == 'Q':
                return False
            elif answer == 'H':
                self.hints_used += 1
                self.print_colored(f"\n💡 Hint: {question_data['hint']}", Colors.YELLOW)
                print()
                continue
            elif answer in ['A', 'B', 'C', 'D']:
                break
            else:
                self.print_colored("❌ Ungültige Eingabe! Bitte A, B, C, D, 'h' oder 'q' eingeben.", Colors.RED)
        
        # Check answer
        correct = answer == question_data['correct']
        
        if correct:
            self.print_colored("\n✅ Richtig!", Colors.GREEN + Colors.BOLD)
            self.score += 1
        else:
            self.print_colored(f"\n❌ Falsch! Die richtige Antwort ist {question_data['correct']}", Colors.RED + Colors.BOLD)
            self.wrong_answers.append({
                'question': question_data['question'],
                'your_answer': answer,
                'correct_answer': question_data['correct'],
                'explanation': question_data['explanation']
            })
        
        # Show explanation
        self.print_colored(f"\n📚 Erklärung: {question_data['explanation']}", Colors.BLUE)
        
        input("\nDrücke Enter für die nächste Frage...")
        return True

    def show_wrong_answers_review(self):
        """Show review of wrong answers"""
        if not self.wrong_answers:
            return
        
        self.clear_screen()
        self.print_colored("=" * 70, Colors.HEADER)
        self.print_colored("📝 WIEDERHOLUNG DER FALSCHEN ANTWORTEN", Colors.HEADER + Colors.BOLD)
        self.print_colored("=" * 70, Colors.HEADER)
        
        for i, wrong in enumerate(self.wrong_answers, 1):
            self.print_colored(f"\n{i}. {wrong['question']}", Colors.BLUE + Colors.BOLD)
            self.print_colored(f"   Deine Antwort: {wrong['your_answer']}", Colors.RED)
            self.print_colored(f"   Richtige Antwort: {wrong['correct_answer']}", Colors.GREEN)
            self.print_colored(f"   Erklärung: {wrong['explanation']}", Colors.CYAN)
            self.print_colored("-" * 50, Colors.HEADER)
        
        input("\nDrücke Enter, um fortzufahren...")

    def save_stats(self):
        """Save quiz statistics"""
        try:
            # Load existing stats
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    stats = json.load(f)
            else:
                stats = {"games": [], "total_games": 0, "best_score": 0}
            
            # Add current game
            if self.total_questions > 0:
                percentage = (self.score / self.total_questions) * 100
                time_taken = time.time() - self.start_time if self.start_time else 0
                
                game_stats = {
                    "date": datetime.now().isoformat(),
                    "score": self.score,
                    "total_questions": self.total_questions,
                    "percentage": percentage,
                    "time_taken": time_taken,
                    "hints_used": self.hints_used,
                    "difficulty": self.current_difficulty,
                    "category": self.current_category
                }
                
                stats["games"].append(game_stats)
                stats["total_games"] += 1
                if percentage > stats["best_score"]:
                    stats["best_score"] = percentage
                
                # Keep only last 10 games
                if len(stats["games"]) > 10:
                    stats["games"] = stats["games"][-10:]
                
                # Save stats
                with open(self.stats_file, 'w', encoding='utf-8') as f:
                    json.dump(stats, f, ensure_ascii=False, indent=2)
                    
        except Exception as e:
            self.print_colored(f"Fehler beim Speichern der Statistiken: {e}", Colors.RED)

    def show_stats(self):
        """Show quiz statistics"""
        try:
            if not os.path.exists(self.stats_file):
                self.print_colored("Noch keine Statistiken verfügbar.", Colors.YELLOW)
                return
            
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                stats = json.load(f)
            
            self.print_colored("\n" + "="*50, Colors.HEADER)
            self.print_colored("📊 DEINE AP2-QUIZ STATISTIKEN", Colors.HEADER + Colors.BOLD)
            self.print_colored("="*50, Colors.HEADER)
            
            self.print_colored(f"🎮 Gespielte Spiele: {stats['total_games']}", Colors.CYAN)
            self.print_colored(f"🏆 Beste Punktzahl: {stats['best_score']:.1f}%", Colors.GREEN)
            
            if stats["games"]:
                recent_games = stats["games"][-5:]  # Last 5 games
                self.print_colored(f"\n📈 Letzte {len(recent_games)} Spiele:", Colors.YELLOW)
                
                for i, game in enumerate(reversed(recent_games), 1):
                    date = datetime.fromisoformat(game["date"]).strftime("%d.%m.%Y %H:%M")
                    self.print_colored(f"  {i}. {date}: {game['score']}/{game['total_questions']} ({game['percentage']:.1f}%) - {game['difficulty']} - {game['category']}", Colors.BLUE)
            
        except Exception as e:
            self.print_colored(f"Fehler beim Laden der Statistiken: {e}", Colors.RED)

    def show_final_score(self):
        self.clear_screen()
        self.print_colored("=" * 70, Colors.HEADER)
        self.print_colored("🏆 AP2 QUIZ BEENDET!", Colors.HEADER + Colors.BOLD)
        self.print_colored("=" * 70, Colors.HEADER)
        
        if self.total_questions > 0:
            percentage = (self.score / self.total_questions) * 100
            time_taken = time.time() - self.start_time if self.start_time else 0
            
            self.print_colored(f"📊 Endergebnis: {self.score}/{self.total_questions} ({percentage:.1f}%)", Colors.CYAN + Colors.BOLD)
            self.print_colored(f"⏱️  Zeit: {time_taken:.0f} Sekunden", Colors.BLUE)
            self.print_colored(f"💡 Hints verwendet: {self.hints_used}", Colors.YELLOW)
            self.print_colored(f"🎯 Schwierigkeit: {self.current_difficulty.upper()}", Colors.CYAN)
            self.print_colored(f"📂 Kategorie: {self.current_category}", Colors.CYAN)
            
            if percentage >= 90:
                self.print_colored("\n🌟 HERVORRAGEND! Du beherrschst die AP2-Themen perfekt!", Colors.GREEN + Colors.BOLD)
            elif percentage >= 80:
                self.print_colored("\n👍 SEHR GUT! Du bist gut auf die AP2 vorbereitet!", Colors.GREEN)
            elif percentage >= 70:
                self.print_colored("\n📚 SOLIDE! Vertiefe noch einige Themenbereiche für die AP2.", Colors.YELLOW)
            elif percentage >= 60:
                self.print_colored("\n💪 GRUNDLAGEN VORHANDEN! Arbeite an den komplexeren Konzepten.", Colors.YELLOW)
            else:
                self.print_colored("\n📖 MEHR LERNEN NÖTIG! Fokussiere dich auf die AP2-Kernthemen.", Colors.RED)
            
            # Save statistics
            self.save_stats()
        
        self.print_colored("\nViel Erfolg bei deiner AP2-Prüfung! 🎯", Colors.BLUE + Colors.BOLD)

    def play(self) -> bool:
        """Main game loop"""
        self.used_questions.clear()
        
        self.display_welcome()
        
        # Show stats option
        show_stats = input("\nMöchtest du deine Statistiken sehen? (j/n): ").lower().strip()
        if show_stats in ['j', 'ja', 'y', 'yes']:
            self.show_stats()
            input("\nDrücke Enter, um fortzufahren...")
        
        # Select difficulty and category
        self.select_difficulty()
        self.select_category()
        
        # Get questions
        questions = self.get_questions_for_quiz()
        if not questions:
            self.print_colored("❌ Keine Fragen für diese Kombination verfügbar!", Colors.RED)
            return True
        
        self.print_colored(f"Verfügbare Fragen: {len(questions)}", Colors.GREEN)
        
        self.total_questions = len(questions)
        self.start_time = time.time()
        
        # Ask questions
        for i, question in enumerate(questions, 1):
            if not self.ask_question(question, i, self.total_questions):
                # User quit
                self.print_colored("\nSpiel beendet. Bis zum nächsten Mal! 👋", Colors.BLUE)
                return False
        
        # Show results
        self.show_final_score()
        
        # Show wrong answers review
        if self.wrong_answers:
            review = input("\nMöchtest du deine falschen Antworten nochmal durchgehen? (j/n): ").lower().strip()
            if review in ['j', 'ja', 'y', 'yes']:
                self.show_wrong_answers_review()
        
        return True

    def load_questions(self):
        """Load questions from a JSON file"""
        try:
            with open("ap2_quiz_fragen.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            self.print_colored("Fehler: 'ap2_quiz_fragen.json' nicht gefunden.", Colors.RED)
            return {}
        except json.JSONDecodeError:
            self.print_colored("Fehler: Fehler beim Decodieren von 'ap2_quiz_fragen.json'.", Colors.RED)
            return {}

    def load_stats(self):
        """Load quiz statistics from a JSON file"""
        try:
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return {"games": [], "total_games": 0, "best_score": 0}
        except (FileNotFoundError, json.JSONDecodeError):
            return {"games": [], "total_games": 0, "best_score": 0}

def main():
    game = IHKAP2Quiz()
    
    while True:
        # Reset game state
        game.score = 0
        game.total_questions = 0
        game.wrong_answers = []
        game.start_time = None
        game.hints_used = 0
        
        # Play game
        if not game.play():
            break
        
        # Ask to play again
        game.print_colored("\n" + "="*50, Colors.HEADER)
        play_again = input("Möchtest du nochmal spielen? (j/n): ").lower().strip()
        if play_again not in ['j', 'ja', 'y', 'yes']:
            break
    
    game.print_colored("\nViel Erfolg bei deiner AP2-Prüfung! 👋", Colors.BLUE + Colors.BOLD)

if __name__ == "__main__":
    main()
