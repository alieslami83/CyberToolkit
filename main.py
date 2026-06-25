from rich.console import Console
from rich.table import Table
from modules.web.ssl_analyzer import SSLAnalyzer
from core.banner import banner
from modules.web.header_analyzer import HeaderAnalyzer
from modules.recon.ip_info import IPInfo
from modules.recon.dns_lookup import DNSLookup
from modules.recon.whois_lookup import WhoisLookup
from modules.network.port_scanner import PortScanner
from modules.web.technology_detector import TechnologyDetector
from modules.utils.reports_dashboard import ReportsDashboard
from modules.crypto.hash_generator import HashGenerator
from modules.crypto.hash_identifier import HashIdentifier
from modules.utils.base64_tool import Base64Tool
from modules.utils.url_parser import URLParser
from modules.crypto.jwt_decoder import JWTDecoder
from modules.utils.settings_manager import SettingsManager
from modules.utils.dashboard import Dashboard
from modules.utils.html_report import HTMLReportGenerator
from modules.utils.statistics import Statistics
console = Console()
def ip_menu():

    target = input("\nTarget: ")

    tool = IPInfo()

    data = tool.lookup(target)

    table = Table(title="IP Information")

    table.add_column("Field")
    table.add_column("Value")

    for key, value in data.items():

        table.add_row(
            str(key),
            str(value)
        )

    console.print(table)

    input("\nPress Enter...")


def dns_menu():

    domain = input("\nDomain: ")

    tool = DNSLookup()

    data = tool.lookup(domain)

    table = Table(
        title=f"DNS Records - {domain}"
    )

    table.add_column("Type")
    table.add_column("Value")

    for record, values in data.items():

        for value in values:

            table.add_row(
                record,
                value
            )

    console.print(table)

    input("\nPress Enter...")


def whois_menu():

    domain = input("\nDomain: ")

    tool = WhoisLookup()

    data = tool.lookup(domain)

    table = Table(
        title=f"Whois - {domain}"
    )

    table.add_column("Field")
    table.add_column("Value")

    for key, value in data.items():

        table.add_row(
            str(key),
            str(value)
        )

    console.print(table)

    input("\nPress Enter...")

def ssl_menu():

    domain = input(
        "\nDomain: "
    )

    tool = SSLAnalyzer()

    data = tool.analyze(domain)

    table = Table(
        title=f"SSL Info - {domain}"
    )

    table.add_column("Field")
    table.add_column("Value")

    for key, value in data.items():

        table.add_row(
            str(key),
            str(value)
        )

    console.print(table)

    input("\nPress Enter...")

def header_menu():

    target = input(
        "\nURL/Domain: "
    )

    tool = HeaderAnalyzer()

    data = tool.analyze(
        target
    )

    table = Table(
        title=f"Headers - {target}"
    )

    table.add_column(
        "Header"
    )

    table.add_column(
        "Status"
    )

    for key, value in data[
        "security_headers"
    ].items():

        table.add_row(
            key,
            value
        )

    console.print(table)

    input(
        "\nPress Enter..."
    )

def portscan_menu():

    host = input(
        "\nHost/IP: "
    )

    ports = input(
        "Ports (e.g. 80,443,8080): "
    )

    ports = [
        int(p.strip())
        for p in ports.split(",")
    ]

    tool = PortScanner()

    result = tool.scan(
        host,
        ports
    )

    table = Table(
        title=f"Open Ports - {host}"
    )

    table.add_column(
        "Port"
    )

    for port in result[
        "open_ports"
    ]:

        table.add_row(
            str(port)
        )

    console.print(table)

    input(
        "\nPress Enter..."
    )

def technology_menu():

    target = input(
        "\nTarget: "
    )

    tool = TechnologyDetector()

    data = tool.detect(
        target
    )

    table = Table(
        title="Technology Detection"
    )

    table.add_column(
        "Technology"
    )

    for tech in data[
        "technologies"
    ]:

        table.add_row(
            tech
        )

    console.print(table)

    input(
        "\nPress Enter..."
    )

def reports_menu():

    dashboard = ReportsDashboard()

    reports = dashboard.get_reports()

    table = Table(
        title="Reports Dashboard"
    )

    table.add_column("File")

    table.add_column("Size (KB)")

    table.add_column("Modified")

    for report in reports:

        table.add_row(
            report["name"],
            str(report["size_kb"]),
            report["modified"]
        )

    console.print(table)

    input(
        "\nPress Enter..."
    )

def hash_menu():

    text = input(
        "\nText: "
    )

    tool = HashGenerator()

    data = tool.generate(
        text
    )

    table = Table(
        title="Hash Generator"
    )

    table.add_column(
        "Algorithm"
    )

    table.add_column(
        "Hash"
    )

    for key, value in data.items():

        table.add_row(
            key,
            value
        )

    console.print(table)

    input(
        "\nPress Enter..."
    )

def hash_identifier_menu():

    value = input(
        "\nHash: "
    )

    tool = HashIdentifier()

    data = tool.identify(
        value
    )

    table = Table(
        title="Hash Identifier"
    )

    table.add_column(
        "Possible Algorithm"
    )

    for algo in data[
        "possible_algorithms"
    ]:

        table.add_row(
            algo
        )

    console.print(table)

    input(
        "\nPress Enter..."
    )

