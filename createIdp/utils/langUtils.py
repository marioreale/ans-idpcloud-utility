#!/usr/bin/env python
# coding=utf-8

from collections import OrderedDict

def get_os_orderedDict(lang):

   if (lang == 'it-IT'):
      return OrderedDict([
               ("ip_priv","Inserisci l'IP Privato della VM: "),
               ("ip_pub","Inserisci l'IP Pubblico della VM: "),
               ("boot_vlm_size","Inserisci la dimensione, in GB, del disco di boot della VM: (default: 10)"),
               ("boot_vlm_image","Inserisci la distribuzione che verrà installata sulla VM (default: Debian-8.8.2): "),
               ("flavor","Inserisci il flavor della VM (default: idem-idpcloud): "),
               ("data_vlm_size","Vuoi aggiungere un ulteriore volume persistente? (default: no): "),
               ("sec_groups","Aggiungere security groups aggiuntivi oltre a default? (default: no): "),
            ])

   if (lang == 'en-GB'):
      return OrderedDict([
               ("ip_priv","Insert Private IP for the VM: "),
               ("ip_pub","Insert Public IP for the VM: "),
               ("boot_vlm_size","Insert the Boot Disk size, in GB, for the VM: (default: 10)"),
               ("boot_vlm_image","Insert the Openstack image used for the VM (default: Debian-8.10.10): "),
               ("flavor","Insert the flavor for the VM (default: idem-idpcloud): "),
               ("data_vlm_size","Do you want to add a persistent volume to the VM? (default: no): "),
               ("sec_groups","Do you want to add other security groups than default? (default: no): "),
            ])

