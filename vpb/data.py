"""Define standard scheme for Vpb Tax Declaration"""
# Copyright 2019 - Ronald Portier - <ronald@portier.eu>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

VPB_SCHEME = (
    # Root nodes.
    ('passiva', 'root', 'Passiva'),
    ('activa', 'root', 'Activa'),
    ('opbrengsten', 'root', 'Opbrengsten'),
    ('kosten', 'root', 'Kosten'),
    ('overig', 'root', 'Overig'),
    # Activa / Debet / Links.
    ('immaterieel', 'activa', 'Immateriële vaste activa'),
    ('financieel', 'activa', 'Financiële vaste activa'),
    ('langlopend', 'financieel', 'Langlopende vorderingen op participanten'),
    ('deelnemingen', 'financieel', 'Deelnemingen'),
    ('vorderingen', 'activa', 'Financiële vaste activa'),
    ('kortlopend', 'vorderingen', 'Kortlopende vorderingen op participanten'),
    ('liquide', 'activa', 'Liquide middelen'),
    # Passiva / Credit / Rechts.
    ('vermogen', 'passiva', 'Ondernemingsvermogen'),
    ('winstreserve', 'vermogen', 'Winstreserve'),
    ('gestort_kapitaal', 'vermogen', 'Gestort kapitaal'),
    ('schulden', 'passiva', 'Kortlopende schulden'),
    ('omzetbelasting', 'schulden', 'Nog af te dragen btw'),
    ('loonbelasting', 'schulden', 'Nog af te dragen loonbelasting'),
    ('voorzieningen', 'passiva', 'Voorzieningen'),
    ('pensioen', 'voorzieningen', 'Pensioen'),
    # Kosten / Debet / Links.
    ('personeel', 'kosten', 'Personeelskosten'),
    ('salaris', 'personeel', 'Loon- en salariskosten'),
    ('overig', 'personeel', 'Overige personeelskosten'),
    ('afschrijvingen', 'kosten', 'Afschrijvingen'),
    # Opbrengsten / Credit / Rechts.
    ('omzet', 'opbrengsten', 'Netto omzet'),
    ('financieel', 'opbrengsten', 'Financiele baten en lasten'),
    # Overige gegevens.
    ('goodwill_origineel', 'overig', 'Goodwill oorspronkelijk'),
    ('goodwill_jaren', 'overig', 'Goodwill jaren afgeschreven'),
    ('goodwill_afscrhijving', 'overig', 'Goodwill jaarlijkse afschrijvingen'),
    ('winstresere_vorig_jaar', 'overig', 'Winstreserve ultimo vorig jaar'),
)