def base64_menu():

    console.print(
        "\n1. Encode"
    )

    console.print(
        "2. Decode"
    )

    option = input(
        "\nSelect > "
    )

    text = input(
        "\nText: "
    )

    tool = Base64Tool()

    if option == "1":

        result = tool.encode(
            text
        )

    elif option == "2":

        result = tool.decode(
            text
        )

    else:

        return

    table = Table(
        title="Base64 Tool"
    )

    table.add_column(
        "Result"
    )

    table.add_row(
        result
    )

    console.print(
        table
    )

    input(
        "\nPress Enter..."
    )

def url_parser_menu():

    url = input(
        "\nURL: "
    )

    tool = URLParser()

    data = tool.parse(
        url
    )

    table = Table(
        title="URL Parser"
    )

    table.add_column(
        "Field"
    )

    table.add_column(
        "Value"
    )

    for key, value in data.items():

        table.add_row(
            str(key),
            str(value)
        )

    console.print(
        table
    )

    input(
        "\nPress Enter..."
    )

def jwt_menu():

    token = input(
        "\nJWT: "
    )

    tool = JWTDecoder()

    try:

        data = tool.decode(
            token
        )

        console.print(
            "\n[bold cyan]Header[/bold cyan]"
        )

        console.print(
            data["header"]
        )

        console.print(
            "\n[bold green]Payload[/bold green]"
        )

        console.print(
            data["payload"]
        )

    except Exception as e:

        console.print(
            f"[red]{e}[/red]"
        )

    input(
        "\nPress Enter..."
    )

def settings_menu():

    manager = SettingsManager()

    config = manager.load()

    while True:

        console.clear()

        table = Table(
            title="Settings"
        )

        table.add_column(
            "Key"
        )

        table.add_column(
            "Value"
        )

        for key, value in config.items():

            table.add_row(
                str(key),
                str(value)
            )

        console.print(table)

        console.print(
            "\n1. Change Timeout"
        )

        console.print(
            "2. Change Threads"
        )

        console.print(
            "3. Toggle Reports"
        )

        console.print(
            "0. Back"
        )

        choice = input(
            "\nSelect > "
        )

        if choice == "1":

            config[
                "timeout"
            ] = int(
                input(
                    "New Timeout: "
                )
            )

        elif choice == "2":

            config[
                "threads"
            ] = int(
                input(
                    "New Threads: "
                )
            )

        elif choice == "3":

            config[
                "save_reports"
            ] = not config[
                "save_reports"
            ]

        elif choice == "0":

            manager.save(
                config
            )

            break

def html_report_menu():

    path = input(
        "\nJSON Report Path: "
    )

    tool = HTMLReportGenerator()

    try:

        html_file = tool.generate(
            path
        )

        console.print(
            f"\n[green]Generated:[/green] {html_file}"
        )

    except Exception as e:

        console.print(
            f"[red]{e}[/red]"
        )

    input(
        "\nPress Enter..."
    )

def statistics_menu():

    stats = Statistics()

    data = stats.get_stats()

    table = Table(
        title="Statistics Dashboard"
    )

    table.add_column(
        "Metric"
    )

    table.add_column(
        "Value"
    )

    for key, value in data.items():

        table.add_row(
            str(key),
            str(value)
        )

    console.print(table)

    input(
        "\nPress Enter..."
    )


while True:

    console.clear()

    console.print(banner())
    stats = Dashboard().get_stats()
    table = Table(
        title="Dashboard"
    )

    table.add_column("Item")
    table.add_column("Value")

    table.add_row(
        "Version",
        stats["version"]
    )

    table.add_row(
        "Modules",
        str(stats["modules"])
    )

    table.add_row(
        "Reports",
        str(stats["reports"])
    )

    table.add_row(
        "Logs",
        str(stats["logs"])
    )

    console.print(table)
    console.print("1. IP Information")
    console.print("2. DNS Lookup")
    console.print("3. Whois Lookup")
    console.print("4. SSL Analyzer")
    console.print("5. Header Analyzer")
    console.print("6. Port Scanner")
    console.print("7. Technology Detector")
    console.print("8. Reports Dashboard")
    console.print("9. Hash Generator")
    console.print("10. Hash Identifier")
    console.print("11. Base64 Tool")
    console.print("12. URL Parser")
    console.print("13. JWT Decoder")
    console.print("14. Settings")
    console.print("15. HTML Report")
    console.print("16. Statistics")
    console.print("17. CSV Exporter")
    console.print("0. Exit")
    
    choice = input("\nSelect > ")

    if choice == "1":

        ip_menu()

    elif choice == "2":

        dns_menu()

    elif choice == "3":

        whois_menu()

    elif choice == "4":

        ssl_menu()

    elif choice == "5":

        header_menu()

    elif choice == "6":

        portscan_menu()
    
    elif choice == "7":

        technology_menu()

    elif choice == "8":

        reports_menu()
    
    elif choice == "9":

        hash_menu()
    
    elif choice == "10":

        hash_identifier_menu()
    
    elif choice == "11":

        base64_menu()
    
    elif choice == "12":

        url_parser_menu()
    
    elif choice == "13":

        jwt_menu()

    elif choice == "14":

        settings_menu()
    
    elif choice == "15":

        html_report_menu()
    
    elif choice == "16":

        statistics_menu()
     
    elif choice == "17":

        statistics_menu()

    elif choice == "0":

        break

    else:

        console.print("\n[red]Invalid Option[/red]")

        input("\nPress Enter...")