def get_yml_orderedDict(lang):

   if (lang == 'it-IT'):
      return OrderedDict([
               ("mdui_displayName_it","Inserisci il nome dell'istituzione in ITALIANO: "),
               ("mdui_displayName_en","Inserisci il nome dell'istituzione in INGLESE: "),
               ("domain","Inserisci il dominio dell'istituzione: "),
               ("org_url_it","Inserisci il sito istituzionale pubblico in ITALIANO: "),
               ("org_url_en","Inserisci il sito istituzionale pubblico in INGLESE: "),
               ("mdui_logo_it","Inserisci la URL HTTPS del Logo ITALIANO(160x120) dell'istituzione (premi 'Invio' per tenere il valore predefinito): "),
               ("mdui_logo_en","Inserisci la URL HTTPS del Logo INGLESE(160x120) dell'istituzione (premi 'Invio' per tenere il valore predefinito): "),
               ("mdui_favicon_it","Inserisci la URL HTTPS della Favicon ITALIANA (32x32) dell'istituzione (premi 'Invio' per tenere il valore predefinito): "),
               ("mdui_favicon_en","Inserisci la URL HTTPS della Favicon INGLESE (32x32) dell'istituzione (premi 'Invio' per tenere il valore predefinito): "),
               ("footer_bkgr_color","Inserisci il colore esadecimale rappresentativo dell'istituzione (premi 'Invio' per generare un valore casuale): "),
               ("mdui_description_it","Inserisci la descrizione dell'IdP istituzionale in lingua ITALIANA (premi 'Invio' per tenere il valore predefinito): "),
               ("mdui_description_en","Inserisci la descrizione dell'IdP istituzionale in lingua INGLESE (premi 'Invio' per tenere il valore predefinito ): "),
               ("mdui_privacy_it","Inserisci la pagina di Privacy Policy per l'IdP in ITALIANO (premi 'Invio' per tenere il valore predefinito): "),
               ("mdui_privacy_en","Inserisci la pagina di Privacy Policy per l'IdP in INGLESE (premi 'Invio' per tenere il valore predefinito): "),
               ("mdui_info_it","Inserisci la pagina Informativa per l'IdP in ITALIANO (premi 'Invio' per tenere il valore predefinito): "),
               ("mdui_info_en","Inserisci la pagina Informativa per l'IdP in INGLESE (premi 'Invio' per tenere il valore predefinito): "),
               ("idp_support_email","Inserisci la mail di supporto per gli utenti dell'IdP istituzionale (premi 'Invio' per tenere il valore 'idpcloud-service@garr.it'): "),
               ("idp_support_address","Inserisci l'indirizzo postale dell'istituzione (premi 'Invio' per inserire in futuro): "),
               ("idp_type","Inserisci 'Debian-IdP-with-IdM' o 'Debian-IdP-without-IdM': (premi 'Invio' per 'Debian-IdP-with-IdM'): "),
               ("ca","Inserisci la URL dove recuperare la CA, in formato PEM, utilizzata per creare il certificato e la chiave SSL per l'IdP. Esempi:\n1) https://www.terena.org/activities/tcs/repository/sha2/TERENA_SSL_CA_2.pem\n2) https://www.terena.org/activities/tcs/repository-g3/TERENA_SSL_CA_3.pem\nDigita la URL: "),
               ("idp_persistentId_salt","Inserisci il persistent-id salt da applicare (premi 'Invio' per generare un valore casuale): "),
               ("idp_fticks_salt","Inserisci il salt per gli f-ticks da applicare (premi 'Invio' per generare un valore casuale): "),
               ("web_gui_user","Inserisci il nome dell'utente che accederà via Web l'IDM dell'IdP (premi 'Invio' per tenere il valore predefinito 'idm-admin'): "),
               ("web_gui_pw","Inserisci la password dell'utente che accederà via web all'IDM dell'IdP (premi 'Invio' per generare un valore casuale): "),
               ("root_ldap_pw","Inserisci la password dell'utente 'admin' di openLDAP (premi 'Invio' per generare un valore casuale): "),
               ("mysql_root_password","Inserisci la password dell'utente 'root' di MySQL (premi 'Invio' per generare un valore casuale): "),
               ("shibboleth_db_password","Inserisci la password dell'utente 'shibboleth' di MySQL (premi 'Invio' per generare un valore casuale): "),
               ("bindDNCredential","Inserisci la password dell'utente 'idpuser' di OpenLDAP (premi 'Invio' per generare un valore casuale): "),
               ("idp_stats_db_pw","Inserisci la password dell'utente 'statistics' di MySQL (premi 'Invio' per generare un valore casuale): "),
            ])

   if (lang == 'en-GB'):
      return OrderedDict([
               ("mdui_displayName_it","Insert the Institution Name for the ITALIAN language: "),
               ("mdui_displayName_en","Insert the Institution Name for the ENGLISH language: "),
               ("domain","Insert the Institution domain: "),
               ("org_url_it","Insert the Institution site for the ITALIAN language: "),
               ("org_url_en","Insert the Institution site for the ENGLISH language: "),
               ("mdui_logo_it","Insert the URL HTTPS of the Institution Logo (160x120) for the ITALIAN language (press Enter to keep the default value): "),
               ("mdui_logo_en","Insert the URL HTTPS of the Institution Logo (160x120) for the ENGLISH language (press Enter to keep the default value): "),
               ("mdui_favicon_it","Insert the URL HTTPS of the Institution Favicon (32x32) for the ITALIAN language (press Enter to keep the default value): "),
               ("mdui_favicon_en","Insert the URL HTTPS of the Institution Favicon (32x32) for the ENGLISH language (press Enter to keep the default value): "),
               ("footer_bkgr_color","Insert the hexadecimal color of the institution (press Enter to generate a random value): "),
               ("mdui_description_it","Insert Institution IdP description for the ITALIAN language (press Enter to keep the default value): "),
               ("mdui_description_en","Insert Institution IdP description for the ENGLISH language (press Enter to keep the default value): "),
               ("mdui_privacy_it","Insert the URL of the Privacy Policy page valid for the Institution in ITALIAN language (press Enter to keep the default value): "),
               ("mdui_privacy_en","Insert the URL of the Privacy Policy page valid for the Institution in ENGLISH language (press Enter to keep the default value): "),
               ("mdui_info_it","Insert the URL of the Information page valid for the Institution in ITALIAN language (press Enter to keep the default value): "),
               ("mdui_info_en","Insert the URL of the Information page valid for the Institution in ENGLISH language (press Enter to keep the default value): "),
               ("idp_support_email","Insert the User Support e-mail address for the Institutional IdP (press Enter to keep the default value 'idpcloud-service@example.org'): "),
               ("idp_support_address","Insert your institution address (press Enter to provide it later): "),
               ("idp_type","Insert 'Debian-IdP-with-IdM' or 'Debian-IdP-without-IdM': (press 'Enter' for 'Debian-IdP-with-IdM'): "),
               ("ca","Insert the URL where the CA PEM certificate, used to generate SSL Key and Certificate of the IdP, can be retrieved. Examples:\n1) https://www.terena.org/activities/tcs/repository/sha2/TERENA_SSL_CA_2.pem\n2) https://www.terena.org/activities/tcs/repository-g3/TERENA_SSL_CA_3.pem\nDigit the CA URL here: "),
               ("idp_persistentId_salt","Insert the persistent-id salt (press Enter to generate a random value): "),
               ("idp_fticks_salt","Insert the f-ticks salt (press Enter to generate a random value): "),
               ("web_gui_user","Insert the username of the user who will have access to the IdP IDM (press Enter to keep the default value 'idm-admin'): "),
               ("web_gui_pw","Insert the password of the user who will have access to the IdP IDM (press Enter to generate a random value): "),
               ("root_ldap_pw","Insert the openLDAP root password (press Enter to generate a random value): "),
               ("mysql_root_password","Insert the MySQL root password (press Enter to generate a random value): "),
               ("shibboleth_db_password","Insert the 'shibboleth' user password (press Enter to generate a random value): "),
               ("bindDNCredential","Insert the 'idpuser' user password (press Enter to generate a random value): "),
               ("idp_stats_db_pw","Insert the 'statistics' user password (press Enter to generate a random value): "),
            ])
