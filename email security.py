import dns.resolver

def check_domain(domain):
    spf = False
    dmarc = False
    dkim = False

    # Checks SPF record
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            if 'v=spf1' in rdata.to_text():
                spf = True
                break
    except:
        pass

    # Checks DMARC record
    try:
        answers = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
        for rdata in answers:
            if 'v=DMARC1' in rdata.to_text():
                dmarc = True
                break
    except:
        pass

    # Checks DKIM record
    try:
        answers = dns.resolver.resolve('selector1._domainkey.' + domain, 'TXT')
        for rdata in answers:
            if 'v=DKIM1' in rdata.to_text():
                dkim = True
                break
    except:
        pass

    return {'domain': domain, 'spf': spf, 'dmarc': dmarc, 'dkim': dkim}

if __name__ == '__main__':
    domains = ['cleartile.com', 'saddlewest.com', 'orbissolutionsinc.com', 'spmlv.com', 'GalaxyGaming.com'] # Enter list here
    results = []
    for domain in domains:
        results.append(check_domain(domain))

    # Export results to CSV file
    with open('results.csv', 'w') as f: 
        f.write('Domain,SPF,DMARC,DKIM\n') # This writes the first line or HEADER, then moves to 2nd line
        for result in results:
            f.write(result['domain'] + ',' + str(result['spf']) + ',' + str(result['dmarc']) + ',' + str(result['dkim']) + '\n')