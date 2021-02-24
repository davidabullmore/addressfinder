# -*- coding: utf-8 -*-

"""
    pyap.source_AU.data
    ~~~~~~~~~~~~~~~~~~~~

    This module provides regular expression definitions required for
    detecting AU/Australian addresses.

    The module is expected to always contain 'full_address' variable containing
    all address parsing definitions.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
    :AU addition by David Bullmore, on 17/08/2020. Contact daveabullmore@gmail.com.
"""


'''Numerals from one to nine
Note: here and below we use syntax like '[Oo][Nn][Ee]'
instead of '(one)(?i)' to match 'One' or 'oNe' because
Python Regexps don't seem to support turning On/Off
case modes for subcapturing groups.
'''
zero_to_nine = r"""(?:
    [Zz][Ee][Rr][Oo]\ |[Oo][Nn][Ee]\ |[Tt][Ww][Oo]\ |
    [Tt][Hh][Rr][Ee][Ee]\ |[Ff][Oo][Uu][Rr]\ |
    [Ff][Ii][Vv][Ee]\ |[Ss][Ii][Xx]\ |
    [Ss][Ee][Vv][Ee][Nn]\ |[Ee][Ii][Gg][Hh][Tt]\ |
    [Nn][Ii][Nn][Ee]\ |[Tt][Ee][Nn]\ |
    [Ee][Ll][Ee][Vv][Ee][Nn]\ |
    [Tt][Ww][Ee][Ll][Vv][Ee]\ |
    [Tt][Hh][Ii][Rr][Tt][Ee][Ee][Nn]\ |
    [Ff][Oo][Uu][Rr][Tt][Ee][Ee][Nn]\ |
    [Ff][Ii][Ff][Tt][Ee][Ee][Nn]\ |
    [Ss][Ii][Xx][Tt][Ee][Ee][Nn]\ |
    [Ss][Ee][Vv][Ee][Nn][Tt][Ee][Ee][Nn]\ |
    [Ee][Ii][Gg][Hh][Tt][Ee][Ee][Nn]\ |
    [Nn][Ii][Nn][Ee][Tt][Ee][Ee][Nn]\ 
    )"""

# Numerals - 10, 20, 30 ... 90
ten_to_ninety = r"""(?:
    [Tt][Ee][Nn]\ |[Tt][Ww][Ee][Nn][Tt][Yy]\ |
    [Tt][Hh][Ii][Rr][Tt][Yy]\ |
    [Ff][Oo][Rr][Tt][Yy]\ |
    [Ff][Oo][Uu][Rr][Tt][Yy]\ |
    [Ff][Ii][Ff][Tt][Yy]\ |[Ss][Ii][Xx][Tt][Yy]\ |
    [Ss][Ee][Vv][Ee][Nn][Tt][Yy]\ |
    [Ee][Ii][Gg][Hh][Tt][Yy]\ |
    [Nn][Ii][Nn][Ee][Tt][Yy]\ 
    )"""

# One hundred
hundred = r"""(?:
    [Hh][Uu][Nn][Dd][Rr][Ee][Dd]\ 
    )"""

# One thousand
thousand = r"""(?:
    [Tt][Hh][Oo][Uu][Ss][Aa][Nn][Dd]\ 
    )"""

'''
Regexp for matching street number.
Street number can be written 2 ways:
1) Using letters - "One thousand twenty two"
2) Using numbers
   a) - "1022"
   b) - "85-1190"
   c) - "85 1190"
'''
street_number = r"""(?P<street_number>
                        (?:
                            [Aa][Nn][Dd]\ 
                            |
                            {thousand}
                            |
                            {hundred}
                            |
                            {zero_to_nine}
                            |
                            {ten_to_ninety}
                        ){from_to}
                        |
                        (?:\d{from_to}
                            (?:\ ?\-?\ ?\d{from_to})?\ 
                        )
                    )
                """.format(thousand=thousand,
                           hundred=hundred,
                           zero_to_nine=zero_to_nine,
                           ten_to_ninety=ten_to_ninety,
                           from_to='{1,5}')

'''
Regexp for matching street name.
In example below:
"Hoover Boulevard": "Hoover" is a street name
'''
street_name = r"""(?P<street_name>
                  [a-zA-Z0-9\ \.]{0,31}  # Seems like the longest US street is
                                         # 'Northeast Kentucky Industrial
                                         # Parkway'
                                         # https://atkinsbookshelf.wordpress.com/tag/longest-street-name-in-us/
                 )
              """

post_direction = r"""
                    (?P<post_direction>
                        (?:
                            [Nn][Oo][Rr][Tt][Hh]\ |
                            [Ss][Oo][Uu][Tt][Hh]\ |
                            [Ee][Aa][Ss][Tt]\ |
                            [Ww][Ee][Ss][Tt]\ 
                        )
                        |
                        (?:
                            NW\ |NE\ |SW\ |SE\ 
                        )
                        |
                        (?:
                            N[\.\ ]|S[\.\ ]|E[\.\ ]|W[\.\ ]
                        )
                    )
                """

