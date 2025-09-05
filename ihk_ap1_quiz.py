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

class IHKAP1Quiz:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.wrong_answers = []
        self.start_time = None
        self.hints_used = 0
        self.current_difficulty = "medium"
        self.current_category = "alle"
        self.stats_file = "ap1_quiz_stats.json"
        
        self.questions = {
            "hardware": {
                "easy": [
                    {
                        "question": "Was ist die Hauptfunktion der CPU?",
                        "options": [
                            "A) Daten speichern",
                            "B) Befehle ausführen und Berechnungen durchführen",
                            "C) Netzwerkverbindungen verwalten",
                            "D) Grafiken anzeigen"
                        ],
                        "correct": "B",
                        "explanation": "Die CPU (Central Processing Unit) ist das Herzstück des Computers und führt Befehle aus sowie Berechnungen durch.",
                        "hint": "CPU steht für Central Processing Unit - das Wort 'Processing' gibt einen Hinweis."
                    },
                    {
                        "question": "Welche Speicherart verliert ihre Daten beim Ausschalten des Computers?",
                        "options": [
                            "A) Festplatte (HDD)",
                            "B) SSD",
                            "C) RAM",
                            "D) ROM"
                        ],
                        "correct": "C",
                        "explanation": "RAM (Random Access Memory) ist ein flüchtiger Speicher, der seine Daten beim Ausschalten verliert.",
                        "hint": "Denke an 'flüchtigen' vs. 'permanenten' Speicher."
                    },
                    {
                        "question": "Was bedeutet die Abkürzung 'BIOS'?",
                        "options": [
                            "A) Basic Input Output System",
                            "B) Binary Input Output System",
                            "C) Boot Input Output System",
                            "D) Basic Internal Operating System"
                        ],
                        "correct": "A",
                        "explanation": "BIOS steht für Basic Input Output System und ist die Firmware, die beim Computerstart ausgeführt wird.",
                        "hint": "Es geht um grundlegende Ein- und Ausgabefunktionen."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist der Unterschied zwischen SATA und NVMe?",
                        "options": [
                            "A) SATA ist für Grafikkarten, NVMe für Festplatten",
                            "B) SATA ist eine ältere Schnittstelle, NVMe ist schneller und moderner",
                            "C) NVMe ist nur für externe Geräte",
                            "D) Kein Unterschied"
                        ],
                        "correct": "B",
                        "explanation": "SATA ist eine ältere Schnittstelle für Speichergeräte, während NVMe (Non-Volatile Memory Express) deutlich schneller ist und über PCIe läuft.",
                        "hint": "Denke an die Entwicklung von Speichertechnologien über die Zeit."
                    },
                    {
                        "question": "Welche Funktion hat der Chipsatz auf dem Mainboard?",
                        "options": [
                            "A) Strom verteilen",
                            "B) Kommunikation zwischen CPU und anderen Komponenten koordinieren",
                            "C) Grafiken berechnen",
                            "D) Daten verschlüsseln"
                        ],
                        "correct": "B",
                        "explanation": "Der Chipsatz koordiniert die Kommunikation zwischen der CPU und anderen Systemkomponenten wie RAM, Festplatten und Erweiterungskarten.",
                        "hint": "Es geht um die Koordination und Kommunikation im System."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist der Unterschied zwischen DDR4 und DDR5 RAM?",
                        "options": [
                            "A) DDR5 hat höhere Geschwindigkeit und bessere Energieeffizienz",
                            "B) DDR4 ist schneller",
                            "C) Nur die Farbe ist unterschiedlich",
                            "D) DDR5 ist nur für Server"
                        ],
                        "correct": "A",
                        "explanation": "DDR5 bietet höhere Datenraten, bessere Energieeffizienz und erweiterte Funktionen im Vergleich zu DDR4.",
                        "hint": "Neuere Generationen sind meist schneller und effizienter."
                    }
                ]
            },
            "betriebssysteme": {
                "easy": [
                    {
                        "question": "Was ist ein Betriebssystem?",
                        "options": [
                            "A) Ein Computerspiel",
                            "B) Software, die Hardware und andere Programme verwaltet",
                            "C) Ein Internetbrowser",
                            "D) Eine Programmiersprache"
                        ],
                        "correct": "B",
                        "explanation": "Ein Betriebssystem ist die grundlegende Software, die Hardware-Ressourcen verwaltet und eine Plattform für andere Programme bietet.",
                        "hint": "Es 'betreibt' das System und verwaltet Ressourcen."
                    },
                    {
                        "question": "Welches ist KEIN Betriebssystem?",
                        "options": [
                            "A) Windows",
                            "B) Linux",
                            "C) Microsoft Office",
                            "D) macOS"
                        ],
                        "correct": "C",
                        "explanation": "Microsoft Office ist eine Anwendungssoftware (Office-Suite), kein Betriebssystem.",
                        "hint": "Denke daran, was auf dem Computer läuft vs. was den Computer betreibt."
                    },
                    {
                        "question": "Was ist ein Prozess in einem Betriebssystem?",
                        "options": [
                            "A) Ein laufendes Programm",
                            "B) Ein Dateisystem",
                            "C) Ein Netzwerkprotokoll",
                            "D) Ein Speichertyp"
                        ],
                        "correct": "A",
                        "explanation": "Ein Prozess ist ein laufendes Programm mit eigenem Speicherbereich und Systemressourcen.",
                        "hint": "Es geht um etwas, das gerade ausgeführt wird."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist virtueller Speicher?",
                        "options": [
                            "A) Speicher in der Cloud",
                            "B) Eine Technik, die Festplattenspeicher als RAM-Erweiterung nutzt",
                            "C) Speicher für virtuelle Maschinen",
                            "D) Verschlüsselter Speicher"
                        ],
                        "correct": "B",
                        "explanation": "Virtueller Speicher erweitert den verfügbaren RAM durch Nutzung von Festplattenspeicher (Swap/Auslagerungsdatei).",
                        "hint": "Es geht um die Erweiterung des Arbeitsspeichers."
                    },
                    {
                        "question": "Was ist der Unterschied zwischen einem Thread und einem Prozess?",
                        "options": [
                            "A) Kein Unterschied",
                            "B) Threads teilen sich Speicher, Prozesse haben eigenen Speicher",
                            "C) Threads sind langsamer",
                            "D) Prozesse können nur einzeln laufen"
                        ],
                        "correct": "B",
                        "explanation": "Threads innerhalb eines Prozesses teilen sich den Speicherbereich, während Prozesse isolierte Speicherbereiche haben.",
                        "hint": "Denke an 'teilen' vs. 'getrennt'."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist ein Deadlock?",
                        "options": [
                            "A) Ein Systemabsturz",
                            "B) Eine Situation, wo Prozesse sich gegenseitig blockieren",
                            "C) Ein Netzwerkfehler",
                            "D) Ein Speicherfehler"
                        ],
                        "correct": "B",
                        "explanation": "Ein Deadlock tritt auf, wenn zwei oder mehr Prozesse sich gegenseitig blockieren und auf Ressourcen warten, die der andere hält.",
                        "hint": "Das Wort 'Dead' und 'Lock' beschreibt eine blockierte Situation."
                    }
                ]
            },
            "netzwerke": {
                "easy": [
                    {
                        "question": "Was bedeutet 'IP' in IP-Adresse?",
                        "options": [
                            "A) Internet Provider",
                            "B) Internet Protocol",
                            "C) Internal Process",
                            "D) Information Package"
                        ],
                        "correct": "B",
                        "explanation": "IP steht für Internet Protocol, das grundlegende Protokoll für die Datenübertragung im Internet.",
                        "hint": "Es ist ein Protokoll für das Internet."
                    },
                    {
                        "question": "Welcher Port wird standardmäßig für HTTPS verwendet?",
                        "options": [
                            "A) 80",
                            "B) 21",
                            "C) 443",
                            "D) 25"
                        ],
                        "correct": "C",
                        "explanation": "Port 443 ist der Standardport für HTTPS (HTTP Secure), die verschlüsselte Version von HTTP.",
                        "hint": "Es ist eine höhere Zahl als der HTTP-Port."
                    },
                    {
                        "question": "Was ist ein Router?",
                        "options": [
                            "A) Ein Speichergerät",
                            "B) Ein Gerät, das Datenpakete zwischen Netzwerken weiterleitet",
                            "C) Ein Eingabegerät",
                            "D) Ein Bildschirm"
                        ],
                        "correct": "B",
                        "explanation": "Ein Router leitet Datenpakete zwischen verschiedenen Netzwerken weiter und bestimmt den besten Pfad für die Datenübertragung.",
                        "hint": "Das Wort 'Route' gibt einen Hinweis auf die Funktion."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist der Unterschied zwischen einem Hub und einem Switch?",
                        "options": [
                            "A) Kein Unterschied",
                            "B) Ein Switch lernt MAC-Adressen und sendet gezielt, ein Hub sendet an alle",
                            "C) Ein Hub ist schneller",
                            "D) Ein Switch funktioniert nur mit WLAN"
                        ],
                        "correct": "B",
                        "explanation": "Ein Switch lernt MAC-Adressen und sendet Daten gezielt an den richtigen Port, während ein Hub alle Daten an alle Ports sendet.",
                        "hint": "Denke an 'intelligent' vs. 'einfach weiterleiten'."
                    },
                    {
                        "question": "Welche IP-Adresse ist eine private Adresse?",
                        "options": [
                            "A) 8.8.8.8",
                            "B) 192.168.1.1",
                            "C) 1.1.1.1",
                            "D) 208.67.222.222"
                        ],
                        "correct": "B",
                        "explanation": "192.168.x.x ist ein privater IP-Adressbereich, der in lokalen Netzwerken verwendet wird und nicht im Internet geroutet wird.",
                        "hint": "Private Adressen beginnen oft mit 192.168 oder 10.x oder 172.16-31.x"
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist VLAN?",
                        "options": [
                            "A) Very Large Area Network",
                            "B) Virtual Local Area Network",
                            "C) Variable Length Area Network",
                            "D) Verified Local Area Network"
                        ],
                        "correct": "B",
                        "explanation": "VLAN (Virtual Local Area Network) ermöglicht es, ein physisches Netzwerk in mehrere logische Netzwerke zu unterteilen.",
                        "hint": "Es geht um virtuelle Unterteilung von Netzwerken."
                    }
                ]
            },
            "programmierung": {
                "easy": [
                    {
                        "question": "Was ist ein Algorithmus?",
                        "options": [
                            "A) Ein Computervirus",
                            "B) Eine Schritt-für-Schritt-Anleitung zur Problemlösung",
                            "C) Ein Betriebssystem",
                            "D) Eine Programmiersprache"
                        ],
                        "correct": "B",
                        "explanation": "Ein Algorithmus ist eine eindeutige Schritt-für-Schritt-Anleitung zur Lösung eines Problems oder zur Ausführung einer Aufgabe.",
                        "hint": "Denke an ein Rezept oder eine Anleitung."
                    },
                    {
                        "question": "Was ist der Unterschied zwischen Compiler und Interpreter?",
                        "options": [
                            "A) Kein Unterschied",
                            "B) Compiler übersetzt vor Ausführung, Interpreter zur Laufzeit",
                            "C) Interpreter ist schneller",
                            "D) Compiler funktioniert nur mit Java"
                        ],
                        "correct": "B",
                        "explanation": "Ein Compiler übersetzt den gesamten Quellcode vor der Ausführung in Maschinencode, während ein Interpreter den Code zur Laufzeit Zeile für Zeile ausführt.",
                        "hint": "Denke an 'vorher übersetzen' vs. 'während der Ausführung übersetzen'."
                    },
                    {
                        "question": "Was ist eine Schleife in der Programmierung?",
                        "options": [
                            "A) Ein Fehler im Code",
                            "B) Eine Struktur, die Code wiederholt ausführt",
                            "C) Eine Funktion",
                            "D) Eine Variable"
                        ],
                        "correct": "B",
                        "explanation": "Eine Schleife ist eine Kontrollstruktur, die es ermöglicht, einen Codeblock mehrfach zu wiederholen.",
                        "hint": "Das Wort 'Schleife' deutet auf Wiederholung hin."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist Rekursion?",
                        "options": [
                            "A) Eine Funktion, die sich selbst aufruft",
                            "B) Eine Art von Schleife",
                            "C) Ein Datentyp",
                            "D) Ein Fehlertyp"
                        ],
                        "correct": "A",
                        "explanation": "Rekursion ist eine Programmiertechnik, bei der eine Funktion sich selbst aufruft, um ein Problem in kleinere Teilprobleme zu zerlegen.",
                        "hint": "Das Wort kommt von 'recurrere' = zurückkehren."
                    },
                    {
                        "question": "Was ist der Unterschied zwischen Stack und Heap?",
                        "options": [
                            "A) Kein Unterschied",
                            "B) Stack für lokale Variablen, Heap für dynamische Speicherallokation",
                            "C) Heap ist schneller",
                            "D) Stack ist nur für Zahlen"
                        ],
                        "correct": "B",
                        "explanation": "Der Stack wird für lokale Variablen und Funktionsaufrufe verwendet, während der Heap für dynamische Speicherallokation genutzt wird.",
                        "hint": "Stack = stapeln (LIFO), Heap = Haufen (flexibel)."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist Big-O-Notation?",
                        "options": [
                            "A) Eine Programmiersprache",
                            "B) Eine Methode zur Beschreibung der Zeitkomplexität von Algorithmen",
                            "C) Ein Datentyp",
                            "D) Eine Art von Schleife"
                        ],
                        "correct": "B",
                        "explanation": "Die Big-O-Notation beschreibt die Zeitkomplexität von Algorithmen und wie sich die Laufzeit mit der Eingabegröße verändert.",
                        "hint": "Es geht um die Effizienz und Geschwindigkeit von Algorithmen."
                    }
                ]
            },
            "sicherheit": {
                "easy": [
                    {
                        "question": "Was ist ein starkes Passwort?",
                        "options": [
                            "A) Ein kurzes, einfaches Wort",
                            "B) Ein langes Passwort mit Buchstaben, Zahlen und Sonderzeichen",
                            "C) Der eigene Name",
                            "D) '123456'"
                        ],
                        "correct": "B",
                        "explanation": "Ein starkes Passwort sollte lang sein und eine Kombination aus Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten.",
                        "hint": "Komplexität und Länge machen ein Passwort sicher."
                    },
                    {
                        "question": "Was ist Malware?",
                        "options": [
                            "A) Gute Software",
                            "B) Schädliche Software",
                            "C) Kostenlose Software",
                            "D) Schnelle Software"
                        ],
                        "correct": "B",
                        "explanation": "Malware (Malicious Software) ist schädliche Software, die darauf ausgelegt ist, Computer zu beschädigen oder unerwünschte Aktionen auszuführen.",
                        "hint": "'Mal' bedeutet schlecht oder schädlich."
                    },
                    {
                        "question": "Was ist Phishing?",
                        "options": [
                            "A) Ein Computerspiel",
                            "B) Ein Versuch, persönliche Daten durch gefälschte E-Mails zu stehlen",
                            "C) Eine Programmiersprache",
                            "D) Ein Betriebssystem"
                        ],
                        "correct": "B",
                        "explanation": "Phishing ist ein Cyberangriff, bei dem Angreifer sich als vertrauenswürdige Entitäten ausgeben, um sensible Daten zu stehlen.",
                        "hint": "Es geht ums 'Fischen' nach persönlichen Informationen."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist Zwei-Faktor-Authentifizierung (2FA)?",
                        "options": [
                            "A) Zwei Passwörter verwenden",
                            "B) Eine zusätzliche Sicherheitsebene neben dem Passwort",
                            "C) Zwei verschiedene Browser verwenden",
                            "D) Zwei Computer verwenden"
                        ],
                        "correct": "B",
                        "explanation": "2FA fügt eine zusätzliche Sicherheitsebene hinzu, indem neben dem Passwort ein zweiter Faktor (z.B. SMS-Code, App) erforderlich ist.",
                        "hint": "Es geht um zwei verschiedene Arten der Identitätsprüfung."
                    },
                    {
                        "question": "Was ist ein VPN?",
                        "options": [
                            "A) Very Private Network",
                            "B) Virtual Private Network",
                            "C) Verified Private Network",
                            "D) Variable Private Network"
                        ],
                        "correct": "B",
                        "explanation": "Ein VPN (Virtual Private Network) erstellt eine sichere, verschlüsselte Verbindung über ein öffentliches Netzwerk.",
                        "hint": "Es geht um ein virtuelles, privates Netzwerk."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist ein Zero-Day-Exploit?",
                        "options": [
                            "A) Ein Exploit, der am ersten Tag entdeckt wird",
                            "B) Ein Exploit für eine Sicherheitslücke, die noch nicht bekannt oder gepatcht ist",
                            "C) Ein Exploit, der null Schäden verursacht",
                            "D) Ein kostenloser Exploit"
                        ],
                        "correct": "B",
                        "explanation": "Ein Zero-Day-Exploit nutzt eine Sicherheitslücke aus, die den Entwicklern noch nicht bekannt ist und für die daher noch kein Patch existiert.",
                        "hint": "'Zero Days' bezieht sich auf null Tage seit der Entdeckung durch die Entwickler."
                    }
                ]
            },
            "projektmanagement": {
                "easy": [
                    {
                        "question": "Was ist ein Projekt?",
                        "options": [
                            "A) Eine dauerhafte Aufgabe",
                            "B) Ein einmaliges Vorhaben mit definiertem Anfang und Ende",
                            "C) Eine tägliche Routine",
                            "D) Ein Computerprogramm"
                        ],
                        "correct": "B",
                        "explanation": "Ein Projekt ist ein zeitlich begrenztes Vorhaben mit einem definierten Anfang und Ende, das ein einzigartiges Ergebnis hervorbringt.",
                        "hint": "Projekte haben einen klaren Start und ein klares Ende."
                    },
                    {
                        "question": "Was ist ein Meilenstein in einem Projekt?",
                        "options": [
                            "A) Ein großer Stein",
                            "B) Ein wichtiger Zwischenschritt oder Etappenziel",
                            "C) Das Ende des Projekts",
                            "D) Ein Fehler im Projekt"
                        ],
                        "correct": "B",
                        "explanation": "Ein Meilenstein ist ein wichtiger Zwischenschritt oder Etappenziel in einem Projekt, der den Fortschritt markiert.",
                        "hint": "Wie Meilensteine an Straßen zeigen sie wichtige Punkte an."
                    }
                ],
                "medium": [
                    {
                        "question": "Was ist der kritische Pfad in einem Projekt?",
                        "options": [
                            "A) Der gefährlichste Teil des Projekts",
                            "B) Die längste Kette von Aktivitäten, die die Projektdauer bestimmt",
                            "C) Der wichtigste Mitarbeiter",
                            "D) Das teuerste Element"
                        ],
                        "correct": "B",
                        "explanation": "Der kritische Pfad ist die längste Kette von abhängigen Aktivitäten, die die minimale Projektdauer bestimmt.",
                        "hint": "Es geht um die zeitkritische Abfolge von Aufgaben."
                    }
                ],
                "hard": [
                    {
                        "question": "Was ist Scrum?",
                        "options": [
                            "A) Ein Rugbyspiel",
                            "B) Ein agiles Framework für Projektmanagement",
                            "C) Eine Programmiersprache",
                            "D) Ein Betriebssystem"
                        ],
                        "correct": "B",
                        "explanation": "Scrum ist ein agiles Framework für das Management und die Entwicklung von Produkten, besonders in der Softwareentwicklung.",
                        "hint": "Es ist eine moderne, flexible Methode für Projektmanagement."
                    }
                ]
            }
        }

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
        self.print_colored("🎯 IHK AP1 Prüfungsfragen Quiz - 30 Fragen", Colors.HEADER + Colors.BOLD)
        self.print_colored("=" * 70, Colors.HEADER)
        self.print_colored("Willkommen zum AP1 (Abschlussprüfung Teil 1) Quiz!", Colors.BLUE)
        self.print_colored("✨ 30 Fragen zu allen wichtigen AP1-Themen!", Colors.GREEN)
        print()
        self.print_colored("Verfügbare Kategorien:", Colors.YELLOW)
        self.print_colored("• Hardware (Computer-Hardware)", Colors.CYAN)
        self.print_colored("• Betriebssysteme (Operating Systems)", Colors.CYAN)
        self.print_colored("• Netzwerke (Networking)", Colors.CYAN)
        self.print_colored("• Programmierung (Programming Basics)", Colors.CYAN)
        self.print_colored("• Sicherheit (IT Security)", Colors.CYAN)
        self.print_colored("• Projektmanagement (Project Management)", Colors.CYAN)
        self.print_colored("• Alle Kategorien gemischt", Colors.CYAN)
        print()
        self.print_colored("Schwierigkeitsgrade: Easy, Medium, Hard", Colors.YELLOW)
        self.print_colored("Gib 'q' ein, um das Spiel zu beenden.", Colors.RED)
        self.print_colored("Gib 'h' ein, um einen Hint zu erhalten.", Colors.GREEN)
        self.print_colored("=" * 70, Colors.HEADER)


    def select_category(self):
        """Let user select question category"""
        while True:
            self.print_colored("\nKategorie wählen:", Colors.YELLOW + Colors.BOLD)
            self.print_colored("1) Hardware (Computer-Hardware)", Colors.CYAN)
            self.print_colored("2) Betriebssysteme (Operating Systems)", Colors.CYAN)
            self.print_colored("3) Netzwerke (Networking)", Colors.CYAN)
            self.print_colored("4) Programmierung (Programming Basics)", Colors.CYAN)
            self.print_colored("5) Sicherheit (IT Security)", Colors.CYAN)
            self.print_colored("6) Projektmanagement (Project Management)", Colors.CYAN)
            self.print_colored("7) Alle Kategorien gemischt", Colors.BLUE)
            
            choice = input("\nDeine Wahl (1-7): ").strip()
            
            categories = {
                "1": "hardware",
                "2": "betriebssysteme", 
                "3": "netzwerke",
                "4": "programmierung",
                "5": "sicherheit",
                "6": "projektmanagement",
                "7": "alle"
            }
            
            if choice in categories:
                self.current_category = categories[choice]
                category_names = {
                    "hardware": "Hardware",
                    "betriebssysteme": "Betriebssysteme",
                    "netzwerke": "Netzwerke",
                    "programmierung": "Programmierung", 
                    "sicherheit": "Sicherheit",
                    "projektmanagement": "Projektmanagement",
                    "alle": "Alle Kategorien"
                }
                self.print_colored(f"✅ {category_names[self.current_category]} gewählt!", Colors.GREEN)
                break
            else:
                self.print_colored("❌ Ungültige Eingabe! Bitte 1-7 wählen.", Colors.RED)

    def select_difficulty(self):
        """Let user select difficulty level"""
        while True:
            self.print_colored("\nSchwierigkeitsgrad wählen:", Colors.YELLOW + Colors.BOLD)
            self.print_colored("1) Easy (Einfach)", Colors.GREEN)
            self.print_colored("2) Medium (Mittel)", Colors.YELLOW)
            self.print_colored("3) Hard (Schwer)", Colors.RED)
            
            choice = input("\nDeine Wahl (1-3): ").strip()
            
            if choice == "1":
                self.current_difficulty = "easy"
                self.print_colored("✅ Easy gewählt!", Colors.GREEN)
                break
            elif choice == "2":
                self.current_difficulty = "medium"
                self.print_colored("✅ Medium gewählt!", Colors.YELLOW)
                break
            elif choice == "3":
                self.current_difficulty = "hard"
                self.print_colored("✅ Hard gewählt!", Colors.RED)
                break
            else:
                self.print_colored("❌ Ungültige Eingabe! Bitte 1-3 wählen.", Colors.RED)

    def get_questions_for_quiz(self) -> List[Dict]:
        """Get exactly 30 questions based on selected category and difficulty"""
        questions = []
        
        if self.current_category == "alle":
            # Mix questions from all categories
            for category in self.questions:
                if self.current_difficulty in self.questions[category]:
                    questions.extend(self.questions[category][self.current_difficulty])
        else:
            # Get questions from specific category
            if self.current_difficulty in self.questions[self.current_category]:
                questions.extend(self.questions[self.current_category][self.current_difficulty])
        
        random.shuffle(questions)
        
        if len(questions) >= 30:
            return questions[:30]
        else:
            # If not enough questions, repeat some to reach 30
            while len(questions) < 30:
                questions.extend(questions[:min(30-len(questions), len(questions))])
            return questions[:30]

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
                if 'hint' in question_data:
                    self.print_colored(f"💡 Hint: {question_data['hint']}", Colors.YELLOW)
                    self.hints_used += 1
                else:
                    self.print_colored("💡 Kein Hint verfügbar für diese Frage.", Colors.YELLOW)
                print()
                continue
            elif answer in ['A', 'B', 'C', 'D']:
                break
            else:
                self.print_colored("❌ Bitte A, B, C, D, 'h' oder 'q' eingeben.", Colors.RED)
        
        # Check answer
        correct = answer == question_data['correct']
        
        if correct:
            self.print_colored("✅ RICHTIG!", Colors.GREEN + Colors.BOLD)
            self.score += 1
        else:
            self.print_colored(f"❌ FALSCH! Die richtige Antwort ist {question_data['correct']}", Colors.RED + Colors.BOLD)
            self.wrong_answers.append({
                'question': question_data['question'],
                'your_answer': answer,
                'correct_answer': question_data['correct'],
                'explanation': question_data['explanation']
            })
        
        # Show explanation
        self.print_colored(f"\n💭 Erklärung: {question_data['explanation']}", Colors.BLUE)
        
        input("\nDrücke Enter für die nächste Frage...")
        return True

    def show_wrong_answers_review(self):
        """Show review of wrong answers"""
        if not self.wrong_answers:
            return
        
        self.clear_screen()
        self.print_colored("=" * 70, Colors.HEADER)
        self.print_colored("📚 WIEDERHOLUNG - FALSCHE ANTWORTEN", Colors.HEADER + Colors.BOLD)
        self.print_colored("=" * 70, Colors.HEADER)
        
        for i, wrong in enumerate(self.wrong_answers, 1):
            self.print_colored(f"\n{i}. {wrong['question']}", Colors.BLUE + Colors.BOLD)
            self.print_colored(f"   Deine Antwort: {wrong['your_answer']}", Colors.RED)
            self.print_colored(f"   Richtige Antwort: {wrong['correct_answer']}", Colors.GREEN)
            self.print_colored(f"   💭 {wrong['explanation']}", Colors.CYAN)
            self.print_colored("-" * 50, Colors.HEADER)
        
        input("\nDrücke Enter um fortzufahren...")

    def save_stats(self):
        """Save quiz statistics to file"""
        try:
            # Load existing stats
            stats = []
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    stats = json.load(f)
            
            # Add current game stats
            current_stats = {
                'date': datetime.now().isoformat(),
                'score': self.score,
                'total': self.total_questions,
                'percentage': (self.score / self.total_questions * 100) if self.total_questions > 0 else 0,
                'difficulty': self.current_difficulty,
                'category': self.current_category,
                'hints_used': self.hints_used,
                'time_taken': time.time() - self.start_time if self.start_time else 0
            }
            
            stats.append(current_stats)
            
            # Keep only last 50 games
            stats = stats[-50:]
            
            # Save stats
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.print_colored(f"⚠️  Statistiken konnten nicht gespeichert werden: {e}", Colors.YELLOW)

    def show_final_score(self):
        self.clear_screen()
        self.print_colored("=" * 70, Colors.HEADER)
        self.print_colored("🏆 AP1 QUIZ BEENDET!", Colors.HEADER + Colors.BOLD)
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
                self.print_colored("\n🌟 AUSGEZEICHNET! Du bist bestens für die AP1 vorbereitet!", Colors.GREEN + Colors.BOLD)
            elif percentage >= 75:
                self.print_colored("\n👍 SEHR GUT! Du hast gute Chancen bei der AP1!", Colors.GREEN)
            elif percentage >= 60:
                self.print_colored("\n📚 SOLIDE BASIS! Wiederhole noch einmal die schwächeren Themen.", Colors.YELLOW)
            elif percentage >= 50:
                self.print_colored("\n💪 GRUNDLAGEN VORHANDEN! Intensiviere dein Lernen für die AP1.", Colors.YELLOW)
            else:
                self.print_colored("\n📖 MEHR LERNEN NÖTIG! Arbeite systematisch die AP1-Themen durch.", Colors.RED)
            
            # Save statistics
            self.save_stats()
        
        self.print_colored("\nViel Erfolg bei deiner AP1-Prüfung! 🎯", Colors.BLUE + Colors.BOLD)

    def play(self) -> bool:
        """Main game loop - returns False if user wants to quit"""
        self.display_welcome()
        
        # Select category and difficulty
        self.select_category()
        self.select_difficulty()
        
        # Get questions for the quiz
        questions = self.get_questions_for_quiz()
        
        if not questions:
            self.print_colored("❌ Keine Fragen verfügbar für diese Auswahl!", Colors.RED)
            return True
        
        self.total_questions = len(questions)
        self.start_time = time.time()
        
        # Ask all questions
        for i, question in enumerate(questions, 1):
            if not self.ask_question(question, i, self.total_questions):
                # User quit
                self.print_colored("\n👋 Quiz beendet!", Colors.YELLOW)
                return False
        
        # Show wrong answers review
        self.show_wrong_answers_review()
        
        # Show final score
        self.show_final_score()
        
        return True

def main():
    game = IHKAP1Quiz()
    
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
    
    game.print_colored("\nViel Erfolg bei deiner AP1-Prüfung! 👋", Colors.BLUE + Colors.BOLD)

if __name__ == "__main__":
    main()
