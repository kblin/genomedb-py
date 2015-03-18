# vim: set fileencoding=utf-8 :

from helperlibs.bio import seqio
from sqlalchemy.orm.exc import NoResultFound

from genomedb.utils import init_database
from genomedb.config import load_config
from genomedb.models import (
    Domain,
    Kingdom,
    Phylum,
    Class,
    Order,
    Family,
    Genus,
    Species,
    Record,
    LocusTag,
)

def setup_add_args(subparsers):
    """Set up command line options for 'genomedb add'"""
    p_add = subparsers.add_parser('add',
                                  help="Add a genome from a gbk file to the database")
    p_add.add_argument('genome_files', metavar='genome_files', nargs="+",
                       help="GenBank genome file(s) to add to the database")
    p_add.set_defaults(func=add)

def add(args):
    """Parse a GBK file and add it to the database"""
    load_config(args)
    session = init_database(args)

    for fname in args.genome_files:
        bprec = seqio.read(fname)
        taxonomy = bprec.annotations['taxonomy']
        if len(taxonomy) < 8:
            print "invalid taxonomy, skipping {name}".format(name=fname)
            continue
        domain = _get_domain(session, taxonomy[0])
        kingdom = _get_kingdom(session, domain, taxonomy[1])
        phylum = _get_phylum(session, domain, kingdom, taxonomy[2])
        class_ = _get_class(session, domain, kingdom, phylum, taxonomy[3])
        order = _get_order(session, domain, kingdom, phylum, class_, taxonomy[4])
        family = _get_family(session, domain, kingdom, phylum, class_, order, taxonomy[5])
        genus = _get_genus(session, domain, kingdom, phylum, class_, order, family, taxonomy[6])
        species = _get_species(session, domain, kingdom, phylum, class_, order, family, genus, taxonomy[7])
        record = _get_record(session, domain, kingdom, phylum, class_, order, family, genus,
                             species, bprec.annotations['organism'])

        for feature in bprec.features:
            if feature.type != 'CDS':
                continue
            if 'locus_tag' not in feature.qualifiers:
                continue
            LocusTag(name=feature.qualifiers['locus_tag'][0], record=record)

        session.add(record)
    session.commit()



def _get_domain(session, domain_name):
    try:
        domain = session.query(Domain).filter(Domain.name == domain_name).one()
    except NoResultFound:
        domain = Domain(name=domain_name)

    return domain


def _get_kingdom(session, domain, kingdom_name):
    try:
        kingdom = session.query(Kingdom).filter(Kingdom.name == kingdom_name).one()
    except NoResultFound:
        kingdom = Kingdom(name=kingdom_name, domain=domain)

    return kingdom


def _get_phylum(session, domain, kingdom, phylum_name):
    try:
        phylum = session.query(Phylum).filter(Phylum.name == phylum_name).one()
    except NoResultFound:
        phylum = Phylum(name=phylum_name, domain=domain, kingdom=kingdom)

    return phylum


def _get_class(session, domain, kingdom, phylum, class_name):
    try:
        class_ = session.query(Class).filter(Class.name == class_name).one()
    except NoResultFound:
        class_ = Class(name=class_name, domain=domain, kingdom=kingdom, phylum=phylum)

    return class_


def _get_order(session, domain, kingdom, phylum, class_, order_name):
    try:
        order = session.query(Order).filter(Order.name == order_name).one()
    except NoResultFound:
        order = Order(name=order_name, domain=domain, kingdom=kingdom, phylum=phylum, class_=class_)

    return order


def _get_family(session, domain, kingdom, phylum, class_, order, family_name):
    try:
        family = session.query(Family).filter(Family.name == family_name).one()
    except NoResultFound:
        family = Family(name=family_name, domain=domain, kingdom=kingdom, phylum=phylum,
                 class_=class_, order=order)

    return family


def _get_genus(session, domain, kingdom, phylum, class_, order, family, genus_name):
    try:
        genus = session.query(Genus).filter(Genus.name == genus_name).one()
    except NoResultFound:
        genus = Genus(name=genus_name, domain=domain, kingdom=kingdom, phylum=phylum, class_=class_,
                order=order, family=family)

    return genus


def _get_species(session, domain, kingdom, phylum, class_, order, family, genus, species_name):
    try:
        species = session.query(Species).filter(Species.name == species_name).one()
    except NoResultFound:
        species = Species(name=species_name, domain=domain, kingdom=kingdom, phylum=phylum,
                  class_=class_, order=order, family=family, genus=genus)

    return species


def _get_record(session, domain, kingdom, phylum, class_, order, family, genus, species, record_name):
    try:
        record = session.query(Record).filter(Record.name == record_name).one()
    except NoResultFound:
        record = Record(name=record_name, domain=domain, kingdom=kingdom, phylum=phylum, class_=class_,
                 order=order, family=family, genus=genus, species=species)

    return record


