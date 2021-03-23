from django.db import models
from rest_framework import serializers

from ..productor.models import Productor
from hortum.picture.models import Picture

class Announcement(models.Model):
    idProductor = models.ForeignKey(Productor, on_delete=models.CASCADE, related_name='announcements')
    idPicture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    inventory = models.BooleanField(default=False)

    
    TYPE_OF_PRODUCTS = [
        AVICULTURA + BEBIDAS + CARNE + COGUMELOS + CONGELADOS + DERIVADOS_DE_CANA + DERIVADOS_DE_MANDIOCA + DESIDRATADOS + DOCES + FLORES +FRUTAS + GRAO + HORTALICAS + LATICINIOS + PANIFICADOS + OTHERS
    ]

    AVICULTURA = [
        ('Frango Caipira', 'Frango Caipira'),
        ('Galinhos poedeiras', 'Galinhos poedeiras'),
        ('Ovos de Galinha','Ovos de Galinha'),
        ('Ovos ferteis', 'Ovos ferteis'),
    ]

    BEBIDAS = [
        ('Licor', 'Licor'),
        ('Suco', 'Suco'),
        ('Vinho', 'Vinho'),
    ]

    CARNE = [
        ('Carne Suina', 'Carne Suina'),
        ('Carne Caprina/Ovina', 'Carne Caprina/Ovina'),
        ('Carne de frango', 'Carne de frango'),
        ('Carne de outras Aves', 'Carne de outras Aves'),
        ('Peixes', 'Peixes'),
    ]

    COGUMELOS = [
        ('Cogumelos em Conserva', 'Cogumelos em Conserva'),
        ('Champingnon', 'Champingnon'),
        ('Cogumelo Hiratake', 'Cogumelo Hiratake'),
        ('Cogumelo Hiratake Salmao', 'Cogumelo Hiratake Salmao'),
        ('Cogumelo Shimeji', 'Cogumelo Shimeji'),
    ]

    CONGELADOS = [
        ('Mandioca Descascada Congelada', 'Mandioca Descascada Congelada'),
        ('Polpa de Frutas', 'Polpa de Frutas'),
        ('Pratos congelados', 'Pratos congelados'),
        ('Sorvetes', 'Sorvetes'),
    ]

    DERIVADOS_DE_CANA = [
        ('Acucar Mascavo', 'Acucar Mascavo'),
        ('Melado', 'Melado'),
        ('Rapadura', 'Rapadura'),
    ]

    DERIVADOS_DE_MANDIOCA = [
        ('Farinha de Mandioca', 'Farinha de Mandioca'),
        ('Farinha de Tapioca', 'Farinha de Tapioca'),
        ('Massa de Tapioca', 'Massa de Tapioca'),
        ('Massa para Bolos', 'Massa para Bolos'),
    ]

    DESIDRATADOS = [
        ('Hibiscus', 'Hibiscus'),
        ('Hortaliças', 'Hortaliças'),
        ('Plantas Aromaticas', 'Plantas Aromaticas'),
    ]

    DOCES = [
        ('Doce de Corte', 'Doce de Corte'),
        ('Doce pastoso','Doce pastoso'),
    ]

    FLORES = [
        ('Agave', 'Agave'),
        ('Areca bambu', 'Areca bambu'),
        ('Arnica', 'Arnica'),
        ('Aster', 'Aster'),
        ('Azaleia', 'Azaleia'),
        ('Babosa', 'Babosa'),
        ('Bambu', 'Bambu'),
        ('Begonia - Vaso', 'Begonia - Vaso'),
        ('Boldo', 'Boldo'),
        ('Brinco de princesa (Fuchsia)', 'Brinco de princesa (Fuchsia)'),
        ('Bromelias', 'Bromelias'),
        ('Buxinho', 'Buxinho'),
        ('Cactos/suculentas', 'Cactos/suculentas'),
        ('Citronela', 'Citronela'),
        ('Croton', 'Croton'),
        ('Dracena', 'Dracena'),
        ('Fenix', 'Fenix'),
        ('Ficus - Folhagem', 'Ficus - Folhagem'),
        ('Flores comestivies - Brinco de princesa', 'Flores comestivies - Brinco de princesa'),
        ('Flores comestivies - Capuchinha', 'Flores comestivies - Capuchinha'),
        ('Geranio comum', 'Geranio comum'),
        ('Heliconias - Psittacorum Adrian', 'Heliconias - Psittacorum Adrian'),
        ('Jurubeba', 'Jurubeba'),
        ('Lavanda', 'Lavanda'),
        ('Liriopsis', 'Liriopsis'),
        ('Margarida', 'Margarida'),
        ('Moreia', 'Moreia'),
        ('Moringa', 'Moringa'),
        ('Mudas Frutíferas', 'Mudas Frutíferas'),
        ('Mudas Nativas', 'Mudas Nativas'),
        ('Murta', 'Murta'),
        ('Orquídeas - Catlleya', 'Orquídeas - Catlleya'),
        ('Palmeiras em geral', 'Palmeiras em geral'),
        ('Pata de elefante', 'Pata de elefante'),
        ('Plantas medicinais', 'Plantas medicinais'),
        ('Primavera', 'Primavera'),
        ('Rosa - Corte', 'Rosa - Corte'),
        ('Rosa do deserto', 'Rosa do deserto'),
        ('Samambaia americana', 'Samambaia americana'),
        ('Tango', 'Tango'),
        ('Vinagreira', 'Vinagreira'),
    ]

    FRUTAS = [
        ('Abacate', 'Abacate'),
        ('Abacaxi', 'Abacaxi'),
        ('Acerola', 'Acerola'),
        ('Amora', 'Amora'),
        ('Banana', 'Banana'),
        ('Caju', 'Caju'),
        ('Cara', 'Cara'),
        ('Carambola', 'Carambola'),
        ('Coco', 'Coco'),
        ('Figo', 'Figo'),
        ('Framboesa', 'Framboesa'),
        ('Goiaba', 'Goiaba'),
        ('Graviola', 'Graviola'),
        ('Jabuticaba', 'Jabuticaba'),
        ('Jaca', 'Jaca'),
        ('Laranja', 'Laranja'),
        ('Limao', 'Limao'),
        ('Longana', 'Longana/Lichia Branca/Olho de dragao'),
        ('Mamao', 'Mamao'),
        ('Manga', 'Manga'),
        ('Maracuja', 'Maracuja'),
        ('Maracuja Perola', 'Maracuja Perola'),
        ('Melancia', 'Melancia'),
        ('Morango', 'Morango'),
        ('Pitaia', 'Pitaia'),
        ('Pitanga', 'Pitanga'),
        ('Tamarindo', 'Tamarindo'),
        ('Tangerina', 'Tangerina'),
        ('Uva', 'Uva'),
    ]

    GRAO = [
        ('Amendoim', 'Amendoim'),
        ('Arroz', 'Arroz'),
        ('Cafe', 'Cafe'),
        ('Milho', 'Milho'),
        ('Soja', 'Soja'),
        ('Feijao', 'Feijao'),
    ]

    HORTALICAS = [
        ('Abobora', 'Abobora'),
        ('Açafrao da terra', 'Açafrao da terra'),
        ('Acelga', 'Acelga '),
        ('Couve Chinesa', 'Couve Chinesa'),
        ('Agriao', 'Agriao'),
        ('Alface', 'Alface'),
        ('Algodao', 'Algodao'),
        ('Alho', 'Alho'),
        ('Almeirao', 'Almeirao'),
        ('Batata', 'Batata'),
        ('Batata-doce', 'Batata-doce'),
        ('Berinjela', 'Berinjela'),
        ('Beterraba', 'Beterraba'),
        ('Brocolis', 'Brocolis'),
        ('Cebola', 'Cebola'),
        ('Cebolinha', 'Cebolinha'),
        ('Cenoura', 'Cenoura'),
        ('Chicoria', 'Chicoria'),
        ('Chuchu', 'Chuchu'),
        ('Coentro', 'Coentro'),
        ('Couve', 'Couve'),
        ('Couve-flor', 'Couve-flor'),
        ('Ervilha', 'Ervilha'),
        ('Espinafre', 'Espinafre'),
        ('Gengibre', 'Gengibre'),
        ('Hibiscus', 'Hibiscus'),
        ('Hortela', 'Hortela'),
        ('Inhame', 'Inhame'),
        ('Jilo', 'Jilo'),
        ('Mandioca', 'Mandioca'),
        ('Maxixe', 'Maxixe'),
        ('Milho-verde', 'Milho-verde'),
        ('Mostarda', 'Mostarda'),
        ('Ora pro-nobis', 'Ora pro-nobis'),
    ]

    LATICINIOS = [
        ('Iogurte', 'Iogurte'),
        ('Queijo', 'Queijo'),
        ('Leite', 'Leite'),
    ]

    PANIFICADOS = [
        ('Biscoitos', 'Biscoitos'),
        ('Bolos', 'Bolos'),
        ('Paes', 'Paes'),
        ('Salgados', 'Salgados'),
    ]

    OTHERS = [
        ('Artesanato', 'Artesanato'),
        ('Abelhas', 'Abelhas'),
        ('Animais Ornamentais', 'Animais Ornamentais'),
        ('Composto organico', 'Composto organico'),
        ('Esterco de gado', 'Esterco de gado'),
        ('Cafe', 'Cafe'),
        ('Cabritas/Cabritos', 'Cabritas/Cabritos'),
        ('Damasco', 'Damasco'),
        ('Defumado de Suinos', 'Defumado de Suinos'),
        ('Farinha de Trigo', 'Farinha de Trigo'),
        ('Linguiça artesanal e defumados', 'Linguiça artesanal e defumados'),
        ('Potros/Potras', 'Potros/Potras'),
        ('Cana-de-acucar', 'Cana-de-acucar'),
        ('Feno', 'Feno'),
        ('Geleias', 'Geleias'),
        ('Pepino', 'Pepino'),
        ('Pimenta', 'Pimenta'),
        ('Pimentao', 'Pimentao'),
        ('Quiabo', 'Quiabo'),
        ('Rabanete', 'Rabanete'),
        ('Repolho', 'Repolho'),
        ('Rucula', 'Rucula'),
        ('Salsa', 'Salsa'),
        ('Tomate', 'Tomate'),
        ('Mel', 'Mel'),
        ('Extrato de Tomate', 'Extrato de Tomate'),
        ('Molho de Pimenta', 'Molho de Pimenta'),
        ('Carneiros', 'Carneiros'),
        ('Cordeiros/Cordeiras', 'Cordeiros/Cordeiras'),
        ('Eucalipto', 'Eucalipto'),
        ('Leitoes/Leitoas', 'Leitoes/Leitoas'),
        ('Outros', 'Outros'),
    ]