# Regexp for matching street type
street_type = r"""
            (?P<street_type>
                # Street
                [Ss][Tt][Rr][Ee][Ee][Tt]{div}|[Ss][Tt](?![A-Za-z]){div}|
                # Court
                [Cc][Oo][Uu][Rr][Tt]|[Cc][Rr][Tt]{div}|[Cc][Tt]{div}|
                # Alley
                [Aa][Ll][Ll][Ee][Yy]|[Aa][Ll][Ll][Yy]{div}|
                # Arcade
                [Aa][Rr][Cc][Aa][Dd][Ee]|[Aa][Rr][Cc]{div}|
                # Avenue
                [Aa][Vv][Ee][Nn][Uu][Ee]|[Aa][Vv][Ee]{div}|
                # Boulevard
                [Bb][Oo][Uu][Ll][Ee][Vv][Aa][Rr][Dd]|[Bb][Vv][Dd]{div}|
                # Bypass
                [Bb][Yy][Pp][Aa][Ss][Ss]|[Bb][Yy][Pp][Aa]{div}|
                # Circuit
                [Cc][Ii][Rr][Cc][Uu][Ii][Tt]|[Cc][Cc][Tt]{div}|
                # Close
                [Cc][Ll][Oo][Ss][Ee]|[Cc][Ll]{div}|
                # Corner
                [Cc][Oo][Rr][Nn][Ee][Rr]|[Cc][Rr][Nn]{div}|
                # Court
                [Cc][Oo]Uu[Rr][Tt]|[Cc][Tt]|[Cc][Rr][Tt]{div}|
                # Crescent
                [Cc][Rr][Ee][Ss][Cc][Ee][Nn][Tt]|[Cc][Rr][Ee][Ss]{div}|
                # Cul-de-sac
                [Cc][Uu][Ll][-][Dd][Ee][-][Ss][Aa][Cc]|[Cc][Uu][Ll][Dd][Ee][Ss][Aa][Cc]|[Cc][Dd][Ss]{div}|
                # Drive
                [Dd][Rr][Ii][Vv][Ee]|[Dd][Rr][Vv]|[Dd][Rr]{div}|
                # Esplanade
                [Ee][Ss][Pp][Ll][Aa][Nn][Aa][Dd][Ee]|[Ee][Ss][Pp]{div}|
                # Green
                [Gg][Rr][Ee][Ee][Nn]|[Gg][Rr][Nn]{div}|
                # Grove
                [Gg][Rr][Oo][Vv][Ee]|[Gg][Rr]
                # Highway
                [Hh][Ii][Gg][Hh][Ww][Aa][Yy]|[Hh][Ww][Yy]{div}|
                # Junction
                [Jj][Uu][Nn][Cc][Tt][Ii][Oo][Nn]|[Jj][Nn][Cc]{div}|
                # Lane
                [Ll][Aa][Nn][Ee]|[Ll]|[Ll][Aa][Nn][Ee]{div}|
                # Link
                [Ll][Ii][Nn][Kk]|[Ll][Ii][Nn][Kk]{div}|
                # Mews Mews
                [Mm][Ee][Ww][Ss]|[Mm][Ee][Ww][Ss]{div}|
                # Parade Pde
                [Pp][Aa][Rr][Aa][Dd][Ee]|[Pp][Dd][Ee]{div}|
                # Place PL
                [Pp][Ll][Aa][Cc][Ee]|[Pp][Ll]{div}|
                # Ridge
                [Rr][Ii][Dd][Gg][Ee]|[Rr][Dd][Gg][Ee]{div}|
                # Road
                [Rr][Oo][Aa][Dd]|[Rr][Dd]{div}|
                # Square
                [Ss][Qq][Uu][Aa][Rr][Ee]|[Ss][Qq]{div}|
                # Terrace
                [Tt][Ee][Rr][Rr][Aa][Cc][Ee]|[Tt][Cc][Ee]{div}
                
                # Freeway
                [Ff][Rr][Ee][Ee][Ww][Aa][Yy]{div}|
                # Way
                [Ww][Aa][Yy]{div}|
                # Circle
                [Cc][Ii][Rr][Cc][Ll][Ee]{div}|[Cc][Ii][Rr]{div}|
                # Cove
                [Cc][Oo][Vv][Ee]{div}|[Cc][Vv]{div}|
                # Parkway
                [Pp][Aa][Rr][Kk][Ww][Aa][Yy]{div}|[Pp][Kk][Ww][Yy]{div}|
                # Park
                [Pp][Aa][Rr][Kk]{div}
            )
            (?P<route_id>
                [\(\ \,]{route_symbols}
                [Rr][Oo][Uu][Tt][Ee]\ [A-Za-z0-9]+[\)\ \,]{route_symbols}
            )?
            """.format(div="[\.\ ,]?", route_symbols='{0,3}')

