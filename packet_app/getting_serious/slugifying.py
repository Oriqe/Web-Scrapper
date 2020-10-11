def slug_xome_prop_facts(address, zip):
    return f'https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=PropertyFacts&hideMap=true&streetAddress="{" ".join([i[0].upper()+i[1:].lower() for i in address.split(" ")])}"&zip={zip}'


def slug_xome_comp_sold(address, zip):
    return f'https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=ComparableHomeSales&hideMap=true&listedOrSold=2&streetAddress="{" ".join([i[0].upper()+i[1:].lower() for i in address.split(" ")])}"&zip={zip}&maxRecordsToDisplay=50'


def slug_xome_comp_listed(address, zip):
    return f'https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=ComparableHomeSales&hideMap=true&listedOrSold=1&streetAddress="{" ".join([i[0].upper()+i[1:].lower() for i in address.split(" ")])}"&zip={zip}&maxRecordsToDisplay=50'


def slug_xome_price_history(address, zip):
    return f'https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=PriceHistory&streetAddress="{" ".join([i[0].upper()+i[1:].lower() for i in address.split(" ")])}"&zip={zip}'


def slug_xome_tax_history(address, zip):
    return f'https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=TaxHistory&streetAddress="{" ".join([i[0].upper()+i[1:].lower() for i in address.split(" ")])}"&zip={zip}'


def slug_xome_estimate(address, zip):
    return f'https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=HomeValuationEstimate&streetAddress="{" ".join([i[0].upper()+i[1:].lower() for i in address.split(" ")])}"&zip={zip}'
