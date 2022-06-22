import dns.resolver
import sys

rec_types=['A','AAAA','NS','CNAME','MX','SOA','PTR','TXT']
domain="youtube.com"
for rec in rec_types:
    try:
        answer = dns.resolver.resolve(domain,rec)
        print(f'{rec} Records')
        print('-'*20)
        for server in answer:
            print(server.to_text()+'\n')
    
    except dns.resolver.NoAnswer:
        pass
    except KeyboardInterrupt:
        quit()
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist')
        quit()