floor = r"""
            (?P<floor>
                (?:
                \d+[A-Za-z]{0,2}\.?\ [Ff][Ll][Oo][Oo][Rr]\ 
                )
                |
                (?:
                    [Ff][Ll][Oo][Oo][Rr]\ \d+[A-Za-z]{0,2}\ 
                )
            )
        """

building = r"""
            (?:
                (?:
                    (?:[Bb][Uu][Ii][Ll][Dd][Ii][Nn][Gg])
                    |
                    (?:[Bb][Ll][Dd][Gg])
                )
                \ \d{0,2}[A-Za-z]?
            )
            """

occupancy = r"""
            (?:
                (?:
                    (?:
                        # Suite
                        [Ss][Uu][Ii][Tt][Ee]\ |[Ss][Tt][Ee]\.?\ 
                        |
                        # Apartment
                        [Aa][Pp][Tt]\.?\ |[Aa][Pp][Aa][Rr][Tt][Mm][Ee][Nn][Tt]\ 
                        |
                        # Room
                        [Rr][Oo][Oo][Mm]\ |[Rr][Mm]\.?\ 
                    )
                    (?:
                        [A-Za-z\#\&\-\d]{1,7}
                    )?
                )
                |
                (?:
                    \#[0-9]{,3}[A-Za-z]{1}
                )
            )\ ?
            """

po_box = r"""
            (?:
                [Pp]\.?\ ?[Oo]\.?\ [Bb][Oo][Xx]\ \d+
            )
        """

full_street = r"""
    (?:
        (?P<full_street>

            {street_number}
            {street_name}?\,?\ ?
            (?:[\ \,]{street_type})\,?\ ?
            {post_direction}?\,?\ ?
            {floor}?\,?\ ?

            (?P<building_id>
                {building}
            )?\,?\ ?

            (?P<occupancy>
                {occupancy}
            )?\,?\ ?

            {po_box}?
        )
    )""".format(street_number=street_number,
                street_name=street_name,
                street_type=street_type,
                post_direction=post_direction,
                floor=floor,
                building=building,
                occupancy=occupancy,
                po_box=po_box,
                )

# region1 is actually a "state"
region1 = r"""
        (?P<region1>
            (?:
                #states and territories abbreviations
                V|Q|T
                VIC|NSW|QLD|NT|TAS|WA|ACT|SA|
                Vic|Nsw|Qld|Nt|Tas|Wa|Act|Sa|
                vic|nsw|qld|nt|tas|wa|act|sa
            )
            |
            (?:
                # states full
                [Vv][Ii][Cc][Tt][Oo][Rr][Ii][Aa]|
                [Nn][Ee][Ww]\ [Ss][Oo][Uu][Tt][Hh]\ [Ww][Aa][Ll][Ee][Ss]|
                [Qq][Uu][Ee][Ee][Nn][Ss][Ll][Aa][Nn][Dd]|
                [Nn][Oo][Rr][Tt][Hh][Ee][Rr][Nn]\ [Tt][Ee][Rr][Rr][Ii][Tt][Oo][Rr][Yy]|
                [Tt][Aa][Ss][Mm][Aa][Nn][Ii][Aa]|
                [Ww][Ee][Ss][Tt][Ee][Rr][Nn]\ [Aa][Uu][Ss][Tt][Rr][Aa][Ll][Ii][Aa]|
                [Aa][Uu][Ss][Tt][Rr][Aa][Ll][Ii][Aa][Nn]\ [Cc][Aa][Pp][Ii][Tt][Aa][Ll]\ [Tt][Ee][Rr][Rr][Ii][Tt][Oo][Rr][Yy]|
                [Ss][Oo][Uu][Tt][Hh]\ [Aa][Uu][Ss][Tt][Rr][Aa][Ll][Ii][Aa]

            )
        )
        """

# TODO: doesn't catch cities containing French characters
city = r"""
        (?P<city>
            [A-za-z]{1}[a-zA-Z\ \-\'\.]{2,20}
        )
        """

postal_code = r"""
            (?P<postal_code>
                (?:\d{4}(?:\-\d{4})?)
            )
            """

country = r"""
            (?:
                ([Aa]\.?[Uu]\.?[Ss]\.?)|
                ([Aa][Uu][Ss][Tt][Rr][Aa][Ll][Ii][Aa])
                # we do not catch for "United States of America"
                # since nobody really uses that form to write an
                # address
            )
            """

full_address = r"""
                (?P<full_address>
                    {full_street} {div}
                    {city} {div}
                    {region1} {div}
                    (?:
                        (?:{postal_code}?\ ?,?{country}?)
                    )
                )
                """.format(
    full_street=full_street,
    div='[\, ]{,2}',
    city=city,
    region1=region1,
    country=country,
    postal_code=postal_code,
)
