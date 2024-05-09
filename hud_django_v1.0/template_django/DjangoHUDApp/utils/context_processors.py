from django.urls import resolve

def mark_active_link(menu, current_path_name):
    for item in menu:
        item['is_active'] = item.get('name', '') == current_path_name

        if 'children' in item:
            item['children'] = mark_active_link(item['children'], current_path_name)

            if any(child.get('is_active', False) for child in item['children']):
                item['is_active'] = True

    return menu

def sidebar_menu(request):
	sidebar_menu = [{
		'text': 'Επιλογές',
		'is_header': 1
	},{
		'url': '/dashboard',
		'icon': 'bi bi-cpu',
		'text': 'Διαχείρηση',
		'name': 'dashboard'
	}, {
		'is_divider': 1
	}, {
		'text': 'Ενέργειες Προιόντων',
		'is_header': 1
	}, 
    #  {
	# 	'icon': 'bi bi-bag-check',
	# 	'text': 'Προιόντα',
	# 	'children': ''
	# }, 
     {
		'url': '/product',
		'icon': 'fas fa-tags',
		'text': 'Λίστα Προιόντων',
		'name': 'pageProduct'
	},{
		'url': '/add-product',
		'icon': 'fas fa-plus',
		'text': 'Προσθήκη Προιόντος',
		'name': 'dashboard'
	},{
		'url': '/page/data-management',
		'icon': 'fas fa-barcode',
		'text': 'Αποθέματα',
		'name': 'pageDataManagement'
	}, {
		'is_divider': 1
	}, {
		'text': 'Ενέργιες Διακινίσεων',
		'is_header': 1
	}, {
		'url': '/order',
		'icon': 'bi bi-layout-sidebar',
		'text': 'Λίστα Διακινίσεων',
		'name': ''
	}, {
		'url': '/add-shipment',
		'icon': 'far fa-envelope',
		'text': 'Δημιουργία Διακίνισης',
		'name': 'dashboard'
	},{
		'url': '/recipient',
		'icon': 'far fa-address-book',
		'text': 'Παραλήπτες',
		'name': 'dashboard'
	}, {
		'is_divider': 1
	}, {
		'text': 'Ενέργειες Αποθηκών',
		'is_header': 1
	}, {
		'url': '/warehouse',
		'icon': 'fas fa-cubes',
		'text': 'Λίστα Αποθηκών',
		'name': 'dashboard'
	}, {
		'url': '/stock-per-warehouse/1',
		'icon': 'fas fa-server',
		'text': 'Αποθήκη ΚΕΠΙΚ',
		'name': 'dashboard'
	},{
		'url': '/stock-per-warehouse/2',
		'icon': 'fas fa-building',
		'text': 'Αποθήκη Τάγματος',
		'name': 'dashboard'
	}, {
		'url': '/stock-per-warehouse/3',
		'icon': 'fas fa-signal',
		'text': 'Αποθήκη Δορυφορικών',
		'name': 'dashboard'
	}, {
		'is_divider': 1
	}, {
		'text': 'Άλλες Ενέργειες',
		'is_header': 1
	}, {
		'url': '/logout',
		'icon': 'bi bi-people',
		'text': 'Έξοδος',
		'name': 'logout'
	},
    # {
	# 	'url': '/settings',
	# 	'icon': 'bi bi-gear',
	# 	'text': 'Ρυθμίσεις',
	# 	'name': 'settings'
	# }
     ]
	
	resolved_path = resolve(request.path_info)

	current_path_name = resolved_path.url_name
	
	sidebar_menu = mark_active_link(sidebar_menu, current_path_name)

	return {'sidebar_menu': sidebar_menu}