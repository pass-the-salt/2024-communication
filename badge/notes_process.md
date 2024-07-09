# Collect orders

https://pretix.eu/control/event/passthesalt/2024/orders/export/

* Orders/Export/Order Data
* Export Format: Order positions - CSV (with semicolons)
* Only paid orders
* => `2024_orders.csv`

# Generate lists

Check START_DATE to only process latest orders in
* `gen_badges.py`
* `gen_security_lists.py`
* `gen_wifi_lists.py`
* `list_template.py`

## Wi-Fi

Lists for Wi-Fi:

`gen_wifi_lists.py` => `*_ppl_wifi.csv`

## Vigiles

Lists for vigiles:

`gen_security_lists.py` => `*_ppl*.txt`

## Badges

`gen_badges.py`

Check *txt

Check for special chars
```
cat  *.txt|tr -d "a-zA-Z~ 0-9"|sed 's/\(.\)/\1\n/g'|sort|uniq|tr -d '\n';echo
=> "#'(),-./@_éèêëïôü
```

# Generate SVG for badges

Run
* `list_attendees_fr.py`
* `list_attendees_uk.py`
* `list_orga_fr.py`
* `list_orga_uk.py`
* `list_speakers_fr.py`
* `list_speakers_uk.py`
* `list_template.py`

Don't forget to do a few empty attendee fr/uk badges

# Lightburn

Import all SVG in Lightburn

Layers:
- Blue/Magenta
  - line 2100/4 no-air
- Cyan
  - multi
    - fill 3000/2 overscan:2.5% 0.1mm "fill shapes individually" no-air
    - line 2100/3 no-air
- Red
  - line 1400/90 air
- Green
  - line 1400/90 air

Fix code font to monotrait:
- Show only Magenta
- Ungroup all
- Ungroup all
- Select all magenta
- font: SL_exthalf2/exthalf2 H2.5mm

# Merge Wi-Fi codes

Once we got the Wi-Fi codes from university, create a merged list for printout

Get `*_ppl_wifi.csv` + `*_ppl_wifi_codes.csv`

Run `merge_wifi_lists.py` => `*_ppl_wifi_merged.txt`
