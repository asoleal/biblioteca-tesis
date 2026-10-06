import os
import json
import time
import urllib.request
import urllib.error
import urllib.parse

DOIS = [
    '10.1017/CBO9780511805400',
    '10.1890/14-0976.1',
    '10.1016/j.seares.2006.03.001',
    '10.1098/rspb.2015.1973',
    '10.1007/s11356-024-33308-8',
    '10.55214/25768484.v8i6.2182'
]

EMAIL = 'jlealgom@unal.edu.co'
OUTPUT_DIR = 'nuevos_deb_pdfs'


def safe_filename(doi):
    """Crea un nombre de archivo seguro a partir del DOI."""
    return doi.replace('/', '_').replace('\\', '_').replace(':', '_') + '.pdf'


def fetch_unpaywall(doi):
    """Consulta la API de Unpaywall y devuelve el JSON parseado."""
    encoded_doi = urllib.parse.quote(doi, safe='')
    url = f'https://api.unpaywall.org/v2/{encoded_doi}?email={EMAIL}'
    req = urllib.request.Request(url, headers={'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as response:
        data = response.read().decode('utf-8')
        return json.loads(data)


def find_pdf_url(record):
    """Busca la URL del PDF en la respuesta de Unpaywall."""
    # Primero intenta con best_oa_location
    best = record.get('best_oa_location') or {}
    if best.get('pdf_url'):
        return best['pdf_url']
    if best.get('url_for_pdf'):
        return best['url_for_pdf']

    # Luego recorre todas las ubicaciones OA
    for loc in record.get('oa_locations') or []:
        if loc.get('pdf_url'):
            return loc['pdf_url']
        if loc.get('url_for_pdf'):
            return loc['url_for_pdf']

    return None


def download_pdf(url, dest_path):
    """Descarga un PDF desde url y lo guarda en dest_path."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; PDF downloader via Unpaywall)'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as response:
        content_type = response.headers.get('Content-Type', '')
        data = response.read()
        if not data:
            raise ValueError('Respuesta vacía')
        with open(dest_path, 'wb') as f:
            f.write(data)
    return len(data), content_type


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f'Directorio de salida: {os.path.abspath(OUTPUT_DIR)}\n')

    for i, doi in enumerate(DOIS, start=1):
        print(f'[{i}/{len(DOIS)}] Procesando DOI: {doi}')
        try:
            record = fetch_unpaywall(doi)
            is_oa = record.get('is_oa', False)
            print(f'    Título: {record.get("title", "(sin título)")[:80]}')
            print(f'    Acceso abierto: {is_oa}')

            if not is_oa:
                print('    No está disponible en acceso abierto.')
                continue

            pdf_url = find_pdf_url(record)
            if not pdf_url:
                print('    No se encontró enlace directo a PDF.')
                continue

            print(f'    Enlace PDF: {pdf_url}')
            filename = safe_filename(doi)
            dest_path = os.path.join(OUTPUT_DIR, filename)

            size, content_type = download_pdf(pdf_url, dest_path)
            print(f'    Descargado: {filename} ({size} bytes, {content_type})')

            # Pausa corta para ser respetuoso con la API
            time.sleep(1)

        except urllib.error.HTTPError as e:
            print(f'    Error HTTP {e.code}: {e.reason}')
        except Exception as e:
            print(f'    Error: {e}')

    print('\nProceso completado.')


if __name__ == '__main__':
    main()
