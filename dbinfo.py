#import database
#from app import db

def dbinfo(db):
	classes, models, table_names = [], [], []
	for clazz in db.Model._decl_class_registry.values():
	    try:
	        table_names.append(clazz.__tablename__)
	        classes.append(clazz)
	    except:
	        pass
	for table in db.metadata.tables.items():
	    if table[0] in table_names:
	        models.append(classes[table_names.index(table[0])])

	print 'classes'
	print classes
	print

	print 'models'
	print models
	print

	print 'table_names'
	print table_names